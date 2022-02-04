# ContractForDifferenceAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **datetime** | The start date of the CFD. | 
**maturityDate** | **datetime** | The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set. | [optional] 
**code** | **str** | The code of the underlying. | 
**contractSize** | **int, float** | The size of the CFD contract, this should represent the total number of stocks that the CFD represents. | 
**payCcy** | **str** | The currency that this CFD pays out, this can be different to the UnderlyingCcy. | 
**referenceRate** | **int, float** | The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0. | [optional] 
**type** | **str** | The type of CFD.  Supported string (enumeration) values are: [Cash, Futures]. | 
**underlyingCcy** | **str** | The currency of the underlying | 
**underlyingIdentifier** | **str** | external market codes and identifiers for the CFD, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**instrumentType** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

