from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="asadalpay",
    version="0.1.0",
    author="Bakhtiyar Sailauov",
    author_email="cena61454@gmail.com",
    description="A client for interacting with the AsadalPay API",
    long_description=long_description,
    url="https://github.com/bakhtiyarsailauov/asadalpay",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.26.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "requests-mock>=1.9.3",
        ]
    },
)
