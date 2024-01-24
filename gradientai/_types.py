from enum import Enum
from typing import Literal, Mapping, TypedDict, Union

from typing_extensions import NotRequired


class AnswerParamsSourceRAG(TypedDict):
    collection_id: str
    type: Literal["rag"]


class AnswerParamsSourceDocument(TypedDict):
    type: Literal["document"]
    value: str


AnswerParamsSource = Union[
    AnswerParamsSourceRAG,
    AnswerParamsSourceDocument,
]


class AnswerResponse(TypedDict):
    answer: str


class SummarizeParamsExample(TypedDict):
    document: str
    summary: str


class SummarizeParamsLength(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class SummarizeResponse(TypedDict):
    summary: str


class Sentiment(str, Enum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"


class AnalyzeSentimentParamsExample(TypedDict):
    document: str
    sentiment: Sentiment


class AnalyzeSentimentResponse(TypedDict):
    sentiment: Sentiment


class PersonalizeResponse(TypedDict):
    personalized_document: str


class ExtractParamsSchemaValueType(str, Enum):
    STRING = "string"
    BOOLEAN = "boolean"
    NUMBER = "number"


class ExtractParamsSchemaValue(TypedDict):
    required: NotRequired[bool]
    type: ExtractParamsSchemaValueType


class ExtractResponse(TypedDict):
    entity: Mapping[str, Union[str, bool, int, float]]
