import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="lynx",
    packages=setuptools.find_packages(where="./src/lynx",
                                      exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version="0.0.1",
    license='MIT',
    author="kmuumdmrj76",
    author_email="kmuumdmrj76@163.com",
    description="lynx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmuumdmrj76/lynx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    keywords=['lynx'],
    python_requires='>=3.6',
    install_requires=[
    ],
)
