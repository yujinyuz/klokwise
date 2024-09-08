from pathlib import Path
from litestar import get, Litestar
from litestar.response import Template
from litestar.template import TemplateConfig

from litestar.contrib.jinja import JinjaTemplateEngine

from . import controllers


@get("/")
async def index() -> Template:
    return Template(template_name="pages/index.html", context={"name": "World"})


template_config = TemplateConfig(
    directory=Path(__file__).parent / "templates",
    engine=JinjaTemplateEngine,
)


app = Litestar(
    route_handlers=[
        index,
        controllers.time_entry.toggle_work,
    ],
    template_config=template_config,
)
