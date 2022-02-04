# TargetTaxLot

Used to specify holdings target amounts at the tax-lot level

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **int, float** | The number of units of the instrument in this tax-lot. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**portfolioCost** | **int, float, none_type** | The total cost of the tax-lot in the transaction portfolio&#x27;s base currency. | [optional] 
**price** | **int, float, none_type** | The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**purchaseDate** | **datetime, none_type** | The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**settlementDate** | **datetime, none_type** | The settlement date of the tax-lot&#x27;s opening transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

