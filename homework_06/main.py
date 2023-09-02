import logging
import time


class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # logger.info(...)
        self.end_time = time.time()
        difference_time = self.end_time - self.start_time
        logging.info(f"Время выполнения: {difference_time} секунд")


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContext():
    time.sleep(2)
