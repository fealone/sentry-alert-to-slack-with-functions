# sentry-alert-to-slack-with-functions

## Deploy for GCP

```shell
poetry export -f requirements.txt > requirements.txt
gcloud functions deploy sentry-alert-to-slack-with-functions \
    --runtime python37 \
    --trigger-http \
    --entry-point entry_point \
    --region {region} \
    --set-env-vars SLACK_ENDPOINT={SLACK_WEBHOOK_ENDPOINT} \
    --set-env-vars PLATFORM=GCP
```

## Deploy for AWS

* Packaging

```shell
poetry export -f requirements.txt > requirements.txt
mkdir dist \
    && cp main.py dist/ \
    && pip install -r requirements.txt -t dist/ \
    && cd dist \
    && zip ../dist.zip * \
    && cd ../ \
    && rm -rf dist
```

* Deploy

```shell
aws lambda create-function \
    --function-name sentry-alert-to-slack-with-functions \
    --runtime python3.7 \
    --role {LambdaExecuteRole} \
    --handler entry_point \
    --zip-file fileb://dist.zip \
    --environment "Variables={SLACK_ENDPOINT={SLACK_WEBHOOK_ENDPOINT},PLATFORM=AWS}"
```

* Configure API Gateway
    - Supported REST API only

## Example alert

```
An error occurred, for details from the issue below url.
https://sentry.io/organizations/{project_name}/issues/{id}/?referrer=webhooks_plugin
```
