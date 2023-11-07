from setuptools import setup

setup(
    name="efficiency",
    version="0.1",
    description="Boilerplate code for ML projects",
    author="Ojasv Kamal",
    author_email="kamalojasv2000",
    packages=["efficiency"],
    install_requires=[
        "PyYAML",
        "flake8",
        "black",
        "usort",
        "ufmt",
        "pre-commit",
        "prettier",
    ],
    zip_safe=False,
)
