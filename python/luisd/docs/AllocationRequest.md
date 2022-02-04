# AllocationRequest

A request to create or update an Allocation.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **{str: (PerpetualProperty,)}, none_type** | Client-defined properties associated with this allocation. | [optional] 
**instrumentIdentifiers** | **{str: (str,)}** | The instrument allocated. | 
**quantity** | **int** | The quantity of given instrument allocated. | 
**portfolioId** | [**ResourceId**](ResourceId.md) |  | 
**allocatedOrderId** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**placementIds** | **[ResourceId], none_type** | A placement - also known as an order placed in the market - associated with this allocation. | [optional] 
**state** | **str, none_type** | The state of this allocation. | [optional] 
**side** | **str, none_type** | The side of this allocation (examples: Buy, Sell, ...). | [optional] 
**type** | **str, none_type** | The type of order associated with this allocation (examples: Limit, Market, ...). | [optional] 
**settlementDate** | **datetime** | The settlement date for this allocation. | [optional] 
**date** | **datetime** | The date of this allocation. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**settlementCurrency** | **str, none_type** | The settlement currency of this allocation. | [optional] 
**settlementCurrencyFxRate** | **int, float** | The settlement currency to allocation currency FX rate. | [optional] 
**counterparty** | **str, none_type** | The counterparty for this allocation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

