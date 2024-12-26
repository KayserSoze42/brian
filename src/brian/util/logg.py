import logging

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# abs deez nuts
def logInfo(message):
    logging.info("\n\n*#*#*#*#*#*\n" + message + "\n")

def logError(message, exci=False):
    logging.error("\n\n*#*#*#*#*#*\n" + message + "\n", exc_info=exci)
