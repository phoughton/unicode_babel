import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unicode_babel",
    version="0.1.4",
    author="Peter Houghton",
    author_email="pete@investigatingsoftware.co.uk",
    description="A tool for generating random characters/code-points",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phoughton/unicode_babel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

