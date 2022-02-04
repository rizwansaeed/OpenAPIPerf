# ExecutionRequest

A request to create or update a Execution.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placementId** | [**ResourceId**](ResourceId.md) |  | 
**properties** | **{str: (PerpetualProperty,)}, none_type** | Client-defined properties associated with this execution. | [optional] 
**instrumentIdentifiers** | **{str: (str,)}** | The instrument ordered. | 
**quantity** | **int, float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this execution (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this execution. | 
**type** | **str** | The type of this execution (Market, Limit, etc). | 
**createdDate** | **datetime** | The active date of this execution. | 
**settlementDate** | **datetime** | The (optional) settlement date for this execution | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**settlementCurrency** | **str** | The execution&#x27;s settlement currency. | 
**settlementCurrencyFxRate** | **int, float** | The exectuion&#x27;s settlement currency rate. | 
**counterparty** | **str** | The market entity this placement is placed with. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

