import sentry_sdk

sentry_sdk.init(
    "https://3bb1bdb8bd5847afb2eaa62f7af6aa34@o987609.ingest.sentry.io/5944553",
)

division_by_zero = 1 / 0
