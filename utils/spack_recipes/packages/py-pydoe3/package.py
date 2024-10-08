# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyPydoe3(PythonPackage):
    """Design of experiments for Python"""

    url = "https://files.pythonhosted.org/packages/4e/c4/adf186c5d61793230e50027feb70b187dd82352112cec48a9d9ff0daedb1/pydoe3-1.0.4-py2.py3-none-any.whl"

    # maintainers = []

    license("BSD-3-Clause", checked_by="corentinbeaulieu")

    version("1.0.4", sha256="233b15a2191c70a0d35a1306d23c45423b2995472c2c1402a60fdf4408caf3dd")

    # General dependency
    depends_on("python@3.8:", type=("build", "run"))

    # Build dependency
    depends_on("py-hatchling", type="build")

    # Additional dependencies
    depends_on("py-numpy", type="run")
    depends_on("py-scipy", type="run")
