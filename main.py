from formulas_logicas import *

p = Atom('p')
q = Atom('q')
A1 = Binary('Y', Negation(Atom('p')), Atom('q'))

print(A1)
print(A1.sub_forms())