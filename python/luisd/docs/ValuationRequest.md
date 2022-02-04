# ValuationRequest

Specification object for the parameters of a valuation

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipeId** | [**ResourceId**](ResourceId.md) |  | [optional] 
**asAt** | **datetime, none_type** | The asAt date to use | [optional] 
**metrics** | **[AggregateSpec]** | The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#x27;Holding/default/PV&#x27;,&#x27;Sum&#x27;) for returning the PV (present value) of holdings  AggregateSpec(&#x27;Holding/default/Units&#x27;,&#x27;Sum&#x27;) for returning the units of holidays  AggregateSpec(&#x27;Instrument/default/LusidInstrumentId&#x27;,&#x27;Value&#x27;) for returning the Lusid Instrument identifier | 
**groupBy** | **[str], none_type** | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | [optional] 
**filters** | **[PropertyFilter], none_type** | A set of filters to use to reduce the data found in a request. Equivalent to the &#x27;where ...&#x27; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value. | [optional] 
**sort** | **[OrderBySpec], none_type** | A (possibly empty/null) set of specifications for how to order the results. | [optional] 
**reportCurrency** | **str, none_type** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place. | [optional] 
**equipWithSubtotals** | **bool** | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 
**portfolioEntityIds** | **[PortfolioEntityId], none_type** | The set of portfolio or portfolio group identifier(s) that is to be valued. | [optional] 
**valuationSchedule** | [**ValuationSchedule**](ValuationSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

