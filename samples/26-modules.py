# all modules included into functools.py        /usr/lib/python3.12/functools.py

# ls /usr/lib/python3.12 | grep all
# compileall.py
# tracemalloc.py

# ls /usr/lib/python3.12/ | grep random
# random.py

import random
print(random)  # get the module path
# \\wsl.localhost\Ubuntu\home\eraki\Documents\gitReposPersonal\Python

print(f"Print random float number: {random.random()}")  # Print random float number: 0.47063227586186196
print(dir(random))  # get all random module objects
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# import one or two functions from random module
from random import randint
# from random import randint, randrange  # import multiple functions from random module
# from random import *  # all
print(f"Print random interger {randint(100, 900)}")  # Print random interger 675
