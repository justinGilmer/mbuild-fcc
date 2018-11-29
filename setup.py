from setuptools import setup

setup(
    name="mbuild-fcc",
    install_requires="mbuild",
    entry_points={"mbuild": ["fcc = mbuild_fcc"]},
    py_modules=["mbuild_fcc"],
)