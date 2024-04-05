from abc import ABC
import os
from typing import List

from gradientai.openapi.client.api.files_api import FilesApi
from gradientai.openapi.client.api.rag_api import RAGApi
from gradientai.openapi.client.models.add_files_to_rag_collection_body_params import (
    AddFilesToRagCollectionBodyParams,
)
from gradientai.openapi.client.models.create_rag_collection_body_params_files_inner import (
    CreateRagCollectionBodyParamsFilesInner,
)


class RAGCollection(ABC):
    _id: str
    _rag_api: RAGApi
    _files_api: FilesApi
    _workspace_id: str

    def __init__(
        self,
        *,
        id_: str,
        files_api: FilesApi,
        rag_api: RAGApi,
        workspace_id: str,
    ) -> None:
        self._id = id_
        self._files_api = files_api
        self._rag_api = rag_api
        self._workspace_id = workspace_id

    @property
    def id_(self) -> str:
        return self._id

    def add_files(self, *, filepaths: List[os.PathLike]) -> None:
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
