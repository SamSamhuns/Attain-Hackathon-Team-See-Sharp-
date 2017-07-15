import json


def get_ID_by_name(country_name):
    with open('test.json') as data_file:
        data = json.load(data_file)
        return list(data.keys())[list(data.values()).index('China')]

def get_name_by_ID(country_id):
    with open('test.json') as data_file:
        data = json.load(data_file)
        return data[country_id]
