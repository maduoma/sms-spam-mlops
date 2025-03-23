data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../lambda/lambda_canary_shift.py"
  output_path = "${path.module}/lambda_canary_shift.zip"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Effect = "Allow",
    }]
  })
}

resource "aws_lambda_function" "traffic_shift" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "canary-traffic-shift"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "lambda_canary_shift.lambda_handler"
  runtime          = "python3.9"
  timeout          = 10
  environment {
    variables = {
      ENDPOINT_NAME = var.endpoint_name
    }
  }
}

resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/canary-traffic-shift"
  retention_in_days = 7
}
