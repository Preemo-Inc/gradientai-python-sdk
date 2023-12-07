from typing import List, TypedDict, Union

from typing_extensions import NotRequired

from gradientai._model import Model
from gradientai.openapi.client.api.models_api import ModelsApi
from gradientai.openapi.client.models.fine_tune_model_body_params import (
    FineTuneModelBodyParams,
)
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner import (
    FineTuneModelBodyParamsSamplesInner,
)
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_fine_tuning_parameters import (
    FineTuneModelBodyParamsSamplesInnerFineTuningParameters,
)
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_inputs import (
    FineTuneModelBodyParamsSamplesInnerInputs,
)
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_inputs_any_of_inner import (
    FineTuneModelBodyParamsSamplesInnerInputsAnyOfInner,
)
from gradientai.pydantic_models.types import FineTuneResponse


class StructuredInput(TypedDict):
    parse_special_tokens: NotRequired[bool]
    trainable: NotRequired[bool]
    value: str


class Sample(TypedDict):
    inputs: Union[str, List[StructuredInput]]
    multiplier: NotRequired[float]


class ModelAdapter(Model):
    _base_model_id: str
    _name: str

    def __init__(
        self,
        *,
        api_instance: ModelsApi,
        id: str,
        base_model_id: str,
        name: str,
        workspace_id: str,
    ) -> None:
        super().__init__(
            api_instance=api_instance, id=id, workspace_id=workspace_id
        )
        self._base_model_id = base_model_id
        self._name = name

    @property
    def base_model_id(self) -> str:
        return self._base_model_id

    @property
    def name(self) -> str:
        return self._name

    def delete(self) -> None:
        self._api_instance.delete_model(
            id=self._id, x_gradient_workspace_id=self._workspace_id
        )

    def fine_tune(
        self,
        *,
        samples: List[Sample],
    ) -> FineTuneResponse:
        fine_tune_samples = []
        for sample in samples:
            inputs: Union[str, List[FineTuneModelBodyParamsSamplesInnerInputsAnyOfInner]]
            if isinstance(sample["inputs"], list):
                inputs = [
                    FineTuneModelBodyParamsSamplesInnerInputsAnyOfInner(**input_)
                    for input_ in sample["inputs"]
                ]
            elif isinstance(sample["inputs"], str):
                inputs = sample["inputs"]
            else:
                raise TypeError('received unexpected type for sample inputs')

            fine_tune_samples.append(
                FineTuneModelBodyParamsSamplesInner(
                    fine_tuning_parameters=FineTuneModelBodyParamsSamplesInnerFineTuningParameters(
                        multiplier=sample["multiplier"]
                        if "multiplier" in sample
                        else None
                    ),
                    inputs=FineTuneModelBodyParamsSamplesInnerInputs(inputs),
                )
            )

        response = self._api_instance.fine_tune_model(
            id=self._id,
            x_gradient_workspace_id=self._workspace_id,
            fine_tune_model_body_params=FineTuneModelBodyParams(
                samples=fine_tune_samples,
            ),
        )
        return FineTuneResponse(
            number_of_trainable_tokens=response.number_of_trainable_tokens,
            sum_loss=response.sum_loss,
        )
