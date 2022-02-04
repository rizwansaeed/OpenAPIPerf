# Package

A structure used to describe the structure of an order or orders that make up a non-trivial trade.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**orderIds** | **[ResourceId]** | Related order ids. | 
**orderInstructionIds** | **[ResourceId]** | Related order instruction ids. | 
**properties** | **{str: (PerpetualProperty,)}, none_type** | Client-defined properties associated with this execution. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

