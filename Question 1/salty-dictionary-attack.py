import hashlib

pw_file = open('rockyou.txt', 'r')

corp_file = open('salty-digitalcorp.txt', 'r')

hashed_pw = {}
for line in corp_file:
    split = line.strip().split(',')
    if split[0] == "username":
        continue
    hashed_pw[split[0]] = (split[1], split[2])

#print(hashed_pw)
corp_file.close()

result = {}
for line in pw_file:

    for user, (salt, hashed) in hashed_pw.items():

        hash_app = hashlib.sha512(f"{line.strip()}{salt}".encode("utf-8")).hexdigest()
        hash_pre = hashlib.sha512(f"{salt}{line.strip()}".encode("utf-8")).hexdigest()

        if hashed == hash_pre:
            print("Salt is prepended.")
            result[user] = line.strip()
        elif hashed == hash_app:
            print("Salt is appended.")
            result[user] = line.strip()

print(result)


