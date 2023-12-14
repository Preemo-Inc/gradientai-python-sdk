from abc import ABC
from concurrent.futures import ThreadPoolExecutor
from gradientai.openapi.client.api.embeddings_api import EmbeddingsApi
from typing import List, TypedDict
from gradientai.openapi.client.models.generate_embedding_body_params import (
    GenerateEmbeddingBodyParams,
)
from gradientai.openapi.client.models.generate_embedding_success import (
    GenerateEmbeddingSuccess,
)
from gradientai.helpers.asyncio_threads import to_thread as _asyncio_to_thread
import asyncio


class EmbeddingsInput(TypedDict):
    input: str


MAX_BATCH_SIZE_DEFAULT = 256


class EmbeddingsModel(ABC):
    _api_instance: EmbeddingsApi
    _slug: str
    _workspace_id: str

    def __init__(
        self, *, api_instance: EmbeddingsApi, slug: str, workspace_id: str
    ) -> None:
        self._api_instance = api_instance
        self._slug = slug
        self._workspace_id = workspace_id
        # internal variables, limit to max 8*8 concurrent requests
        self._max_batch_size = MAX_BATCH_SIZE_DEFAULT
        self._threads_per_request = 8
        self._async_semaphore = asyncio.Semaphore(8)

    @property
    def slug(self) -> str:
        return self._slug

    @property
    def workspace_id(self) -> str:
        return self._workspace_id

    def generate_embeddings(
        self,
        *,
        inputs: List[EmbeddingsInput],
    ) -> GenerateEmbeddingSuccess:
        """generate a micro-batch of embeddings

        Args:
            inputs (List[EmbeddingsInput]): List of inputs,
                len(inputs) must be smaller than server-side accepted batch_size.

        Returns:
            GenerateEmbeddingSuccess: Embeddings
        """
        response = self._api_instance.generate_embedding(
            slug=self._slug,
            x_gradient_workspace_id=self._workspace_id,
            generate_embedding_body_params=GenerateEmbeddingBodyParams(
                inputs=inputs,
            ),
        )

        return response

    def embed(
        self,
        *,
        inputs: List[EmbeddingsInput],
    ) -> GenerateEmbeddingSuccess:
        """Returns embeddings with automatic batching

        Args:
            inputs (List[EmbeddingsInput]): List of inputs

        Returns:
            GenerateEmbeddingSuccess: Embeddings
        """
        if len(inputs) <= self._max_batch_size:
            return self.generate_embeddings(inputs=inputs)
        # perform concurrent calls, by micro-batching the inputs
        with ThreadPoolExecutor(
            max_workers=min(
                self._threads_per_request,
                1 + len(inputs) // self._max_batch_size,
            )
        ) as executor:
            responses = executor.map(
                lambda start_index: self.generate_embeddings(
                    inputs=inputs[
                        start_index : start_index + self._max_batch_size
                    ]
                ),
                range(0, len(inputs), self._max_batch_size),
            )

        all_embeddings = []
        all_additional_properties = {}
        idx = 0

        for response in responses:
            for embedding in response.embeddings:
                embedding.index = idx
                idx += 1
            all_embeddings.extend(response.embeddings)
            all_additional_properties.update(response.additional_properties)

        return GenerateEmbeddingSuccess(
            embeddings=all_embeddings,
            additional_properties=all_additional_properties,
        )

    async def aembed(
        self,
        *,
        inputs: List[EmbeddingsInput],
    ) -> GenerateEmbeddingSuccess:
        """Async wrapper for self.embed

        Args:
            inputs (List[EmbeddingsInput]): List of inputs

        Returns:
            GenerateEmbeddingSuccess: Embeddings
        """
        async with self._async_semaphore:
            response = await _asyncio_to_thread(
                self.embed, inputs=inputs
            )
        return response
