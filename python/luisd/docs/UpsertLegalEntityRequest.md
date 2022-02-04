# UpsertLegalEntityRequest

Request to create or update an legal entity

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **{str: (ModelProperty,)}** | The identifiers the legal entity will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**properties** | **{str: (ModelProperty,)}, none_type** | A set of properties associated to the Legal Entity. | [optional] 
**displayName** | **str** | The display name of the Legal Entity | 
**description** | **str, none_type** | The description of the Legal Entity | [optional] 
**counterpartyRiskInformation** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

