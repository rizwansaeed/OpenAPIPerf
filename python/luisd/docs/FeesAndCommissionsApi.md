# luisd.FeesAndCommissionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_applicable_fees**](FeesAndCommissionsApi.md#get_applicable_fees) | **GET** /api/feesandcommissions | [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
[**list_all_fees**](FeesAndCommissionsApi.md#list_all_fees) | **GET** /api/feesandcommissions/rules | [EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.

# **get_applicable_fees**
> ResourceListOfFeeCalculationDetails get_applicable_fees()

[EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.

Additionally, matching can be based on the instrument's properties, its portfolio properties, and any additional property keys present in the data file.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import fees_and_commissions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_fee_calculation_details import ResourceListOfFeeCalculationDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fees_and_commissions_api.FeesAndCommissionsApi(api_client)

    # example passing only optional values
    query_params = {
        'instrumentIdentifierType': "instrumentIdentifierType_example",
        'instrumentIdentifier': "instrumentIdentifier_example",
        'portfolioScope': "z",
        'portfolioCode': "z",
        'additionalSearchKeys': [
        "additionalSearchKeys_example",
    ],
        'fileName': "298JLe5iL60 aa -Ctq9dcsc-2 790gAa7Xa5u50ArrlGpCQjkQVRmfnjddwcDM-9f",
    }
    try:
        # [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
        api_response = api_instance.get_applicable_fees(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling FeesAndCommissionsApi->get_applicable_fees: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
instrumentIdentifierType | InstrumentIdentifierTypeSchema | | optional
instrumentIdentifier | InstrumentIdentifierSchema | | optional
portfolioScope | PortfolioScopeSchema | | optional
portfolioCode | PortfolioCodeSchema | | optional
additionalSearchKeys | AdditionalSearchKeysSchema | | optional
fileName | FileNameSchema | | optional


#### InstrumentIdentifierTypeSchema

Optional. The unique identifier type to use, eg 'Figi' or 'LusidInstrumentId'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### InstrumentIdentifierSchema

Optional. The Instrument Identifier to get properties for.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### PortfolioScopeSchema

Optional. The scope of the portfolio to fetch additional properties from.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### PortfolioCodeSchema

Optional. The code of the portfolio to fetch additional properties from.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AdditionalSearchKeysSchema

Any other property keys or fields and their corresponding values that should be matched for fees. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The list of fields available is as follows : \"RuleName\", \"Country\", \"FeeType\", \"FeeRate\", \"MinFee\", \"MaxFee\", \"PropertyKey\",               \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",               \"Custodian\", \"Exchange\"

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### FileNameSchema

Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your {fees-and-commissions} Drive folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The List of applicable fee calculations details 
400 | ApiResponseFor400 | The details of the input related failure 
default | ApiResponseForDefault | Error response 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](LusidValidationProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](LusidValidationProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](LusidValidationProblemDetails.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](LusidProblemDetails.md) |  | 



[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_fees**
> ResourceListOfFeeCalculationDetails list_all_fees()

[EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.

By default, will list ALL rules available. Additional keys and be specified to list a smaller subset of rules.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import fees_and_commissions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_fee_calculation_details import ResourceListOfFeeCalculationDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fees_and_commissions_api.FeesAndCommissionsApi(api_client)

    # example passing only optional values
    query_params = {
        'additionalSearchKeys': [
        "additionalSearchKeys_example",
    ],
        'fileName': "298JLe5iL60 aa -Ctq9dcsc-2 790gAa7Xa5u50ArrlGpCQjkQVRmfnjddwcDM-9f",
    }
    try:
        # [EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.
        api_response = api_instance.list_all_fees(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling FeesAndCommissionsApi->list_all_fees: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
additionalSearchKeys | AdditionalSearchKeysSchema | | optional
fileName | FileNameSchema | | optional


#### AdditionalSearchKeysSchema

Any other property keys or fields and their corresponding values that should be matched to reduce the list of rules returned. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The minimum list of fields available is as follows : \"RuleName\", \"Country\", \"FeeCalculationMethod\", \"FeeMultiplier\", \"MinFeeCalculationMethod\",               \"MinFeeMultiplier\", \"MaxFeeCalculationMethod\", \"MaxFeeMultiplier\", \"PropertyKey\",               \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",               \"Custodian\", \"Exchange\"

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### FileNameSchema

Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your Drive {fees-and-commissions} folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The List of all fee and commission rules available 
400 | ApiResponseFor400 | The details of the input related failure 
default | ApiResponseForDefault | Error response 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](LusidValidationProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](LusidValidationProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidValidationProblemDetails**](LusidValidationProblemDetails.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LusidProblemDetails**](LusidProblemDetails.md) |  | 



[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

