from romanos import *

# print(romano_a_entero('M'))
# print(romano_a_entero('D'))
# print(romano_a_entero('C'))
# print(romano_a_entero('L'))
# print(romano_a_entero('X'))
# print(romano_a_entero('V'))
# print(romano_a_entero('I'))
# print(romano_a_entero('Z'))
# print(romano_a_entero(23))

assert romano_a_entero('M') == 1000, 'M es incorecto'
assert romano_a_entero('D') == 500, 'D es incorecto'
assert romano_a_entero('C') == 100, 'C es incorecto'
assert romano_a_entero('L') == 50, 'L es incorecto'
assert romano_a_entero('X') == 10, 'X es incorecto'
assert romano_a_entero('V') == 5, 'V es incorecto'
assert romano_a_entero('I') == 1, 'I es incorecto'