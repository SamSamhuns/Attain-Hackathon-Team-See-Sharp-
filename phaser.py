import json

def get_ID_by_name(country_name):
    with open('test.json') as data_file:
        data = json.load(data_file)
        return list(data['id_dic'].keys())[list(data['id_dic'].values()).index(country_name)]

def get_name_by_ID(country_id):
    with open('test.json') as data_file:
        data = json.load(data_file)
        return data['id_dic'][country_id]

def get_region(country_id):
    with open('test.json') as data_file:
        data = json.load(data_file)
        return data['region_dic'][country_id]
