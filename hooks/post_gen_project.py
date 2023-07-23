"""Post gen hook to clean files."""
import logging
import os
import shutil
import sys

_logger = logging.getLogger()


def log_hook():
    """Removes either requirements files and folder or the Pipfile."""
    _logger.info("Starting post gen hook")


def remove_line(filename, line_to_remove):
    """Removes a line from a file."""

    # Check if the file exists
    if not os.path.isfile(filename):
        _logger.warning("Error: The file %s does not exist.", filename)
        return

    try:
        with open(filename, "r", encoding="utf8") as file:
            lines = file.readlines()

        lines = [line for line in lines if line.strip() != line_to_remove]

        with open(filename, "w", encoding="utf8") as file:
            file.writelines(lines)
    except IOError as err:
        _logger.warning("Error: Unable to open the file %s. %s", filename, err)


def clean_extra_files():
    """Removes either requirements files and folder or the Pipfile."""
    to_delete = []

    if "{{ cookiecutter.use_checkov }}".lower() == "n":
        to_delete.append(".checkov.yml")

    if "{{ cookiecutter.license }}".lower() == "no":
        to_delete.append("LICENSE")

    if "{{ cookiecutter.use_github }}".lower() == "n":
        to_delete.append(".github")

    try:
        for file_or_dir in to_delete:
            if os.path.isfile(file_or_dir):
                os.remove(file_or_dir)
            else:
                shutil.rmtree(file_or_dir)
    except OSError as err:
        _logger.warning("While attempting to remove file(s) an error occurred")
        _logger.warning("Error: %s", err)
        sys.exit(1)


if __name__ == "__main__":
    log_hook()
    clean_extra_files()
    remove_line(".devcontainer/init.sh", "# shellcheck disable=all")
