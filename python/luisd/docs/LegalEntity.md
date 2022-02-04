# LegalEntity

Representation of Legal Entity on LUSID API

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **str, none_type** | The display name of the Legal Entity | [optional] 
**description** | **str, none_type** | The description of the Legal Entity | [optional] 
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**lusidLegalEntityId** | **str, none_type** | The unique LUSID Legal Entity Identifier (LULEID) of the Legal Entity. This field is not populated until further notice. | [optional] 
**identifiers** | **{str: (ModelProperty,)}, none_type** | Unique client-defined identifiers of the Legal Entity. | [optional] 
**properties** | **{str: (ModelProperty,)}, none_type** | A set of properties associated to the Legal Entity. | [optional] 
**counterpartyRiskInformation** | [**CounterpartyRiskInformation**](CounterpartyRiskInformation.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

