import requests

def print_result():
    print(res.status_code)
    if 'application/json' in res.headers['Content-Type']:
        print(res.json())
    else:
        print(res.text)
    print("________________")

# GET-запрос поиск питомца по ID
petID = "8263364"
res = requests.get( f"https://petstore.swagger.io/v2/pet/{petID}",
                    headers = {'accept': 'application/json'})
print_result()
# -------------------------------------

# POST-запрос добавление нового питомца (тэг: собака-танцевака)
data_MyNewPet = {
  "id": 8263364666,
  "category": {
    "id": 0,
    "name": "собака"
  },
  "name": "Королева",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "собака-танцевака"
    }
  ],
  "status": "available"
}

res = requests.post("https://petstore.swagger.io/v2/pet",
                    headers = {'accept': 'application/json'},
                    json = data_MyNewPet)
print_result()
# -------------------------------------

# PUT-запрос изменение данных питомца (тэг: собака-улыбака)
data_MyPet = {
  "id": 8263364666,
  "category": {
    "id": 0,
    "name": "собака"
  },
  "name": "Королева",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "собака-улыбака"
    }
  ],
  "status": "available"
}

res = requests.put("https://petstore.swagger.io/v2/pet",
                   json = data_MyPet)
print_result()
# -------------------------------------

# DELETE-запрос удаление по ID (собаки-улыбаки)
petID = "8263364666"
res = requests.delete( f"https://petstore.swagger.io/v2/pet/{petID}")
print_result()

