# CompletePortfolio

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str, none_type** | The long form description of the portfolio. | [optional] 
**displayName** | **str, none_type** | The name of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | [optional] 
**parentPortfolioId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**isDerived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | [optional] 
**version** | [**Version**](Version.md) |  | 
**properties** | **[ModelProperty], none_type** | The requested portfolio properties. These will be from the &#x27;Portfolio&#x27; domain. | [optional] 
**baseCurrency** | **str, none_type** | If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

