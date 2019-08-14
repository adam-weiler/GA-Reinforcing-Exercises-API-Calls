import requests

url = 'https://represent.opennorth.ca/'


def name_all_wards():
    ottawa_wards_response = requests.get(f'{url}/boundaries/?sets=ottawa-wards')
    ottawa_wards_json = ottawa_wards_response.json()
    # print(ottawa_wards_json['objects'])  # A dictionary containing all Ottawa political boundaries.

    print('All wards in the collection:')
    for ward in ottawa_wards_json['objects']:
        print(ward['name'])


def all_representatives():
    representatives_response = requests.get(f'{url}/representatives/')
    representatives_response_json = representatives_response.json()
    # print(representatives_response_json['objects'])  # A dictionary containing all representatives.

    print('All representatives in the collection:')
    for representative in representatives_response_json['objects']:
        print(f"{representative['name']}")


name_all_wards()
print()
all_representatives()


