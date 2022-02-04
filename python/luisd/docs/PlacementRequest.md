# PlacementRequest

A request to create or update a Placement.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**blockIds** | **[ResourceId]** | IDs of Blocks associated with this placement. | 
**properties** | **{str: (PerpetualProperty,)}, none_type** | Client-defined properties associated with this order. | [optional] 
**instrumentIdentifiers** | **{str: (str,)}** | The instrument ordered. | 
**quantity** | **int, float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this placement (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this placement. | 
**timeInForce** | **str** | The time in force applicable to this placement (GTC, FOK, Day, etc) | 
**type** | **str** | The type of this placement (Market, Limit, etc). | 
**createdDate** | **datetime** | The active date of this placement. | 
**limitPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stopPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**counterparty** | **str** | The market entity this placement is placed with. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

