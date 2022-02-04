# ResultDataKeyRule

A rule that describes how we resolve (unit) result data.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceKey** | **str** | The result data key that identifies the address pattern that this is a rule for | 
**supplier** | **str** | the result resource supplier (where the data comes from) | 
**dataScope** | **str** | which is the scope in which the data should be found | 
**documentCode** | **str** | document code that defines which document is desired | 
**quoteInterval** | **str, none_type** | Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#x27;5D.0D&#x27; to look back 5 days from today (0 days ago). | [optional] 
**asAt** | **datetime, none_type** | The AsAt predicate specification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

