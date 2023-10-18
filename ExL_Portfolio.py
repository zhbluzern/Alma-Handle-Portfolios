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
        self.params = {'apikey': self.apiKey}
        self.apiUrl = "https://api-eu.hosted.exlibrisgroup.com/almaws/v1/electronic/"

    # getCollection Funktion
    def getCollection(self,params=""):
        thisParams = self.params
        thisParams.update({"limit": 100, "offset": 0})
        if params != "":
            thisParams.update(params)
        r = requests.get(f"{self.apiUrl}e-collections",
                        params=thisParams,
                        headers=self.headers)
        return r.json()
        
    # die Service-ID ist neben der Collection ID wesentlicher Bestandteil für die API-Url zur Behandlung der einzelnen Portfolios
    def getServices(self,collectionId):
        r = requests.get(f"{self.apiUrl}e-collections/{collectionId}/e-services",
                        params=self.params,
                        headers=self.headers)
        return  r.json()

    #List all Portfolios for given collection and service either by id
    def getPortfolios(self,collectionId,serviceId,params=""):
        thisParams = self.params
        thisParams.update({"limit": 100, "offset": 0})
        if params != "":
            thisParams.update(params)
        r = requests.get(f"{self.apiUrl}e-collections/{collectionId}/e-services/{serviceId}/portfolios",
                        params=thisParams,
                        headers=self.headers)
        return  r.json()

    #List all detailed portfolio informations "portfolio metadata" (e.g. links)
    def getPortfolioDetails(self,collectionId,serviceId,portfolioId):
        r = requests.get(f"{self.apiUrl}e-collections/{collectionId}/e-services/{serviceId}/portfolios/{portfolioId}",
                        params=self.params,
                        headers=self.headers)
        return  r.json()
    
    #Create a new Portfolio
    def createPortfolio(self,collectionId,serviceId,portfolioData):
        r = requests.post(f"{self.apiUrl}e-collections/{collectionId}/e-services/{serviceId}/portfolios/",
                        params=self.params,
                        data=portfolioData,
                        headers=self.headers)
        return r.json()
