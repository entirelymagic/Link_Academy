sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# Your code here
sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)