import sentry_sdk
from sentry_sdk import set_user

sentry_sdk.init(
    "https://3bb1bdb8bd5847afb2eaa62f7af6aa34@o987609.ingest.sentry.io/5944553",
)

set_user({"email": "sentry@pycon.kr", "name": "lee ho sung"})

# 개인정보가 포함되어 있지 않은 정보로 변경
set_user({"id": 14253})

division_by_zero = 1 / 0

