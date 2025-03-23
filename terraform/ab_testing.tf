resource "aws_sagemaker_model" "model_a" {
  name               = var.model_a_name
  execution_role_arn = data.aws_iam_role.sagemaker_execution.arn
  primary_container {
    image           = "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.5-1"
    model_data_url  = "s3://${var.bucket}/${var.model_a_name}/output/model.tar.gz"
  }
}

resource "aws_sagemaker_model" "model_b" {
  name               = var.model_b_name
  execution_role_arn = data.aws_iam_role.sagemaker_execution.arn
  primary_container {
    image           = "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.5-1"
    model_data_url  = "s3://${var.bucket}/${var.model_b_name}/output/model.tar.gz"
  }
}

resource "aws_sagemaker_endpoint_configuration" "ab_config" {
  name = "${var.endpoint_name}-config"

  production_variants {
    variant_name           = "VariantA"
    model_name             = aws_sagemaker_model.model_a.name
    initial_instance_count = 1
    instance_type          = "ml.m5.large"
    initial_variant_weight = 90
  }

  production_variants {
    variant_name           = "VariantB"
    model_name             = aws_sagemaker_model.model_b.name
    initial_instance_count = 1
    instance_type          = "ml.m5.large"
    initial_variant_weight = 10
  }
}

resource "aws_sagemaker_endpoint" "ab_endpoint" {
  name                 = var.endpoint_name
  endpoint_config_name = aws_sagemaker_endpoint_configuration.ab_config.name
}
