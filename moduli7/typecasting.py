from pandas.io.sas.sas_constants import page_type_mask

from moduli6.main import result

age = 25

age_to_str = str(age)

print(age_to_str, type(age_to_str))

x= 32
y = 5.3

result = x+y
print(result,"of type", type(result))

a = 5
b = "3"

c = a * int(b)
print(c,"of type", type(c))