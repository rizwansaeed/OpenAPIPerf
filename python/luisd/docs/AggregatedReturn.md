# AggregatedReturn

A list of Aggregated Returns.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveAt** | **datetime** | The effectiveAt for the return. | 
**openingMarketValue** | **int, float, none_type** | The opening market value. | [optional] 
**closingMarketValue** | **int, float, none_type** | The closing market value. | [optional] 
**metricsValue** | **{str: (int, float,)}** | The value for the specified metric. | 
**frequency** | **str, none_type** | Show the aggregated output returns on a Daily or Monthly period. | [optional] 
**compositeMembers** | **int, none_type** | The number of members in the Composite on the given day. | [optional] 
**compositeMembersWithoutReturn** | **[ResourceId], none_type** | List containing Composite members which post no return on the given day. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

