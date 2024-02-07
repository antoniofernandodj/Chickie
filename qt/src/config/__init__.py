
from dynaconf import Dynaconf  # type: ignore
from os.path import join, dirname
from pathlib import Path

PROJECT_PATH = str(Path(dirname(__file__)).parent.absolute())


settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        join(PROJECT_PATH, "config", "settings.toml"),
        join(PROJECT_PATH, "config", ".secrets.toml")
    ]
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
