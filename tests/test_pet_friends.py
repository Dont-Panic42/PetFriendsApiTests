from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result



def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0



def test_add_new_pet_with_valid_data(name='Песель', animal_type= 'терьер', age='4', pet_photo='images/dog_1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_animal_type_pet_with_valid_data(name='Песель', animal_type= 'терьер', age='4', pet_photo='images/dog_1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['animal_type'] == animal_type

def test_add_new_age_pet_with_valid_data(name='Песель', animal_type= 'терьер', age='4', pet_photo='images/dog_1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age

def test_add_new_pet_photo_pet_with_valid_data(name='Песель', animal_type= 'терьер', age='4', pet_photo='images/dog_1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'pet_photo' in result



def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()



def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

def test_successful_update_animal_type_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['animal_type'] == animal_type
    else:
        raise Exception("There is no my pets")

def test_successful_update_age_self_pet_info(name='Мурзик', animal_type='Котэ', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['age'] == age
    else:
        raise Exception("There is no my pets")



def test_add_pet_without_photo(name='Барсик', animal_type='кот', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_pet_animal_type_without_photo(name='Барсик', animal_type='кот', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['animal_type'] == animal_type

def test_add_pet_age_without_photo(name='Барсик', animal_type='кот', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['age'] == age



def test_add_photo(pet_photo='images/dog_1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) >= 1:
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo(auth_key, pet_id, pet_photo)
    assert status == 200
    assert 'pet_photo' in result











