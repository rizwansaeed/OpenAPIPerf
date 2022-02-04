# Transaction

A list of transactions.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionId** | **str** | The unique identifier for the transaction. | 
**type** | **str** | The type of the transaction e.g. &#x27;Buy&#x27;, &#x27;Sell&#x27;. The transaction type should have been pre-configured via the System Configuration API endpoint. | 
**instrumentIdentifiers** | **{str: (str,)}, none_type** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | [optional] 
**instrumentScope** | **str, none_type** | The scope in which the transaction&#x27;s instrument lies. | [optional] 
**instrumentUid** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in. | 
**transactionDate** | **datetime** | The date of the transaction. | 
**settlementDate** | **datetime** | The settlement date of the transaction. | 
**units** | **int, float** | The number of units transacted in the associated instrument. | 
**transactionPrice** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**totalConsideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchangeRate** | **int, float, none_type** | The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. | [optional] 
**transactionCurrency** | **str, none_type** | The transaction currency. | [optional] 
**properties** | **{str: (PerpetualProperty,)}, none_type** | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#x27;Transaction&#x27; domain. | [optional] 
**counterpartyId** | **str, none_type** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str, none_type** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**entryDateTime** | **datetime** | The asAt datetime that the transaction was added to LUSID. | [optional] 
**otcConfirmation** | [**OtcConfirmation**](OtcConfirmation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

