import logging
import click
from pathlib import Path

from .forecast import get_average_bakes

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument("file")
@click.option("--verbose", "-v", is_flag=True, help="Enable debug logging.")
def main(file: str, verbose: bool):
    file_path = Path(file)

    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled.")

    # Validate input
    if not file:
        logger.warning("No file path was provided.")
        click.echo("Usage: get_average_bakes <file_path>")
        return

    if not file_path.is_file():
        logger.warning("File not found error.")
        click.echo("Double check file path.")
        return

    logger.debug(f"Received verbose flag: {verbose}")
    logger.debug(f"Received file path: {file_path}")

    logger.info(f"Starting processing file '{file_path.name}'")

    result = get_average_bakes(file_path)

    click.echo("\n --RESULT--")
    logger.debug("Process finished with success.")
    logger.info (f"Recommended number of cookies to bake today is: {result:.1f}")
   
