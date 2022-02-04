# CreateTransactionPortfolioRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **str** | The name of the transaction portfolio. | 
**description** | **str, none_type** | A description for the transaction portfolio. | [optional] 
**code** | **str** | The code of the transaction portfolio. Together with the scope this uniquely identifies the transaction portfolio. | 
**created** | **datetime, none_type** | The effective datetime at which to create the transaction portfolio. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified. | [optional] 
**baseCurrency** | **str** | The base currency of the transaction portfolio in ISO 4217 currency code format. | 
**corporateActionSourceId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accountingMethod** | **str** | Determines the accounting treatment given to the transaction portfolio&#x27;s tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**subHoldingKeys** | **[str], none_type** | A set of unique transaction properties to group the transaction portfolio&#x27;s holdings by, perhaps for strategy tagging. Each property must be from the &#x27;Transaction&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Transaction/strategies/quantsignal&#x27;. Note that sub-holding keys cannot currently be added after the transaction portfolio has been created; see https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**properties** | **{str: (ModelProperty,)}, none_type** | A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the &#x27;Portfolio&#x27; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#x27;Portfolio/Manager/Id&#x27;. Note these properties must be pre-defined. | [optional] 
**instrumentScopes** | **[str], none_type** | The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

