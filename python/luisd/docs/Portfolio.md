# Portfolio

A list of portfolios.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | 
**displayName** | **str** | The name of the portfolio. | 
**description** | **str, none_type** | The long form description of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parentPortfolioId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**isDerived** | **bool** | Whether or not this is a derived portfolio. | [optional] 
**baseCurrency** | **str, none_type** | The base currency of the portfolio. This will be an empty string for reference portfolios. | [optional] 
**properties** | **{str: (ModelProperty,)}, none_type** | The requested portfolio properties. These will be from the &#x27;Portfolio&#x27; domain. | [optional] 
**instrumentScopes** | **[str], none_type** | The instrument scope resolution strategy of this portfolio. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

