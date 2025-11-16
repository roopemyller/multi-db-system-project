from setuptools import setup, find_packages


# define the setup for the dbaccess package
setup(
    name="dbaccess",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "psycopg2-binary",
    ],
    entry_points={
        "console_scripts": [
            "dbaccess=dbaccess_cli:app",
        ],
    },
    author="Roope Myller",
    description="Multi-database access CLI for camera equipment databases",
)