from romanos import romano_a_entero


assert romano_a_entero('M') == 1000, "M es incorecto"
assert romano_a_entero('D') == 500
assert romano_a_entero('C') == 100
assert romano_a_entero('L') == 50
assert romano_a_entero('X') == 10
assert romano_a_entero('V') == 5
assert romano_a_entero('I') == 1, 'I es incorecto'
'''
print(romano_a_entero('Z'))
print(romano_a_entero(23))
'''