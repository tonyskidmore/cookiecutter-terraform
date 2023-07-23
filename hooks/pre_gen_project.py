"""Pre gen hook """
import logging

_logger = logging.getLogger()


def log_hook():
    """Removes either requirements files and folder or the Pipfile."""
    _logger.info("Starting pre gen hook")


if __name__ == "__main__":
    log_hook()
