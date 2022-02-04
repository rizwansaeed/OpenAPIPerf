# CreateRelationDefinitionRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the relation exists in. | 
**code** | **str** | The code of the relation. Together with the scope this uniquely defines the relation. | 
**sourceEntityDomain** | **str** | The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**targetEntityDomain** | **str** | The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**displayName** | **str** | The display name of the relation. | 
**outwardDescription** | **str** | The description to relate source entity object and target entity object. | 
**inwardDescription** | **str** | The description to relate target entity object and source entity object. | 
**lifeTime** | **str, none_type** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraintStyle** | **str, none_type** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

