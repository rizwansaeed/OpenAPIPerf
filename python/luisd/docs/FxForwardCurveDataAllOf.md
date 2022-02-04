# FxForwardCurveDataAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseDate** | **datetime** | EffectiveAt date of the quoted rates | 
**domCcy** | **str** | Domestic currency of the fx forward | 
**fgnCcy** | **str** | Foreign currency of the fx forward | 
**dates** | **[datetime]** | Dates for which the forward rates apply | 
**rates** | **[int, float]** | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) | 
**marketDataType** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

