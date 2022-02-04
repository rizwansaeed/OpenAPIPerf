# TranslateInstrumentDefinitionsResponse

A response from a request to translate a collection of instruments to a given target dialect.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **{str: (LusidInstrument,)}, none_type** | The instruments which have been successfully translated. | [optional] 
**failed** | **{str: (ErrorDetail,)}, none_type** | The instruments that could not be translated along with a reason for their failure. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

