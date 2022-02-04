# luisd.ReconciliationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reconcile_generic**](ReconciliationsApi.md#reconcile_generic) | **POST** /api/portfolios/$reconcileGeneric | [EXPERIMENTAL] ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are &#x27;empty&#x27; or null or zero.
[**reconcile_holdings**](ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
[**reconcile_holdings_preview**](ReconciliationsApi.md#reconcile_holdings_preview) | **POST** /api/portfolios/preview/$reconcileholdings | [EXPERIMENTAL] ReconcileHoldingsPreview: Reconcile portfolio holdings with given tolerance
[**reconcile_inline**](ReconciliationsApi.md#reconcile_inline) | **POST** /api/portfolios/$reconcileInline | [BETA] ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
[**reconcile_valuation**](ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | [BETA] ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.

# **reconcile_generic**
> ReconciliationResponse reconcile_generic()

[EXPERIMENTAL] ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.

Perform evaluation of one or two set of holdings (a portfolio of instruments) using one or two (potentially different) configuration recipes.  Produce a breakdown of the resulting differences in evaluation that can be iterated through.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import reconciliations_api
from luisd.model.reconciliation_response import ReconciliationResponse
from luisd.model.reconciliation_request import ReconciliationRequest
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
    api_instance = reconciliations_api.ReconciliationsApi(api_client)

    # example passing only optional values
    body = ReconciliationRequest(
        left=ValuationRequest(
            recipe_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
            metrics=[
                AggregateSpec(
                    key="key_example",
                    op="Sum",
                ),
            ],
            group_by=[
                "group_by_example",
            ],
            filters=[
                PropertyFilter(
                    left="left_example",
                    operator="Equals",
                    right=dict(),
                    right_operand_type="Absolute",
                ),
            ],
            sort=[
                OrderBySpec(
                    key="key_example",
                    sort_order="Ascending",
                ),
            ],
            report_currency="report_currency_example",
            equip_with_subtotals=True,
            portfolio_entity_ids=[
                PortfolioEntityId(
                    scope="z",
                    code="z",
                    portfolio_entity_type="portfolio_entity_type_example",
                ),
            ],
            valuation_schedule=ValuationSchedule(
                effective_from="effective_from_example",
                effective_at="effective_at_example",
                tenor="tenor_example",
                roll_convention="roll_convention_example",
                holiday_calendars=[
                    "holiday_calendars_example",
                ],
                valuation_date_times=[
                    "valuation_date_times_example",
                ],
            ),
        ),
        right=ValuationRequest(
            recipe_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
            metrics=[
                AggregateSpec(
                    key="key_example",
                    op="Sum",
                ),
            ],
            group_by=[
                "group_by_example",
            ],
            filters=[
                PropertyFilter(
                    left="left_example",
                    operator="Equals",
                    right=dict(),
                    right_operand_type="Absolute",
                ),
            ],
            sort=[
                OrderBySpec(
                    key="key_example",
                    sort_order="Ascending",
                ),
            ],
            report_currency="report_currency_example",
            equip_with_subtotals=True,
            portfolio_entity_ids=[
                PortfolioEntityId(
                    scope="z",
                    code="z",
                    portfolio_entity_type="portfolio_entity_type_example",
                ),
            ],
            valuation_schedule=ValuationSchedule(
                effective_from="effective_from_example",
                effective_at="effective_at_example",
                tenor="tenor_example",
                roll_convention="roll_convention_example",
                holiday_calendars=[
                    "holiday_calendars_example",
                ],
                valuation_date_times=[
                    "valuation_date_times_example",
                ],
            ),
        ),
        left_to_right_mapping=[
            ReconciliationLeftRightAddressKeyPair(
                left="left_example",
                right="right_example",
            ),
        ],
        comparison_rules=[
            ReconciliationRule(),
        ],
        preserve_keys=[
            "preserve_keys_example",
        ],
    )
    try:
        # [EXPERIMENTAL] ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.
        api_response = api_instance.reconcile_generic(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_generic: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReconciliationRequest**](ReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReconciliationRequest**](ReconciliationRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReconciliationRequest**](ReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReconciliationRequest**](ReconciliationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested reconciliation 
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
[**ReconciliationResponse**](ReconciliationResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReconciliationResponse**](ReconciliationResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReconciliationResponse**](ReconciliationResponse.md) |  | 


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



[**ReconciliationResponse**](ReconciliationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_holdings**
> ResourceListOfReconciliationBreak reconcile_holdings()

[EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings

Reconcile the holdings of two portfolios.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import reconciliations_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_reconciliation_break import ResourceListOfReconciliationBreak
from luisd.model.portfolios_reconciliation_request import PortfoliosReconciliationRequest
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
    api_instance = reconciliations_api.ReconciliationsApi(api_client)

    # example passing only optional values
    query_params = {
        'sortBy': [
        "sortBy_example",
    ],
        'start': 1,
        'limit': 1,
        'filter': "",
    }
    body = PortfoliosReconciliationRequest(
        left=PortfolioReconciliationRequest(
            portfolio_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            effective_at="effective_at_example",
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
        ),
        right=PortfolioReconciliationRequest(
            portfolio_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            effective_at="effective_at_example",
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
        ),
        instrument_property_keys=[
            "instrument_property_keys_example",
        ],
    )
    try:
        # [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
        api_response = api_instance.reconcile_holdings(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_holdings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sortBy | SortBySchema | | optional
start | StartSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional


#### SortBySchema

Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### StartSchema

Optional. When paginating, skip this number of results

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### LimitSchema

Optional. When paginating, limit the number of returned results to this many.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### FilterSchema

Optional. Expression to filter the result set.              For example, to filter on the left portfolio Code, use \"left.portfolioId.code eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested reconciliation 
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
[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md) |  | 


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



[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_holdings_preview**
> ResourceListOfReconciliationBreak reconcile_holdings_preview()

[EXPERIMENTAL] ReconcileHoldingsPreview: Reconcile portfolio holdings with given tolerance

Reconcile the holdings of two portfolios.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import reconciliations_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.portfolios_reconciliation_request_preview import PortfoliosReconciliationRequestPreview
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_reconciliation_break import ResourceListOfReconciliationBreak
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
    api_instance = reconciliations_api.ReconciliationsApi(api_client)

    # example passing only optional values
    query_params = {
        'sortBy': [
        "sortBy_example",
    ],
        'start': 1,
        'limit': 1,
        'filter': "",
    }
    body = PortfoliosReconciliationRequestPreview(
        tolerance=dict(
            "key": Tolerance(
                value=3.14,
                type="Absolute",
            ),
        ),
        left=PortfolioReconciliationRequest(
            portfolio_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            effective_at="effective_at_example",
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
        ),
        right=PortfolioReconciliationRequest(
            portfolio_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            effective_at="effective_at_example",
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
        ),
        instrument_property_keys=[
            "instrument_property_keys_example",
        ],
    )
    try:
        # [EXPERIMENTAL] ReconcileHoldingsPreview: Reconcile portfolio holdings with given tolerance
        api_response = api_instance.reconcile_holdings_preview(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_holdings_preview: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequestPreview**](PortfoliosReconciliationRequestPreview.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequestPreview**](PortfoliosReconciliationRequestPreview.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequestPreview**](PortfoliosReconciliationRequestPreview.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortfoliosReconciliationRequestPreview**](PortfoliosReconciliationRequestPreview.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sortBy | SortBySchema | | optional
start | StartSchema | | optional
limit | LimitSchema | | optional
filter | FilterSchema | | optional


#### SortBySchema

Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, list, tuple, ] | | 

#### StartSchema

Optional. When paginating, skip this number of results

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### LimitSchema

Optional. When paginating, limit the number of returned results to this many.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[int, None, ] | | 

#### FilterSchema

Optional. Expression to filter the result set

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested reconciliation 
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
[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md) |  | 


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



[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_inline**
> ListAggregationReconciliation reconcile_inline()

[BETA] ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.

Perform valuation of one or two set of inline instruments using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import reconciliations_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.inline_valuations_reconciliation_request import InlineValuationsReconciliationRequest
from luisd.model.list_aggregation_reconciliation import ListAggregationReconciliation
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
    api_instance = reconciliations_api.ReconciliationsApi(api_client)

    # example passing only optional values
    body = InlineValuationsReconciliationRequest(
        left=InlineValuationRequest(
            recipe_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
            metrics=[
                AggregateSpec(
                    key="key_example",
                    op="Sum",
                ),
            ],
            group_by=[
                "group_by_example",
            ],
            filters=[
                PropertyFilter(
                    left="left_example",
                    operator="Equals",
                    right=dict(),
                    right_operand_type="Absolute",
                ),
            ],
            sort=[
                OrderBySpec(
                    key="key_example",
                    sort_order="Ascending",
                ),
            ],
            report_currency="report_currency_example",
            equip_with_subtotals=True,
            valuation_schedule=ValuationSchedule(
                effective_from="effective_from_example",
                effective_at="effective_at_example",
                tenor="tenor_example",
                roll_convention="roll_convention_example",
                holiday_calendars=[
                    "holiday_calendars_example",
                ],
                valuation_date_times=[
                    "valuation_date_times_example",
                ],
            ),
            instruments=[
                WeightedInstrument(
                    quantity=3.14,
                    holding_identifier="holding_identifier_example",
                    instrument=LusidInstrument(),
                ),
            ],
        ),
        right=InlineValuationRequest(
            recipe_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
            metrics=[
                AggregateSpec(
                    key="key_example",
                    op="Sum",
                ),
            ],
            group_by=[
                "group_by_example",
            ],
            filters=[
                PropertyFilter(
                    left="left_example",
                    operator="Equals",
                    right=dict(),
                    right_operand_type="Absolute",
                ),
            ],
            sort=[
                OrderBySpec(
                    key="key_example",
                    sort_order="Ascending",
                ),
            ],
            report_currency="report_currency_example",
            equip_with_subtotals=True,
            valuation_schedule=ValuationSchedule(
                effective_from="effective_from_example",
                effective_at="effective_at_example",
                tenor="tenor_example",
                roll_convention="roll_convention_example",
                holiday_calendars=[
                    "holiday_calendars_example",
                ],
                valuation_date_times=[
                    "valuation_date_times_example",
                ],
            ),
            instruments=[
                WeightedInstrument(
                    quantity=3.14,
                    holding_identifier="holding_identifier_example",
                    instrument=LusidInstrument(),
                ),
            ],
        ),
        left_to_right_mapping=[
            ReconciliationLeftRightAddressKeyPair(
                left="left_example",
                right="right_example",
            ),
        ],
        preserve_keys=[
            "preserve_keys_example",
        ],
    )
    try:
        # [BETA] ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
        api_response = api_instance.reconcile_inline(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_inline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested reconciliation 
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
[**ListAggregationReconciliation**](ListAggregationReconciliation.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationReconciliation**](ListAggregationReconciliation.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationReconciliation**](ListAggregationReconciliation.md) |  | 


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



[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_valuation**
> ListAggregationReconciliation reconcile_valuation()

[BETA] ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.

Perform valuation of one or two set of holdings using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import reconciliations_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.list_aggregation_reconciliation import ListAggregationReconciliation
from luisd.model.valuations_reconciliation_request import ValuationsReconciliationRequest
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
    api_instance = reconciliations_api.ReconciliationsApi(api_client)

    # example passing only optional values
    body = ValuationsReconciliationRequest(
        left=ValuationRequest(
            recipe_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
            metrics=[
                AggregateSpec(
                    key="key_example",
                    op="Sum",
                ),
            ],
            group_by=[
                "group_by_example",
            ],
            filters=[
                PropertyFilter(
                    left="left_example",
                    operator="Equals",
                    right=dict(),
                    right_operand_type="Absolute",
                ),
            ],
            sort=[
                OrderBySpec(
                    key="key_example",
                    sort_order="Ascending",
                ),
            ],
            report_currency="report_currency_example",
            equip_with_subtotals=True,
            portfolio_entity_ids=[
                PortfolioEntityId(
                    scope="z",
                    code="z",
                    portfolio_entity_type="portfolio_entity_type_example",
                ),
            ],
            valuation_schedule=ValuationSchedule(
                effective_from="effective_from_example",
                effective_at="effective_at_example",
                tenor="tenor_example",
                roll_convention="roll_convention_example",
                holiday_calendars=[
                    "holiday_calendars_example",
                ],
                valuation_date_times=[
                    "valuation_date_times_example",
                ],
            ),
        ),
        right=ValuationRequest(
            recipe_id=ResourceId(
                scope="scope_example",
                code="code_example",
            ),
            as_at=isoparse('1970-01-01T00:00:00.00Z'),
            metrics=[
                AggregateSpec(
                    key="key_example",
                    op="Sum",
                ),
            ],
            group_by=[
                "group_by_example",
            ],
            filters=[
                PropertyFilter(
                    left="left_example",
                    operator="Equals",
                    right=dict(),
                    right_operand_type="Absolute",
                ),
            ],
            sort=[
                OrderBySpec(
                    key="key_example",
                    sort_order="Ascending",
                ),
            ],
            report_currency="report_currency_example",
            equip_with_subtotals=True,
            portfolio_entity_ids=[
                PortfolioEntityId(
                    scope="z",
                    code="z",
                    portfolio_entity_type="portfolio_entity_type_example",
                ),
            ],
            valuation_schedule=ValuationSchedule(
                effective_from="effective_from_example",
                effective_at="effective_at_example",
                tenor="tenor_example",
                roll_convention="roll_convention_example",
                holiday_calendars=[
                    "holiday_calendars_example",
                ],
                valuation_date_times=[
                    "valuation_date_times_example",
                ],
            ),
        ),
        left_to_right_mapping=[
            ReconciliationLeftRightAddressKeyPair(
                left="left_example",
                right="right_example",
            ),
        ],
        preserve_keys=[
            "preserve_keys_example",
        ],
    )
    try:
        # [BETA] ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
        api_response = api_instance.reconcile_valuation(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_valuation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested reconciliation 
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
[**ListAggregationReconciliation**](ListAggregationReconciliation.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationReconciliation**](ListAggregationReconciliation.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListAggregationReconciliation**](ListAggregationReconciliation.md) |  | 


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



[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

