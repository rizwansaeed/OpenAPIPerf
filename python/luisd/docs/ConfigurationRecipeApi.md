# luisd.ConfigurationRecipeApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration_recipe**](ConfigurationRecipeApi.md#delete_configuration_recipe) | **DELETE** /api/recipes/{scope}/{code} | [EXPERIMENTAL] DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.
[**get_configuration_recipe**](ConfigurationRecipeApi.md#get_configuration_recipe) | **GET** /api/recipes/{scope}/{code} | [EXPERIMENTAL] GetConfigurationRecipe: Get Configuration Recipe
[**list_configuration_recipes**](ConfigurationRecipeApi.md#list_configuration_recipes) | **GET** /api/recipes | [EXPERIMENTAL] ListConfigurationRecipes: List the set of Configuration Recipes
[**upsert_configuration_recipe**](ConfigurationRecipeApi.md#upsert_configuration_recipe) | **POST** /api/recipes | [EXPERIMENTAL] UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.

# **delete_configuration_recipe**
> AnnulSingleStructuredDataResponse delete_configuration_recipe(scopecode)

[EXPERIMENTAL] DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.

Delete the specified Configuration Recipe from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import configuration_recipe_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
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
    api_instance = configuration_recipe_api.ConfigurationRecipeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    try:
        # [EXPERIMENTAL] DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.
        api_response = api_instance.delete_configuration_recipe(
            path_params=path_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->delete_configuration_recipe: %s\n" % e)
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
scope | ScopeSchema | | 
code | CodeSchema | | 

#### ScopeSchema

The scope of the Configuration Recipe to delete.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The scope of the Configuration Recipe to delete. | 

#### CodeSchema

The Configuration Recipe to delete.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The Configuration Recipe to delete. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The AsAt of deletion or failure 
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
[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md) |  | 


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



[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_recipe**
> GetRecipeResponse get_configuration_recipe(scopecode)

[EXPERIMENTAL] GetConfigurationRecipe: Get Configuration Recipe

Get a Configuration Recipe from a single scope.                The response will return either the recipe that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import configuration_recipe_api
from luisd.model.get_recipe_response import GetRecipeResponse
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
    api_instance = configuration_recipe_api.ConfigurationRecipeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
    }
    try:
        # [EXPERIMENTAL] GetConfigurationRecipe: Get Configuration Recipe
        api_response = api_instance.get_configuration_recipe(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->get_configuration_recipe: %s\n" % e)

    # example passing only optional values
    path_params = {
        'scope': "z",
        'code': "z",
    }
    query_params = {
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
    }
    try:
        # [EXPERIMENTAL] GetConfigurationRecipe: Get Configuration Recipe
        api_response = api_instance.get_configuration_recipe(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->get_configuration_recipe: %s\n" % e)
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

The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified.

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

The scope of the Configuration Recipe to retrieve.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The scope of the Configuration Recipe to retrieve. | 

#### CodeSchema

The name of the recipe to retrieve the data for.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The name of the recipe to retrieve the data for. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The successfully retrieved Configuration Recipe or any failure 
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
[**GetRecipeResponse**](GetRecipeResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetRecipeResponse**](GetRecipeResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetRecipeResponse**](GetRecipeResponse.md) |  | 


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



[**GetRecipeResponse**](GetRecipeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_recipes**
> ResourceListOfGetRecipeResponse list_configuration_recipes()

[EXPERIMENTAL] ListConfigurationRecipes: List the set of Configuration Recipes

List the set of configuration recipes at the specified date/time and scope

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import configuration_recipe_api
from luisd.model.resource_list_of_get_recipe_response import ResourceListOfGetRecipeResponse
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
    api_instance = configuration_recipe_api.ConfigurationRecipeApi(api_client)

    # example passing only optional values
    query_params = {
        'asAt': isoparse('1970-01-01T00:00:00.00Z'),
        'filter': "",
    }
    try:
        # [EXPERIMENTAL] ListConfigurationRecipes: List the set of Configuration Recipes
        api_response = api_instance.list_configuration_recipes(
            query_params=query_params,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->list_configuration_recipes: %s\n" % e)
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
filter | FilterSchema | | optional


#### AsAtSchema

The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[None, ] | | 

#### FilterSchema

Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid.

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[str, None, ] | | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The requested configuration recipes 
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
[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md) |  | 


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



[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_configuration_recipe**
> UpsertSingleStructuredDataResponse upsert_configuration_recipe(upsert_recipe_request)

[EXPERIMENTAL] UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.

Update or insert one Configuration Recipe in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Configuration Recipe or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
import luisd
from luisd.api import configuration_recipe_api
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.upsert_recipe_request import UpsertRecipeRequest
from luisd.model.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
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
    api_instance = configuration_recipe_api.ConfigurationRecipeApi(api_client)

    # example passing only required values which don't have defaults set
    body = UpsertRecipeRequest(
        configuration_recipe=ConfigurationRecipe(
            scope="z",
            code="z",
            market=MarketContext(
                market_rules=[
                    MarketDataKeyRule(
                        key="key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        quote_type="Price",
                        field="field_example",
                        quote_interval="quote_interval_example",
                        as_at=isoparse('1970-01-01T00:00:00.00Z'),
                        price_source="price_source_example",
                        mask="mask_example",
                    ),
                ],
                suppliers=MarketContextSuppliers(
                    commodity="commodity_example",
                    credit="credit_example",
                    equity="equity_example",
                    fx="fx_example",
                    rates="rates_example",
                ),
                options=MarketOptions(
                    default_supplier="default_supplier_example",
                    default_instrument_code_type="default_instrument_code_type_example",
                    default_scope="z",
                    attempt_to_infer_missing_fx=True,
                    calendar_scope="z",
                    convention_scope="z",
                ),
            ),
            pricing=PricingContext(
                model_rules=[
                    VendorModelRule(
                        supplier="Lusid",
                        model_name="model_name_example",
                        instrument_type="instrument_type_example",
                        parameters="parameters_example",
                        model_options=ModelOptions(),
                        instrument_id="instrument_id_example",
                    ),
                ],
                model_choice=dict(
                    "key": ModelSelection(
                        library="Lusid",
                        model="SimpleStatic",
                    ),
                ),
                options=PricingOptions(
                    model_selection=ModelSelection(
                        library="Lusid",
                        model="SimpleStatic",
                    ),
                    use_instrument_type_to_determine_pricer=True,
                    allow_any_instruments_with_sec_uid_to_price_off_lookup=True,
                    allow_partially_successful_evaluation=True,
                    produce_separate_result_for_linear_otc_legs=True,
                    enable_use_of_cached_unit_results=True,
                    window_valuation_on_instrument_start_end=True,
                    remove_contingent_cashflows_in_payment_diary=True,
                    use_child_sub_holding_keys_for_portfolio_expansion=True,
                    validate_domestic_and_quote_currencies_are_consistent=True,
                ),
                result_data_rules=[
                    ResultDataKeyRule(
                        resource_key="resource_key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        document_code="document_code_example",
                        quote_interval="quote_interval_example",
                        as_at=isoparse('1970-01-01T00:00:00.00Z'),
                    ),
                ],
            ),
            aggregation=AggregationContext(
                options=AggregationOptions(
                    use_ansi_like_syntax=True,
                    allow_partial_entitlement_success=True,
                ),
            ),
            inherited_recipes=[
                ResourceId(
                    scope="scope_example",
                    code="code_example",
                ),
            ],
            description="",
            holding=HoldingContext(
                tax_lot_level_holdings=True,
            ),
        ),
        configuration_recipe_snippet=ConfigurationRecipeSnippet(
            scope="z",
            code="z",
            aggregation_options=AggregationOptions(
                use_ansi_like_syntax=True,
                allow_partial_entitlement_success=True,
            ),
            model_rules=[
                VendorModelRule(
                    supplier="Lusid",
                    model_name="model_name_example",
                    instrument_type="instrument_type_example",
                    parameters="parameters_example",
                    model_options=ModelOptions(),
                    instrument_id="instrument_id_example",
                ),
            ],
            pricing_options=PricingOptions(
                model_selection=ModelSelection(
                    library="Lusid",
                    model="SimpleStatic",
                ),
                use_instrument_type_to_determine_pricer=True,
                allow_any_instruments_with_sec_uid_to_price_off_lookup=True,
                allow_partially_successful_evaluation=True,
                produce_separate_result_for_linear_otc_legs=True,
                enable_use_of_cached_unit_results=True,
                window_valuation_on_instrument_start_end=True,
                remove_contingent_cashflows_in_payment_diary=True,
                use_child_sub_holding_keys_for_portfolio_expansion=True,
                validate_domestic_and_quote_currencies_are_consistent=True,
            ),
            market_rules=[
                MarketDataKeyRule(
                    key="key_example",
                    supplier="supplier_example",
                    data_scope="z",
                    quote_type="Price",
                    field="field_example",
                    quote_interval="quote_interval_example",
                    as_at=isoparse('1970-01-01T00:00:00.00Z'),
                    price_source="price_source_example",
                    mask="mask_example",
                ),
            ],
            market_options=MarketOptions(
                default_supplier="default_supplier_example",
                default_instrument_code_type="default_instrument_code_type_example",
                default_scope="z",
                attempt_to_infer_missing_fx=True,
                calendar_scope="z",
                convention_scope="z",
            ),
            recipe=ConfigurationRecipe(
                scope="z",
                code="z",
                market=MarketContext(
                    market_rules=[
                        MarketDataKeyRule(
                            key="key_example",
                            supplier="supplier_example",
                            data_scope="z",
                            quote_type="Price",
                            field="field_example",
                            quote_interval="quote_interval_example",
                            as_at=isoparse('1970-01-01T00:00:00.00Z'),
                            price_source="price_source_example",
                            mask="mask_example",
                        ),
                    ],
                    suppliers=MarketContextSuppliers(
                        commodity="commodity_example",
                        credit="credit_example",
                        equity="equity_example",
                        fx="fx_example",
                        rates="rates_example",
                    ),
                    options=MarketOptions(
                        default_supplier="default_supplier_example",
                        default_instrument_code_type="default_instrument_code_type_example",
                        default_scope="z",
                        attempt_to_infer_missing_fx=True,
                        calendar_scope="z",
                        convention_scope="z",
                    ),
                ),
                pricing=PricingContext(
                    model_rules=[
                        VendorModelRule(
                            supplier="Lusid",
                            model_name="model_name_example",
                            instrument_type="instrument_type_example",
                            parameters="parameters_example",
                            model_options=ModelOptions(),
                            instrument_id="instrument_id_example",
                        ),
                    ],
                    model_choice=dict(
                        "key": ModelSelection(
                            library="Lusid",
                            model="SimpleStatic",
                        ),
                    ),
                    options=PricingOptions(
                        model_selection=ModelSelection(
                            library="Lusid",
                            model="SimpleStatic",
                        ),
                        use_instrument_type_to_determine_pricer=True,
                        allow_any_instruments_with_sec_uid_to_price_off_lookup=True,
                        allow_partially_successful_evaluation=True,
                        produce_separate_result_for_linear_otc_legs=True,
                        enable_use_of_cached_unit_results=True,
                        window_valuation_on_instrument_start_end=True,
                        remove_contingent_cashflows_in_payment_diary=True,
                        use_child_sub_holding_keys_for_portfolio_expansion=True,
                        validate_domestic_and_quote_currencies_are_consistent=True,
                    ),
                    result_data_rules=[
                        ResultDataKeyRule(
                            resource_key="resource_key_example",
                            supplier="supplier_example",
                            data_scope="z",
                            document_code="document_code_example",
                            quote_interval="quote_interval_example",
                            as_at=isoparse('1970-01-01T00:00:00.00Z'),
                        ),
                    ],
                ),
                aggregation=AggregationContext(
                    options=AggregationOptions(
                        use_ansi_like_syntax=True,
                        allow_partial_entitlement_success=True,
                    ),
                ),
                inherited_recipes=[
                    ResourceId(
                        scope="scope_example",
                        code="code_example",
                    ),
                ],
                description="",
                holding=HoldingContext(
                    tax_lot_level_holdings=True,
                ),
            ),
        ),
    )
    try:
        # [EXPERIMENTAL] UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.
        api_response = api_instance.upsert_configuration_recipe(
            body=body,
        )
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->upsert_configuration_recipe: %s\n" % e)
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
[**UpsertRecipeRequest**](UpsertRecipeRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertRecipeRequest**](UpsertRecipeRequest.md) |  | 


#### SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertRecipeRequest**](UpsertRecipeRequest.md) |  | 


#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertRecipeRequest**](UpsertRecipeRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | The successfully updated or inserted item or any failure 
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
[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md) |  | 


#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md) |  | 


#### SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md) |  | 


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



[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

