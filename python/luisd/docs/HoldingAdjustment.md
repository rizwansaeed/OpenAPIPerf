# HoldingAdjustment

The target holdings.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentIdentifiers** | **{str: (str,)}, none_type** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | [optional] 
**instrumentScope** | **str, none_type** | The scope of the instrument that the holding adjustment is in. | [optional] 
**instrumentUid** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in. | 
**subHoldingKeys** | **{str: (PerpetualProperty,)}, none_type** | The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#x27;Transaction&#x27; domain. | [optional] 
**properties** | **{str: (PerpetualProperty,)}, none_type** | The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#x27;Holding&#x27; domain. | [optional] 
**taxLots** | **[TargetTaxLot]** | The tax-lots that together make up the target holding. | 
**currency** | **str, none_type** | The Holding currency. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

