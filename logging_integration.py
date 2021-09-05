import logging
import sentry_sdk

sentry_sdk.init(
    "https://3bb1bdb8bd5847afb2eaa62f7af6aa34@o987609.ingest.sentry.io/5944553",
    traces_sample_rate=1.0,
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("I am ignored")
logging.info("I am a breadcrumb")
logging.error("I am an event",
              extra={'event_name': 'PyCon2021'})
