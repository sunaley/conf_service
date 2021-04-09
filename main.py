import hug
from conf_service.converter import Renderer


@hug.get('/Dockerfile', examples="image=registry.gitlab.com/cloudybay/house:latest", output=hug.output_format.text)
@hug.cli()
def dockerfile(image):
    """Get Dockerfile with ptoject name"""

    renderer = Renderer('Dockerfile')
    return renderer.render(image=image)


@hug.get('/Dockerfile.base', examples="image=registry.gitlab.com/cloudybay/house:latest", output=hug.output_format.text)
@hug.cli()
def dockerfile_base(image):
    """Get Dockerfile.base with ptoject name"""
    renderer = Renderer('Dockerfile.base')
    return renderer.render(image=image)


@hug.get('/rsync_app.sh', output=hug.output_format.text)
@hug.cli()
def rsync_app():
    """Get rsync_app.sh with ptoject name"""
    renderer = Renderer('rsync_app.sh')
    return renderer.render()


@hug.get('/entrypoint.sh', examples="migrate=1&timedrive=1&timedrive_name=house_timdrived.py", output=hug.output_format.text)
@hug.cli()
def entrypoint(project,
               migrate:hug.types.boolean=False,
               collectstatic:hug.types.boolean=False,
               timedrive:hug.types.boolean=False,
               filedrive:hug.types.boolean=False,
               timedrive_name:hug.types.text='',
               filedrive_name:hug.types.text=''):
    """Get entrypoint.sh with ptoject name"""

    renderer = Renderer('entrypoint.sh')
    return renderer.render(
        project=project,
        migrate=migrate,
        collectstatic=collectstatic,
        timedrive=timedrive,
        filedrive=filedrive,
        timedrive_name=timedrive_name,
        filedrive_name=filedrive_name,
    )
