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

    def parseTimeDelta(self, timeDeltaString):
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
        try:
            flexPur = self.toDict()
            for key in self.objectKeys:
                flexPur[key]
        except Exception as error:
            return False
        return True

    # Specific object parameter tests
    def bidLinking_test(self):
        try:
            bidLinkingAllowed = self.toDict()["bidLinkingAllowed"]
            return (self.isBool(bidLinkingAllowed))
        except:
            return False

    def callForTenderID_test(self):
        try:
            callForTenderID = self.toDict()["callForTenderID"]
            if (self.isString(callForTenderID)):
                return len(callForTenderID) > 2
            else:
                return False
        except:
            return False

    def closeDate_test(self):
        try:
            closeDate = self.toDict()["closeDate"]
            if (self.parseDateTime(closeDate)):
                # If closingDate is in the past, test not passed
                if (self.parseDateTime(closeDate) > datetime.now(timezone.utc)):
                    return True
            return False
        except:
            return False

    def deliveryStartDate_test(self):
        try:
            startDate = self.toDict()["deliveryStartDate"]
            if (self.parseDateTime(startDate)):
                # If closingDate is in the past, test not passed
                if (self.parseDateTime(startDate) > datetime.now(timezone.utc)):
                    return True
            return False
        except:
            return False    

    def deliveryEndDate_test(self):
        try:
            startDate = self.toDict()["deliveryStartDate"]
            endDate = self.toDict()["deliveryEndDate"]
            if (self.parseDateTime(endDate)):
                # If closingDate is in the past, test not passed
                if (self.parseDateTime(endDate) > self.parseDateTime(startDate)):
                    return True
            return False
        except:
            return False    

    def direction_test(self):
        try:
            allowedValues = ["up", "down"]
            direction = self.toDict()["direction"]
            if (self.isString(direction)):
                if (direction.lower() in allowedValues):
                    return True
            return False
        except:
            return False    

    def gateClosureDuration_test(self):
        try:
            gateClosureDuration = self.toDict()["gateClosureDuration"]
            if (self.parseTimeDelta(gateClosureDuration)):
                if (self.parseTimeDelta(gateClosureDuration) > timedelta(seconds=0)):
                    return True
            return False
        except:
            return False    

    def localization_test(self):
        try:
            localization = self.toDict()["localizationFactor"]
            if (localization >= 0):
                return True
            else:
                return False
        except:
            return False

    def minPrice_test(self):
        try:
            minPrice = self.toDict()["minPrice"]
            if (minPrice >= 0):
                return True
            else:
                return False
        except:
            return False

    def maxPrice_test(self):
        try:
            minPrice = self.toDict()["minPrice"]
            maxPrice = self.toDict()["maxPrice"]
            if (maxPrice >= minPrice):
                return True
            else:
                return False
        except:
            return False

    def openDate_test(self):
        try:
            openDate = self.toDict()["openDate"]
            closeDate = self.toDict()["closeDate"]
            if (self.parseDateTime(openDate)):
                # If closingDate is in the past, test not passed
                if (self.parseDateTime(openDate) < self.parseDateTime(closeDate)):
                    return True
            return False
        except:
            return False    

    def productCode_test(self):
        try:
            productCode = self.toDict()["productCode"]
            if (self.isString(productCode)):
                return len(productCode) > 2
            else:
                return False
        except:
            False        

    def recoveryPeriodDuration_test(self):
        try:
            recoveryPeriodDuration = self.toDict()["gateClosureDuration"]
            if (self.parseTimeDelta(recoveryPeriodDuration)):
                if (self.parseTimeDelta(recoveryPeriodDuration) > timedelta(seconds=0)):
                    return True
            return False
        except:
            return False    

    def relatedEnergyProduct_test(self):
        try:
            relatedEnergyProduct = self.toDict()["callForTenderID"]
            if (self.isString(relatedEnergyProduct)):
                return len(relatedEnergyProduct) > 2
            else:
                return False
        except:
            return False        

    def soEic_test(self):
        try:
            soEic = self.toDict()["callForTenderID"]
            if (self.isString(soEic)):
                return len(soEic) > 2
            else:
                return False
        except:
            return False        

    def testAll(self):
        tests = [self.isJSON_test,
                 self.objectKey_test,
                 self.bidLinking_test,
                 self.callForTenderID_test,
                 self.closeDate_test,
                 self.deliveryStartDate_test,
                 self.deliveryEndDate_test,
                 self.direction_test,
                 self.gateClosureDuration_test,
                 self.localization_test,
                 self.minPrice_test,
                 self.maxPrice_test,
                 self.openDate_test,
                 self.productCode_test,
                 self.recoveryPeriodDuration_test,
                 self.relatedEnergyProduct_test,
                 self.soEic_test
                 ]
        results = {}
        for test in tests:
            result = test()
            results[test.__name__] = result
        return results
