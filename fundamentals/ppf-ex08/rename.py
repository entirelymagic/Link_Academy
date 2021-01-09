sampleDict = {
    "name": "Kelly",
    "age": 25,
    "city": "New york",
    "salary": 8000,
}

# Your code here

for key in sampleDict:
    if key == "city":
        temp = sampleDict["city"]
        sampleDict.pop(key)
        sampleDict["location"] = temp
        break

print(sampleDict)
