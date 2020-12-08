name = "gcc"

version = "6.4.0"

requires=["gmp-4.3.2+", "mpfr-3.1.0+", "mpc-1.0.1+"]

variants=[["platform-linux", "arch-x86_64"]]

tools = ["gcc", "g++", "gfortran"]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.GCC_CXX_INCLUDE_DIR="{root}/include/c++{version}"
    if building:
	env.CC="{root}/bin/gcc"
	env.CXX="{root}/bin/g++"


