import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

frmttr = logging.Formatter(
    '%(asctime)-30s, %(levelname)-15s, %(name)-15s, %(message)s'
)

file_handler = logging.FileHandler("/var/www/html/items-rest/resources/requests_log/reqlog.log")
# file_handler = logging.FileHandler("/tmp/req_log.log")

file_handler.setLevel(logging.INFO)

file_handler.setFormatter(frmttr)
logger.addHandler(file_handler)
