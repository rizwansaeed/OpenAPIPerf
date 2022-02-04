# AggregatedReturnsRequest

The request used in the AggregatedReturns.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **[PerformanceReturnsMetric]** | A list of metrics to calculate in the AggregatedReturns. | 
**recipeId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**compositeMethod** | **str, none_type** | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**period** | **str, none_type** | The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
**outputFrequency** | **str, none_type** | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
**alternativeInceptionDate** | **str, none_type** | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

