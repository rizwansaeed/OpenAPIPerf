# ComplianceRuleResult

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleId** | **str** | The unique identifierof a compliance rule | 
**ruleName** | **str** | The User-given name of the rule | 
**ruleDescription** | **str** | The User-given description of the rule | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**passed** | **bool** | The result of an individual compliance run, true if passed | 
**resultValue** | **int, float** | The calculation result that was used to confirm a pass/fail | 
**ruleInformationMatch** | **str** | The value matched by the rule | 
**ruleInformationKey** | **str** | The property key matched by the rule | 
**ruleLowerLimit** | **int** | The lower limit of the rule | 
**ruleUpperLimit** | **int** | The upper limit of the rule | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

