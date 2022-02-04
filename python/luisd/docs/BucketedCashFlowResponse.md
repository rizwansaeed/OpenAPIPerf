# BucketedCashFlowResponse

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** |  | [optional] 
**data** | **[{str: (bool, date, datetime, dict, float, int, list, str,)}], none_type** | List of dictionary bucketed cash flow result set.  Each dictionary represent a bucketed cashflow result set keyed by AddressKeys.  e.g. dictionary[\&quot;Valuation/CashFlowAmount\&quot;] for the aggregated cash flow amount for the bucket.  e.g. suppose \&quot;RoundUp\&quot; method, then dictionary[\&quot;Valuation/CashFlowDate/RoundUp\&quot;] returns the bucketed cashflow date. | [optional] 
**reportCurrency** | **str, none_type** | Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant. | [optional] 
**dataSchema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

