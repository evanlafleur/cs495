

auth_code = []

# for i in range(0, 10000):
#     auth_code.append('%04d' % i)

for i in range(0, 10000):
    auth_code.append('%04d' % i)

auth_code2 = auth_code
for i in reversed(auth_code2):
    auth_code2.append('%04d' % int(i))

print (auth_code)
print (auth_code2)