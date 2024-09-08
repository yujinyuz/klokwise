from litestar import post
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.response import Template


@post("/session/{session_id:int}/toggle-work", request_class=HTMXRequest)
async def toggle_work(request: HTMXRequest, session_id: int) -> Template:
    print(f"Current session: {session_id}")

    htmx = request.htmx

    if htmx:
        print(htmx.current_url)

    context = {}

    return HTMXTemplate(template_name="partials/sample.html", context=context)
