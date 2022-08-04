# luisd.model.create_derived_property_definition_request.CreateDerivedPropertyDefinitionRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**displayName** | **str** | The display name of the property. | 
**dataTypeId** | [**ResourceId**](ResourceId.md) |  | 
**propertyDescription** | **str, none_type** | Describes the property | [optional] 
**derivationFormula** | **str, none_type** | The rule that defines how data is composed for a derived property. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

