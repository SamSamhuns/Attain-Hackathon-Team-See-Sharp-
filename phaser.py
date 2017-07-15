import json

def get_ID_by_name(country_name):
    with open('dic.json') as data_file:
        data = (json.load(data_file))['id_dic']
        return list(data.keys())[list(data.values()).index(country_name)]

def get_name_by_ID(country_id):
    with open('dic.json') as data_file:
        data = (json.load(data_file))['id_dic']
        return data[country_id]

def get_region(country_id):
    with open('dic.json') as data_file:
        data = (json.load(data_file))['region_dic']
        return data[country_id]

def get_ID_by_region(region_name):
    with open('region.json') as data_file:
        data = json.load(data_file)
        return list(data.key())[list(data.values()).index(region_name)]

def get_region_by_ID(region_id):
    with open('region.json') as data_file:
        data = json.load(data_file)
        return data[region_id]

def get_countries(region_id):
    with open('dic.json') as data_file:
        data = (json.load(data_file))['region_dic']
        r = []
        for k, v in data.items():
            if v == region_id:
                r.append(k)
        return r
