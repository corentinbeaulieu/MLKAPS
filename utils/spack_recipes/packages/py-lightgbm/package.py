# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLightgbm(PythonPackage):
    """LightGBM is a gradient boosting framework that uses tree
    based learning algorithms."""

    homepage = "https://github.com/microsoft/LightGBM"
    pypi = "lightgbm/lightgbm-4.5.0.tar.gz"

    license("MIT")

    version("4.5.0", sha256="e1cd7baf0318d4e308a26575a63a4635f08df866ad3622a9d8e3d71d9637a1ba")
    version("3.1.1", sha256="babece2e3613e97748a67ed45387bb0e984bdb1f4126e39f010fbfe7503c7b20")

    depends_on("cxx", type="build")  # generated

    variant("mpi", default=False, description="Build with mpi support")

    depends_on("python@3.7:", when="@4.5:", type=("build", "run"))
    depends_on("py-scikit-build-core", when="@4.5:", type="build")
    depends_on("py-setuptools", when="@:4.5", type="build")
    # in newer pip versions --install-option does not exist
    depends_on("py-pip@:23.0", when="+mpi", type="build")
    depends_on("py-wheel", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    # https://github.com/microsoft/LightGBM/issues/6454
    # https://github.com/microsoft/LightGBM/pull/6439
    depends_on("py-numpy@:1", when="@:4.3", type=("build", "run"))
    depends_on("py-numpy@1.17:2", when="@4.5:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn@:0.21,0.22.1:", type=("build", "run"))
    depends_on("py-pandas@0.24:", when="@4.5:", type=("build", "run"))

    depends_on("cmake@3.8:", type="build")
    depends_on("ninja@1.11:", when="build")

    depends_on("mpi", when="+mpi")

    def install_options(self, spec, prefix):
        args = []

        if spec.satisfies("+mpi"):
            args.append("--mpi")

        return args
