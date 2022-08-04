# luisd.model.upsert_corporate_actions_response.UpsertCorporateActionsResponse

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str, none_type** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **{str: (CorporateAction,)}, none_type** | The corporate actions which have been successfully updated or inserted. | [optional] 
**failed** | **{str: (ErrorDetail,)}, none_type** | The corporate actions that could not be updated or inserted along with a reason for their failure. | [optional] 
**links** | **[Link], none_type** | Collection of links. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

