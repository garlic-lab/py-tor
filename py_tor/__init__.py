import click
import py_tor.commands.install as install_command
import py_tor.commands.tor as tor_command


@click.group()
def main():
    """
    CLI to setup and manage Tor process
    """
    pass

@main.command()
def install():
    """Install CLI dependencies"""
    install_command.install_all()

@main.command()
@click.argument('service')
@click.option('--interface', default="Wi-Fi", help="Tor interface, default: 'Wi-Fi'")
def tor(service, interface):
    """Command to manage tor process, argument 'start', 'stop' or 'status'"""
    services = ["start", "stop", "status"]
    if services.index(service) >= 0:
        if service == "start" or service == "stop":
            tor_command.run(service, interface)
        if service == "status":
            tor_command.status()
    else:
        print("Service argument not defined, accepted arguments 'start' or 'stop'")