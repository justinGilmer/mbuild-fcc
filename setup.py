from setuptools import setup

setup(
    name="mbuild_fcc",
    install_requires="mbuild",
    entry_points={
        "mbuild.plugins":[
            "FCC = mbuild_fcc.mbuild_fcc:FCC"
        ]
    },
    py_modules=["mbuild_fcc"],
)

