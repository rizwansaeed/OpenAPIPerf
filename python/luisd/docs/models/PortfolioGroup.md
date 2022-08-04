# luisd.model.portfolio_group.PortfolioGroup

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**displayName** | **str** | The name of the portfolio group. | 
**description** | **str, none_type** | The long form description of the portfolio group. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date. | [optional] 
**portfolios** | **[ResourceId], none_type** | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**subGroups** | **[ResourceId], none_type** | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

