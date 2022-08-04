# luisd.model.market_context.MarketContext

Market context node. This defines how LUSID processes parts of a request that require resolution of market data such as instrument prices or  Fx rates. It controls where the data is loaded from and which sources take precedence.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketRules** | **[MarketDataKeyRule], none_type** | The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible. | [optional] 
**suppliers** | **{str: typing.Any}, none_type** | It is possible to control which supplier is used for a given asset class. | [optional] 
**options** | [**MarketOptions**](MarketOptions.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

