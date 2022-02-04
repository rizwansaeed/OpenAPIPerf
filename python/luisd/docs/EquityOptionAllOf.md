# EquityOptionAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**optionMaturityDate** | **datetime** | The maturity date of the option. | 
**optionSettlementDate** | **datetime** | The settlement date of the option. | 
**deliveryType** | **str** | The available values are: Cash, Physical | 
**optionType** | **str** | The available values are: None, Call, Put | 
**strike** | **int, float** | The strike of the option. | 
**domCcy** | **str** | The domestic currency of the instrument. | 
**underlyingIdentifier** | **str** | The available values are: LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode | 
**code** | **str** | The identifying code for the equity underlying, e.g. &#x27;IBM.N&#x27;. | 
**instrumentType** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

