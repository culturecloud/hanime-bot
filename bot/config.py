import logging

from os import environ, getenv

if not "TZ" in environ:
    environ["TZ"] = "Asia/Dhaka"

PORT = int(getenv("PORT", "7860"))
HANIME_EMAIL = getenv("HANIME_EMAIL")
HANIME_PASS = getenv("HANIME_PASS")

LOG_LEVEL = logging.getLevelName(getenv("LOG_LEVEL", "INFO"))
JSON_LOGS = True if getenv("JSON_LOGS", "False") == "true" else False
