# CreateDerivedTransactionPortfolioRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **str** | The name of the derived transaction portfolio. | 
**description** | **str, none_type** | A description for the derived transaction portfolio. | [optional] 
**code** | **str** | The code of the derived transaction portfolio. Together with the scope this uniquely identifies the derived transaction portfolio. | 
**parentPortfolioId** | [**ResourceId**](ResourceId.md) |  | 
**created** | **datetime, none_type** | The effective datetime at which to create the derived transaction portfolio. No transactions can be added to the derived transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified. | [optional] 
**corporateActionSourceId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accountingMethod** | **str** | Determines the accounting treatment given to the transaction portfolio&#x27;s tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**subHoldingKeys** | **[str], none_type** | A set of unique transaction properties to group the derived transaction portfolio&#x27;s holdings by, perhaps for strategy tagging. Each property must be from the &#x27;Transaction&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Transaction/strategies/quantsignal&#x27;. Note that sub-holding keys cannot currently be added after the transaction portfolio has been created; see https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**instrumentScopes** | **[str], none_type** | The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

