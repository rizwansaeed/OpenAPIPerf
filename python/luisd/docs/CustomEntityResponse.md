# CustomEntityResponse

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entityType** | **str** | The EntityType to be used when relations are created to the CustomEntity | 
**customEntityId** | **str** | A unique identifier for the CustomEntity | 
**version** | [**Version**](Version.md) |  | 
**displayName** | **str** | The display name of the CustomEntity | 
**description** | **str, none_type** | The description of the CustomEntity | [optional] 
**identifiers** | **[CustomEntityIdResponse]** | A collection of CustomEntityIdentifiers that can identify the CustomEntity | 
**fields** | **[CustomEntityField]** | A collection of CustomEntityFields that decorate the CustomEntity | 
**effectiveRange** | [**DateRange**](DateRange.md) |  | 
**asAtRange** | [**DateRange**](DateRange.md) |  | 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

