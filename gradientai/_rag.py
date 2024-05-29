from gradientai.openapi.client.models.simple_node_parser import (
    SimpleNodeParser as ApiSimpleNodeParser,
)
from gradientai.openapi.client.models.sentence_window_node_parser import (
    SentenceWindowNodeParser as ApiSentenceWindowNodeParser,
)
from dataclasses import dataclass
import os
from typing import List, Optional, Type, TypeVar, TypedDict, Union

from gradientai._types import RAGFileIngestionStatus
from gradientai.openapi.client.api.files_api import FilesApi
from gradientai.openapi.client.api.rag_api import RAGApi
from gradientai.openapi.client.models.add_files_to_rag_collection_body_params import (
    AddFilesToRagCollectionBodyParams,
)
from gradientai.openapi.client.models.create_rag_collection_body_params_files_inner import (
    CreateRagCollectionBodyParamsFilesInner,
)

from typing_extensions import dataclass_transform


class RAGFile(TypedDict):
    id_: str
    name: str
    status: RAGFileIngestionStatus


T = TypeVar("T")


@dataclass_transform(kw_only_default=True)
def dataclass_with_kw_only(cls: Type[T]) -> Type[T]:
    return dataclass(cls)


@dataclass_with_kw_only
class SimpleNodeParser:
    chunk_size: Optional[int] = None
    chunk_overlap: Optional[int] = None

    @property
    def parser_type(self) -> str:
        return "simpleNodeParser"

    def __init__(
        self,
        *,
        chunk_size: Optional[int] = None,
        chunk_overlap: Optional[int] = None,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap


@dataclass_with_kw_only
class SentenceWindowNodeParser:
    chunk_size: Optional[int] = None
    chunk_overlap: Optional[int] = None
    window_size: Optional[int] = None

    @property
    def parser_type(self) -> str:
        return "sentenceWindowNodeParser"

    def __init__(
        self,
        *,
        chunk_size: Optional[int] = None,
        chunk_overlap: Optional[int] = None,
        window_size: Optional[int] = None,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.window_size = window_size


RAGParser = Union[SentenceWindowNodeParser, SimpleNodeParser]


def build_api_parser(
    parser: RAGParser,
) -> Union[ApiSentenceWindowNodeParser, ApiSimpleNodeParser]:
    if type(parser) is SimpleNodeParser:
        return ApiSimpleNodeParser(
            chunk_overlap=parser.chunk_overlap,
            chunk_size=parser.chunk_size,
            parser_type=parser.parser_type,
        )
    elif type(parser) is SentenceWindowNodeParser:
        return ApiSentenceWindowNodeParser(
            chunk_overlap=parser.chunk_overlap,
            chunk_size=parser.chunk_size,
            parser_type=parser.parser_type,
            window_size=parser.window_size,
        )
    else:
        raise ValueError(f"Unsupported parser type {parser.parser_type}")


class RAGCollection:
    _files: List[RAGFile]
    _files_api: FilesApi
    _id: str
    _name: str
    _parser: RAGParser
    _rag_api: RAGApi
    _workspace_id: str

    def __init__(
        self,
        *,
        files: List[RAGFile],
        files_api: FilesApi,
        id_: str,
        name: str,
        parser: RAGParser,
        rag_api: RAGApi,
        workspace_id: str,
    ) -> None:
        self._files = files
        self._files_api = files_api
        self._id = id_
        self._name = name
        self._parser = parser
        self._rag_api = rag_api
        self._workspace_id = workspace_id

    @property
    def id_(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def files(self) -> List[RAGFile]:
        return self._files

    @property
    def parser(self) -> RAGParser:
        return self._parser

    def __str__(self) -> str:
        return f"RAGCollection(id={self._id}, name={self._name}, parser={self._parser})"

    def add_files(self, *, filepaths: List[str]) -> None:
        file_results = [
            self._files_api.upload_file(
                file=file_,
                type="ragUserFile",
                x_gradient_workspace_id=self._workspace_id,
            )
            for file_ in filepaths
        ]

        self._rag_api.add_files_to_rag_collection(
            id=self._id,
            x_gradient_workspace_id=self._workspace_id,
            add_files_to_rag_collection_body_params=AddFilesToRagCollectionBodyParams(
                files=[
                    CreateRagCollectionBodyParamsFilesInner(
                        id=file_result.id, name=os.path.basename(file_path)
                    )
                    for (file_result, file_path) in zip(file_results, filepaths)
                ],
            ),
        )

        result = self._rag_api.get_rag_collection(
            x_gradient_workspace_id=self._workspace_id,
            id=self._id,
        )

        self._files = [
            {"id_": file.id, "name": file.name, "status": file.status}
            for file in result.files
        ]

    def delete(self) -> None:
        self._rag_api.delete_rag_collection(
            id=self._id,
            x_gradient_workspace_id=self._workspace_id,
        )
