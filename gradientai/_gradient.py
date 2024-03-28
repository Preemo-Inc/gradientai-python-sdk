from types import TracebackType
from typing import Any, List, Literal, Mapping, Optional, Type, overload

from typing_extensions import Self, assert_never

from gradientai._base_model import BaseModel, CapabilityFilterOption
from gradientai._embeddings_model import EmbeddingsModel
from gradientai._model import Model
from gradientai._model_adapter import ModelAdapter
from gradientai._types import (
    AnalyzeSentimentParamsExample,
    AnalyzeSentimentResponse,
    AnswerParamsSource,
    AnswerResponse,
    ExtractParamsSchemaValue,
    ExtractPdfResponse,
    ExtractResponse,
    PersonalizeResponse,
    Sentiment,
    SummarizeParamsExample,
    SummarizeParamsLength,
    SummarizeResponse,
)
from gradientai.helpers.env_manager import ENV_MANAGER
from gradientai.openapi.client.api.blocks_api import BlocksApi
from gradientai.openapi.client.api.embeddings_api import EmbeddingsApi
from gradientai.openapi.client.api.models_api import ModelsApi
from gradientai.openapi.client.api_client import ApiClient
from gradientai.openapi.client.configuration import Configuration
from gradientai.openapi.client.models.analyze_sentiment_body_params import (
    AnalyzeSentimentBodyParams,
)
from gradientai.openapi.client.models.extract_entity_body_params import (
    ExtractEntityBodyParams,
)
from gradientai.openapi.client.models.generate_answer_body_params import (
    GenerateAnswerBodyParams,
)
from gradientai.openapi.client.models.model_adapter import (
    ModelAdapter as ApiModelAdapter,
)
from gradientai.openapi.client.models.personalize_document_body_params import (
    PersonalizeDocumentBodyParams,
)
from gradientai.openapi.client.models.summarize_document_body_params import (
    SummarizeDocumentBodyParams,
)


class Gradient:
    _api_client: ApiClient
    _blocks_api: BlocksApi
    _embeddings_api: EmbeddingsApi
    _models_api: ModelsApi
    _workspace_id: str

    def __init__(
        self,
        *,
        access_token: Optional[str] = None,
        host: Optional[str] = None,
        workspace_id: Optional[str] = None,
    ) -> None:
        """
        Parameters:
            access_token (str): must either be provided or exist at os.environ["GRADIENT_ACCESS_TOKEN"]
            workspace_id (str): must either be provided or exist at os.environ["GRADIENT_WORKSPACE_ID"]
        """
        if host is None:
            host = ENV_MANAGER.public_api_url

        missing_required_argument_messages = []
        if (
            access_token is None
            and (access_token := ENV_MANAGER.access_token) is None
        ):
            missing_required_argument_messages.append(
                "access_token must either be provided or exist at os.environ['GRADIENT_ACCESS_TOKEN']"
            )
        if (
            workspace_id is None
            and (workspace_id := ENV_MANAGER.workspace_id) is None
        ):
            missing_required_argument_messages.append(
                "workspace_id must either be provided or exist at os.environ['GRADIENT_WORKSPACE_ID']"
            )
        if len(missing_required_argument_messages) != 0:
            raise ValueError(
                f"missing required arguments {missing_required_argument_messages}"
            )
        assert access_token is not None and workspace_id is not None

        self._api_client = ApiClient(
            Configuration(
                access_token=access_token,
                host=host,
            )
        )
        self._blocks_api = BlocksApi(self._api_client)
        self._embeddings_api = EmbeddingsApi(self._api_client)
        self._models_api = ModelsApi(self._api_client)
        self._workspace_id = workspace_id

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_val: Optional[BaseException],
        __exc_tb: Optional[TracebackType],
    ) -> None:
        self.close()

    @property
    def workspace_id(self) -> str:
        return self._workspace_id

    def close(self) -> None:
        self._api_client.close()

    def get_base_model(self, *, base_model_slug: str) -> BaseModel:
        models: List[BaseModel] = self.list_models(only_base=True)
        return next(
            filter(lambda model: model._slug == base_model_slug, models)
        )

    def get_model_adapter(self, *, model_adapter_id: str) -> ModelAdapter:
        response = self._models_api.get_model(
            id=model_adapter_id, x_gradient_workspace_id=self._workspace_id
        )
        return ModelAdapter(
            api_instance=self._models_api,
            base_model_id=response.base_model_id,
            id=response.id,
            name=response.name,
            workspace_id=self._workspace_id,
        )

    @overload
    def list_models(
        self,
        *,
        only_base: Literal[True],
        capability: Optional[CapabilityFilterOption],
    ) -> List[BaseModel]: ...

    @overload
    def list_models(
        self,
        *,
        only_base: Literal[False],
        capability: Optional[CapabilityFilterOption],
    ) -> List[Model]: ...

    def list_models(
        self,
        *,
        only_base: bool,
        capability: Optional[
            CapabilityFilterOption
        ] = CapabilityFilterOption.ANY,
    ) -> List[Model]:  # type: ignore
        response = self._models_api.list_models(
            capability=capability.value,
            only_base=only_base,
            x_gradient_workspace_id=self._workspace_id,
        )

        def deserialize_model(
            api_model: Any,
        ) -> Model:
            

            if api_model.type == "baseModel":
                return BaseModel(
                    api_instance=self._models_api,
                    capabilities=api_model.capabilities,
                    id=api_model.id,
                    slug=api_model.slug,
                    workspace_id=self._workspace_id,
                )
            if api_model.type == "modelAdapter":
                response: ApiModelAdapter = api_model
                return ModelAdapter(
                    api_instance=self._models_api,
                    base_model_id=response.base_model_id,
                    id=response.id,
                    name=response.name,
                    workspace_id=self._workspace_id,
                )
            assert_never(api_model.type)

        models = [
            deserialize_model(model.actual_instance)
            for model in response.models
        ]
        return models

    def get_embeddings_model(self, *, slug: str) -> EmbeddingsModel:
        embeddings_models: List[EmbeddingsModel] = self.list_embeddings_models()
        return next(
            filter(lambda model: model._slug == slug, embeddings_models)
        )

    def list_embeddings_models(self) -> List[EmbeddingsModel]:
        response = self._embeddings_api.list_embeddings(
            x_gradient_workspace_id=self._workspace_id
        )

        def deserialize_embeddings_model(
            api_model: Any,
        ) -> EmbeddingsModel:
            return EmbeddingsModel(
                api_instance=self._embeddings_api,
                slug=api_model.slug,
                workspace_id=self._workspace_id,
            )

        return [
            deserialize_embeddings_model(embeddings_model)
            for embeddings_model in response.embeddings_models
        ]

    def answer(
        self,
        *,
        question: str,
        source: AnswerParamsSource,
    ) -> AnswerResponse:
        response = self._blocks_api.generate_answer(
            x_gradient_workspace_id=self._workspace_id,
            generate_answer_body_params=GenerateAnswerBodyParams.from_dict(
                {
                    "question": question,
                    "source": source,
                }
            ),
        )

        return AnswerResponse(
            answer=response.answer, rag_context=response.rag_context
        )

    def summarize(
        self,
        *,
        document: str,
        examples: Optional[List[SummarizeParamsExample]] = None,
        length: Optional[SummarizeParamsLength] = None,
    ) -> SummarizeResponse:
        response = self._blocks_api.summarize_document(
            x_gradient_workspace_id=self._workspace_id,
            summarize_document_body_params=SummarizeDocumentBodyParams(
                document=document,
                examples=examples,
                length=None if length is None else length.value,
            ),
        )

        return SummarizeResponse(summary=response.summary)

    def analyze_sentiment(
        self,
        *,
        document: str,
        examples: Optional[List[AnalyzeSentimentParamsExample]] = None,
    ) -> AnalyzeSentimentResponse:
        parsed_examples = (
            None
            if not examples
            else [
                {
                    "document": example["document"],
                    "sentiment": example["sentiment"].value,
                }
                for example in examples
            ]
        )

        result = self._blocks_api.analyze_sentiment(
            x_gradient_workspace_id=self._workspace_id,
            analyze_sentiment_body_params=AnalyzeSentimentBodyParams(
                document=document, examples=parsed_examples
            ),
        )

        return AnalyzeSentimentResponse(
            sentiment=Sentiment(result.sentiment),
        )

    def personalize(
        self, *, document: str, audience_description: str
    ) -> PersonalizeResponse:
        result = self._blocks_api.personalize_document(
            x_gradient_workspace_id=self._workspace_id,
            personalize_document_body_params=PersonalizeDocumentBodyParams(
                document=document,
                audience_description=audience_description,
            ),
        )

        return PersonalizeResponse(
            personalized_document=result.personalized_document
        )

    def extract(
        self, *, document: str, schema_: Mapping[str, ExtractParamsSchemaValue]
    ) -> ExtractResponse:
        parsed_schema = {
            key: {
                "type": value["type"].value,
                "required": value.get("required"),
            }
            for key, value in schema_.items()
        }

        result = self._blocks_api.extract_entity(
            x_gradient_workspace_id=self._workspace_id,
            extract_entity_body_params=ExtractEntityBodyParams(
                document=document,
                schema=parsed_schema,
            ),
        )

        entity = {
            key: value.actual_instance for key, value in result.entity.items()
        }
        return ExtractResponse(entity=entity)

    def extract_pdf(
        self,
        *,
        filepath: str,
    ) -> ExtractPdfResponse:
        result = self._blocks_api.extract_pdf(
            x_gradient_workspace_id=self._workspace_id,
            file=filepath,
        )

        pages = [
            {
                "images": [
                    {
                        "data": image.data,
                        "format": image.format,
                    }
                    for image in page.images
                ],
                "page_number": page.page_number,
                "tables": [
                    {
                        "name": table.name,
                        "table_rows": [
                            {
                                "cells": [
                                    {
                                        "cell_value": cell.cell_value,
                                        "col_span": cell.col_span,
                                        "row_span": cell.row_span,
                                    }
                                    for cell in row.cells
                                ],
                                "type": row.type,
                            }
                            for row in table.table_rows
                        ],
                    }
                    for table in page.tables
                ],
                "text": page.text,
                "text_blocks": [
                    {
                        "kind": text_block.kind,
                        "texts": text_block.texts,
                    }
                    for text_block in page.text_blocks
                ],
            }
            for page in result.pages
        ]

        return ExtractPdfResponse(
            pages=pages,
            text=result.text,
            title=result.title,
        )
