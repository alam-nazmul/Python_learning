client = {
    "name": "Nazmul Alam",
    "age": 32,
    "team": "SRE"
}

print(client["name"])

print(client.get("name"))
print(client.get("birthday", "25-Dec-1992"))