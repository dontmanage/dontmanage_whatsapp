from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dontmanage_whatsapp/__init__.py
from dontmanage_whatsapp import __version__ as version

setup(
    name="dontmanage_whatsapp",
    version=version,
    description="WhatsApp integration for dontmanage",
    author="Shridhar Patil",
    author_email="shridhar.p@zerodha.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
