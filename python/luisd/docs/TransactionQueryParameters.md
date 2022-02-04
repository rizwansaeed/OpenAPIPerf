# TransactionQueryParameters

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **str** | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. | 
**endDate** | **str** | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. | 
**queryMode** | **str** | The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to &#x27;TradeDate&#x27; if not specified. The available values are: TradeDate, SettleDate | [optional] 
**showCancelledTransactions** | **bool** | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

