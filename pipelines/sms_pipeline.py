# pipelines/sms_pipeline.py

import os
import boto3
import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.processing import ProcessingInput, ProcessingOutput, ScriptProcessor
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.inputs import TrainingInput
from sagemaker.xgboost.estimator import XGBoost
from sagemaker.workflow.parameters import ParameterString
from sagemaker.workflow.pipeline_context import PipelineSession

role = sagemaker.get_execution_role()
region = boto3.Session().region_name
sagemaker_session = sagemaker.session.Session()
pipeline_session = PipelineSession()

# Parameters
input_data = ParameterString(name="InputData", default_value="s3://your-bucket/sms-spam/sms.tsv")

# ----------------- Step 1: Preprocessing ----------------- #
sklearn_processor = SKLearnProcessor(
    framework_version="1.2-1",
    role=role,
    instance_type="ml.m5.xlarge",
    instance_count=1,
    base_job_name="sms-preprocess",
    sagemaker_session=pipeline_session,
)

step_process = ProcessingStep(
    name="PreprocessSMS",
    processor=sklearn_processor,
    inputs=[ProcessingInput(source=input_data, destination="/opt/ml/processing/input")],
    outputs=[
        ProcessingOutput(output_name="train", source="/opt/ml/processing/output")
    ],
    code=os.path.join("..", "scripts", "sagemaker_preprocess.py")
)

# ----------------- Step 2: Training ----------------- #
xgb_estimator = XGBoost(
    entry_point=os.path.join("..", "scripts", "sagemaker_train.py"),
    framework_version="1.5-1",
    role=role,
    instance_type="ml.m5.xlarge",
    instance_count=1,
    output_path=f"s3://{sagemaker_session.default_bucket()}/sms-spam/output",
    base_job_name="sms-xgb-train",
    sagemaker_session=pipeline_session
)

step_train = TrainingStep(
    name="TrainXGBoostSMS",
    estimator=xgb_estimator,
    inputs={
        "train": TrainingInput(s3_data=step_process.properties.ProcessingOutputConfig.Outputs["train"].S3Output.S3Uri, content_type="application/x-npy")
    }
)

# ----------------- Final Pipeline ----------------- #
pipeline = Pipeline(
    name="SMS-Text-Classifier-Pipeline",
    parameters=[input_data],
    steps=[step_process, step_train],
    sagemaker_session=pipeline_session
)