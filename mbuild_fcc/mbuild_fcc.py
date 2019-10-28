import mbuild


class FCC(mbuild.Compound):
    """Create a mBuild Compound with a repeating unit of the FCC unit cell.

    Passing in a compound, unit cell length (nm), and the amount of repeat
        units in x, y, and z will generate a FCC lattice with clones of the
        passed-in compound at the lattice points. The lattice points of a FCC
        unit cell are the following in normalized values:

        [0.0, 0.0, 0.0]
        [0.5, 0.5, 0.0]
        [0.5, 0.0, 0.5]
        [0.0, 0.5, 0.5]

    Note that this is a sample recipe and is only intended to serve as
        an example rather showcasing the mBuild `entry_point` plugin system.
    A standard plugin would have additonal unit tests, as well as increased
        flexibility for inputs compared to this class.
    """

    def __init__(self, lattice_spacing=None, compound_to_add=None, x=1, y=1, z=1):
        super(FCC, self).__init__()
        lattice_points = {'A': [[0, 0, 0],
                                [0, 0.5, 0.5],
                                [0.5, 0.5, 0],
                                [0.5, 0, 0.5]]}
        angles = [90, 90, 90]

        fcc_lattice = mbuild.Lattice(lattice_spacing=lattice_spacing,
                                     angles=angles,
                                     lattice_points=lattice_points)
        self.add(fcc_lattice.populate(x=x, y=y, z=z,
                                      compound_dict={'A': compound_to_add}))


if __name__ == "__main__":
    au_fcc_lattice = FCC(lattice_spacing=0.40782,
                         compound_to_add=mbuild.Compound(name="Au"),
                         x=5, y=5, z=1)
    print(au_fcc_lattice)
