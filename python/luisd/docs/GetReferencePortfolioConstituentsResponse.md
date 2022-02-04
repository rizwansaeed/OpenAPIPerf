# GetReferencePortfolioConstituentsResponse

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveFrom** | **datetime** |  | 
**weightType** | **str** | The available values are: Static, Floating, Periodical | 
**periodType** | **str, none_type** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**periodCount** | **int, none_type** |  | [optional] 
**constituents** | **[ReferencePortfolioConstituent]** | Set of constituents (instrument/weight pairings) | 
**href** | **str, none_type** | The Uri that returns the same result as the original request,  but may include resolved as at time(s). | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

