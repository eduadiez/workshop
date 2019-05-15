import click
from eth_utils import to_checksum_address

@click.command()
@click.option(
    '-a', '--address'
)
def main(address):
    click.secho(to_checksum_address(address), fg='green')

if __name__ == "__main__":
    main()