# UpsertQuoteRequest

The details of the quote including its unique identifier, value and lineage.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quoteId** | [**QuoteId**](QuoteId.md) |  | 
**metricValue** | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | **str, none_type** | Description of the quote&#x27;s lineage e.g. &#x27;FundAccountant_GreenQuality&#x27;. | [optional] 
**scaleFactor** | **int, float, none_type** | An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

