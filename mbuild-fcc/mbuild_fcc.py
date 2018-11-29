import mbuild


class FCC(mbuild.Lattice):
    """Test"""
    @mbuild.hookimpl
    def __init__(self):
        self.lattice_spacing=None
        self.lattice_vectors=None
        self.lattice_points={'A': [[0,0,0], [0, 0.5, 0.5],[0.5, 0.5, 0], [0.5, 0, 0.5]]}
        self.angles=[90, 90, 90]

        self = super(FCC, self).__init__(
            lattice_spacing=self.lattice_spacing,
            angles=self.angles,
            lattice_points=self.lattice_points)