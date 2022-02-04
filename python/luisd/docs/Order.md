# Order

An Order for a certain quantity of a specific instrument

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **{str: (PerpetualProperty,)}, none_type** | Client-defined properties associated with this order. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**instrumentIdentifiers** | **{str: (str,)}** | The instrument ordered. | 
**quantity** | **int** | The quantity of given instrument ordered. | 
**side** | **str** | The client&#x27;s representation of the order&#x27;s side (buy, sell, short, etc) | 
**orderBookId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolioId** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**lusidInstrumentId** | **str** | The LUSID instrument id for the instrument ordered. | 
**state** | **str, none_type** | The order&#x27;s state (examples: New, PartiallyFilled, ...) | [optional] 
**type** | **str, none_type** | The order&#x27;s type (examples: Limit, Market, ...) | [optional] 
**timeInForce** | **str, none_type** | The order&#x27;s time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**orderInstructionId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**packageId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

