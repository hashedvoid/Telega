import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="Telega",
    version="0.1",
    author="voidstring",
    author_email="voidstringgithub@gmail.com",
    description="A simple module for creating telegram bots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ootokonohito/Telega",
    packages=setuptools.find_packages(),
    license="GNU v3.0",
    keywords="Telegram",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU v3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    install_requires=[
        "requests"
    ]
)
