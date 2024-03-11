from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="style_bert_vits2",
    version="2.3.1",
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=Path(__file__).parent.joinpath(
        "requirements.txt").read_text().splitlines(),
)
