# FxForwardModelOptionsAllOf

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwardRateObservableType** | **str** | The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid | 
**discountingMethod** | **str** | The available values are: Standard, ConstantTimeValueOfMoney, Invalid | 
**convertToReportCcy** | **bool** | Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. | 
**modelOptionsType** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

