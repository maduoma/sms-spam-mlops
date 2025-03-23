import boto3
import os


def lambda_handler(event, context):
    sm = boto3.client("sagemaker")
    endpoint_name = os.environ["ENDPOINT_NAME"]

    print(f"[INFO] Adjusting traffic weights for {endpoint_name}")

    sm.update_endpoint_weights_and_capacities(
        EndpointName=endpoint_name,
        DesiredWeightsAndCapacities=[
            {"VariantName": "VariantA", "DesiredWeight": 50},
            {"VariantName": "VariantB", "DesiredWeight": 50}
        ]
    )

    return {
        "statusCode": 200,
        "body": "Traffic shifted to 50/50"
    }