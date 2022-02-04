# RealisedGainLoss

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentUid** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with. | 
**units** | **int, float** | The number of units of the associated instrument against which the gain or loss has been realised. | 
**purchaseTradeDate** | **datetime, none_type** | The effective datetime that the units associated with this gain or loss where originally purchased. | [optional] [readonly] 
**purchaseSettlementDate** | **datetime, none_type** | The effective datetime that the units associated with this gain or loss where originally settled. | [optional] [readonly] 
**purchasePrice** | **int, float, none_type** | The purchase price of each unit associated with this gain or loss. | [optional] 
**costTradeCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**costPortfolioCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realisedTradeCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realisedTotal** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realisedMarket** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**realisedCurrency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

