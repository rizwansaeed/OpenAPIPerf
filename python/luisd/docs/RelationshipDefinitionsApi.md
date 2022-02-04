# luisd.RelationshipDefinitionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship_definition**](RelationshipDefinitionsApi.md#create_relationship_definition) | **POST** /api/relationshipdefinitions | [EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition
[**get_relationship_definition**](RelationshipDefinitionsApi.md#get_relationship_definition) | **GET** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
[**list_relationship_definitions**](RelationshipDefinitionsApi.md#list_relationship_definitions) | **GET** /api/relationshipdefinitions | [EXPERIMENTAL] ListRelationshipDefinitions: List relationship definitions
[**update_relationship_definition**](RelationshipDefinitionsApi.md#update_relationship_definition) | **PUT** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition

# **create_relationship_definition**
> RelationshipDefinition create_relationship_definition(create_relationship_definition_request)

[EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition

Create a new relationship definition to be used for creating relationships between entities.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import relationship_definitions_api
from luisd.model.create_relationship_definition_request import CreateRelationshipDefinitionRequest
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.relationship_definition import RelationshipDefinition
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
    api_instance = relationship_definitions_api.RelationshipDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateRelationshipDefinitionRequest(
        scope="z",
        code="z",
        source_entity_type="source_entity_type_example",
        target_entity_type="target_entity_type_example",
        display_name="",
        outward_description="",
        inward_description="",
        life_time="life_time_example",
        relationship_cardinality="relationship_cardinality_example",
    )
    try:
        # [EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition
        api_response = api_instance.create_relationship_definition(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->create_relationship_definition: %s\n" % e)
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
[**CreateRelationshipDefinitionRequest**](CreateRelationshipDefinitionRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateRelationshipDefinitionRequest**](CreateRelationshipDefinitionRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateRelationshipDefinitionRequest**](CreateRelationshipDefinitionRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateRelationshipDefinitionRequest**](CreateRelationshipDefinitionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | The newly created relationship definition 
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
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


#### SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


#### SchemaFor201ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


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



[**RelationshipDefinition**](RelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationship_definition**
> RelationshipDefinition get_relationship_definition(scopecode)

[EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition

Retrieve the specified relationship definition

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import relationship_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.relationship_definition import RelationshipDefinition
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
    api_instance = relationship_definitions_api.RelationshipDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
        api_response = api_instance.get_relationship_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->get_relationship_definition: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
    }
    try:
        # [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
        api_response = api_instance.get_relationship_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->get_relationship_definition: %s\n" % e)
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
asAt | AsAtSchema | | optional


#### AsAtSchema

The asAt datetime at which to retrieve the relationship definition. Defaults to return              the latest version of the definition if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

#### ScopeSchema

The scope of the specified relationship definition.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

The code of the specified relationship definition. Together with the domain and scope this uniquely              identifies the relationship definition.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested relationship definition 
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
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


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



[**RelationshipDefinition**](RelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_relationship_definitions**
> PagedResourceListOfRelationshipDefinition list_relationship_definitions()

[EXPERIMENTAL] ListRelationshipDefinitions: List relationship definitions

Retrieve one or more specified relationship definitions.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import relationship_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.paged_resource_list_of_relationship_definition import PagedResourceListOfRelationshipDefinition
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
    api_instance = relationship_definitions_api.RelationshipDefinitionsApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'page': "zA9LCSLv1C1ylmgd0/Y2T",
        'limit': 1,
        'filter': "",
    }
    try:
        # [EXPERIMENTAL] ListRelationshipDefinitions: List relationship definitions
        api_response = api_instance.list_relationship_definitions(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->list_relationship_definitions: %s\n" % e)
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
page | PageSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional


#### AsAtSchema

The asAt datetime at which to retrieve the relationship definitions. Defaults to return              the latest version of each definition if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### PageSchema

The pagination token to use to continue listing relationship definitions from a previous call to list relationship definitions. This  value is returned from the previous call. If a pagination token is provided the filter, asAt field  must not have changed since the original request.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### LimitSchema

When paginating, limit the number of returned results to this many. Defaults to 100 if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### FilterSchema

Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'ExampleScope'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested relationship definitions 
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
[**PagedResourceListOfRelationshipDefinition**](PagedResourceListOfRelationshipDefinition.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfRelationshipDefinition**](PagedResourceListOfRelationshipDefinition.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PagedResourceListOfRelationshipDefinition**](PagedResourceListOfRelationshipDefinition.md) |  | 


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



[**PagedResourceListOfRelationshipDefinition**](PagedResourceListOfRelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_relationship_definition**
> RelationshipDefinition update_relationship_definition(scopecodeupdate_relationship_definition_request)

[EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition

Update the definition of a specified existing relationship. Not all elements within a relationship definition  are modifiable due to the potential implications for values already stored against the relationship.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import relationship_definitions_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.relationship_definition import RelationshipDefinition
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.update_relationship_definition_request import UpdateRelationshipDefinitionRequest
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
    api_instance = relationship_definitions_api.RelationshipDefinitionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    body = UpdateRelationshipDefinitionRequest(
        display_name="",
        outward_description="",
        inward_description="",
    )
    try:
        # [EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition
        api_response = api_instance.update_relationship_definition(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->update_relationship_definition: %s\n" % e)
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
[**UpdateRelationshipDefinitionRequest**](UpdateRelationshipDefinitionRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateRelationshipDefinitionRequest**](UpdateRelationshipDefinitionRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateRelationshipDefinitionRequest**](UpdateRelationshipDefinitionRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateRelationshipDefinitionRequest**](UpdateRelationshipDefinitionRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | 
code | CodeSchema | | 

#### ScopeSchema

The scope of the relationship definition being updated.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

#### CodeSchema

The code of the relationship definition being updated. Together with the scope this uniquely              identifies the relationship definition.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The updated relationship definition 
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
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RelationshipDefinition**](RelationshipDefinition.md) |  | 


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



[**RelationshipDefinition**](RelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

