from logging import raiseExceptions
from flourish_app import create_app
import json
import pytest

def test_index(client):
    response = client.get("/")
    assert  response.status == "200 OK"
    assert response.data == b"Hello World!"

def test_getAllProducts(client):
    mock_data = json.dumps(
        {
        "category_id": 7,
        "date_time": "Wed, 05 Apr 2022 00:00:00 GMT",
        "description": 'Tomatoes',
        "expiry": "07/04/2022",
        "image": "LINK",
        "is_retail": 1,
        "longitude": 51.5014,
        "latitude":  0.1419,
        "price": 2.99,
        "user_id": 1
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.post('/products', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'
    res = client.get("/products")
    assert res.status == '200 OK'
    #assert len(res.json) == 14
    #assert res.json[0]['description'] == 'Oranges'

def test_getAllProductsExceptions(client):
    with pytest.raises(Exception):
        mock_data = json.dumps(
        {
        "category_id": 7,
        "date_time": "Wed, 05 Apr 2022 00:00:00 GMT",
        "descriptio": 'Tomatoes',
        "expiry": "07/04/2022",
        "image": "LINK",
        "is_retail": 1,
        "longitud": 51.5014,
        "latitude":  0.1419,
        "price": 2.99,
        "user_id": 1
        })
        mock_headers = {'Content-Type': 'application/json'}
        res = client.post('/products', data=mock_data, headers=mock_headers)
        res = client.post('/products',data = mock_data ,headers=mock_headers)
        assert res.status == "500 INTERNAL SERVER ERROR"






def test_getProductById(client):

    res = client.get("/products/1")
    assert res.status == '200 OK'
    # assert len(res.json) == 1
    # assert res.json[0]['description'] == 'Oranges'

def test_getProductByIdExceptions(client):
    with pytest.raises(Exception):
        res = client.get("/products/10")
        assert res.status == "404 Not Found"

def test_getProductByCategoryId(client):
    res = client.get("/products/category/5")
    assert res.status == '200 OK'
    #assert res.json[0]['description'] == 'Oranges'

def test_getProductByCategoryIdExceptions(client):
    with pytest.raises(Exception):
        res = client.get("/products/category/100")
        assert res.status == '404 Not Found'

def test_getAllUsers(client):
    res = client.get("/users")
    assert res.status == '200 OK'
    #assert res.json[0]['email'] == 'hamza@hotmail.com'

def test_getAllUsersProductsById(client):
    res = client.get("/users/1/products")
    assert res.status == '200 OK'   
    #assert res.json[0]['expiry'] == '02/04/2022'

def test_getAllUsersProductsByIdExceptions(client):
    with pytest.raises(Exception):
        res = client.get("/users/100/products")
        assert res.status == '404 Not Found'   

def test_handleUserById(client):
    res = client.get("/users/1")
    assert res.status == '200 OK'  
    res = client.delete("/users/7")
    assert res.status == '204 NO CONTENT'
   # assert res.json[0]['id'] == 1

def test_handleUserByIdExceptions(client):
    with pytest.raises(Exception):
        res = client.get("/users/100")
        assert res.status == "404 Not Found"  

 

def test_vote(client):
    mock_data = json.dumps(
        {    
            "product_id": 1,
            "user_id": 1,
            "rating": 4.0
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.post('/rating/vote', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'

def test_voteExceptions(client):
    with pytest.raises(Exception):
        mock_data = json.dumps(
            {    
                "product_id": 1,
                "usegfdas_id": 1,
                "rating": 4.0
            }
        )
        mock_headers = {'Content-Type': 'application/json'}
        res = client.post('/rating/vote', data=mock_data, headers=mock_headers)
        assert res.status == '500 Internal Server Error'

def test_getAllRatings(client):
    res = client.get("/ratings")
    assert res.status == '200 OK'  


def test_getRatingByUserId(client):
    res = client.get("/ratings/users/2")
    assert res.status == '200 OK'  
    #assert res.json[0]['rating'] == 4

def test_getRatingByUserIdExceptions(client):
    with pytest.raises(Exception):
        res = client.get("/ratings/users/10")
        assert res.status == '404 Not Found'  



def test_getRatingById(client):
    res = client.get("/ratings/users/2/products/1")
    assert res.status == '200 OK'  
    #assert res.json[0]['rating'] == 4

def test_updateLocation(client):
    mock_data = json.dumps(
        {
        "updated_longitude" : 51.49793868596544 ,
        "updated_latitude" : -0.14218409261798856
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.patch('/users/1/location', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'

def test_updateRadius(client):
    mock_data = json.dumps(
        {
        "updated_radius": 3.0
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.patch('/users/1/radius', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'



def test_register(client):
    mock_data = json.dumps(
        {
        "email": "testexceptions@hotmail.com",
        "passwrd": "test",
        "username": "testing"
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.post('/register', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'

def test_login(client):
    mock_data = json.dumps(
        {
        "email": "testexceptions@hotmail.com",
        "passwrd": "test",
        }
    )
    mock_headers = {'Content-Type': 'application/json'}
    res = client.post('/login', data=mock_data, headers=mock_headers)
    assert res.status == '200 OK'

def test_categories(client):
    res = client.get("/products/categories")
    assert res.status == '200 OK'  
