import logging

filehandler = logging.FileHandler(filename="output.log")
filehandler.setLevel(level=logging.INFO)

streamhandler = logging.StreamHandler() # stdout stderr
streamhandler.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.addHandler(filehandler)
logger.addHandler(streamhandler)
logger.setLevel(logging.DEBUG)

logger.info("Hello, world!")
logger.debug("Debug")