from datetime import date

import typer
from jinja2 import Template

from app.config.helpers import TEMPLATE, get_config_path

app = typer.Typer(no_args_is_help=True)


def metadata_init():
    """Create a default metadata file, overwrite any existing."""
    data = {
        "title": "API Template",
        "desc": "Run 'api-admin custom metadata' to change this information.",
        "repo": "https://github.com/seapagan/fastapi-template",
        "license": {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
        },
        "author": "Grant Ramsay (seapagan)",
        "website": "https://www.gnramsay.com",
        "email": "seapagan@gmail.com",
        "this_year": date.today().year,
    }

    out = Template(TEMPLATE).render(data)
    try:
        with open(get_config_path(), "w", encoding="UTF-8") as file:
            file.write(out)
    except OSError as err:
        print(f"Cannot Write the metadata : {err}")
