import json


def save_to_db(data):
    with open('database.txt', 'a+') as f:
        json.dump(data, f, sort_keys=True, indent=4)


def return_data():
    with open('database.txt') as f:
        data = json.load(f)
        jtopy = json.dumps(data)
        dict_json = json.loads(jtopy)
        print(dict_json)
        return data


return_data()
