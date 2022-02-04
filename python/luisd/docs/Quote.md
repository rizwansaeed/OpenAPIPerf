# Quote

The quote id, value and lineage of the quotes all keyed by a unique correlation id.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quoteId** | [**QuoteId**](QuoteId.md) |  | 
**metricValue** | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | **str, none_type** | Description of the quote&#x27;s lineage e.g. &#x27;FundAccountant_GreenQuality&#x27;. | [optional] 
**cutLabel** | **str, none_type** | The cut label that this quote was updated or inserted with. | [optional] 
**uploadedBy** | **str** | The unique id of the user that updated or inserted the quote. | 
**asAt** | **datetime** | The asAt datetime at which the quote was committed to LUSID. | 
**scaleFactor** | **int, float, none_type** | An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

