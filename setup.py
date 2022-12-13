from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bakkes_mod_inventory",
    version="0.0.3",
    author="gustavopedrosob",
    author_email="thevicio27@gmail.com",
    description="Easy way to interact with your Bakkesmod inventory.",
    long_description=long_description,
    url="https://github.com/gustavopedrosob/bakkes_mod_inventory",
    project_urls={
        "Bug Tracker": "https://github.com/gustavopedrosob/bakkes_mod_inventory/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["bakkes_mod_inventory"],
    install_requires=["git+https://github.com/gustavopedrosob/rocket_league_utils"],
    python_requires=">=3.6"
)
