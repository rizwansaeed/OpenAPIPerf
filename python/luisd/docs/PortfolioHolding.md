# PortfolioHolding

A list of holdings.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrumentScope** | **str, none_type** | The scope in which the holding&#x27;s instrument is in. | [optional] 
**instrumentUid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**subHoldingKeys** | **{str: (PerpetualProperty,)}, none_type** | The sub-holding properties which identify the holding. Each property will be from the &#x27;Transaction&#x27; domain. These are configured when a transaction portfolio is created. | [optional] 
**properties** | **{str: (ModelProperty,)}, none_type** | The properties which have been requested to be decorated onto the holding. These will be from the &#x27;Instrument&#x27; or &#x27;Holding&#x27; domain. | [optional] 
**holdingType** | **str** | The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | 
**units** | **int, float** | The total number of units of the holding. | 
**settledUnits** | **int, float** | The total number of settled units of the holding. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**costPortfolioCcy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**currency** | **str, none_type** | The holding currency. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

