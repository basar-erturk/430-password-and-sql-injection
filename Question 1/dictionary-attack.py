import hashlib

dict_file = open('dict.csv', 'w+')
pw_file = open('rockyou.txt', 'r')

dict_file.write("password,hashed\n")

for line in pw_file:
    hash = hashlib.sha512(line.strip().encode("utf-8")).hexdigest()
    dict_file.write(f"{line.strip()},{hash}\n")

dict_file.close()
pw_file.close()

dict_file = open('dict.txt', 'r')

passwords = {}
for line in dict_file:
    lst = line.strip().split(",")
    corp_file = open('digitalcorp.txt', 'r')
    for line2 in corp_file:
        lst2 = line2.strip().split(",")
        if lst[1] == lst2[1]:
            passwords[lst2[0]] = lst[0]
    corp_file.close()

print(passwords)

dict_file.close()





