import sentry_sdk
import logging

sentry_sdk.init(
    "https://3bb1bdb8bd5847afb2eaa62f7af6aa34@o987609.ingest.sentry.io/5944553",
    traces_sample_rate=1.0,
)

for i in [1, 2, None]:
    try:
        print(i / 0)
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.fingerprint = ['test zero division']
            logging.error("{} can not be divided by zero".format(i))
            continue
