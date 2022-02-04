# PortfolioCashFlow

The details for the cashflow for a given portfolio.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupById** | **int** | The groupBy subHoldings and currency. | 
**sequenceNumber** | **int** | Sequence number determining the order of the cash flow records. | 
**effectiveDate** | **datetime** | Indicates the date when the cash-flow settles. | [optional] 
**subHoldingKeys** | **{str: (PerpetualProperty,)}, none_type** | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | [optional] 
**type** | **str** | Indicates the record type (Closed, Open, Activity). | 
**movementName** | **str** | Indicates the specific movement of the transaction that generated this cash flow. | 
**cashflow** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**balance** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**fxRate** | **int, float** | Exchange rate between the currency of this cash flow and the reporting currency. | 
**cashflowReportingCurrency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**balanceReportingCurrency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**translationGainLoss** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**costBasisReportingCurrency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**unrealisedGainLossReportingCurrency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

