# LegDefinition

Definition of the set of flow and index conventions along with other miscellaneous information required to generate an instrument leg.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conventionName** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**indexConvention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**indexConventionName** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notionalExchangeType** | **str** | what type of notional exchange does the leg have  Supported string (enumeration) values are: [None, Initial, Final, Both]. | 
**payReceive** | **str** | Is the leg to be paid or received  Supported string (enumeration) values are: [Pay, Receive]. | 
**rateOrSpread** | **int, float** | Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. | 
**resetConvention** | **str, none_type** | Control how resets are generated relative to swap payment convention(s).  Supported string (enumeration) values are: [InAdvance, InArrears]. | [optional] 
**stubType** | **str** | If a stub is required should it be at the front or back of the leg.  Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both]. | 
**compounding** | [**Compounding**](Compounding.md) |  | [optional] 
**amortisation** | [**StepSchedule**](StepSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

