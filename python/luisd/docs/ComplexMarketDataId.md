# ComplexMarketDataId

An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the complex market data, e.g. &#x27;DataScope&#x27;, &#x27;LUSID&#x27;, &#x27;ISDA&#x27; etc. | 
**priceSource** | **str, none_type** | The source or originator of the complex market data, e.g. a bank or financial institution. | [optional] 
**lineage** | **str, none_type** | Description of the complex market data&#x27;s lineage e.g. &#x27;FundAccountant_GreenQuality&#x27;. | [optional] 
**effectiveAt** | **str, none_type** | The effectiveAt or cut label that this item of complex market data is/was updated/inserted with. | [optional] 
**marketAsset** | **str, none_type** | The name of the market entity that the document represents | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

