from enum import Enum
from typing import List, Optional

from gradientai._model import Model
from gradientai._model_adapter import ModelAdapter
from gradientai.openapi.client.api.models_api import ModelsApi
from gradientai.openapi.client.models import (
    CreateModelBodyParams,
    CreateModelBodyParamsInitialHyperparameters,
    CreateModelBodyParamsInitialHyperparametersLoraHyperparameters,
    CreateModelBodyParamsInitialHyperparametersTrainingArguments,
    CreateModelBodyParamsModel,
)


class BaseModelCapability(str, Enum):
    FINE_TUNE = "fineTune"
    COMPLETE = "complete"


class CapabilityFilterOption(str, Enum):
    ANY = "any"
    FINE_TUNE = BaseModelCapability.FINE_TUNE.value
    COMPLETE = BaseModelCapability.COMPLETE.value


class BaseModel(Model):
    _capabilities: List[BaseModelCapability]
    _slug: str

    def __init__(
        self,
        *,
        api_instance: ModelsApi,
        capabilities: List[BaseModelCapability],
        id: str,
        slug: str,
        workspace_id: str,
    ) -> None:
        super().__init__(
            api_instance=api_instance, id=id, workspace_id=workspace_id
        )
        self._capabilities = capabilities
        self._slug = slug

    @property
    def capabilities(self) -> List[BaseModelCapability]:
        return self._capabilities

    @property
    def slug(self) -> str:
        return self._slug

    def create_model_adapter(
        self,
        *,
        name: str,
        rank: Optional[int] = None,
        learning_rate: Optional[float] = None,
    ) -> ModelAdapter:
        
        response = self._api_instance.create_model(
            create_model_body_params=CreateModelBodyParams(
                initial_hyperparameters=CreateModelBodyParamsInitialHyperparameters(
                    lora_hyperparameters=CreateModelBodyParamsInitialHyperparametersLoraHyperparameters(
                        rank=rank
                    ),
                    training_arguments=CreateModelBodyParamsInitialHyperparametersTrainingArguments(
                        learning_rate=learning_rate
                    ),
                ),
                model=CreateModelBodyParamsModel(
                    name=name, base_model_id=self._id
                ),
            ),
            x_gradient_workspace_id=self._workspace_id,
        )
        return ModelAdapter(
            api_instance=self._api_instance,
            base_model_id=self._id,
            id=response.id,
            name=name,
            workspace_id=self._workspace_id,
        )
