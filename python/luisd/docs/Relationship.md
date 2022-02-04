# Relationship

Representation of a Relationship between a requested entity with the stated entity as RelatedEntityId

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relationshipDefinitionId** | [**ResourceId**](ResourceId.md) |  | 
**relatedEntity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**traversalDirection** | **str** | Direction of relationship betwen the requested entity and related entity. This can be &#x27;In&#x27; or &#x27;Out&#x27;. Read more about relationships traversal direction in LUSID Knowledge Base here https://support.lusid.com/relationships. | 
**traversalDescription** | **str** | Description of the relationship based on relationship&#x27;s traversal direction. If &#x27;TraversalDirection&#x27; is &#x27;Out&#x27;, this description would be &#x27;OutwardDescription&#x27; from the associated relationship definition. If &#x27;TraversalDirection&#x27; is &#x27;In&#x27;, this description would be &#x27;InwardDescription&#x27; from the associated relationship definition. | 
**effectiveFrom** | **datetime** | The effective datetime from which the relationship is valid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

