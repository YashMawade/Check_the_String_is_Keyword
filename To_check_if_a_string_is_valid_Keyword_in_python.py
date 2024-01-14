import keyword
keys = ["for","Yash","else","if","Akash"]
for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
       print(keys[i] + " is python keyword")
    else:
       print(keys[i] + " is not python keyword")