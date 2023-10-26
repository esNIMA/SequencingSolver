import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SequencingSolver",
    version="1.0.2",
    author="Nima Mahmoodian",
    author_email="s.nima.mahmoodian@gmail.com",
    description="Package for solving various sequencing problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esNIMA/SequencingSolver",
    project_urls={
        "Bug Tracker": "https://github.com/esNIMA/SequencingSolver/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
