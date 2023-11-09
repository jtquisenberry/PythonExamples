import logging
import sys
log_name = './my_log.log'
logging.basicConfig(filename=log_name,
                    filemode='a',
                    format='%(asctime)s, %(name)s %(levelname)s %(message)s',
                    level=logging.INFO)
logger = logging.getLogger("main")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.info("Test")
print("DONE")
