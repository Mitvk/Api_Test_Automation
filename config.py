import requests
import logging

SESSION = requests.session() #creates session for all the req-res calls, SESSION is used as a global variable

APP_URL = 'http://127.0.0.1:8080'
ADMIN_USER = 'admin'
ADMIN_PASSWORD = 'admin'

LOG = logging.getLogger()

# extending the Filter class and creating a custom filter to hide the sensitive data
class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, "***")
        return True
# adding filtering to the logs generated
LOG.addFilter(HideSensitiveData())