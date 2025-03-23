variable "region" {
  default = "us-east-1"
}

variable "model_a_name" {
  description = "Name of Model A (baseline)"
}

variable "model_b_name" {
  description = "Name of Model B (canary)"
}

variable "endpoint_name" {
  description = "SageMaker endpoint name"
  default     = "sms-ab-endpoint"
}

variable "bucket" {
  description = "S3 bucket for artifacts"
}
