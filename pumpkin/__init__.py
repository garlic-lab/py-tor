import click
import pumpkin.commands.tor as tor_command


@click.group()
def main():
    """
    CLI tool quick and dirty to setup and manage Tor process. Stay hungry stay anonymous.
    """
    pass

@main.command()
@click.argument('service')
@click.option('--interface', default="Wi-Fi", help="Tor interface, default: 'Wi-Fi'")
@click.option('--background', default=False, help="Use to run process in background, default: 'False'")
def tor(service, interface, background):
    """Manage Tor process using argument 'start', 'stop' and 'status'"""
    tor_command.run(service, interface, background)