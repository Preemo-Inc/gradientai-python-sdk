from types import TracebackType
from typing import Any, List, Literal, Optional, overload, Type
from typing_extensions import Self

from gradientai.openapi.client.api.models_api import ModelsApi
from gradientai.openapi.client.api.embeddings_api import EmbeddingsApi
from gradientai.openapi.client.api_client import ApiClient
from gradientai.openapi.client.configuration import Configuration
from gradientai.openapi.client.models.model_adapter import (
    ModelAdapter as ApiModelAdapter,
)
from typing_extensions import assert_never

from gradientai.helpers.env_manager import ENV_MANAGER
from gradientai._base_model import BaseModel
from gradientai._model_adapter import ModelAdapter
from gradientai._model import Model
from gradientai._embeddings_model import EmbeddingsModel


class Gradient:
    _api_client: ApiClient
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
    def list_models(self, *, only_base: Literal[True]) -> List[BaseModel]:
        ...

    @overload
    def list_models(self, *, only_base: Literal[False]) -> List[Model]:
        ...

    def list_models(self, *, only_base: bool) -> List[Model]:  # type: ignore
        response = self._models_api.list_models(
            x_gradient_workspace_id=self._workspace_id, only_base=only_base
        )

        def deserialize_model(
            api_model: Any,
        ) -> Model:
            if api_model.type == "baseModel":
                return BaseModel(
                        api_instance=self._models_api,
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
                workspace_id=self._workspace_id
            )

        return [
            deserialize_embeddings_model(embeddings_model)
            for embeddings_model in response.embeddings_models
        ]
