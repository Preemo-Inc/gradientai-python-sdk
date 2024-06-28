import os
from dataclasses import asdict, dataclass
from typing import List, Optional, Type, TypedDict, TypeVar, Union

from gradientai._types import RAGFileIngestionStatus
from gradientai.openapi.client.api.files_api import FilesApi
from gradientai.openapi.client.api.rag_api import RAGApi
from gradientai.openapi.client.models.add_files_to_rag_collection_body_params import (
    AddFilesToRagCollectionBodyParams,
)
from gradientai.openapi.client.models.create_rag_collection_body_params_files_inner import (
    CreateRagCollectionBodyParamsFilesInner,
)
from gradientai.openapi.client.models.file_chunker import (
    FileChunker as ApiFileChunker,
)
from gradientai.openapi.client.models.meaning_based_chunker import (
    MeaningBasedChunker as ApiMeaningBasedChunker,
)
from gradientai.openapi.client.models.normal_chunker import (
    NormalChunker as ApiNormalChunker,
)
from gradientai.openapi.client.models.sentence_with_context_chunker import (
    SentenceWithContextChunker as ApiSentenceWithContextChunker,
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
class MeaningBasedChunker:
    _chunker_type: str = "meaningBasedChunker"
    similiarity_percent_threshold: Optional[int] = None
    sentence_group_length: Optional[int] = None
    size: Optional[int] = None
    overlap: Optional[int] = None

    @property
    def chunker_type(self) -> str:
        return self._chunker_type

    @classmethod
    def get_chunker_type(cls) -> str:
        return cls._chunker_type

    def __init__(
        self,
        *,
        similiarity_percent_threshold: Optional[int] = None,
        sentence_group_length: Optional[int] = None,
        size: Optional[int] = None,
        overlap: Optional[int] = None,
    ) -> None:
        self.similiarity_percent_threshold = similiarity_percent_threshold
        self.sentence_group_length = sentence_group_length
        self.size = size
        self.overlap = overlap


@dataclass_with_kw_only
class SentenceWithContextChunker:
    _chunker_type: str = "sentenceWithContextChunker"
    size: Optional[int] = None
    overlap: Optional[int] = None
    context_sentences: Optional[int] = None

    @property
    def chunker_type(self) -> str:
        return self._chunker_type

    @classmethod
    def get_chunker_type(cls) -> str:
        return cls._chunker_type

    def __init__(
        self,
        *,
        size: Optional[int] = None,
        overlap: Optional[int] = None,
        context_sentences: Optional[int] = None,
    ) -> None:
        self.size = size
        self.overlap = overlap
        self.context_sentences = context_sentences


@dataclass_with_kw_only
class FileChunker:
    _chunker_type: str = "fileChunker"

    @property
    def chunker_type(self) -> str:
        return self._chunker_type

    @classmethod
    def get_chunker_type(cls) -> str:
        return cls._chunker_type


@dataclass_with_kw_only
class NormalChunker:
    _chunker_type: str = "normalChunker"
    size: Optional[int] = None
    overlap: Optional[int] = None

    @property
    def chunker_type(self) -> str:
        return self._chunker_type

    @classmethod
    def get_chunker_type(cls) -> str:
        return cls._chunker_type

    def __init__(
        self,
        *,
        size: Optional[int] = None,
        overlap: Optional[int] = None,
    ) -> None:
        self.size = size
        self.overlap = overlap


RAGChunker = Union[
    MeaningBasedChunker,
    SentenceWithContextChunker,
    FileChunker,
    NormalChunker,
]

ApiRAGChunker = Union[
    ApiFileChunker,
    ApiMeaningBasedChunker,
    ApiNormalChunker,
    ApiSentenceWithContextChunker,
]


def build_api_chunker(
    chunker: RAGChunker,
) -> ApiRAGChunker:
    if type(chunker) is MeaningBasedChunker:
        return ApiMeaningBasedChunker(
            chunker_type=chunker.chunker_type,
            overlap=chunker.overlap,
            sentence_group_length=chunker.sentence_group_length,
            similiarity_percent_threshold=chunker.similiarity_percent_threshold,
            size=chunker.size,
        )
    elif type(chunker) is SentenceWithContextChunker:
        return ApiSentenceWithContextChunker(
            chunker_type=chunker.chunker_type,
            context_sentences=chunker.context_sentences,
            overlap=chunker.overlap,
            size=chunker.size,
        )
    elif type(chunker) is NormalChunker:
        return ApiNormalChunker(
            chunker_type=chunker.chunker_type,
            overlap=chunker.overlap,
            size=chunker.size,
        )
    elif type(chunker) is FileChunker:
        return ApiFileChunker(chunker_type=chunker.chunker_type)
    else:
        raise ValueError(f"Unsupported chunker type {chunker.chunker_type}")


class RAGCollection:
    _files: List[RAGFile]
    _files_api: FilesApi
    _id: str
    _name: str
    _chunker: RAGChunker
    _rag_api: RAGApi
    _workspace_id: str

    def __init__(
        self,
        *,
        files: List[RAGFile],
        files_api: FilesApi,
        id_: str,
        name: str,
        chunker: RAGChunker,
        rag_api: RAGApi,
        workspace_id: str,
    ) -> None:
        self._files = files
        self._files_api = files_api
        self._id = id_
        self._name = name
        self._chunker = chunker
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
    def chunker(self) -> RAGChunker:
        return self._chunker

    def __str__(self) -> str:
        return f"RAGCollection(id={self._id}, name={self._name}, chunker={self._chunker})"

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

    @staticmethod
    def deserialize_rag_chunker(instance: ApiRAGChunker) -> RAGChunker:
        if instance.chunker_type == MeaningBasedChunker.get_chunker_type():
            return MeaningBasedChunker(
                similiarity_percent_threshold=instance.similiarity_percent_threshold,
                sentence_group_length=instance.sentence_group_length,
                overlap=instance.overlap,
                size=instance.size,
            )
        elif (
            instance.chunker_type
            == SentenceWithContextChunker.get_chunker_type()
        ):
            return SentenceWithContextChunker(
                overlap=instance.overlap,
                size=instance.size,
                context_sentences=instance.context_sentences,  # type: ignore
            )
        elif instance.chunker_type == FileChunker.get_chunker_type():
            return FileChunker()
        elif instance.chunker_type == NormalChunker.get_chunker_type():
            return NormalChunker(
                overlap=instance.overlap,
                size=instance.size,
            )
        else:
            raise ValueError(
                f"Unknown chunker type: {instance.chunker_type}. Please upgrade Gradient library to the latest version."
            )
