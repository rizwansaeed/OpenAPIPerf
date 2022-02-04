# ReconcileDateTimeRuleAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisonType** | **str** | The available values are: Exact, AbsoluteDifference | 
**tolerance** | **int, float** | For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction. | [optional] 
**appliesTo** | [**AggregateSpec**](AggregateSpec.md) |  | 
**ruleType** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

