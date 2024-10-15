from setuptools import setup, find_packages

setup(
    name='morning_greetings',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "typer",     # For CLI interface
        "schedule",  # For task scheduling
    ],
    entry_points={
        'console_scripts': [
            'morning_greetings=main:app',  # Optionally, if you want to run it via a command
        ],
    },
    description='A package to automate sending personalized morning messages.',
    author='Awar Abdulkarim'
)
