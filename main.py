import hashlib
with open('Git-2.39.2-64-bit.exe', 'rb') as f:
    hsh = hashlib.md5()
    while True:
        data = f.read(2048)
        if not data:
            break
        hsh.update(data)
    rez = hsh.hexdigest()

    print(rez)

    f.read()