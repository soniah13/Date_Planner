from setuptools import setup, find_packages

setup(
    name="date-planner",
    version="1.0.0",
    packages=find_packages(include=["planner", "planner.*"]),
    entry_points={
        "console_scripts": [
            "date-planner=planner.plans:main",
        ],
    },
    include_package_data=True,
    install_requires=[],  # can add requirements later
)
