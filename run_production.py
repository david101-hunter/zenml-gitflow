#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.


from pipelines import production_train_and_deploy_pipeline
from steps import (
    deployment_trigger,
    evaluator,
    model_deployer,
    svc_trainer_mlflow,
    training_data_loader,
    TrainerParams
)
from utils.kubeflow_helper import get_kubeflow_settings

def main():

    # initialize and run the training pipeline
    training_pipeline_instance = production_train_and_deploy_pipeline(
        training_data_loader=training_data_loader(),
        trainer=svc_trainer_mlflow(
            params=TrainerParams(
                degree=2,
            )
        ),
        evaluator=evaluator(),
        deployment_trigger=deployment_trigger(),
        model_deployer=model_deployer,
    )
    
    training_pipeline_instance.run(
         settings={
            "orchestrator.kubeflow": get_kubeflow_settings()
        }
    )


if __name__ == "__main__":
    main()