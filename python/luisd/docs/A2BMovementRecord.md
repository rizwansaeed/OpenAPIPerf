# A2BMovementRecord

A2B Movement Record - shows A2B category based changes relating to a specific movement

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolioId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holdingType** | **str, none_type** | The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | [optional] 
**instrumentScope** | **str, none_type** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**instrumentUid** | **str, none_type** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**subHoldingKeys** | **{str: (PerpetualProperty,)}, none_type** | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | [optional] 
**currency** | **str, none_type** | The holding currency. | [optional] 
**transactionId** | **str, none_type** | The unique identifier for the transaction. | [optional] 
**movementName** | **str, none_type** | The name of the movement. | [optional] 
**effectiveDate** | **datetime** | The date of the movement. | [optional] 
**units** | **int, float** | The number of units of the instrument that are affected by the movement. | [optional] 
**start** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**flows** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**gains** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**carry** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**end** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**properties** | **{str: (ModelProperty,)}, none_type** | The properties which have been requested to be decorated onto the holding. These will be from the &#x27;Instrument&#x27; domain. | [optional] 
**groupId** | **str, none_type** | Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

