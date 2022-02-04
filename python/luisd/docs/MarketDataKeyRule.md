# MarketDataKeyRule

A market data key rule describes a mapping for satisfying a particular market dependency. The supplier, scope, quote type and price side  information define the quote in the market and which Vendor for market data would be used to perform the lookup.  The market data key defines what dependency this satisfies. The key is a rule that describes the asset class, its identifier and any other  specifics required to uniquely describe a specific economic entity (e.g. an Fx currency pair, equity name or credit curve).

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The market data key pattern which this is a rule for. A dot separated string (A.B.C.D.*) | 
**supplier** | **str** | The market data supplier (where the data comes from) | 
**dataScope** | **str** | The scope in which the data should be found when using this rule. | 
**quoteType** | **str** | The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront | 
**field** | **str** | The conceptual qualification for the field, such as bid, mid, or ask.  The field must be one of a defined set for the given supplier, in the same way as it  is for the Finbourne.WebApi.Interface.Dto.Quotes.QuoteSeriesId | 
**quoteInterval** | **str, none_type** | Shorthand for the time interval used to select market data. This must be a dot-separated string              nominating a start and end date, for example &#x27;5D.0D&#x27; to look back 5 days from today (0 days ago). The syntax              is &lt;i&gt;int&lt;/i&gt;&lt;i&gt;char&lt;/i&gt;.&lt;i&gt;int&lt;/i&gt;&lt;i&gt;char&lt;/i&gt;, where &lt;i&gt;char&lt;/i&gt; is one of D(ay), W(eek), M(onth) or Y(ear). | [optional] 
**asAt** | **datetime, none_type** | The AsAt predicate specification. | [optional] 
**priceSource** | **str, none_type** | The source of the quote. For a given provider/supplier of market data there may be an additional qualifier, e.g. the exchange or bank that provided the quote | [optional] 
**mask** | **str, none_type** | Allows for partial or complete override of the market asset resolved for a dependency  Either a named override or a dot separated string (A.B.C.D.*).  e.g. for Rates curve &#x27;EUR.*&#x27; will replace the resolve MarketAsset &#x27;GBP/12M&#x27;, &#x27;GBP/3M&#x27; with the EUR equivalent, if there  are no wildcards in the mask, the mask is taken as the MarketAsset for any dependency matching the rule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

