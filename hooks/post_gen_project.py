"""Post gen hook to clean files."""
import logging
import os
import shutil
import sys

_logger = logging.getLogger()


def log_hook():
    """Removes either requirements files and folder or the Pipfile."""
    _logger.info("Starting post gen hook")


def clean_extra_files():
    """Removes either requirements files and folder or the Pipfile."""
    to_delete = []

    if "{{ cookiecutter.use_checkov }}".lower() == "n":
        to_delete = to_delete + [".checkov.yml"]
        # TODO: remove checkov from .pre-commit-config.yaml

    if "{{ cookiecutter.license }}".lower() == "no":
        to_delete = to_delete + ["LICENSE"]

    try:
        for file_or_dir in to_delete:
            if os.path.isfile(file_or_dir):
                os.remove(file_or_dir)
            else:
                shutil.rmtree(file_or_dir)
    except OSError as e:
        _logger.warning("While attempting to remove file(s) an error occurred")
        _logger.warning(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    log_hook()
    clean_extra_files()