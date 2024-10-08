# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

# Package automatically generated using 'pip2spack' converter


class PyPymoo(PythonPackage):
    """
    Multi-Objective Optimization in Python
    """

    homepage = "https://pymoo.org"
    # pypi = "pymoo/pymoo-0.6.1.1.tar.gz"
    url = "https://files.pythonhosted.org/packages/65/98/7b655122e0e9beed69d5fd080e01db3170bc1943af2d8384d715e15db40a/pymoo-0.6.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
    maintainers("liuyangzhuan")

    license("Apache-2.0")

    version("0.6.1.1", sha256="993fbfb4a271b57c5bfe26b9835e61c10ddedde53193aae8339d0e80f5f4b563")
    version("0.5.0", sha256="2fbca1716f6b45e430197ce4ce2210070fd3b6b9ec6b17bb25d98486115272c2")
    version("0.4.2", sha256="6ec382a7d29c8775088eec7f245a30fd384b42c40f230018dea0e3bcd9aabdf1")

    depends_on("cxx", type="build")  # generated

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-autograd@1.4:", when="@0.6.1.1", type=("build", "run"))

    depends_on("py-numpy@1.15:", when="@0.6.1.1", type=("build", "run"))
    depends_on("py-scipy@1.1:", when="@0.6.1.1", type=("build", "run"))
    depends_on("py-matplotlib@3:", when="@0.6.1.1", type=("build", "run"))
    depends_on("py-cma@3.2.2:", when="@0.6.1.1", type=("build", "run"))
    depends_on("py-dill", when="@0.6.1.1", type=("build", "run"))
    depends_on("py-deprecated", when="@0.6.1.1", type=("build", "run"))
    depends_on("py-alive-progress", when="@0.6.1.1", type=("build", "run"))
