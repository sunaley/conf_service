from pathlib import Path, PurePath

from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).parent.parent


class Renderer:
    def __init__(self, template):
        self.env = Environment(
            loader=FileSystemLoader(PurePath(BASE_DIR, 'conf_service', 'templates'))
        )
        self.template = self.env.get_template(template)

    def render(self, **kwargs):
        render_result = self.template.render(**kwargs)
        return render_result
