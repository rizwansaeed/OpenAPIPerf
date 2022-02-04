# RelationDefinition

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relationDefinitionId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**sourceEntityDomain** | **str, none_type** | The entity domain of the source entity object. | [optional] 
**targetEntityDomain** | **str, none_type** | The entity domain of the target entity object. | [optional] 
**displayName** | **str, none_type** | The display name of the relation. | [optional] 
**outwardDescription** | **str, none_type** | The description to relate source entity object and target entity object | [optional] 
**inwardDescription** | **str, none_type** | The description to relate target entity object and source entity object | [optional] 
**lifeTime** | **str, none_type** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraintStyle** | **str, none_type** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

