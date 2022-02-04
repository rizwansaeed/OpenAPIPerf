# Block

A block of orders for the same instrument, intended to record for example a trader's aggregation  of outstanding orders at a given time.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**orderIds** | **[ResourceId]** | The related order ids. | 
**properties** | **{str: (PerpetualProperty,)}, none_type** | Client-defined properties associated with this block. | [optional] 
**instrumentIdentifiers** | **{str: (str,)}** | The instrument ordered. | 
**lusidInstrumentId** | **str** | The LUSID instrument id for the instrument ordered. | 
**quantity** | **int, float** | The total quantity of given instrument ordered. | 
**side** | **str** | The client&#x27;s representation of the block&#x27;s side (buy, sell, short, etc) | 
**type** | **str** | The block order&#x27;s type (examples: Limit, Market, ...) | 
**timeInForce** | **str** | The block orders&#x27; time in force (examples: Day, GoodTilCancel, ...) | 
**createdDate** | **datetime** | The date on which the block was made | 
**limitPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stopPrice** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

