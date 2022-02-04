# CompleteRelationship

Representation of a relationship containing details of source and target entities, and both outward and inward descriptions.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**relationshipDefinitionId** | [**ResourceId**](ResourceId.md) |  | 
**sourceEntity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**targetEntity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**outwardDescription** | **str** | Description of the relationship based on relationship definition&#x27;s outward description. | 
**inwardDescription** | **str** | Description of the relationship based on relationship definition&#x27;s inward description. | 
**effectiveFrom** | **datetime** | The effective datetime from which the relationship is valid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

