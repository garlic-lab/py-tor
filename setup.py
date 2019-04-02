from setuptools import setup, find_packages

setup(
    name="py-tor",
    version="0.1",
    packages=find_packages(),
    install_requires=['Click==7.0'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'py-tor = py_tor:main',
        ],
    },

    author="Lorenzo D'Isidoro",
    author_email="lorenzo.disidoro@gmail.com",
    description="Setup and manage Tor process.",
    license="MIT",
    keywords="tor",
    url="https://github.com/garlic-lab/py-tor",
)