#!/usr/bin/env python
# Download and move snippets to the desired place
# Not ready yet

import click


MY_REPO = 'https://github.com/prokaktus/snippets/blob/master/'


@click.group()
def cli():
    pass


@cli.command()
@click.argument('django', default='default', required=False)
@click.option('--to', required=True)
def django(django, to):
    pass


cli.add_command(django)


if __name__ == '__main__':
    cli()
