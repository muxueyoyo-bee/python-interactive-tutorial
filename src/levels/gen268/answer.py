import click

@click.command()
click.option('--host', '-h', default='127.0.0.1', help='The interface to bind to.')
click.option('--port', '-p', default=5000, help='The port to bind to.')
def run_command():
    click.echo('Hello, World!')