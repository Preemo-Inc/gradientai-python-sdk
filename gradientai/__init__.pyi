from importlib import metadata as _metadata
from types import TracebackType

from pydantic import StrictFloat, StrictInt

__version__ = _metadata.version("gradientai")

from typing import List, Literal, Mapping, Optional, Type, Union, overload

from typing_extensions import NotRequired, Protocol, TypedDict, Self

from gradientai._base_model import BaseModelCapability, CapabilityFilterOption
from gradientai._model import Guidance
from gradientai._rag import (
    FileChunker,
    MeaningBasedChunker,
    NormalChunker,
    RAGChunker,
    RAGFile,
    SentenceWithContextChunker,
)
from gradientai._types import (
    AnalyzeSentimentParamsExample,
    AnalyzeSentimentResponse,
    AnswerParamsSource,
    AnswerResponse,
    ExtractParamsSchemaValue,
    ExtractParamsSchemaValueType,
    ExtractPdfResponse,
    ExtractResponse,
    PersonalizeResponse,
    Sentiment,
    SummarizeParamsExample,
    SummarizeParamsLength,
    SummarizeResponse,
    TranscribeAudioResponse,
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
        guidance: Optional[Guidance] = ...,
        rag_collection_id: Optional[str] = ...,
        max_generated_token_count: Optional[int] = ...,
        temperature: Optional[float] = ...,
        top_k: Optional[int] = ...,
        top_p: Optional[float] = ...,
    ) -> CompleteResponse: ...
    async def acomplete(
        self,
        *,
        query: str,
        guidance: Optional[Guidance] = ...,
        rag_collection_id: Optional[str] = ...,
        max_generated_token_count: Optional[int] = ...,
        temperature: Optional[float] = ...,
        top_k: Optional[int] = ...,
        top_p: Optional[float] = ...,
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
        learning_rate: Optional[float] = ...,
    ) -> ModelAdapter: ...

class EmbeddingsInput(TypedDict):
    input: str

class EmbeddingResult(Protocol):
    embedding: List[Union[StrictFloat, StrictInt]]
    index: int

class GenerateEmbeddingSuccess(Protocol):
    embeddings: List[EmbeddingResult]

class EmbeddingsModel(Protocol):
    @property
    def slug(self) -> str: ...
    @property
    def workspace_id(self) -> str: ...
    def generate_embeddings(
        self,
        *,
        inputs: List[EmbeddingsInput],
    ) -> GenerateEmbeddingSuccess: ...
    def embed(
        self,
        *,
        inputs: List[EmbeddingsInput],
    ) -> GenerateEmbeddingSuccess: ...
    async def aembed(
        self,
        *,
        inputs: List[EmbeddingsInput],
    ) -> GenerateEmbeddingSuccess: ...

class RAGCollection:
    @property
    def id_(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def files(self) -> List[RAGFile]: ...
    @property
    def chunker(self) -> RAGChunker: ...
    def add_files(self, *, filepaths: List[str]) -> None: ...
    def delete(self) -> None: ...

class Gradient:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_val: Optional[BaseException],
        __exc_tb: Optional[TracebackType],
    ) -> None: ...
    @property
    def workspace_id(self) -> str: ...
    def close(self) -> None: ...
    def get_base_model(self, *, base_model_slug: str) -> BaseModel: ...
    def get_model_adapter(self, *, model_adapter_id: str) -> ModelAdapter: ...
    @overload
    def list_models(
        self,
        *,
        only_base: Literal[True],
        capability: Optional[CapabilityFilterOption] = ...,
    ) -> List[BaseModel]: ...
    @overload
    def list_models(
        self,
        *,
        only_base: Literal[False],
        capability: Optional[CapabilityFilterOption] = ...,
    ) -> List[Model]: ...
    @overload
    def list_models(
        self,
        *,
        capability: Optional[CapabilityFilterOption] = ...,
    ) -> List[Model]: ...
    def get_embeddings_model(self, *, slug: str) -> EmbeddingsModel: ...
    def list_embeddings_models(self) -> List[EmbeddingsModel]: ...
    def answer(
        self,
        *,
        question: str,
        source: AnswerParamsSource,
    ) -> AnswerResponse: ...
    def summarize(
        self,
        *,
        document: str,
        examples: Optional[List[SummarizeParamsExample]] = ...,
        length: Optional[SummarizeParamsLength] = ...,
    ) -> SummarizeResponse: ...
    def analyze_sentiment(
        self,
        *,
        document: str,
        examples: Optional[List[AnalyzeSentimentParamsExample]] = ...,
    ) -> AnalyzeSentimentResponse: ...
    def personalize(
        self, *, document: str, audience_description: str
    ) -> PersonalizeResponse: ...
    def extract(
        self, *, document: str, schema_: Mapping[str, ExtractParamsSchemaValue]
    ) -> ExtractResponse: ...
    def extract_pdf(
        self,
        *,
        filepath: str,
    ) -> ExtractPdfResponse: ...
    def transcribe_audio(
        self,
        *,
        filepath: str,
    ) -> TranscribeAudioResponse: ...
    def create_rag_collection(
        self,
        *,
        name: str,
        slug: str,
        filepaths: Optional[List[str]] = ...,
        chunker: Optional[RAGChunker] = ...,
    ) -> RAGCollection: ...
    def list_rag_collections(self) -> List[RAGCollection]: ...
    def get_rag_collection(self, *, id_: str) -> RAGCollection: ...

__all__ = [
    "AnalyzeSentimentParamsExample",
    "AnswerParamsSource",
    "BaseModel",
    "CapabilityFilterOption",
    "ExtractParamsSchemaValue",
    "ExtractParamsSchemaValueType",
    "FileChunker",
    "Gradient",
    "Guidance",
    "MeaningBasedChunker",
    "Model",
    "ModelAdapter",
    "NormalChunker",
    "RAGChunker",
    "RAGCollection",
    "Sample",
    "SentenceWithContextChunker",
    "Sentiment",
    "StructuredInput",
    "SummarizeParamsExample",
    "SummarizeParamsLength",
]
