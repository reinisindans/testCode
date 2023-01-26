import Tests
import TestObjects

# testCase has to be an implementation of test interface, with implemented function .testAll()
# This function prints the test results in human readable format
def reportResults(testCase):
    results= testCase.testAll()
    failedTests=[k for k, v in results.items() if v ==False]
    passedTests=[k for k, v in results.items() if v ==True]
    print("\nTests passed: ", len(passedTests))
    print("Tests FAILED: ", len(failedTests))
    if (len(failedTests)>0):
        print("\nFAILED Tests:")
        for test in failedTests:
            print(test)

# Setting up the test cases for demonstration purposes
validTestCase=Tests.FlexPurTest(TestObjects.flexPur_true)

invalidTestCase= Tests.FlexPurTest(TestObjects.flexPur_false)

notJSONCase= Tests.FlexPurTest(TestObjects.flexPur_notJson)

missingKeysCase=Tests.FlexPurTest(TestObjects.flexPur_missingKeys)

wrongKeyNameCase=Tests.FlexPurTest(TestObjects.flexPur_wrongKeyNames)


# Prints out the test results
#reportResults(validTestCase)
#reportResults(invalidTestCase)
#reportResults(notJSONCase)
#reportResults(missingKeysCase)
reportResults(wrongKeyNameCase)


