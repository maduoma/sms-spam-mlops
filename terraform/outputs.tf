output "endpoint_name" {
  value = aws_sagemaker_endpoint.ab_endpoint.name
}

output "cloudwatch_alarm" {
  value = aws_cloudwatch_metric_alarm.low_accuracy_alarm.arn
}
