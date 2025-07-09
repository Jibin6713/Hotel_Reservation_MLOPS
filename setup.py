from setuptools import setup,find_packages

 
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name = "ML-OPS_Hotel_Reservation",
    version = 0.1,
    author = "Jibin Joy",
    packages = find_packages(),
    install_requires = requirements
)    