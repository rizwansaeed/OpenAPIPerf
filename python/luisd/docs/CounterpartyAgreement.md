# CounterpartyAgreement

Represents the legal agreement between two parties engaged in an OTC transaction.  A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **str** | A user-defined display label for the Counterparty Agreement. | 
**agreementType** | **str** | A user-defined field to capture the type of agreement this represents. Examples might be \&quot;ISDA 2002 Master Agreement\&quot; or \&quot;ISDA 1992 Master Agreement\&quot;. | 
**counterpartySignatory** | [**CounterpartySignatory**](CounterpartySignatory.md) |  | 
**datedAsOf** | **datetime** | The date on which the CounterpartyAgreement was signed by both parties. | 
**creditSupportAnnexId** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

