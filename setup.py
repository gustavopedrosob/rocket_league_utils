from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rocket-league-utils",
    version="0.0.2",
    author="TheVicio",
    author_email="thevicio27@gmail.com",
    description="An easy way to interact with Rocket League data.",
    long_description=long_description,
    url="https://github.com/TheVicio/Rocket-League-Utils",
    project_urls={
        "Bug Tracker": "https://github.com/TheVicio/Rocket-League-Utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6"
)
