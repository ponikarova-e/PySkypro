import requests

base_url = "https://ru.yougile.com/api-v2"
key = "Bearer dvDHCGq7F6lGCRRxkj8PdYa+xEGSEaUgrWOKG8q1BcHA0Sj3GzHSrGSnEBnzry85"
headers = {
        "Authorization": key,
        "Content-Type": "application/json"
         }


def test_create_project_positive():
    body = {
        "title": "test"
    }
    response = requests.post(base_url + "/projects",
                             json=body, headers=headers)
    assert response.status_code == 201


def test_create_project_negative():
    body = {
       "title": ""
    }
    response = requests.post(base_url + "/projects",
                             json=body, headers=headers)
    assert response.status_code == 400


def test_get_project():
    body = {
        "title": "test"
    }
    response = requests.post(base_url + "/projects", json=body,
                             headers=headers)
    id_project = response.json()["id"]
    response = requests.get(base_url + "/projects/" + id_project,
                            headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == id_project


def test_get_project_negative():
    body = {
       "title": "test"
    }
    response = requests.post(base_url + "/projects",
                             json=body, headers=headers)
    id_project = response.json()["id"]
    response = requests.get(base_url + id_project, headers=headers)
    assert response.status_code == 404


def test_change_project():
    body = {
        "title": "test"
    }
    response = requests.post(base_url + "/projects", json=body,
                             headers=headers)
    id_project = response.json()["id"]
    response = requests.put(base_url + "/projects/" + id_project,
                            json={"title": "updated_title"}, headers=headers)
    assert response.status_code == 200
    response = requests.get(base_url + "/projects/" + id_project,
                            headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated_title"


def test_change_project_negative():
    body = {
      "title": "test"
    }
    response = requests.post(base_url + "/projects", json=body,
                             headers=headers)
    id_project = response.json()["id"]
    response = requests.put(base_url + "/projects/" + id_project,
                            json={"title": "updated_title"},
                            headers=headers)
    assert response.status_code == 200
    response = requests.get(base_url + id_project, headers=headers)
    assert response.status_code == 404
