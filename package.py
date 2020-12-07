name = "gcc"
version = "4.8.3"

requires=["gmp-4.3.2+", "mpfr-3.1.0+", "mpc-1.0.1+"]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.LD_LIBRARY_PATH.append("{root}/lib64")


