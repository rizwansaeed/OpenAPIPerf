# ModelProperty

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#x27;Instrument/system/Name&#x27; or &#x27;Transaction/strategy/quantsignal&#x27;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effectiveFrom** | **datetime, none_type** | The effective datetime from which the property is valid. | [optional] 
**effectiveUntil** | **datetime, none_type** | The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next &#x27;effectiveFrom&#x27; datetime of the property. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

