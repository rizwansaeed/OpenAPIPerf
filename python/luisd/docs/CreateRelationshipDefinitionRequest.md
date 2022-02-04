# CreateRelationshipDefinitionRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the relationship definition exists in. | 
**code** | **str** | The code of the relationship definition. Together with the scope this uniquely defines the relationship definition. | 
**sourceEntityType** | **str** | The entity type of the source entity object. Allowed values are &#x27;Portfolio&#x27;, &#x27;PortfolioGroup&#x27;, &#x27;Person&#x27;, &#x27;LegalEntity&#x27; or a custom entity type prefixed with &#x27;~&#x27;. | 
**targetEntityType** | **str** | The entity type of the target entity object. Allowed values are &#x27;Portfolio&#x27;, &#x27;PortfolioGroup&#x27;, &#x27;Person&#x27;, &#x27;LegalEntity&#x27; or a custom entity type prefixed with &#x27;~&#x27;. | 
**displayName** | **str** | The display name of the relationship definition. | 
**outwardDescription** | **str** | The description to relate source entity object and target entity object. | 
**inwardDescription** | **str** | The description to relate target entity object and source entity object. | 
**lifeTime** | **str, none_type** | Describes how the relationships can change over time. Allowed values are &#x27;Perpetual&#x27; and &#x27;TimeVariant&#x27;, defaults to &#x27;Perpetual&#x27; if not specified. | [optional] 
**relationshipCardinality** | **str, none_type** | Describes the cardinality of the relationship with a specific source entity object and relationships under this definition. Allowed values are &#x27;ManyToMany&#x27; and &#x27;OneToMany&#x27;, defaults to &#x27;ManyToMany&#x27; if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

