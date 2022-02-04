# UpsertReferencePortfolioConstituentsRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveFrom** | **str** | The first date from which the weights will apply | 
**weightType** | **str** | The available values are: Static, Floating, Periodical | 
**periodType** | **str, none_type** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**periodCount** | **int, none_type** |  | [optional] 
**constituents** | **[ReferencePortfolioConstituentRequest]** | Set of constituents (instrument/weight pairings) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

