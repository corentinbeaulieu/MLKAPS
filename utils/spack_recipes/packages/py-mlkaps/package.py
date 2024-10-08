# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyMlkaps(PythonPackage):
    """Machine Learning for Accuracy and Performance Studies"""

    # Website homepage
    # homepage = "https://www.mlkaps.com"

    # This url corresponds to the preferred version to install
    url = "https://github.com/MLCGO/MLKAPS/archive/12166778525afd695dd163865610acb112f90ef9.tar.gz"

    # GitHub users in charge of this package
    # maintainers("Thukisdo", "titeup")

    # LICENSE notice
    license("BSD-3-Clause", checked_by="corentinbeaulieu")

    # Versions
    # The hash of main will change with the addition of the spack recipes
    # version("main", sha256="c9a227cdd39e794571be4a0c210ccde510de5e4ea56c1e81515688b12bf7c05f")
    version("first-commit", url="https://github.com/MLCGO/MLKAPS/archive/12166778525afd695dd163865610acb112f90ef9.tar.gz", sha256="1b7378002ab95ebdc8f65fb78afd2f8b3a9fc20c770f3445262b5c7bfc644fa4")

    # General dependency
    depends_on("python@3.10:3", type=("build", "run"))

    # Build dependency
    depends_on("py-flit-core@3.7:3", type="build")
    depends_on("swig", type="build")

    # Run dependencies
    depends_on("py-deprecated", type="run")
    depends_on("py-scikit-learn", type="run")
    depends_on("py-numpy@1.26", type="run")
    depends_on("py-pandas", type="run")
    depends_on("py-pymoo@0.6.1.1", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-smt", type="run")
    depends_on("py-tqdm", type="run")
    depends_on("py-lightgbm", type="run")
    depends_on("py-xgboost+pandas+plotting+scikit-learn", type="run")

    # Not listed in pyproject...
    depends_on("py-optuna", type="run")

    # Test dependencies
    depends_on("py-pytest", type=("run", "test"))

    # Checks
    sanity_check_is_dir = ["bin"]
    sanity_check_is_file = [join_path("bin", "mlkaps")]

    @run_after("install")
    def copy_test_files(self):
        """Copy the tests source directory into the spack cache directory"""
        cache_extra_test_sources(self, "tests")

    def test_help(self):
        """Ensure launching of the application invoking \"mklaps --help\" """
        prog = Executable(self.prefix.bin.mlkaps)
        prog("--help")

    def test_unit(self):
        """Launch unit tests"""
        with working_dir(self.test_suite.current_test_cache_dir.tests):
            pytest = Executable(self.spec["py-pytest"].prefix.bin.pytest)
            pytest("./unit")

    def test_integration(self):
        """Launch integration tests"""
        with working_dir(self.test_suite.current_test_cache_dir.tests):
            pytest = Executable(self.spec["py-pytest"].prefix.bin.pytest)
            pytest("./integration")
