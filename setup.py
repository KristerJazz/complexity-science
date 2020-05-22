import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "complexity-science",
        version = "0.0.6",
        author = "Krister Jazz Urog",
        author_email = "kristerjazz.urog@gmail.com",
        description = "A package for complexity science research",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/complexity-science",
        packages = setuptools.find_packages(),
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
        ],
        python_requires = '>3.6',
        install_requires = [
            "numpy",
            "matplotlib",
            "pandas"
            ]
        )
