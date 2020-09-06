# sentry-alert-to-slack-with-functions

## Deploy

```shell
poetry export -f requirements.txt > requirements.txt
gcloud functions deploy sentry-alert-to-slack-with-functions --runtime python37 --trigger-http --entry-point entry_point --region {region} --set-env-vars SLACK_ENDPOINT={SLACK_WEBHOOK_ENDPOINT}
```

## Example alert

```
An error occurred, for details from the issue below url.
https://sentry.io/organizations/{project_name}/issues/{id}/?referrer=webhooks_plugin
```
