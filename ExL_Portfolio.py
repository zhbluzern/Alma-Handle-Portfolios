import requests
import json

class ExL_Portfolio:

    # Initialisiere ExLibris-Portfolio Klasse für weitere API-Calls
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.headers = {"Accept": "application/json"}
        self.params = {'apikey': self.apiKey}
        self.apiUrl = "https://api-eu.hosted.exlibrisgroup.com/almaws/v1/electronic/"

    # getCollection Funktion
    def getCollection(self,params=""):
        thisParams = self.params
        thisParams.update({"limit": 100, "offset": 0})
        if params != "":
            thisParams.update(params)
        r = requests.get(f"{self.apiUrl}e-collections/",
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
        thisHeaders = self.headers
        thisHeaders.update({"Content":"application/json"})
        r = requests.post(f"{self.apiUrl}e-collections/{collectionId}/e-services/{serviceId}/portfolios/",
                        params=self.params,
                        json=portfolioData,
                        headers=thisHeaders)
        return r.json()
    
    # Return the PortfolioID for a given MMSID (resource_metadata.mms_id.value)
    def getPortfolioByMMSId(self,portfolios,collectionId,serviceId,mmsId):
        returnPortfolioId = None
        for portfolio in portfolios["portfolio"]:
            portfolioData = ExL_Portfolio.getPortfolioDetails(self,collectionId,serviceId,portfolio['id'])
            if portfolioData["resource_metadata"]["mms_id"]["value"] == mmsId:
                returnPortfolioId = (portfolio["id"])
            
        return returnPortfolioId

    # Check if mmsId is NZ Id and returns the local IZ mms id for portfolio creation
    def checkMMSIdisNZId(self, mmsId):
        thisParams = {}
        thisParams.update({"nz_mms_id": mmsId, "view":"full", "expand":"None", "apikey":self.apiKey})
        r = requests.get(f"https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs",
                                params=thisParams,
                                headers=self.headers)
        result = r.json()
        
        try:
            result["errorsExist"] == "True"
            return "Error"
        except KeyError:
            try: 
                return result["bib"][0]["mms_id"]
            except:
                return None

    # Check if an IZ MMS ID is given, returns True if it is a IZ id, returns "Error" on Error
    def checkMMSIdisIZId(self, mmsId):
        thisParams = {}
        thisParams.update({"mms_id": mmsId, "view":"full", "expand":"None", "apikey":self.apiKey})
        r = requests.get(f"https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs",
                                params=thisParams,
                                headers=self.headers)
        result = r.json()
        
        try:
            result["errorsExist"] == "True"
            return "Error"
        except KeyError:
            try: 
                if result["bib"][0]["mms_id"] == mmsId:
                    return True
                else:
                    return False
            except:
                return None