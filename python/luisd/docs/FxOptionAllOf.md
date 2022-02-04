# FxOptionAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**optionMaturityDate** | **datetime** | The maturity date of the option. | 
**optionSettlementDate** | **datetime** | The settlement date of the option. | 
**isDeliveryNotCash** | **bool** | True if the option is settled in cash, false if delivery. | 
**isCallNotPut** | **bool** | True if the option is a call, false if the option is a put. | 
**strike** | **int, float** | The strike of the option. | 
**domCcy** | **str** | The domestic currency of the instrument. | 
**domAmount** | **int, float, none_type** | The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1. | [optional] 
**fgnCcy** | **str** | The foreign currency of the FX. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**instrumentType** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

