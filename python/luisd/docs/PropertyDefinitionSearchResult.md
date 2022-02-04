# PropertyDefinitionSearchResult

A property definition search result

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**key** | **str, none_type** | The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#x27;Portfolio/Manager/Id&#x27;. | [optional] 
**valueType** | **str** | The type of values that can be associated with this property. This is defined by the property&#x27;s data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel | [optional] 
**displayName** | **str, none_type** | The display name of the property. | [optional] 
**dataTypeId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**type** | **str** | The type of the property. The available values are: Label, Metric, Information | [optional] 
**unitSchema** | **str** | The units that can be associated with the property&#x27;s values. This is defined by the property&#x27;s data type. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity | [optional] 
**scope** | **str, none_type** | The scope that the property exists in. | [optional] [readonly] 
**code** | **str, none_type** | The code of the property. Together with the domain and scope this uniquely identifies the property. | [optional] [readonly] 
**valueRequired** | **bool** | Whether or not a value is always required for this property. | [optional] 
**lifeTime** | **str** | Describes how the property&#x27;s values can change over time. The available values are: Perpetual, TimeVariant | [optional] 
**constraintStyle** | **str, none_type** | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. | [optional] 
**propertyDefinitionType** | **str** | The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition | [optional] 
**propertyDescription** | **str, none_type** | A brief description of what a property of this property definition contains. | [optional] 
**derivationFormula** | **str, none_type** | The rule that defines how data is composed for a derived property. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

