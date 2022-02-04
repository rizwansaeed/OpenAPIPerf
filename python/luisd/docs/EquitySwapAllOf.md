# EquitySwapAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **datetime** | The start date of the EquitySwap. | 
**maturityDate** | **datetime** | The maturity date of the EquitySwap. | 
**code** | **str** | The code of the underlying. | 
**equityFlowConventions** | [**FlowConventions**](FlowConventions.md) |  | 
**fundingLeg** | [**InstrumentLeg**](InstrumentLeg.md) |  | 
**includeDividends** | **bool** | Dividend inclusion flag, if true dividends are included in the equity leg (total return). | 
**initialPrice** | **int, float** | The initial equity price of the Equity Swap. | 
**notionalReset** | **bool** | Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity). | 
**quantity** | **int, float** | The quantity or number of shares in the Equity Swap. | 
**underlyingIdentifier** | **str** | external market codes and identifiers for the EquitySwap, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**instrumentType** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

