import json
import requests
from dotenv import load_dotenv
import os

class ExL_Portfolio:

    # Initialisiere ExLibris-Portfolio Klasse für weitere API-Calls
    def __init__(self):
        load_dotenv()
        self.apiKey = os.getenv("apiKey")
        self.headers = {"Accept": "application/json"}
        self.params = {'apikey': self.apiKey, "limit": 100, "offset": 0}
        self.apiUrl = "https://api-eu.hosted.exlibrisgroup.com/almaws/v1/electronic/"

    # getCollection Funktion
    def getCollection(self,params=""):
        if params != "":
            self.params.update(params)
        r = requests.get(f"{self.apiUrl}e-collections",
                        params=self.params,
                        headers=self.headers)
        collectionData = r.json()
        return collectionData
    
