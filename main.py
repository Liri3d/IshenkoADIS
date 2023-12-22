import requests
import pytest
import time

payload1 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        }
    }
}

payload2 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        }
    }
}

payload3 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        },
        "fcontact": {
            "hasContact": True
        }
    }
}

payload4 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        },
        "fcontact": {
            "hasContact": False
        }
    }
}

payload5 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        },
        "fcontact": {
            "hasContact": False
        }
    }
}

payload6 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        },
        "fcontact": {
            "hasContact": True
        }
    }
}

payload7 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        }
    }
}

BASE_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

def test_get_student_list_hasGit_true():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload1)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
    print("test_get_student_list_hasGit_true completed successfully in", end_time-start_time, "seconds")

def test_get_student_list_hasGit_false():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload2)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит не пустое"
    print("test_get_student_list_hasGit_false completed successfully in", end_time-start_time, "seconds")

def test_get_student_list_hasGit_and_hasContact_true():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload3)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    print("test_get_student_list_hasGit_and_hasContact_true completed successfully in", end_time-start_time, "seconds")

def test_get_student_list_hasGit_and_hasContact_false():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload4)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит не пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"
    print("test_get_student_list_hasGit_and_hasContact_false completed successfully in", end_time-start_time, "seconds")

def test_get_student_list_hasGit_true_and_hasContact_false():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload5)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"
    print("test_get_student_list_hasGit_true_and_hasContact_false completed successfully in", end_time-start_time, "seconds")

def test_get_student_list_hasGit_false_and_hasContact_true():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload6)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит не пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    print("test_get_student_list_hasGit_false_and_hasContact_true completed successfully in", end_time-start_time, "seconds")

def test_get_student_list_hasGit_equals():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload7)
    response_body = response.json()
    response1 = requests.post(f'{BASE_URL}', json=payload7)
    response_body1 = response.json()
    end_time = time.time()
    assert response.status_code == 200
    assert response_body["info"][0]["fgit"]["hasGit"] == True, "Поле Гит пустое"
    assert response1.status_code == 200
    assert response_body1["info"][0]["fgit"]["hasGit"] == True, "Поле Гит пустое"
    assert response_body["info"][0]["id"] == response_body1["info"][0]["id"], "Данные не совпадают"
    print("test_get_student_list_hasGit_equals completed successfully in", end_time-start_time, "seconds")

if __name__ == "__main__":
    pytest.main([__file__])