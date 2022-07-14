import requests
from requests.structures import CaseInsensitiveDict
import json

class DBengine:

    cloudantulr = None
    headers = None

    def __init__(self,cloudantulr):
        self.cloudantulr = cloudantulr
        self.headers = CaseInsensitiveDict()
        self.headers["Content-Type"] = "application/json"

    def creatTable(self, tableName):
        url = self.cloudantulr + '/' + tableName
        response = requests.put(url)
        return (response)

    def deleteTable(self, tableName):
        url = self.cloudantulr + '/' + tableName
        response = requests.delete(url)
        return (response)

    def insertIntoTable(self, tableName, value):
        url = self.cloudantulr + '/' + tableName
        data = json.dumps(value)
        response = requests.post(url, headers=self.headers, data=data)
        return (response)

    def findInTable(self, tableName, value):
        url = self.cloudantulr + '/' + tableName + '/_find'
        data = '{"selector":' + json.dumps(value) + '}'
        response = requests.post(url, headers=self.headers, data=data)
        return(response)

