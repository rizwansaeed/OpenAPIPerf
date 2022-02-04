# HoldingsAdjustment

Full content of a holdings adjustment for a single portfolio and effective date.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveAt** | **datetime** | The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment. | 
**version** | [**Version**](Version.md) |  | 
**unmatchedHoldingMethod** | **str** | Describes how the holdings were adjusted. If &#x27;PositionToZero&#x27; the entire transaction portfolio&#x27;s holdings were set via a call to &#x27;Set holdings&#x27;. If &#x27;KeepTheSame&#x27; only the specified holdings were adjusted via a call to &#x27;Adjust holdings&#x27;. The available values are: PositionToZero, KeepTheSame | 
**adjustments** | **[HoldingAdjustment]** | The holding adjustments. | 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

