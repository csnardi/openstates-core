from pathlib import Path
from spatula.cli import scrape
from .people import merge as people_merge
from .committees import merge as committees_merge
import click


@click.command()
@click.argument("abbr")
@click.argument("scraper_type")
@click.option("--scrape-only", help="Only perform scrape.", is_flag=True)
@click.option("--merge-only", help="Only perform merge.", is_flag=True)
@click.option(
    "--fastmode",
    help="Use a cache to avoid making unnecessary requests while developing.",
    is_flag=True,
)
@click.option(
    "--reset-offices",
    is_flag=True,
    help="Reset offices to latest scrape instead of trying to merge old with new.",
)
def main(
    abbr: str,
    scraper_type: str,
    scrape_only: bool,
    merge_only: bool,
    fastmode: bool,
    reset_offices: bool,
) -> None:
    output_dir = Path(f"_scrapes/{abbr}/{scraper_type}")
    if not merge_only:
        args = [
            f"scrapers_next.{abbr}.{scraper_type}",
            "-o",
            output_dir,
            "--rmdir",
        ]
        if fastmode:
            args.append("--fastmode")
        try:
            scrape(args)
        except SystemExit as e:
            if e.code != 0:
                raise
    if not scrape_only and "people" in scraper_type:
        merge_args = [abbr, str(output_dir)]
        if reset_offices:
            merge_args.append("--reset-offices")
        people_merge(merge_args)
    elif not scrape_only and "committees" in scraper_type:
        merge_args = [abbr, str(output_dir)]
        committees_merge(merge_args)


if __name__ == "__main__":
    main()
