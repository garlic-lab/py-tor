# py-tor
👻 Tool quick and dirty to setup and manage Tor process. Stay hungry stay anonymous.

## Supported OS
- OS X

## Prerequisite
- Python more than [3.7.2](https://www.python.org/downloads/release/python-372/)

## Installation

Pull repository using the following commands:
```sh
git clone https://github.com/garlic-lab/py-tor.git
cd py-tor/
```

install `py-tor` command using `install_cli` script
```sh
./scripts/install_cli
```

## Usage commands
### Install
Run `py-tor --help` command should display this
```sh
$ py-tor --help                   
Usage: py-tor [OPTIONS] COMMAND [ARGS]...

  CLI to setup and manage Tor process

Options:
  --help  Show this message and exit.

Commands:
  install  Install CLI dependencies
  tor      Command to manage tor process
```

so you can use the command `py-tor install` to install CLI dependencies.

### Tor
#### Startup
Use the following command to startup Tor using default configurations
```sh
py-tor tor start
```
and leaves the process pending.

Use `--interface=INTERFACE` to specify settings interface, default value `Wi-Fi`.

Stop Tor and reset settings using  the following command
```sh
py-tor tor stop
```

#### Status
You can check if everything is ok click [here](https://check.torproject.org/) or use the following command
```sh
py-tor tor status
```


## To do
- Add `background` argument
- Generate torc file and specify configuration file
- Support for linux
- Spoof mac address

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/garlic-lab/py-tor/blob/master/LICENSE) file for details.