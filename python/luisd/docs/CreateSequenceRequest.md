# CreateSequenceRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the sequence definition to create | 
**increment** | **int, none_type** | The value to increment between each value in the sequence | [optional] 
**minValue** | **int, none_type** | The minimum value of the sequence | [optional] 
**maxValue** | **int, none_type** | The maximum value of the sequence | [optional] 
**start** | **int, none_type** | The start value of the sequence | [optional] 
**cycle** | **bool** | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. Default to false. | [optional] 
**pattern** | **str, none_type** | The pattern to be used to generate next values in the sequence. Default to null. Please provide a null value until further notice. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

