from setuptools import setup, find_packages

with open ("README.md", "r") as f:
    page_description = f.read()

with open ("requirements.txt") as f:
    requeriments = f.read().splitlines()

setup(
    name="package_name",
    version= "0.0.1",
    author="Arthur",
    author_email="arthur_tassinari@hotmail.com",
    description="tentando fazer o desafio",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tassinariarthur/desafios-dio",
    packages=find_packages(),
    install_requirements=requeriments,
    python_requirements=">=3.8",
)