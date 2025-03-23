resource "aws_cloudwatch_metric_alarm" "low_accuracy_alarm" {
  alarm_name                = "sagemaker-low-accuracy"
  comparison_operator       = "LessThanThreshold"
  evaluation_periods        = "1"
  metric_name               = "Accuracy"
  namespace                 = "SageMaker/Endpoints"
  period                    = 60
  statistic                 = "Average"
  threshold                 = 0.90
  alarm_description         = "Alarm if endpoint accuracy drops below 90%"
  alarm_actions             = [aws_lambda_function.traffic_shift.arn]

  dimensions = {
    EndpointName = var.endpoint_name
  }
}

resource "aws_cloudwatch_metric_alarm" "high_latency_alarm" {
  alarm_name          = "sagemaker-high-latency"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "ModelLatency"
  namespace           = "AWS/SageMaker"
  period              = 60
  statistic           = "Average"
  threshold           = 3000 # 3 seconds
  alarm_actions       = [aws_lambda_function.traffic_shift.arn]

  dimensions = {
    EndpointName = var.endpoint_name
  }
}

