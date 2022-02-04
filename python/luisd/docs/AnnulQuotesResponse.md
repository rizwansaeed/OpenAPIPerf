# AnnulQuotesResponse

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **{str: (datetime,)}, none_type** | The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID. | [optional] 
**failed** | **{str: (ErrorDetail,)}, none_type** | The quotes that could not be deleted along with a reason for their failure. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

