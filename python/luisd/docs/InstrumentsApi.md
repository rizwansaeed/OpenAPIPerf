# luisd.InstrumentsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument**](InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] DeleteInstrument: Delete instrument
[**delete_instrument_properties**](InstrumentsApi.md#delete_instrument_properties) | **POST** /api/instruments/{identifierType}/{identifier}/properties/$delete | [EXPERIMENTAL] DeleteInstrumentProperties: Delete instrument properties
[**get_instrument**](InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | GetInstrument: Get instrument
[**get_instrument_identifier_types**](InstrumentsApi.md#get_instrument_identifier_types) | **GET** /api/instruments/identifierTypes | [EARLY ACCESS] GetInstrumentIdentifierTypes: Get instrument identifier types
[**get_instrument_properties**](InstrumentsApi.md#get_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties | [EXPERIMENTAL] GetInstrumentProperties: Get instrument properties
[**get_instrument_property_time_series**](InstrumentsApi.md#get_instrument_property_time_series) | **GET** /api/instruments/{identifierType}/{identifier}/properties/time-series | [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
[**get_instruments**](InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | GetInstruments: Get instruments
[**list_instrument_properties**](InstrumentsApi.md#list_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties/list | [EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)
[**list_instruments**](InstrumentsApi.md#list_instruments) | **GET** /api/instruments | [EARLY ACCESS] ListInstruments: List instruments
[**update_instrument_identifier**](InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] UpdateInstrumentIdentifier: Update instrument identifier
[**upsert_instruments**](InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | UpsertInstruments: Upsert instruments
[**upsert_instruments_properties**](InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | UpsertInstrumentsProperties: Upsert instruments properties

# **delete_instrument**
> DeleteInstrumentResponse delete_instrument(identifier_typeidentifier)

[EARLY ACCESS] DeleteInstrument: Delete instrument

Delete a particular instrument, as identified by a particular instrument identifier.                Once deleted, an instrument is marked as inactive and can no longer be referenced when creating or updating  transactions or holdings. You can still query existing transactions and holdings related to the  deleted instrument.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.delete_instrument_response import DeleteInstrumentResponse
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] DeleteInstrument: Delete instrument
        api_response = api_instance.delete_instrument(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->delete_instrument: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'scope': "default",
    }
    try:
        # [EARLY ACCESS] DeleteInstrument: Delete instrument
        api_response = api_instance.delete_instrument(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->delete_instrument: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | optional


#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to search, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The datetime that the instrument was deleted 
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
[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md) |  | 


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



[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instrument_properties**
> DeleteInstrumentPropertiesResponse delete_instrument_properties(identifier_typeidentifierrequest_body)

[EXPERIMENTAL] DeleteInstrumentProperties: Delete instrument properties

Delete one or more properties from a particular instrument. If the properties are time-variant then an effective datetime from which  to delete properties must be specified. If the properties are perpetual then it is invalid to specify an effective datetime for deletion.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.delete_instrument_properties_response import DeleteInstrumentPropertiesResponse
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
    }
    body = ["Instrument/scope/market-sector","Instrument/scope/tenor"]
    try:
        # [EXPERIMENTAL] DeleteInstrumentProperties: Delete instrument properties
        api_response = api_instance.delete_instrument_properties(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->delete_instrument_properties: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'scope': "default",
    }
    body = ["Instrument/scope/market-sector","Instrument/scope/tenor"]
    try:
        # [EXPERIMENTAL] DeleteInstrumentProperties: Delete instrument properties
        api_response = api_instance.delete_instrument_properties(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->delete_instrument_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson

A list of property keys from the 'Instruments' domain whose properties to delete.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of property keys from the &#x27;Instruments&#x27; domain whose properties to delete. | 

#### SchemaForRequestBodyApplicationJson

A list of property keys from the 'Instruments' domain whose properties to delete.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of property keys from the &#x27;Instruments&#x27; domain whose properties to delete. | 

#### SchemaForRequestBodyTextJson

A list of property keys from the 'Instruments' domain whose properties to delete.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of property keys from the &#x27;Instruments&#x27; domain whose properties to delete. | 

#### SchemaForRequestBodyApplicationJson

A list of property keys from the 'Instruments' domain whose properties to delete.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of property keys from the &#x27;Instruments&#x27; domain whose properties to delete. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
effectiveAt | EffectiveAtSchema | | optional
scope | ScopeSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to search, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The asAt datetime at which properties were deleted. 
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
[**DeleteInstrumentPropertiesResponse**](DeleteInstrumentPropertiesResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteInstrumentPropertiesResponse**](DeleteInstrumentPropertiesResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteInstrumentPropertiesResponse**](DeleteInstrumentPropertiesResponse.md) |  | 


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



[**DeleteInstrumentPropertiesResponse**](DeleteInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument**
> Instrument get_instrument(identifier_typeidentifier)

GetInstrument: Get instrument

Retrieve the definition of a particular instrument, as identified by a particular unique identifier.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.instrument import Instrument
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
    }
    try:
        # GetInstrument: Get instrument
        api_response = api_instance.get_instrument(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'propertyKeys': [
        "propertyKeys_example",
    ],
        'scope': "default",
    }
    try:
        # GetInstrument: Get instrument
        api_response = api_instance.get_instrument(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
propertyKeys | PropertyKeysSchema | | optional
scope | ScopeSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### PropertyKeysSchema

A list of property keys from the 'Instrument' domain to decorate onto the instrument.              These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to use, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested instrument. 
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
[**Instrument**](Instrument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Instrument**](Instrument.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Instrument**](Instrument.md) |  | 


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



[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier_types**
> ResourceListOfInstrumentIdTypeDescriptor get_instrument_identifier_types()

[EARLY ACCESS] GetInstrumentIdentifierTypes: Get instrument identifier types

Retrieve a list of all valid instrument identifier types and whether they are unique or not.                An instrument must have a value for at least one unique identifier type (it can have more than one unique type and value).  In addition, a value is automatically generated for a LUSID Instrument ID (LUID) unique type by the system.                An instrument can have values for multiple non-unique identifier types (or it can have zero non-unique types and values).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.resource_list_of_instrument_id_type_descriptor import ResourceListOfInstrumentIdTypeDescriptor
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # [EARLY ACCESS] GetInstrumentIdentifierTypes: Get instrument identifier types
        api_response = api_instance.get_instrument_identifier_types()
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument_identifier_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A list of valid instrument identifier types. 
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
[**ResourceListOfInstrumentIdTypeDescriptor**](ResourceListOfInstrumentIdTypeDescriptor.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfInstrumentIdTypeDescriptor**](ResourceListOfInstrumentIdTypeDescriptor.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfInstrumentIdTypeDescriptor**](ResourceListOfInstrumentIdTypeDescriptor.md) |  | 


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



[**ResourceListOfInstrumentIdTypeDescriptor**](ResourceListOfInstrumentIdTypeDescriptor.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_properties**
> InstrumentProperties get_instrument_properties(identifier_typeidentifier)

[EXPERIMENTAL] GetInstrumentProperties: Get instrument properties

List all the properties of a particular instrument, as identified by a particular unique identifier.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.instrument_properties import InstrumentProperties
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetInstrumentProperties: Get instrument properties
        api_response = api_instance.get_instrument_properties(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument_properties: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'scope': "default",
    }
    try:
        # [EXPERIMENTAL] GetInstrumentProperties: Get instrument properties
        api_response = api_instance.get_instrument_properties(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
scope | ScopeSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to list the instrument's properties.              Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to list the instrument's properties. Defaults to returning              the latest version of each property if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to search, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The properties of the specified instrument 
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
[**InstrumentProperties**](InstrumentProperties.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InstrumentProperties**](InstrumentProperties.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InstrumentProperties**](InstrumentProperties.md) |  | 


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



[**InstrumentProperties**](InstrumentProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_property_time_series**
> ResourceListOfPropertyInterval get_instrument_property_time_series(identifier_typeidentifierproperty_key)

[EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series

Retrieve the complete time series (history) for a particular property of an instrument.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_property_interval import ResourceListOfPropertyInterval
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'propertyKey': "propertyKey_example",
    }
    try:
        # [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
        api_response = api_instance.get_instrument_property_time_series(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument_property_time_series: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'propertyKey': "propertyKey_example",
        'identifierEffectiveAt': "identifierEffectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'filter': "",
        'page': "zA9LCSLv1C1ylmgd0/Y2T",
        'limit': 1,
        'scope': "default",
    }
    try:
        # [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
        api_response = api_instance.get_instrument_property_time_series(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instrument_property_time_series: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
propertyKey | PropertyKeySchema | | 
identifierEffectiveAt | IdentifierEffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
filter | FilterSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional
scope | ScopeSchema | | optional


#### PropertyKeySchema

The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

#### IdentifierEffectiveAtSchema

The effective datetime used to resolve the instrument from the identifier.              Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the instrument's property history. Defaults to              returning the current datetime if not supplied.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### FilterSchema

Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### PageSchema

The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the <i>filter</i>, <i>effectiveAt</i> and              <i>asAt</i> fields must not have changed since the original request. For more information, see              https://support.lusid.com/knowledgebase/article/KA-01915.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### LimitSchema

When paginating, limit the results to this number.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to search, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The time series of the property 
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
[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md) |  | 


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



[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instruments**
> GetInstrumentsResponse get_instruments(identifier_typerequest_body)

GetInstruments: Get instruments

Retrieve the definition of one or more instruments, as identified by a collection of unique identifiers.                Note that to retrieve all the instruments in the instrument master, use the List instruments endpoint instead.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.get_instruments_response import GetInstrumentsResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'identifierType': "identifierType_example",
    }
    body = ["instrument-identifier-1","instrument-identifier-2"]
    try:
        # GetInstruments: Get instruments
        api_response = api_instance.get_instruments(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instruments: %s\n" % e)

    # example passing only optional values
    query_params = {
        'identifierType': "identifierType_example",
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'propertyKeys': [
        "propertyKeys_example",
    ],
        'scope': "default",
    }
    body = ["instrument-identifier-1","instrument-identifier-2"]
    try:
        # GetInstruments: Get instruments
        api_response = api_instance.get_instruments(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->get_instruments: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson

A list of one or more <i>identifierType</i> values to use to identify instruments.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of one or more &lt;i&gt;identifierType&lt;/i&gt; values to use to identify instruments. | 

#### SchemaForRequestBodyApplicationJson

A list of one or more <i>identifierType</i> values to use to identify instruments.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of one or more &lt;i&gt;identifierType&lt;/i&gt; values to use to identify instruments. | 

#### SchemaForRequestBodyTextJson

A list of one or more <i>identifierType</i> values to use to identify instruments.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of one or more &lt;i&gt;identifierType&lt;/i&gt; values to use to identify instruments. | 

#### SchemaForRequestBodyApplicationJson

A list of one or more <i>identifierType</i> values to use to identify instruments.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | A list of one or more &lt;i&gt;identifierType&lt;/i&gt; values to use to identify instruments. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
propertyKeys | PropertyKeysSchema | | optional
scope | ScopeSchema | | optional


#### IdentifierTypeSchema

The unique identifier type to use, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The unique identifier type to use, for example &#x27;Figi&#x27;. | 

#### EffectiveAtSchema

The effective datetime or cut label at which to retrieve the instrument definitions.               Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the instrument definitions.               Defaults to returning the latest version of each instrument definition if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### PropertyKeysSchema

A list of property keys from the 'Instrument' domain to decorate onto the instrument.               These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested instruments which could be identified along with any failures 
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
[**GetInstrumentsResponse**](GetInstrumentsResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetInstrumentsResponse**](GetInstrumentsResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetInstrumentsResponse**](GetInstrumentsResponse.md) |  | 


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



[**GetInstrumentsResponse**](GetInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instrument_properties**
> ResourceListOfProperty list_instrument_properties(identifier_typeidentifier)

[EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)

List all the properties of a particular instrument, as identified by a particular unique identifier.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_property import ResourceListOfProperty
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)
        api_response = api_instance.list_instrument_properties(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->list_instrument_properties: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'effectiveAt': "A",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'page': "zA9LCSLv1C1ylmgd0/Y2T",
        'limit': 1,
        'scope': "default",
    }
    try:
        # [EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)
        api_response = api_instance.list_instrument_properties(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->list_instrument_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional
scope | ScopeSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to list the instrument's properties.              Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to list the instrument's properties. Defaults to returning              the latest version of each property if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### PageSchema

The pagination token to use to continue listing commands; this value is returned from the previous call.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### LimitSchema

When paginating, limit the results per page to this number.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to search, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The properties of the specified instrument 
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
[**ResourceListOfProperty**](ResourceListOfProperty.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfProperty**](ResourceListOfProperty.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfProperty**](ResourceListOfProperty.md) |  | 


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



[**ResourceListOfProperty**](ResourceListOfProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instruments**
> PagedResourceListOfInstrument list_instruments()

[EARLY ACCESS] ListInstruments: List instruments

List all the instruments in the instrument master.                To retrieve a particular set of instruments instead, use the Get instruments endpoint.  The maximum number of instruments that this method can list per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.paged_resource_list_of_instrument import PagedResourceListOfInstrument
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'effectiveAt': "effectiveAt_example",
        'page': "zA9LCSLv1C1ylmgd0/Y2T",
        'sortBy': [
        "sortBy_example",
    ],
        'start': 1,
        'limit': 1,
        'filter': "State eq 'Active'",
        'instrumentPropertyKeys': [
        "instrumentPropertyKeys_example",
    ],
        'scope': "default",
    }
    try:
        # [EARLY ACCESS] ListInstruments: List instruments
        api_response = api_instance.list_instruments(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->list_instruments: %s\n" % e)
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
asAt | AsAtSchema | | optional
effectiveAt | EffectiveAtSchema | | optional
page | PageSchema | | optional
sortBy | SortBySchema | | optional
start | StartSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional
instrumentPropertyKeys | InstrumentPropertyKeysSchema | | optional
scope | ScopeSchema | | optional


#### AsAtSchema

The asAt datetime at which to list instruments. Defaults to returning the latest               version of each instrument if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### EffectiveAtSchema

The effective datetime or cut label at which to list instruments.               Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### PageSchema

The pagination token to use to continue listing instruments; this value is returned from               the previous call. If a pagination token is provided, the <i>sortBy</i>, <i>filter</i>, <i>effectiveAt</i> and               <i>asAt</i> fields must not have changed since the original request. Also, a <i>start</i> value cannot be               provided. For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### SortBySchema

Order results by particular fields. Use the '-' sign to denote descending order, for               example '-MyFieldName'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### StartSchema

When paginating, skip this number of results.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### LimitSchema

When paginating, limit the results to this number.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### FilterSchema

Expression to filter the result set. Defaults to filtering out inactive instruments               (that is, those that have been deleted). For more information about filtering results,               see https://support.lusid.com/knowledgebase/article/KA-01914.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### InstrumentPropertyKeysSchema

A list of property keys from the 'Instrument' domain to decorate onto               instruments. These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested instruments 
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
[**PagedResourceListOfInstrument**](PagedResourceListOfInstrument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfInstrument**](PagedResourceListOfInstrument.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfInstrument**](PagedResourceListOfInstrument.md) |  | 


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



[**PagedResourceListOfInstrument**](PagedResourceListOfInstrument.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_identifier**
> Instrument update_instrument_identifier(identifier_typeidentifierupdate_instrument_identifier_request)

[EARLY ACCESS] UpdateInstrumentIdentifier: Update instrument identifier

Create, update or delete a particular instrument identifier for an instrument.                To delete the identifier, leave the value unspecified in the request. If not being deleted, the  identifier is updated if it exists and created if it does not.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.instrument import Instrument
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.update_instrument_identifier_request import UpdateInstrumentIdentifierRequest
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
    }
    body = UpdateInstrumentIdentifierRequest(
        type="type_example",
        value="value_example",
        effective_at="effective_at_example",
    )
    try:
        # [EARLY ACCESS] UpdateInstrumentIdentifier: Update instrument identifier
        api_response = api_instance.update_instrument_identifier(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->update_instrument_identifier: %s\n" % e)

    # example passing only optional values
    path_params = {
        'identifierType': "identifierType_example",
        'identifier': "identifier_example",
    }
    query_params = {
        'scope': "default",
    }
    body = UpdateInstrumentIdentifierRequest(
        type="type_example",
        value="value_example",
        effective_at="effective_at_example",
    )
    try:
        # [EARLY ACCESS] UpdateInstrumentIdentifier: Update instrument identifier
        api_response = api_instance.update_instrument_identifier(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->update_instrument_identifier: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | optional


#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
identifierType | IdentifierTypeSchema | | 
identifier | IdentifierSchema | | 

#### IdentifierTypeSchema

The unique identifier type to search, for example 'Figi'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierSchema

An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The updated instrument definition with the identifier created, updated or deleted 
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
[**Instrument**](Instrument.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Instrument**](Instrument.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Instrument**](Instrument.md) |  | 


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



[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments**
> UpsertInstrumentsResponse upsert_instruments(request_body)

UpsertInstruments: Upsert instruments

Create or update one or more instruments in the instrument master. An instrument is updated  if it already exists and created if it does not.                In the request, each instrument definition should be keyed by a unique correlation ID. This ID is ephemeral  and not stored by LUSID. It serves only to easily identify each instrument in the response.                Note that an instrument must have at least one unique identifier, which is a combination of a type  (such as 'Figi') and a value (such as 'BBG000BS1N49'). In addition, a random value is automatically  generated for a LUSID Instrument ID (LUID) unique type by the system. For more information, see  https://support.lusid.com/knowledgebase/article/KA-01862.                The response returns both the collection of successfully created or updated instruments, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.  The maximum number of instruments that this method can upsert per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.instrument_definition import InstrumentDefinition
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_instruments_response import UpsertInstrumentsResponse
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = dict(
        "key": InstrumentDefinition(
            name="name_example",
            identifiers=dict(
                "key": InstrumentIdValue(
                    value="value_example",
                    effective_at=isoparse('1970-01-01T00:00:00.00Z'),
                ),
            ),
            properties=[
                ModelProperty(
                    key="key_example",
                    value=PropertyValue(
                        label_value="label_value_example",
                        metric_value=MetricValue(
                            value=3.14,
                            unit="unit_example",
                        ),
                        label_value_set=LabelValueSet(
                            values=[
                                "values_example",
                            ],
                        ),
                    ),
                    effective_from=isoparse('1970-01-01T00:00:00.00Z'),
                    effective_until=isoparse('1970-01-01T00:00:00.00Z'),
                ),
            ],
            look_through_portfolio_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            definition=LusidInstrument(),
        ),
    )
    try:
        # UpsertInstruments: Upsert instruments
        api_response = api_instance.upsert_instruments(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->upsert_instruments: %s\n" % e)

    # example passing only optional values
    query_params = {
        'scope': "default",
    }
    body = dict(
        "key": InstrumentDefinition(
            name="name_example",
            identifiers=dict(
                "key": InstrumentIdValue(
                    value="value_example",
                    effective_at=isoparse('1970-01-01T00:00:00.00Z'),
                ),
            ),
            properties=[
                ModelProperty(
                    key="key_example",
                    value=PropertyValue(
                        label_value="label_value_example",
                        metric_value=MetricValue(
                            value=3.14,
                            unit="unit_example",
                        ),
                        label_value_set=LabelValueSet(
                            values=[
                                "values_example",
                            ],
                        ),
                    ),
                    effective_from=isoparse('1970-01-01T00:00:00.00Z'),
                    effective_until=isoparse('1970-01-01T00:00:00.00Z'),
                ),
            ],
            look_through_portfolio_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            definition=LusidInstrument(),
        ),
    )
    try:
        # UpsertInstruments: Upsert instruments
        api_response = api_instance.upsert_instruments(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->upsert_instruments: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson

The definitions of the instruments to create or update.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **InstrumentDefinition** | any string name can be used but the value must be the correct type | [optional]

#### SchemaForRequestBodyApplicationJson

The definitions of the instruments to create or update.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **InstrumentDefinition** | any string name can be used but the value must be the correct type | [optional]

#### SchemaForRequestBodyTextJson

The definitions of the instruments to create or update.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **InstrumentDefinition** | any string name can be used but the value must be the correct type | [optional]

#### SchemaForRequestBodyApplicationJson

The definitions of the instruments to create or update.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **InstrumentDefinition** | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | optional


#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | The successfully created or updated instruments along with any failures 
400 | ApiResponseFor400 | The details of the input related failure 
default | ApiResponseForDefault | Error response 

#### ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyTextPlain, SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor201ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md) |  | 


#### SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md) |  | 


#### SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md) |  | 


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



[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments_properties**
> UpsertInstrumentPropertiesResponse upsert_instruments_properties(upsert_instrument_property_request)

UpsertInstrumentsProperties: Upsert instruments properties

Create or update one or more properties for particular instruments.                Each instrument property is updated if it exists and created if it does not. For any failures, a reason  is provided.                Properties have an <i>effectiveFrom</i> datetime from which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import instruments_api
from luisd.model.upsert_instrument_properties_response import UpsertInstrumentPropertiesResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_instrument_property_request import UpsertInstrumentPropertyRequest
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
    api_instance = instruments_api.InstrumentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [{"identifierType":"LusidInstrumentId","identifier":"LUID_00000000","properties":[{"key":"Instrument/MyScope/SomePropertyName","value":{"labelValue":"SomeValue1"},"effectiveFrom":"2016-09-15T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/SomePropertyName","value":{"labelValue":"SomeValue2"},"effectiveFrom":"2017-08-10T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/AnotherPropertyName","value":{"labelValue":"AnotherValue1"},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00","effectiveUntil":"2019-06-01T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/AnotherPropertyName","value":{"labelValue":"AnotherValue2"},"effectiveFrom":"2020-03-15T12:00:00.0000000+00:00","effectiveUntil":"2021-01-15T12:00:00.0000000+00:00"}]}]
    try:
        # UpsertInstrumentsProperties: Upsert instruments properties
        api_response = api_instance.upsert_instruments_properties(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->upsert_instruments_properties: %s\n" % e)

    # example passing only optional values
    query_params = {
        'scope': "default",
    }
    body = [{"identifierType":"LusidInstrumentId","identifier":"LUID_00000000","properties":[{"key":"Instrument/MyScope/SomePropertyName","value":{"labelValue":"SomeValue1"},"effectiveFrom":"2016-09-15T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/SomePropertyName","value":{"labelValue":"SomeValue2"},"effectiveFrom":"2017-08-10T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/AnotherPropertyName","value":{"labelValue":"AnotherValue1"},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00","effectiveUntil":"2019-06-01T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/AnotherPropertyName","value":{"labelValue":"AnotherValue2"},"effectiveFrom":"2020-03-15T12:00:00.0000000+00:00","effectiveUntil":"2021-01-15T12:00:00.0000000+00:00"}]}]
    try:
        # UpsertInstrumentsProperties: Upsert instruments properties
        api_response = api_instance.upsert_instruments_properties(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling InstrumentsApi->upsert_instruments_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson

A list of instruments and associated instrument properties to create or update.

Type | Description | Notes
------------- | ------------- | -------------
**[UpsertInstrumentPropertyRequest]** | A list of instruments and associated instrument properties to create or update. | 

#### SchemaForRequestBodyApplicationJson

A list of instruments and associated instrument properties to create or update.

Type | Description | Notes
------------- | ------------- | -------------
**[UpsertInstrumentPropertyRequest]** | A list of instruments and associated instrument properties to create or update. | 

#### SchemaForRequestBodyTextJson

A list of instruments and associated instrument properties to create or update.

Type | Description | Notes
------------- | ------------- | -------------
**[UpsertInstrumentPropertyRequest]** | A list of instruments and associated instrument properties to create or update. | 

#### SchemaForRequestBodyApplicationJson

A list of instruments and associated instrument properties to create or update.

Type | Description | Notes
------------- | ------------- | -------------
**[UpsertInstrumentPropertyRequest]** | A list of instruments and associated instrument properties to create or update. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | optional


#### ScopeSchema

The scope in which the instrument lies. When not supplied the scope is 'default'.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | The asAt datetime at which the properties were created or updated. 
400 | ApiResponseFor400 | The details of the input related failure 
default | ApiResponseForDefault | Error response 

#### ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyTextPlain, SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor201ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md) |  | 


#### SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md) |  | 


#### SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md) |  | 


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



[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

