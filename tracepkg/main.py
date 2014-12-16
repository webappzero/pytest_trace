import click

@click.command()
def cli():
    """Example script."""
    click.echo('You called the cli function in main.py in tracepkg.')