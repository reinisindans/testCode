import Tests
import TestObjects

validTestCase=Tests.FlexPurTest(TestObjects.flexPur_true)

notJSONCase= Tests.FlexPurTest(TestObjects.flexPur_notJson)

missingKeysCase=Tests.FlexPurTest(TestObjects.flexPur_missingKeys)

wrongKeyNameCase=Tests.FlexPurTest(TestObjects.flexPur_wrongKeyNames)

invalidTestCase= Tests.FlexPurTest(TestObjects.flexPur_false)


"""
print ("Testing if is JSON (True): ", validTestCase.isJSON_test())
print ("Testing if is JSON (False): ", notJSONCase.isJSON_test())

print()
print ("Testing objectkeyTest (True): ", validTestCase.objectKey_test())
print ("Testing objectkeyTest (False, missingKeys): ", missingKeysCase.objectKey_test())
print ("Testing objectkeyTest (False, wrongKeyNames): ", wrongKeyNameCase.objectKey_test())

print()
print ("Testing bidLinkingAllowed (True): ", validTestCase.bidLinking_test())
print ("Testing bidLinkingAllowed (False): ", invalidTestCase.bidLinking_test())

print()
print ("Testing closeDate_test (True): ", validTestCase.closeDate_test())
print ("Testing closeDate_test (False): ", invalidTestCase.closeDate_test())



print()
print ("Testing deliveryStartDate_test (True): ", validTestCase.deliveryStartDate_test())
print ("Testing deliveryStartDate_test (False): ", invalidTestCase.deliveryStartDate_test())


print()
print ("Testing deliveryEndDate_test (True): ", validTestCase.deliveryEndDate_test())
print ("Testing deliveryEndDate_test (False): ", invalidTestCase.deliveryEndDate_test())


print()
print ("Testing direction_test (True): ", validTestCase.direction_test())
print ("Testing direction_test (False): ", invalidTestCase.direction_test())

"""

print()
print ("Testing gateClosureDuration_test (True): ", validTestCase.gateClosureDuration_test())
print ("Testing gateClosureDuration_test (False): ", invalidTestCase.gateClosureDuration_test())