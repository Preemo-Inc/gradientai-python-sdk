from enum import Enum
from typing import List, Literal, Mapping, Optional, TypedDict, Union

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


class Document(TypedDict):
    content: str
    file_name: str


class RagContext(TypedDict):
    documents: List[Document]


class AnswerResponse(TypedDict):
    answer: str
    rag_context: Optional[RagContext]


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


class ExtractPdfResponseImage(TypedDict):
    data: str
    format: Literal["base64-png"]


class ExtractPdfResponseCell(TypedDict):
    cell_value: str
    col_span: Optional[int]
    row_span: Optional[int]


class ExtractPdfResponseRow(TypedDict):
    cells: List[ExtractPdfResponseCell]
    type: Literal["table_data_row", "table_header"]


class ExtractPdfResponseTable(TypedDict):
    name: str
    table_rows: List[ExtractPdfResponseRow]


class ExtractPdfResponseTextBlock(TypedDict):
    kind: Literal["footer", "header", "section_title", "text", "title"]
    texts: List[str]


class ExtractPdfResponsePage(TypedDict):
    images: List[ExtractPdfResponseImage]
    pageNumber: int
    tables: List[ExtractPdfResponseTable]
    text: str
    textBlocks: List[ExtractPdfResponseTextBlock]


class ExtractPdfResponse(TypedDict):
    pages: List[ExtractPdfResponsePage]
    text: str
    title: Optional[str]
