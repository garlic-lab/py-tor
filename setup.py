from setuptools import setup, find_packages

setup(
    name="pumpkin",
    version="0.1",
    packages=find_packages(),
    install_requires=['Click==7.0', 'requests==2.21.0', 'requests[socks]', 'PySocks==1.7.1'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pumpkin = pumpkin:main',
        ],
    },

    author="Lorenzo D'Isidoro",
    author_email="lorenzo.disidoro@gmail.com",
    description="Setup and manage Tor process.",
    license="MIT",
    keywords="tor",
    url="https://github.com/lorenzodisidoro/pumpkin",
)