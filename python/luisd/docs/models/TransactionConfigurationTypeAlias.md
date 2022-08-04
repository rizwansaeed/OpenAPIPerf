# luisd.model.transaction_configuration_type_alias.TransactionConfigurationTypeAlias

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type | 
**description** | **str** | Brief description of the transaction | 
**transactionClass** | **str** | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut | 
**transactionGroup** | **str, none_type** | Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead | [optional] 
**source** | **str, none_type** | Used to group a set of transaction types | [optional] 
**transactionRoles** | **str** | . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles | 
**isDefault** | **bool** | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

