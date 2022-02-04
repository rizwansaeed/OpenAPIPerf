# CreateRecipeRequest

Specification class to request for the creation/supplementing of a configuration recipe

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipeCreationMarketDataScopes** | **[str]** | The scopes in which the recipe creation would look for quotes/data. | 
**recipeId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**inlineRecipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**asAt** | **datetime, none_type** | The asAt date to use | [optional] 
**effectiveAt** | **str** | The market data time, i.e. the recipe generated will look for rules with this effectiveAt. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

