# Instrument

A list of instruments.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**scope** | **str, none_type** | The scope in which the instrument lies. | [optional] 
**lusidInstrumentId** | **str** | The unique LUSID Instrument Identifier (LUID) of the instrument. | 
**version** | [**Version**](Version.md) |  | 
**name** | **str** | The name of the instrument. | 
**identifiers** | **{str: (str,)}** | The set of identifiers that can be used to identify the instrument. | 
**properties** | **[ModelProperty], none_type** | The requested instrument properties. These will be from the &#x27;Instrument&#x27; domain. | [optional] 
**lookthroughPortfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrumentDefinition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**state** | **str** | The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive | 
**assetClass** | **str** | The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown | [optional] 
**domCcy** | **str, none_type** | The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

