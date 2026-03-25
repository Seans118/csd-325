print('Welcome to the program!')

beer=int(input('How many bottles of beer?'))

while beer > 0:
    if beer == 1:
        print(f'{beer} bottle of beer on the wall, {beer} bottle of beer')
        print(f'Take one down and pass it around, 0 bottles of beer.')
        break
    else:
        print(f'{beer} bottle(s) of beer on the wall, {beer} bottle(s) of beer.')
        beer = beer - 1
        print(f'Take one down and pass it around, {beer} bottle(s) of beer.')

print('Time to buy more beer!')