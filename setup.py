from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rocket-league-utils",
    version="0.0.5",
    author="gustavopedrosob",
    author_email="thevicio27@gmail.com",
    description="An easy way to interact with Rocket League data.",
    long_description=long_description,
    url="https://github.com/gustavopedrosob/rocket_league_utils",
    project_urls={
        "Bug Tracker": "https://github.com/gustavopedrosob/rocket_league_utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["rocket_league_utils"],
    install_requires=["Unidecode", "numpy"],
    python_requires=">=3.6"
)
