# TransactionRequest

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionId** | **str** | The unique identifier of the transaction. | 
**type** | **str** | The type of the transaction, for example &#x27;Buy&#x27; or &#x27;Sell&#x27;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction. | 
**instrumentIdentifiers** | **{str: (str,)}** | A set of instrument identifiers that can resolve the transaction to a unique instrument. | 
**transactionDate** | **str** | The date of the transaction. | 
**settlementDate** | **str** | The settlement date of the transaction. | 
**units** | **int, float** | The number of units of the transacted instrument. | 
**transactionPrice** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**totalConsideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**exchangeRate** | **int, float, none_type** | The exchange rate between the transaction and settlement currency (settlement currency being represented by TotalConsideration.Currency). For example, if the transaction currency is USD and the settlement currency is GBP, this would be the appropriate USD/GBP rate. | [optional] 
**transactionCurrency** | **str, none_type** | The transaction currency. | [optional] 
**properties** | **{str: (PerpetualProperty,)}, none_type** | A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#x27;Transaction&#x27; domain. | [optional] 
**counterpartyId** | **str, none_type** | The identifier for the counterparty of the transaction. | [optional] 
**source** | **str, none_type** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

