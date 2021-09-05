import hashlib
import sentry_sdk
from sentry_sdk import set_tag


def before_send(event, hint):
    event["tags"]["birthday"] = hashlib.md5(
        event["tags"]["birthday"].encode()
    ).hexdigest()
    return event

sentry_sdk.init(
    "https://3bb1bdb8bd5847afb2eaa62f7af6aa34@o987609.ingest.sentry.io/5944553",
    traces_sample_rate=1.0,
    before_send=before_send,
)

set_tag("birthday", "2021-10-02")

division_by_zero = 1 / 0
