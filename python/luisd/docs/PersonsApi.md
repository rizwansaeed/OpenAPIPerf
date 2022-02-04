# luisd.PersonsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_person**](PersonsApi.md#delete_person) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] DeletePerson: Delete person
[**delete_person_access_metadata**](PersonsApi.md#delete_person_access_metadata) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
[**delete_person_identifiers**](PersonsApi.md#delete_person_identifiers) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] DeletePersonIdentifiers: Delete Person Identifiers
[**delete_person_properties**](PersonsApi.md#delete_person_properties) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] DeletePersonProperties: Delete Person Properties
[**get_all_person_access_metadata**](PersonsApi.md#get_all_person_access_metadata) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
[**get_person**](PersonsApi.md#get_person) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] GetPerson: Get Person
[**get_person_access_metadata_by_key**](PersonsApi.md#get_person_access_metadata_by_key) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
[**get_person_property_time_series**](PersonsApi.md#get_person_property_time_series) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EXPERIMENTAL] GetPersonPropertyTimeSeries: Get Person Property Time Series
[**get_person_relations**](PersonsApi.md#get_person_relations) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [EXPERIMENTAL] GetPersonRelations: Get Relations for Person
[**get_person_relationships**](PersonsApi.md#get_person_relationships) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relationships | [EXPERIMENTAL] GetPersonRelationships: Get Relationships for Person
[**list_persons**](PersonsApi.md#list_persons) | **GET** /api/persons/{idTypeScope}/{idTypeCode} | [EXPERIMENTAL] ListPersons: List Persons
[**set_person_identifiers**](PersonsApi.md#set_person_identifiers) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] SetPersonIdentifiers: Set Person Identifiers
[**set_person_properties**](PersonsApi.md#set_person_properties) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] SetPersonProperties: Set Person Properties
[**upsert_person**](PersonsApi.md#upsert_person) | **POST** /api/persons | [EXPERIMENTAL] UpsertPerson: Upsert Person
[**upsert_person_access_metadata**](PersonsApi.md#upsert_person_access_metadata) | **PUT** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

# **delete_person**
> DeletedEntityResponse delete_person(id_type_scopeid_type_codecode)

[EXPERIMENTAL] DeletePerson: Delete person

Delete a person. Deletion will be valid from the person's creation datetime.  This means that the person will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.deleted_entity_response import DeletedEntityResponse
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "26bUUGjjNSwg0_bs9ZayI",
        'idTypeCode': "26bUUGjjNSwg0_bs9ZayI",
        'code': "26bUUGjjNSwg0_bs9ZayI",
    }
    try:
        # [EXPERIMENTAL] DeletePerson: Delete person
        api_response = api_instance.delete_person(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

The scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The scope of the person identifier type. | 

#### IdTypeCodeSchema

The code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The code of the person identifier type. | 

#### CodeSchema

Code of the person under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the person to delete.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the person to delete. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The response from deleting person. 
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
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


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



[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_access_metadata**
> DeletedEntityResponse delete_person_access_metadata(id_type_scopeid_type_codecodemetadata_key)

[EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry

Deletes the Person Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.deleted_entity_response import DeletedEntityResponse
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
        'metadataKey': "z",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
        api_response = api_instance.delete_person_access_metadata(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person_access_metadata: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
        'metadataKey': "z",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
    }
    try:
        # [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
        api_response = api_instance.delete_person_access_metadata(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person_access_metadata: %s\n" % e)
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


#### EffectiveAtSchema

The effective date to delete at, if this is not supplied, it will delete all data found

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 
metadataKey | MetadataKeySchema | | 

#### IdTypeScopeSchema

Scope of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Scope of the person identifier. | 

#### IdTypeCodeSchema

Code of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person identifier. | 

#### CodeSchema

Code of the person under specified identifier type's scope and code.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person under specified identifier type&#x27;s scope and code. | 

#### MetadataKeySchema

Key of the metadata entry to retrieve

Type | Description | Notes
------------- | ------------- | -------------
**str** | Key of the metadata entry to retrieve | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The Access Metadata with the given metadataKey has been deleted 
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
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


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



[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_identifiers**
> DeletedEntityResponse delete_person_identifiers(id_type_scopeid_type_codecodeproperty_keys)

[EXPERIMENTAL] DeletePersonIdentifiers: Delete Person Identifiers

Delete identifiers that belong to the given property keys of the person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.deleted_entity_response import DeletedEntityResponse
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "z",
        'idTypeCode': "z",
        'code': "z",
    }
    query_params = {
        'propertyKeys': [
        "propertyKeys_example",
    ],
    }
    try:
        # [EXPERIMENTAL] DeletePersonIdentifiers: Delete Person Identifiers
        api_response = api_instance.delete_person_identifiers(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person_identifiers: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "z",
        'idTypeCode': "z",
        'code': "z",
    }
    query_params = {
        'propertyKeys': [
        "propertyKeys_example",
    ],
        'effectiveAt': "effectiveAt_example",
    }
    try:
        # [EXPERIMENTAL] DeletePersonIdentifiers: Delete Person Identifiers
        api_response = api_instance.delete_person_identifiers(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person_identifiers: %s\n" % e)
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
propertyKeys | PropertyKeysSchema | | 
effectiveAt | EffectiveAtSchema | | optional


#### PropertyKeysSchema

The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". Each property must be from the \"Person\" domain. Identifiers or identifiers not specified in request will not be changed.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. Each property must be from the \&quot;Person\&quot; domain. Identifiers or identifiers not specified in request will not be changed. | 

#### EffectiveAtSchema

The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime if identifiers are perpetual.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The datetime that the identifiers were deleted from the specified person 
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
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


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



[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_properties**
> DeletedEntityResponse delete_person_properties(id_type_scopeid_type_codecodeproperty_keys)

[EXPERIMENTAL] DeletePersonProperties: Delete Person Properties

Delete all properties that belong to the given property keys of the person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.deleted_entity_response import DeletedEntityResponse
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "z",
        'idTypeCode': "z",
        'code': "z",
    }
    query_params = {
        'propertyKeys': [
        "propertyKeys_example",
    ],
    }
    try:
        # [EXPERIMENTAL] DeletePersonProperties: Delete Person Properties
        api_response = api_instance.delete_person_properties(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person_properties: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "z",
        'idTypeCode': "z",
        'code': "z",
    }
    query_params = {
        'propertyKeys': [
        "propertyKeys_example",
    ],
        'effectiveAt': "effectiveAt_example",
    }
    try:
        # [EXPERIMENTAL] DeletePersonProperties: Delete Person Properties
        api_response = api_instance.delete_person_properties(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->delete_person_properties: %s\n" % e)
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
propertyKeys | PropertyKeysSchema | | 
effectiveAt | EffectiveAtSchema | | optional


#### PropertyKeysSchema

The property keys of the person's properties to delete. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". Each property must be from the \"Person\" domain. Properties or identifiers not specified in request will not be changed.

Type | Description | Notes
------------- | ------------- | -------------
**[str]** | The property keys of the person&#x27;s properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. Each property must be from the \&quot;Person\&quot; domain. Properties or identifiers not specified in request will not be changed. | 

#### EffectiveAtSchema

The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The datetime that the properties were deleted from the specified person 
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
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedEntityResponse**](DeletedEntityResponse.md) |  | 


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



[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_person_access_metadata**
> {str: ([AccessMetadataValue],)} get_all_person_access_metadata(id_type_scopeid_type_codecode)

[EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person

Pass the Scope and Code of the Person identifier along with the person code parameter to retrieve the associated Access Metadata

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.access_metadata_value import AccessMetadataValue
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
        api_response = api_instance.get_all_person_access_metadata(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_all_person_access_metadata: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
    }
    try:
        # [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
        api_response = api_instance.get_all_person_access_metadata(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_all_person_access_metadata: %s\n" % e)
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


#### EffectiveAtSchema

The effectiveAt datetime at which to retrieve the Access Metadata

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the Access Metadata

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Scope of the person identifier. | 

#### IdTypeCodeSchema

Code of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person identifier. | 

#### CodeSchema

Code of the person under specified identifier type's scope and code.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person under specified identifier type&#x27;s scope and code. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The access metadata for the Person or any failure. 
400 | ApiResponseFor400 | The details of the input related failure 
default | ApiResponseForDefault | Error response 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyTextPlain

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **[AccessMetadataValue]** | any string name can be used but the value must be the correct type | [optional]

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **[AccessMetadataValue]** | any string name can be used but the value must be the correct type | [optional]

#### SchemaFor200ResponseBodyTextJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **[AccessMetadataValue]** | any string name can be used but the value must be the correct type | [optional]

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



**{str: ([AccessMetadataValue],)}**

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> Person get_person(id_type_scopeid_type_codecode)

[EXPERIMENTAL] GetPerson: Get Person

Retrieve the definition of a person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.person import Person
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetPerson: Get Person
        api_response = api_instance.get_person(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
        'propertyKeys': [
        "propertyKeys_example",
    ],
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
    }
    try:
        # [EXPERIMENTAL] GetPerson: Get Person
        api_response = api_instance.get_person(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person: %s\n" % e)
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
propertyKeys | PropertyKeysSchema | | optional
effectiveAt | EffectiveAtSchema | | optional
asAt | AsAtSchema | | optional


#### PropertyKeysSchema

A list of property keys from the \"Person\" domain to decorate onto each person.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\". Defaults to include all properties if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### EffectiveAtSchema

The effective datetime or cut label at which to retrieve the person. Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the person. Defaults to return the latest version of the person if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested person definition 
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
[**Person**](Person.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


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



[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_access_metadata_by_key**
> [AccessMetadataValue] get_person_access_metadata_by_key(id_type_scopeid_type_codecodemetadata_key)

[EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person

Get a specific Person Access Metadata by specifying the corresponding identifier parts and Person code                No matching will be performed through this endpoint. To retrieve an entry, it is necessary to specify, exactly, the identifier of the entry

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.access_metadata_value import AccessMetadataValue
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
        'metadataKey': "z",
    }
    query_params = {
    }
    try:
        # [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
        api_response = api_instance.get_person_access_metadata_by_key(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_access_metadata_by_key: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
        'metadataKey': "z",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
    }
    try:
        # [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
        api_response = api_instance.get_person_access_metadata_by_key(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_access_metadata_by_key: %s\n" % e)
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


#### EffectiveAtSchema

The effectiveAt datetime at which to retrieve the Access Metadata

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the Access Metadata

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 
metadataKey | MetadataKeySchema | | 

#### IdTypeScopeSchema

Scope of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Scope of the person identifier. | 

#### IdTypeCodeSchema

Code of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person identifier. | 

#### CodeSchema

Code of the person under specified identifier type's scope and code.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person under specified identifier type&#x27;s scope and code. | 

#### MetadataKeySchema

Key of the metadata entry to retrieve

Type | Description | Notes
------------- | ------------- | -------------
**str** | Key of the metadata entry to retrieve | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The successfully retrieved Person access metadata filtered by metadataKey or any failure. 
400 | ApiResponseFor400 | The details of the input related failure 
default | ApiResponseForDefault | Error response 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyTextPlain

Type | Description | Notes
------------- | ------------- | -------------
**[AccessMetadataValue]** |  | 

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[AccessMetadataValue]** |  | 

#### SchemaFor200ResponseBodyTextJson

Type | Description | Notes
------------- | ------------- | -------------
**[AccessMetadataValue]** |  | 

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



[**[AccessMetadataValue]**](AccessMetadataValue.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_property_time_series**
> ResourceListOfPropertyInterval get_person_property_time_series(id_type_scopeid_type_codecodeproperty_key)

[EXPERIMENTAL] GetPersonPropertyTimeSeries: Get Person Property Time Series

List the complete time series of a person property.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
        'propertyKey': "propertyKey_example",
    }
    try:
        # [EXPERIMENTAL] GetPersonPropertyTimeSeries: Get Person Property Time Series
        api_response = api_instance.get_person_property_time_series(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_property_time_series: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
        'propertyKey': "propertyKey_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'filter': "",
        'page': "",
        'limit': 1,
    }
    try:
        # [EXPERIMENTAL] GetPersonPropertyTimeSeries: Get Person Property Time Series
        api_response = api_instance.get_person_property_time_series(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_property_time_series: %s\n" % e)
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
asAt | AsAtSchema | | optional
filter | FilterSchema | | optional
page | PageSchema | | optional
limit | LimitSchema | | optional


#### PropertyKeySchema

The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}. | 

#### AsAtSchema

The asAt datetime at which to list the person's property history. Defaults to return the current datetime if not supplied.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### FilterSchema

Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### PageSchema

The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### LimitSchema

When paginating, limit the number of returned results to this many.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely identifies the person.

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

# **get_person_relations**
> ResourceListOfRelation get_person_relations(id_type_scopeid_type_codecode)

[EXPERIMENTAL] GetPersonRelations: Get Relations for Person

Get relations for the specified person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_relation import ResourceListOfRelation
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetPersonRelations: Get Relations for Person
        api_response = api_instance.get_person_relations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_relations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'filter': "",
        'identifierTypes': [
        "identifierTypes_example",
    ],
    }
    try:
        # [EXPERIMENTAL] GetPersonRelations: Get Relations for Person
        api_response = api_instance.get_person_relations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_relations: %s\n" % e)
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
filter | FilterSchema | | optional
identifierTypes | IdentifierTypesSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve the person's relations. Defaults to return the latest LUSID AsAt time if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### FilterSchema

Expression to filter the relations. Users should provide null or empty string for this field until further notice.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierTypesSchema

Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The relations for the specified person. 
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
[**ResourceListOfRelation**](ResourceListOfRelation.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelation**](ResourceListOfRelation.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelation**](ResourceListOfRelation.md) |  | 


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



[**ResourceListOfRelation**](ResourceListOfRelation.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_relationships**
> ResourceListOfRelationship get_person_relationships(id_type_scopeid_type_codecode)

[EXPERIMENTAL] GetPersonRelationships: Get Relationships for Person

Get relationships for the specified person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_relationship import ResourceListOfRelationship
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "z",
        'idTypeCode': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetPersonRelationships: Get Relationships for Person
        api_response = api_instance.get_person_relationships(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_relationships: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "z",
        'idTypeCode': "z",
        'code': "z",
    }
    query_params = {
        'effectiveAt': "A",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'filter': "",
        'identifierTypes': [
        "identifierTypes_example",
    ],
    }
    try:
        # [EXPERIMENTAL] GetPersonRelationships: Get Relationships for Person
        api_response = api_instance.get_person_relationships(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->get_person_relationships: %s\n" % e)
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
filter | FilterSchema | | optional
identifierTypes | IdentifierTypesSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### FilterSchema

Expression to filter relationships. Users should provide null or empty string for this field until further notice.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdentifierTypesSchema

Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person's identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person's identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The relationships for the specified person. 
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
[**ResourceListOfRelationship**](ResourceListOfRelationship.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelationship**](ResourceListOfRelationship.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfRelationship**](ResourceListOfRelationship.md) |  | 


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



[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_persons**
> PagedResourceListOfPerson list_persons(id_type_scopeid_type_code)

[EXPERIMENTAL] ListPersons: List Persons

List persons which have identifiers of a specific identifier type's scope and code, and satisfies filter criteria.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.paged_resource_list_of_person import PagedResourceListOfPerson
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] ListPersons: List Persons
        api_response = api_instance.list_persons(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->list_persons: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'page': "zA9LCSLv1C1ylmgd0/Y2T",
        'start': 1,
        'limit': 1,
        'filter': "",
        'propertyKeys': [
        "propertyKeys_example",
    ],
    }
    try:
        # [EXPERIMENTAL] ListPersons: List Persons
        api_response = api_instance.list_persons(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->list_persons: %s\n" % e)
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
start | StartSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional
propertyKeys | PropertyKeysSchema | | optional


#### EffectiveAtSchema

The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### AsAtSchema

The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### PageSchema

The pagination token to use to continue listing portfolios from a previous call to list portfolios. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### StartSchema

When paginating, skip this number of results.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### LimitSchema

When paginating, limit the number of returned results to this many. Defaults to 100 if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### FilterSchema

Expression to filter the result set.               For example, to filter on the LUPID, use \"lusidPersonId eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### PropertyKeysSchema

A list of property keys from the \"Person\" domain to decorate onto each person.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\".

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | People in specified scope 
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
[**PagedResourceListOfPerson**](PagedResourceListOfPerson.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPerson**](PagedResourceListOfPerson.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfPerson**](PagedResourceListOfPerson.md) |  | 


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



[**PagedResourceListOfPerson**](PagedResourceListOfPerson.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_person_identifiers**
> Person set_person_identifiers(id_type_scopeid_type_codecodeset_person_identifiers_request)

[EXPERIMENTAL] SetPersonIdentifiers: Set Person Identifiers

Set identifiers of the person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.person import Person
from luisd.model.set_person_identifiers_request import SetPersonIdentifiersRequest
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    body = SetPersonIdentifiersRequest(
        identifiers=dict(
            "key": ModelProperty(
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
        ),
    )
    try:
        # [EXPERIMENTAL] SetPersonIdentifiers: Set Person Identifiers
        api_response = api_instance.set_person_identifiers(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->set_person_identifiers: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
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
[**SetPersonIdentifiersRequest**](SetPersonIdentifiersRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetPersonIdentifiersRequest**](SetPersonIdentifiersRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetPersonIdentifiersRequest**](SetPersonIdentifiersRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetPersonIdentifiersRequest**](SetPersonIdentifiersRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The Person with updated identifiers. 
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
[**Person**](Person.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


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



[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_person_properties**
> Person set_person_properties(id_type_scopeid_type_codecodeset_person_properties_request)

[EXPERIMENTAL] SetPersonProperties: Set Person Properties

Set properties of the person.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.person import Person
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.set_person_properties_request import SetPersonPropertiesRequest
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
    }
    body = SetPersonPropertiesRequest(
        properties=dict(
            "key": [
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
        ),
    )
    try:
        # [EXPERIMENTAL] SetPersonProperties: Set Person Properties
        api_response = api_instance.set_person_properties(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->set_person_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
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
[**SetPersonPropertiesRequest**](SetPersonPropertiesRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetPersonPropertiesRequest**](SetPersonPropertiesRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetPersonPropertiesRequest**](SetPersonPropertiesRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetPersonPropertiesRequest**](SetPersonPropertiesRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 

#### IdTypeScopeSchema

Scope of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### IdTypeCodeSchema

Code of the person identifier type.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The Person with updated properties or identifiers. 
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
[**Person**](Person.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


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



[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_person**
> Person upsert_person(upsert_person_request)

[EXPERIMENTAL] UpsertPerson: Upsert Person

Create or update a new person under the specified scope.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.person import Person
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_person_request import UpsertPersonRequest
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    body = UpsertPersonRequest(
        identifiers=dict(
            "key": ModelProperty(
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
        ),
        properties=dict(
            "key": [
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
        ),
        display_name="display_name_example",
        description="description_example",
    )
    try:
        # [EXPERIMENTAL] UpsertPerson: Upsert Person
        api_response = api_instance.upsert_person(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->upsert_person: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonRequest**](UpsertPersonRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonRequest**](UpsertPersonRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonRequest**](UpsertPersonRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonRequest**](UpsertPersonRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | The newly created or updated person 
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
[**Person**](Person.md) |  | 


#### SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


#### SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Person**](Person.md) |  | 


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



[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_person_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_person_access_metadata(id_type_scopeid_type_codecodemetadata_keyupsert_person_access_metadata_request)

[EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Person Access Metadata entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Person Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import persons_api
from luisd.model.upsert_person_access_metadata_request import UpsertPersonAccessMetadataRequest
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_access_metadata_value_of import ResourceListOfAccessMetadataValueOf
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
    api_instance = persons_api.PersonsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
        'metadataKey': "metadataKey_example",
    }
    query_params = {
    }
    body = UpsertPersonAccessMetadataRequest(
        metadata=[
            AccessMetadataValue(
                value="value_example",
                provider="provider_example",
            ),
        ],
    )
    try:
        # [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
        api_response = api_instance.upsert_person_access_metadata(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->upsert_person_access_metadata: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idTypeScope': "idTypeScope_example",
        'idTypeCode': "idTypeCode_example",
        'code': "z",
        'metadataKey': "metadataKey_example",
    }
    query_params = {
        'effectiveAt': "effectiveAt_example",
    }
    body = UpsertPersonAccessMetadataRequest(
        metadata=[
            AccessMetadataValue(
                value="value_example",
                provider="provider_example",
            ),
        ],
    )
    try:
        # [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
        api_response = api_instance.upsert_person_access_metadata(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling PersonsApi->upsert_person_access_metadata: %s\n" % e)
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
[**UpsertPersonAccessMetadataRequest**](UpsertPersonAccessMetadataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonAccessMetadataRequest**](UpsertPersonAccessMetadataRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonAccessMetadataRequest**](UpsertPersonAccessMetadataRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertPersonAccessMetadataRequest**](UpsertPersonAccessMetadataRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
effectiveAt | EffectiveAtSchema | | optional


#### EffectiveAtSchema

The effectiveAt datetime at which to upsert the Access Metadata

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idTypeScope | IdTypeScopeSchema | | 
idTypeCode | IdTypeCodeSchema | | 
code | CodeSchema | | 
metadataKey | MetadataKeySchema | | 

#### IdTypeScopeSchema

Scope of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Scope of the person identifier. | 

#### IdTypeCodeSchema

Code of the person identifier.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person identifier. | 

#### CodeSchema

Code of the person under specified identifier type's scope and code.

Type | Description | Notes
------------- | ------------- | -------------
**str** | Code of the person under specified identifier type&#x27;s scope and code. | 

#### MetadataKeySchema

Key of the metadata entry to retrieve

Type | Description | Notes
------------- | ------------- | -------------
**str** | Key of the metadata entry to retrieve | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The successfully updated or inserted item or any failure. 
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
[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md) |  | 


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



[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

