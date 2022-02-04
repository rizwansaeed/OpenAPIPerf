# InstrumentDefinition

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instrument. | 
**identifiers** | **{str: (InstrumentIdValue,)}** | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. | 
**properties** | **[ModelProperty], none_type** | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#x27;Instrument&#x27; domain. | [optional] 
**lookThroughPortfolioId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

