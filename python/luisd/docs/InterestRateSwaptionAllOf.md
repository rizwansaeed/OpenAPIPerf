# InterestRateSwaptionAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**payOrReceiveFixed** | **str** | True if on exercise the holder of the option enters the swap paying fixed, false if floating.  Supported string (enumeration) values are: [Pay, Receive]. | 
**deliveryMethod** | **str** | How does the option settle  Supported string (enumeration) values are: [Cash, Physical]. | 
**swap** | [**InterestRateSwap**](InterestRateSwap.md) |  | 
**instrumentType** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

