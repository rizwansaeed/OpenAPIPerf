# FxForwardCurveByQuoteReferenceAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domCcy** | **str** | Domestic currency of the fx forward | 
**fgnCcy** | **str** | Foreign currency of the fx forward | 
**tenors** | **[str]** | Tenors for which the forward rates apply | 
**quoteReferences** | **[{str: (str,)}]** | For each tenor, a list of identifiers. These will be looked up in the quotes store to resolve the actual rates. | 
**marketDataType** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

