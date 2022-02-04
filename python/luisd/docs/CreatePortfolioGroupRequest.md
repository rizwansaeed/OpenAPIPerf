# CreatePortfolioGroupRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. | 
**created** | **datetime, none_type** | The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified. | [optional] 
**values** | **[ResourceId], none_type** | The resource identifiers of the portfolios to be contained within the portfolio group. | [optional] 
**subGroups** | **[ResourceId], none_type** | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. | [optional] 
**properties** | **{str: (ModelProperty,)}, none_type** | A set of unique group properties to add to the portfolio group. Each property must be from the &#x27;PortfolioGroup&#x27; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#x27;PortfolioGroup/Manager/Id&#x27;. These properties must be pre-defined. | [optional] 
**displayName** | **str** | The name of the portfolio group. | 
**description** | **str, none_type** | A long form description of the portfolio group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

