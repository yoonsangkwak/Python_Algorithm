my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

for value in my_family.values():
    print(value)

print()

print(my_family.keys())

print()
for key in my_family.keys():
    value = my_family[key]
    print(key, value)

print()
for key, value in my_family.items():
    print(key, value)