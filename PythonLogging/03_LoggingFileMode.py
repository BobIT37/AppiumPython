import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s' ,filename="test2.log", datefmt='%d/%m/%y %H:%M:%S %p %A', level=logging.DEBUG, filemode="w")
logging.critical("This is critical msg")
logging.error("This is a error msg")
logging.warning("this is warning msg")
logging.info("This is a Info msg")
logging.debug("This is a Debug msg")