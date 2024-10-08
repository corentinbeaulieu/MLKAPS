# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PySmt(PythonPackage):
    """The surrogate modeling toolbox (SMT) is a Python package that contains a collection of surrogate modeling methods, sampling techniques, and benchmarking functions. This package provides a library of surrogate models that is simple to use and facilitates the implementation of additional methods. SMT is different from existing surrogate modeling libraries because of its emphasis on derivatives, including training derivatives used for gradient-enhanced modeling, prediction derivatives, and derivatives with respect to the training data. It also includes new surrogate models that are not available elsewhere: kriging by partial-least squares reduction and energy-minimizing spline interpolation."""

    pypi = "smt/smt-2.6.3.tar.gz"

    license("BSD-3-Clause", checked_by="corentinbeaulieu")

    version("2.6.3", sha256="75ccc28200add5f50fc68c6515013373ea53a71169197167f85d15b4b53ebb5a")

    depends_on("cxx", type="build")

    # Build dependency
    depends_on("py-setuptools", type="build")

    # Additionnal dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-pydoe3", type=("build", "run"))
