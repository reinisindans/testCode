import json

flexPur_true=json.dumps({
"bidLinkingAllowed":True,
"callForTenderID":"string",
"closeDate":"2023-01-31T10:28:59.264Z",
"deliveryEndDate": "2023-01-31T12:28:59.264Z",
"deliveryStartDate": "2023-01-31T10:28:59.264Z",
"direction": "Up",
"gateClosureDuration": "PT15M",
"localizationFactor": 0,
"maxPrice":0,
"minPrice":0,
"openDate":"2023-01-11T10:28:59.264Z",
"productCode":"NRT-P-E",
"recoveryPeriodDuration": "PT15M",
"relatedEnergyProduct": "string",
"soEic":"string"
})

flexPur_false=json.dumps({
"bidLinkingAllowed":0,
"callForTenderID":None,
"closeDate":"1823-01-11T10:28:59.264Z",
"deliveryEndDate": 2023,
"deliveryStartDate": "today",
"direction": 12,
"gateClosureDuration": 143,
"localizationFactor": None,
"maxPrice":"three",
"minPrice":-12,
"openDate":None,
"productCode":13,
"recoveryPeriodDuration": None,
"relatedEnergyProduct": True,
"soEic":"st"
})

flexPur_missingKeys= json.dumps({
"bidLinkingAllowed":0,
"callForTenderID":None,
"closeDate":"1823-01-11T10:28:59.264Z",
"deliveryEndDate": 2023,
"deliveryStartDate": "today",
"direction": 12,
"gateClosureDuration": 143,
})

flexPur_wrongKeyNames=json.dumps({
"bidLinkingAllowed":0,
"callForTendesID":None,
"closeDate":"1823-01-11T10:28:59.264Z",
"deliveryEndDate": 2023,
"deliveryStartDate": "today",
"diretion": 12,
"gateClosureDuration": 143,
"localizationFactor": None,
"maxPrice":"three",
"minPrice":-12,
"openDate":None,
"productCode":13,
"recoveryPeriodDuration": None,
"relatedEnergyProduct": True,
"soEic":"st"
})

flexPur_notJson= {
"bidLinkingAllowed":True,
"callForTenderID":"string",
"closeDate":"2023-01-11T10:28:59.264Z",
"deliveryEndDate": "2023-01-11T10:28:59.264Z",
"deliveryStartDate": "2023-01-11T10:28:59.264Z",
"direction": "Up",
"gateClosureDuration": "PT15M",
"localizationFactor": 0,
"maxPrice":0,
"minPrice":0,
"openDate":"2023-01-11T10:28:59.264Z",
"productCode":"NRT-P-E",
"recoveryPeriodDuration": "PT15M",
"relatedEnergyProduct": "string",
"soEic":"string"
}