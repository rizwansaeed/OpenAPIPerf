# QuoteSeriesId

The time invariant unique identifier of the quote. Combined with the effective datetime of the quote this  uniquely identifies the quote. This can be thought of as a unique identifier for a time series of quotes.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the quote, e.g. &#x27;DataScope&#x27;, &#x27;LUSID&#x27; etc. | 
**priceSource** | **str, none_type** | The source or originator of the quote, e.g. a bank or financial institution. | [optional] 
**instrumentId** | **str** | The value of the instrument identifier that uniquely identifies the instrument that the quote is for, e.g. &#x27;BBG00JX0P539&#x27;. | 
**instrumentIdType** | **str, none_type** | The type of instrument identifier used to uniquely identify the instrument that the quote is for, e.g. &#x27;Figi&#x27;. The available values are: LusidInstrumentId, Figi, RIC, QuotePermId, Isin, CurrencyPair, ClientInternal | 
**quoteType** | **str, none_type** | The type of the quote. This allows for quotes other than prices e.g. rates or spreads to be used. The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront | 
**field** | **str** | The field of the quote e.g. bid, mid, ask etc. This should be consistent across a time series of quotes. The allowed values are dependant on the specified Provider. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

