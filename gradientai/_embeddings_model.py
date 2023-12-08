from abc import ABC
from typing import List, TypedDict

from gradientai.openapi.client.api.embeddings_api import EmbeddingsApi
from gradientai.openapi.client.models.generate_embedding_body_params import (
    GenerateEmbeddingBodyParams,
)
from gradientai.openapi.client.models.generate_embedding_success import (
    GenerateEmbeddingSuccess,
)


class EmbeddingsInput(TypedDict):
    input: str


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
        response = self._api_instance.generate_embedding(
            slug=self._slug,
            x_gradient_workspace_id=self._workspace_id,
            generate_embedding_body_params=GenerateEmbeddingBodyParams(
                inputs=inputs,
            ),
        )

        return response
