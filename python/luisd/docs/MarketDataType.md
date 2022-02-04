# MarketDataType

The format of the complex market data stored. Complex market data is used to store any  data which requires more context than just a simple single point as is the case with a  quote.  Examples of such complex market data are Discount Curve and Volatility Surfaces.

Type | Description | Notes
------------- | ------------- | -------------
**str** | The format of the complex market data stored. Complex market data is used to store any  data which requires more context than just a simple single point as is the case with a  quote.  Examples of such complex market data are Discount Curve and Volatility Surfaces. |  must be one of ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

