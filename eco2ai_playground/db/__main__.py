import argparse
import os
from pathlib import Path

from alembic.config import CommandLine, Config
from eco2ai_playground.core.settings import settings

DEFAULT_DB_URL = settings.DATABASE_URL_FOR_MIGRATE
PROJECT_PATH = Path(__file__).parent.parent.resolve()


def make_alembic_config(cmd_opts):
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(PROJECT_PATH, cmd_opts.config)

    config = Config(
        file_=cmd_opts.config, ini_section=cmd_opts.name, cmd_opts=cmd_opts
    )

    alembic_location = config.get_main_option("script_location")
    if not os.path.isabs(alembic_location):
        config.set_main_option(
            "script_location", os.path.join(PROJECT_PATH, alembic_location)
        )
    if cmd_opts.db_url:
        config.set_main_option("sqlalchemy.url", cmd_opts.db_url)

    return config


def main():
    alembic = CommandLine()
    alembic.parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter
    alembic.parser.add_argument(
        "--db-url",
        default=os.getenv("DB_URL", DEFAULT_DB_URL),
        help="Database URL [env var: DB_URL]",
    )

    options = alembic.parser.parse_args()
    if "cmd" not in options:
        alembic.parser.error("too few arguments")
    else:
        config = make_alembic_config(options)
        exit(alembic.run_cmd(config, options))


if __name__ == "__main__":
    main()
