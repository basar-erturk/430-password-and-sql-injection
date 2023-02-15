import hashlib
import itertools

pw_file = open('rockyou.txt', 'r')

corp_file = open('keystreching-digitalcorp.txt', 'r')

hashed_pw = {}
for line in corp_file:
    split = line.strip().split(',')
    if split[0] == "username":
        continue
    hashed_pw[split[0]] = (split[1], split[2])

# print(hashed_pw)
corp_file.close()

result = {}
for line in pw_file:

    for user, (salt, hashed) in hashed_pw.items():

        pw = line.strip()
        hash_pw_salt, hash_salt_pw, pw_salt_hash, pw_hash_salt, salt_pw_hash, salt_hash_pw = itertools.repeat("", 6)
        for i in range(2000):
            hash_pw_salt = hashlib.sha512(f"{hash_pw_salt}{pw}{salt}".encode("utf-8")).hexdigest()
            hash_salt_pw = hashlib.sha512(f"{hash_salt_pw}{salt}{pw}".encode("utf-8")).hexdigest()
            pw_hash_salt = hashlib.sha512(f"{pw}{pw_hash_salt}{salt}".encode("utf-8")).hexdigest()
            pw_salt_hash = hashlib.sha512(f"{pw}{salt}{pw_salt_hash}".encode("utf-8")).hexdigest()
            salt_pw_hash = hashlib.sha512(f"{salt}{pw}{salt_pw_hash}".encode("utf-8")).hexdigest()
            salt_hash_pw = hashlib.sha512(f"{salt_hash_pw}{salt}{pw}".encode("utf-8")).hexdigest()

            as_list = [hash_pw_salt, hash_salt_pw, pw_hash_salt, pw_salt_hash, salt_pw_hash, salt_hash_pw]
            if hashed in as_list:
                result[user] = pw
                print(f"Number of hashes:{i}")
                print(as_list.index(hashed))  # index from the as_list list gives the combination
                break

print(result)
