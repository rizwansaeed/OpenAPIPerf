# DataTypeSummary

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typeValueRange** | **str** | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**displayName** | **str** | The display name of the data type. | 
**description** | **str** | The description of the data type. | 
**valueType** | **str** | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel | 
**acceptableValues** | **[str], none_type** | The acceptable set of values for this data type. Only applies to &#x27;open&#x27; value type range. | [optional] 
**unitSchema** | **str** | The schema of the data type&#x27;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptableUnits** | **[IUnitDefinitionDto], none_type** | The definitions of the acceptable units. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

