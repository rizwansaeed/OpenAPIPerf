# QuoteAccessMetadataRuleId

An identifier that uniquely identifies a set of Quote access control metadata.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str, none_type** | The platform or vendor that provided the quote, e.g. &#x27;DataScope&#x27;, &#x27;LUSID&#x27; etc. | [optional] 
**priceSource** | **str, none_type** | The source or originator of the quote, e.g. a bank or financial institution. | [optional] 
**instrumentId** | **str, none_type** | The value of the instrument identifier that uniquely identifies the instrument that the quote is for, e.g. &#x27;BBG00JX0P539&#x27;. | [optional] 
**instrumentIdType** | **str, none_type** | The type of instrument identifier used to uniquely identify the instrument that the quote is for, e.g. &#x27;Figi&#x27;. | [optional] 
**quoteType** | **str, none_type** | The type of the quote. This allows for quotes other than prices e.g. rates or spreads to be used. | [optional] 
**field** | **str, none_type** | The field of the quote e.g. bid, mid, ask etc. This should be consistent across a time series of quotes. The allowed values are dependant on the specified Provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

