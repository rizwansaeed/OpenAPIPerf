# CreatePropertyDefinitionRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**valueRequired** | **bool** | Whether or not a value is always required for this property. | [optional] 
**displayName** | **str** | The display name of the property. | 
**dataTypeId** | [**ResourceId**](ResourceId.md) |  | 
**lifeTime** | **str** | Describes how the property&#x27;s values can change over time. The available values are: Perpetual, TimeVariant | [optional] 
**constraintStyle** | **str, none_type** | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. Defaults to \&quot;Property\&quot; if not specified. Valid values for this field are: Property, Collection or Identifier. | [optional] 
**propertyDescription** | **str, none_type** | Describes the property | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

