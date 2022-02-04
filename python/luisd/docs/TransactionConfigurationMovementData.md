# TransactionConfigurationMovementData

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movementTypes** | **str** | . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes, Carry, CarryAsPnl | 
**side** | **str** | The movement side | 
**direction** | **int** | The movement direction | 
**properties** | **{str: (PerpetualProperty,)}, none_type** | The properties associated with the underlying Movement. | [optional] 
**mappings** | **[TransactionPropertyMapping], none_type** | This allows you to map a transaction property to a property on the underlying holding. | [optional] 
**name** | **str, none_type** | The movement name (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

