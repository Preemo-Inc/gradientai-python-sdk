from importlib import metadata as _metadata

__version__ = _metadata.version("gradientai")

from typing import List, Optional, Union

from typing_extensions import NotRequired, Protocol, TypedDict

from gradientai._base_model import BaseModelCapability, CapabilityFilterOption
from gradientai._gradient import Gradient
from gradientai._model import Guidance
from gradientai._types import (
    AnalyzeSentimentParamsExample,
    ExtractParamsSchemaValue,
    ExtractParamsSchemaValueType,
    Sentiment,
    SummarizeParamsExample,
    SummarizeParamsLength,
)
from gradientai.pydantic_models.types import CompleteResponse, FineTuneResponse

class Model(Protocol):
    @property
    def id(self) -> str: ...
    @property
    def workspace_id(self) -> str: ...
    def complete(
        self,
        *,
        query: str,
        rag_collection_id: Optional[str] = ...,
        max_generated_token_count: Optional[int] = ...,
        temperature: Optional[float] = ...,
        top_k: Optional[int] = ...,
        top_p: Optional[float] = ...
    ) -> CompleteResponse: ...

class StructuredInput(TypedDict):
    parse_special_tokens: NotRequired[bool]
    trainable: NotRequired[bool]
    value: str

class Sample(TypedDict):
    inputs: Union[str, List[StructuredInput]]
    multiplier: NotRequired[float]

class ModelAdapter(Model, Protocol):
    @property
    def base_model_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    def delete(self) -> None: ...
    def fine_tune(self, *, samples: List[Sample]) -> FineTuneResponse: ...

class BaseModel(Model, Protocol):
    @property
    def capabilities(self) -> List[BaseModelCapability]: ...
    @property
    def slug(self) -> str: ...
    def create_model_adapter(
        self,
        *,
        name: str,
        rank: Optional[int] = ...,
        learning_rate: Optional[float] = ...
    ) -> ModelAdapter: ...

__all__ = [
    "AnalyzeSentimentParamsExample",
    "BaseModel",
    "CapabilityFilterOption",
    "ExtractParamsSchemaValue",
    "ExtractParamsSchemaValueType",
    "Gradient",
    "Guidance",
    "Model",
    "ModelAdapter",
    "Sample",
    "Sentiment",
    "StructuredInput",
    "SummarizeParamsExample",
    "SummarizeParamsLength",
]
