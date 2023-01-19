#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from zenml.integrations.deepchecks.steps import (
    DeepchecksDataDriftCheckStepParameters,
    deepchecks_data_drift_check_step,
    DeepchecksDataIntegrityCheckStepParameters,
    deepchecks_data_integrity_check_step,
)
from steps.data_loaders import DATASET_TARGET_COLUMN_NAME


data_integrity_checker = deepchecks_data_integrity_check_step(
    step_name="data_integrity_checker",
    params=DeepchecksDataIntegrityCheckStepParameters(
        dataset_kwargs=dict(
            label=DATASET_TARGET_COLUMN_NAME,
            cat_features=[],
        ),
    ),
)

data_drift_detector = deepchecks_data_drift_check_step(
    step_name="data_drift_detector",
    params=DeepchecksDataDriftCheckStepParameters(
        dataset_kwargs=dict(label=DATASET_TARGET_COLUMN_NAME, cat_features=[]),
    ),
)
