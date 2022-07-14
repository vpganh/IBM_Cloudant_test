from DatabaseHelper import DBengine




if __name__ == "__main__":

    db = DBengine("https://apikey-v2-2lngv0194p8kh4qnpkwk4gqpk4hylwg88p3rq4go65yr:53230df54eaba98a57c8d8189f119181@59c0fa4a-2741-4857-9782-e74a36174bad-bluemix.cloudantnosqldb.appdomain.cloud")
    tableName = "employees"
    print(db.deleteTable(tableName).status_code)
    print(db.creatTable(tableName).status_code)

    value = {}
    value['name'] = 'James'
    value['age'] = '25'
    value['position'] = 'Software Engineer'
    print(db.insertIntoTable(tableName, value).status_code)

    value = {}
    value['name'] = 'Anna'
    value['age'] = '26'
    value['position'] = 'QA Engineer'
    print(db.insertIntoTable(tableName, value).status_code)

    wheres = {}
    wheres['name'] = 'James'
    response = db.findInTable(tableName, wheres)
    print(response.json()['docs'])
    