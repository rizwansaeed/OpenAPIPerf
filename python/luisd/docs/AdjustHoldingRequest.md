# AdjustHoldingRequest

This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentIdentifiers** | **{str: (str,)}** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 
**subHoldingKeys** | **{str: (PerpetualProperty,)}, none_type** | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#x27;Transaction&#x27; domain. | [optional] 
**properties** | **{str: (PerpetualProperty,)}, none_type** | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#x27;Holding&#x27; domain. | [optional] 
**taxLots** | **[TargetTaxLotRequest]** | The tax-lots that together make up the target holding. | 
**currency** | **str, none_type** | The Holding currency. This needs to be equal with the one on the TaxLot -&gt; cost if one is specified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

