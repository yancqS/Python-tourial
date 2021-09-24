import pizza

pizza.make_pizza(16, 'a', 'b', 'c')
pizza.make_pizza(12, 'a', 'b')


from pizza import make_pizza

make_pizza(16, 'a', 'b', 'c')
make_pizza(12, 'a', 'b')


from pizza import make_pizza as mp

mp(16, 'a', 'b', 'c')
mp(12, 'a', 'b')

import pizza as p

p.make_pizza(16, 'a', 'b', 'c')
p.make_pizza(12, 'a', 'b')

from pizza import *

make_pizza(16, 'a', 'b', 'c')
make_pizza(12, 'a', 'b')
