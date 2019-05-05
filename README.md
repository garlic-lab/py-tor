<p align="center">
    <img src="./etc/pumpkin.png" width="350">
</p>
<p align="center">
    CLI tool quick and dirty to setup and manage Tor, MAC spoofing, etc.
</p>

## Supported OS
- MacOS
- Linux

## Prerequisite
- Python 3 (more than [3.7.2](https://www.python.org/downloads/release/python-372/))


## Installation
Pull this repository using the following commands:
```sh
git clone https://github.com/lorenzodisidoro/pumpkin.git
```

go to pumpkin directory and install CLI using `install` script
```sh
$ bash ./scripts/install
```

## Usage

### Tor command
#### Startup
Use the following command to startup Tor using default configurations
```sh
pumpkin tor start
```

you can use the following options
- `--interface=INTERFACE` network interface (default value `Wi-Fi`)
- `--background=True` use to run process in background (default `False`)

#### Stop 
To stop Tor process and reset settings using the following command
```sh
pumpkin tor stop
```

#### Status
You can check if everything is ok click [here](https://check.torproject.org/) or use the following command
```sh
pumpkin tor status
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/lorenzodisidoro/pumpkin/blob/master/LICENSE) file for details.

*"Stay hungry stay anonymous."*
