# mbuild-fcc

Example of an `mBuild` recipe using `setuptools` `entry_points`.

This project contains an FCC lattice system, inheriting from `mbuild.Lattice`,
where the only input is an `mbuild.Compound` of choice.
That `Compound` will then be populated at all basis points of an FCC lattice ([0,0,0], [0.5,0.5,0], [0,0.5,0.5], [0.5,0,0.5]).

Note that this recipe does not include unit tests, this is meant to only be a tutorial and example system to showcase the `entry_points` feature now included with `mBuild`.
An actual recipe would require unit testing, continuous integration, etc.

See [this document for a step-by-step tutorial that follows with this repository.](https://github.com/mosdef-hub/mbuild/docs/recipe_development.rst) 
