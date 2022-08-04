# luisd.model.portfolio_search_result.PortfolioSearchResult

A list of portfolios.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | 
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str, none_type** | The long form description of the portfolio. | [optional] 
**displayName** | **str** | The name of the portfolio. | 
**isDerived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parentPortfolioId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**baseCurrency** | **str, none_type** | The base currency of the portfolio. This will be an empty string for reference portfolios. | [optional] 
**properties** | **[ModelProperty], none_type** | The requested portfolio properties. These will be from the &#x27;Portfolio&#x27; domain. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

