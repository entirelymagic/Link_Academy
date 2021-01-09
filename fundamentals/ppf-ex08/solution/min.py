sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

# Your code here
for k in sampleDict:
    if sampleDict[k] == min(sampleDict.values()):
        print(k)
        break
