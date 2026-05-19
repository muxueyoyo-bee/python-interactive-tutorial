import click

@click.command()
click.option('--home', type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Changes the folder to operate on.')
click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode.')
def cli():
    click.echo('Hello, World!')