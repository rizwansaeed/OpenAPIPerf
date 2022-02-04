# CounterpartyRiskInformation

In the event that the legal entity is a counterparty to an OTC transaction  (as signatory to a counterparty agreement such as an ISDA 2002 Master Agreement),  this information would be needed for calculations  such as Credit-Valuation-Adjustments and Debit-Valuation-Adjustments (CVA, DVA, XVA etc).

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryOfRisk** | **str** | The country to which one would naturally ascribe risk, typically the legal entity&#x27;s country of registration. This can be used to infer funding currency and related market data in the absence of a specific preference. | 
**creditRatings** | **[CreditRating]** |  | 
**industryClassifiers** | **[IndustryClassifier]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

