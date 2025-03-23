provider "aws" {
  region = var.region
}

module "sagemaker_ab_testing" {
  source      = "./modules/sagemaker_ab"
  model_a     = var.model_a_name
  model_b     = var.model_b_name
  endpoint    = var.endpoint_name
  bucket      = var.bucket
}
