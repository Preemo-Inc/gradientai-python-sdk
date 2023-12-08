from typing import Optional

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


class BaseModel(Model):
    _slug: str

    def __init__(
        self, *, api_instance: ModelsApi, id: str, slug: str, workspace_id: str
    ) -> None:
        super().__init__(
            api_instance=api_instance, id=id, workspace_id=workspace_id
        )
        self._slug = slug

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
