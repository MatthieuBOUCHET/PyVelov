import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvelov",
    version="0.0.3",
    author="Matthieu BOUCHET",
    author_email="matthieu.bouchet@outlook.com",
    description="Package build to communication with VeloV API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatthieuBOUCHET/PyVelov",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    python_requires='>=3.0',
)