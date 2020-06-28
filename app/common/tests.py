from django.test import TestCase

# Create your tests here.


s = 'Hello world'
l = 'Hi there , my name is blankdog'
split_nopam = s.split()
print(split_nopam)
print(type(split_nopam))

ids = '1;2;3;4;3;'[:-1]
# ids = '1'
idl = ids.split(';')
print(idl)

idset = set(idl)
print(idset)
