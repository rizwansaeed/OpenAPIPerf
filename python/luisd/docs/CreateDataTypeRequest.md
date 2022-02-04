# CreateDataTypeRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the data type will be created in. | 
**code** | **str** | The code of the data type. Together with the scope this uniquely defines the data type. | 
**typeValueRange** | **str** | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | 
**displayName** | **str** | The display name of the data type. | 
**description** | **str** | The description of the data type. | 
**valueType** | **str** | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel | 
**acceptableValues** | **[str], none_type** | The acceptable set of values for this data type. Only applies to &#x27;open&#x27; value type range. | [optional] 
**unitSchema** | **str** | The schema of the data type&#x27;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptableUnits** | **[CreateUnitDefinition], none_type** | The definitions of the acceptable units. | [optional] 
**referenceData** | [**ReferenceData**](ReferenceData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

