# Get the decimal value
dec_number = int(input('Enter a decimal number: '))

binary_number = "{0:b}".format(dec_number)
print(binary_number)
binary_number = '{0:08b}'.format(dec_number)
print(binary_number)
binary_number = f'{dec_number:08b}'
print(binary_number)
binary = format(dec_number, "08b")
print(binary_number)