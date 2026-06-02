import logging

def setup_logger():
    logging.basicConfig(
        filename="logs/test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
logger = logging.getLogger(__name__)