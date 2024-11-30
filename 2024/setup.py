#!/usr/bin/env python3

from datetime import date
import shutil
import sys
from bs4 import BeautifulSoup
import requests
import logging
from pathlib import Path
from typing import Optional


YEAR = "2024"
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def validate_day(day: int) -> None:
    """Validate that the day is within the valid range for Advent of Code."""
    if not 1 <= day <= 25:
        logger.error("❌ Day must be between 1 and 25")
        sys.exit(1)


def get_day() -> str:
    """Determine day to set up based on command line args or current date."""
    day_num = date.today().day
    if len(sys.argv) > 1:
        try:
            day_num = int(sys.argv[1])
        except ValueError:
            logger.error("❌ Day must be a number")

    validate_day(day_num)
    return str(day_num)


def create_directory(path: Path) -> None:
    """Create a new directory for the day if it doesn't exist."""
    try:
        if path.exists():
            logger.info(f"✅ Directory {path} already exists")
        else:
            path.mkdir(exist_ok=True)
            logger.info(f"✅ Created directory {path}")
    except PermissionError:
        logger.error(f"❌ Permission denied when creating directory {path}")


def copy_template(template_path: Path, destination: Path) -> None:
    """Copy template program to the new directory if it doesn't exist."""
    if destination.exists():
        logger.info(f"✅ Program file {destination} already exists")
        return

    try:
        shutil.copy(template_path, destination)
        logger.info(f"✅ Copied template program to {destination}")
    except FileNotFoundError:
        logger.error(f"❌ Template file not found at {template_path}")
    except PermissionError:
        logger.error(f"❌ Permission denied when copying template to {destination}")


def fetch_test_input(day: str) -> Optional[str]:
    """Fetch test input from Advent of Code site."""
    url = f"https://adventofcode.com/{YEAR}/day/{day}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        pre_element = soup.find("pre")

        if pre_element is None:
            logger.warning("❌ No test input found on the page")
            return None

        return pre_element.get_text(strip=True)
    except requests.RequestException as e:
        logger.error(f"❌ Failed to fetch test input: {e}")
        return None


def create_input_file(path: Path, content: Optional[str] = None) -> None:
    """Create input file with optional content if it doesn't exist."""
    if path.exists():
        logger.info(f"✅ Input file {path} already exists")
        return

    try:
        with path.open("w") as f:
            if content:
                f.write(content)
            logger.info(
                f"✅ Created {'empty ' if not content else ''}input file {path}"
            )
    except IOError as e:
        logger.error(f"❌ Failed to create input file {path}: {e}")
        sys.exit(1)


def main():
    # Get the day and set up paths
    day = get_day()
    base_path = Path(f"day{day.zfill(2)}")
    template_path = Path("template.py")
    program_path = base_path / "program.py"
    test_path = base_path / "test.txt"
    input_path = base_path / "input.txt"

    logger.info(f"Setting up AOC {YEAR} day {day}...")

    # Create directory and set up files
    create_directory(base_path)
    copy_template(template_path, program_path)

    # Set up test input
    test_input = fetch_test_input(day)
    create_input_file(test_path, test_input)

    # Set up input
    create_input_file(input_path)


if __name__ == "__main__":
    main()
