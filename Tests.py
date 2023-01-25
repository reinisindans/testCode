import json
import isodate
from datetime import datetime, timezone, timedelta
from dateutil import parser as dateTimeParser

# This is a class has all the methods to test FlexPure objects for integrity
class FlexPurTest:
    def __init__(self, flexPurObject):
        self.flexPurObject = flexPurObject
        self.objectKeys = ["bidLinkingAllowed",
                           "callForTenderID",
                           "closeDate",
                           "deliveryEndDate",
                           "deliveryStartDate",
                           "direction",
                           "gateClosureDuration",
                           "localizationFactor",
                           "maxPrice",
                           "minPrice",
                           "openDate",
                           "productCode",
                           "recoveryPeriodDuration",
                           "relatedEnergyProduct",
                           "soEic"]
    # Utility functions 
    def __str__(self):
        return self.flexPurObject

    def toDict(self):
        return json.loads(self.flexPurObject)

    def isString(self, testString):
        return (isinstance(testString, str))

    def isBool(self, testBool):
        return (isinstance(testBool, bool))

    def parseDateTime(self, dateTimeString):
        try:
            return dateTimeParser.parse(dateTimeString)
        except:
            return False

    def parseTimeDelta(self,timeDeltaString):
        try:
            return isodate.parse_duration(timeDeltaString)
        except:
            return False        

    # Generic tests
    def isJSON_test(self):
        try:
            json.loads(self.flexPurObject)
            return True
        except:
            return False

    def objectKey_test(self):
        flexPur = self.toDict()
        try:
            for key in self.objectKeys:
                flexPur[key]
        except Exception as error:
            print("Parameters missing or named incorrerctly! ", error)
            return False
        return True

    # Specific object parameter tests
    def bidLinking_test(self):
        bidLinkingAllowed= self.toDict()["bidLinkingAllowed"]
        print(bidLinkingAllowed)
        print(self.isBool(bidLinkingAllowed))
        try:
            return (self.isBool(bidLinkingAllowed))
        except:
            print("Error reading bidLinkingAllowed property")
            return False

    def callForTenderID_test(self):
        callForTenderID = self.toDict()["callForTenderID"]
        if (self.isString(callForTenderID)):
            return len(callForTenderID)>2
        else:
            
            return False    

    def closeDate_test(self):
        closeDate= self.toDict()["closeDate"]
        if (self.parseDateTime(closeDate)):
            # If closingDate is in the past, test not passed
            if (self.parseDateTime(closeDate)> datetime.now(timezone.utc)):
                return True    
        return False    

    def deliveryStartDate_test(self):
        startDate= self.toDict()["deliveryStartDate"]  
        if (self.parseDateTime(startDate)):
            # If closingDate is in the past, test not passed
            if (self.parseDateTime(startDate)> datetime.now(timezone.utc)):
                return True    
        return False

    def deliveryEndDate_test(self):
        startDate= self.toDict()["deliveryStartDate"] 
        endDate= self.toDict()["deliveryEndDate"]        
        if (self.parseDateTime(endDate)):
            # If closingDate is in the past, test not passed
            if (self.parseDateTime(endDate)> self.parseDateTime(startDate)):
                return True    
        return False        

    def direction_test(self):
        allowedValues=["up", "down"]
        direction= self.toDict()["direction"] 
        if (self.isString(direction)):
            if (direction.lower() in allowedValues):
                return True
        return False        

    def gateClosureDuration_test(self):
        gateClosureDuration= self.toDict()["gateClosureDuration"]  
        if (self.parseTimeDelta(gateClosureDuration)):
            if (self.parseTimeDelta(gateClosureDuration) > timedelta(seconds = 0)):
                return True    
        return False         