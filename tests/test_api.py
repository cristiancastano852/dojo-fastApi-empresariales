from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_say_hello():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message":"hello world"}

def test_get_user():
    response = client.get("/users/1", headers={"x-token":"fastApiToken"})
    assert response.status_code == 200
    assert response.json() == {
                                "id": 1,
                                "name": "juana paola",
                                "email": "juanaP@udea.edu.co",
                                "password": "\\x674141414141426a4970354d31786f4b44514b564576464e74567677633468705f716c334a64653977526a44486b49385542534d435a7076307a64664475473232797836476e58467648357a4c49347446305a3545417a2d374773587854337537773d3d"
                            }

def test_get_user_bad_token():
    response = client.get("users/1", headers={"x-token":"invalidToken"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Invalid X-Token header"}

def test_create_item():
    newUser = {
                "id": 24,
                "name": "Daiana Prince",
                "email": "wonderWoman@dc.com",
                "password": "Temiskira"
            }
    response = client.post("/users", json=newUser)
    assert response.status_code == 200
    assert response.json() == newUser
