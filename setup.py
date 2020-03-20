import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transipApiV6", # Replace with your own username
    version="0.0.2",
    author="Jeroen van Gemert",
    author_email="pypi@jeroen.van.gemert.net",
    description="Package to interact with the V6 API of Transip ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeromba6/transip_api_v6",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.x',
)