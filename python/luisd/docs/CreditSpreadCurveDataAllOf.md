# CreditSpreadCurveDataAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseDate** | **datetime** | EffectiveAt date of the quoted rates | 
**domCcy** | **str** | Domestic currency of the curve | 
**tenors** | **[str]** | The tenors for which the rates apply | 
**spreads** | **[int, float]** | Par spread quotes corresponding to the tenors. | 
**recoveryRate** | **int, float** | The recovery rate in default. | 
**referenceDate** | **datetime, none_type** | If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve. | [optional] 
**maturities** | **[datetime], none_type** | The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both. | [optional] 
**marketDataType** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

