# Repo

IL Repo Instrument; Lusid-ibor internal representation of a Repo instrument  The repurchase (repo) agreement involves the transfer of instruments (the collateral) from the seller to the buyer.  Ownership is transferred and returns to the seller upon completion of the contract. If the collateral depreciates sharply, it is possible that additional  margin/collateral will be required depending upon the terms of the agreement. The buyer agrees not to sell the securities unless there is some condition of default  in the repo contract.  Repurchase of the securities is at the purchase price plus the agreed upon fixed repo rate, this is the Repurchase price, which can be passed directly or calculated.  On the start date, the buyer receives the collateral and pays Cash (PurchasePrice).  On the maturity date, the buyer returns the collateral and receives Cash (RepurchasePrice).

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

