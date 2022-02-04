# CapFloorAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capFloorType** | **str** | Determine if it&#x27;s CAP, FLOOR, or COLLAR.  Supported string (enumeration) values are: [Cap, Floor, Collar]. | 
**capStrike** | **int, float** | Strike rate of the Cap. | 
**floorStrike** | **int, float** | Strike rate of the Floor. | 
**includeFirstCaplet** | **bool** | Include first caplet flag. | 
**underlyingFloatingLeg** | [**FloatingLeg**](FloatingLeg.md) |  | 
**instrumentType** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

