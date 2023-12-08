from abc import ABC
from typing import List, Literal, Optional, TypedDict

from gradientai.openapi.client.api.models_api import ModelsApi
from gradientai.openapi.client.models.complete_model_body_params import (
    CompleteModelBodyParams,
)
from gradientai.pydantic_models.types import CompleteResponse


class Guidance(TypedDict):
    type: Literal["choice"]
    value: List[str]


class Model(ABC):
    _api_instance: ModelsApi
    _id: str
    _workspace_id: str

    def __init__(
        self, *, api_instance: ModelsApi, id: str, workspace_id: str
    ) -> None:
        self._api_instance = api_instance
        self._id = id
        self._workspace_id = workspace_id

    @property
    def id(self) -> str:
        return self._id

    @property
    def workspace_id(self) -> str:
        return self._workspace_id

    def complete(
        self,
        *,
        query: str,
        guidance: Optional[Guidance] = None,
        max_generated_token_count: Optional[int] = None,
        temperature: Optional[float] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
    ) -> CompleteResponse:
        response = self._api_instance.complete_model(
            id=self._id,
            x_gradient_workspace_id=self._workspace_id,
            complete_model_body_params=CompleteModelBodyParams(
                guidance=guidance,
                query=query,
                max_generated_token_count=max_generated_token_count,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
            ),
        )

        return CompleteResponse(
            finish_reason=response.finish_reason,
            generated_output=response.generated_output,
        )
