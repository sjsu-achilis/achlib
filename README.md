## achlib
### contains basic config, logger, db connection

to install : pip install git+https://github.com/sjsu-achilis/achlib.git#egg=achlib</br>
###to get config:
from achlib.config import file_config</br>
config = file_config()</br>
config.get('SECTION','key')</br>

###for logging:
from achlib.util import logger</br>
log = logger.getLogger(__name__)</br>
log.info("for info")</br>
log.error("for error")</br>
log.exception("for raising exception")</br>

###for db querry
from achlib.util.dbutil import db_fetch, db_insup, close_pool</br>
res = db_fetch('select querry',fetch=100)  <-- to fetch 1st n results</br>
res = db_fetch('select querry')  <-- to fetch all</br>
db_insup('insert or update querry')</br>
close_pool() <-- to destroy db connection pool</br>
