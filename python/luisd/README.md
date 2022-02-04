# luisd
# Introduction

This page documents the [LUSID APIs](https://www.lusid.com/api/swagger), which allows authorised clients to query and update their data within the LUSID platform.

SDKs to interact with the LUSID APIs are available in the following languages and frameworks:

* [C#](https://github.com/finbourne/lusid-sdk-csharp)
* [Java](https://github.com/finbourne/lusid-sdk-java)
* [JavaScript](https://github.com/finbourne/lusid-sdk-js)
* [Python](https://github.com/finbourne/lusid-sdk-python)
* [Angular](https://github.com/finbourne/lusid-sdk-angular)

The LUSID platform is made up of a number of sub-applications. You can find the API / swagger documentation by following the links in the table below.


| Application | Description | API / Swagger Documentation |
| ----- | ----- | ---- |
| LUSID | Open, API-first, developer-friendly investment data platform. | [Swagger](https://www.lusid.com/api/swagger/index.html) |
| Web app | User-facing front end for LUSID. | [Swagger](https://www.lusid.com/app/swagger/index.html) |
| Scheduler | Automated job scheduler. | [Swagger](https://www.lusid.com/scheduler2/swagger/index.html) |
| Insights |Monitoring and troubleshooting service. | [Swagger](https://www.lusid.com/insights/swagger/index.html) |
| Identity | Identity management for LUSID (in conjuction with Access) | [Swagger](https://www.lusid.com/identity/swagger/index.html) |
| Access | Access control for LUSID (in conjunction with Identity) | [Swagger](https://www.lusid.com/access/swagger/index.html) |
| Drive | Secure file repository and manager for collaboration. | [Swagger](https://www.lusid.com/drive/swagger/index.html) |
| Luminesce | Data virtualisation service (query data from multiple providers, including LUSID) | [Swagger](https://www.lusid.com/honeycomb/swagger/index.html) |
| Notification | Notification service. | [Swagger](https://www.lusid.com/notifications/swagger/index.html) |
| Configuration | File store for secrets and other sensitive information. | [Swagger](https://www.lusid.com/configuration/swagger/index.html) |


# Error Codes

| Code|Name|Description |
| ---|---|--- |
| <a name=\"-10\">-10</a>|Server Configuration Error|  |
| <a name=\"-1\">-1</a>|Unknown error|An unexpected error was encountered on our side. |
| <a name=\"102\">102</a>|Version Not Found|  |
| <a name=\"103\">103</a>|Api Rate Limit Violation|  |
| <a name=\"104\">104</a>|Instrument Not Found|  |
| <a name=\"105\">105</a>|Property Not Found|  |
| <a name=\"106\">106</a>|Portfolio Recursion Depth|  |
| <a name=\"108\">108</a>|Group Not Found|  |
| <a name=\"109\">109</a>|Portfolio Not Found|  |
| <a name=\"110\">110</a>|Property Schema Not Found|  |
| <a name=\"111\">111</a>|Portfolio Ancestry Not Found|  |
| <a name=\"112\">112</a>|Portfolio With Id Already Exists|  |
| <a name=\"113\">113</a>|Orphaned Portfolio|  |
| <a name=\"119\">119</a>|Missing Base Claims|  |
| <a name=\"121\">121</a>|Property Not Defined|  |
| <a name=\"122\">122</a>|Cannot Delete System Property|  |
| <a name=\"123\">123</a>|Cannot Modify Immutable Property Field|  |
| <a name=\"124\">124</a>|Property Already Exists|  |
| <a name=\"125\">125</a>|Invalid Property Life Time|  |
| <a name=\"126\">126</a>|Property Constraint Style Excludes Properties|  |
| <a name=\"127\">127</a>|Cannot Modify Default Data Type|  |
| <a name=\"128\">128</a>|Group Already Exists|  |
| <a name=\"129\">129</a>|No Such Data Type|  |
| <a name=\"130\">130</a>|Undefined Value For Data Type|  |
| <a name=\"131\">131</a>|Unsupported Value Type Defined On Data Type|  |
| <a name=\"132\">132</a>|Validation Error|  |
| <a name=\"133\">133</a>|Loop Detected In Group Hierarchy|  |
| <a name=\"134\">134</a>|Undefined Acceptable Values|  |
| <a name=\"135\">135</a>|Sub Group Already Exists|  |
| <a name=\"138\">138</a>|Price Source Not Found|  |
| <a name=\"139\">139</a>|Analytic Store Not Found|  |
| <a name=\"141\">141</a>|Analytic Store Already Exists|  |
| <a name=\"143\">143</a>|Client Instrument Already Exists|  |
| <a name=\"144\">144</a>|Duplicate In Parameter Set|  |
| <a name=\"147\">147</a>|Results Not Found|  |
| <a name=\"148\">148</a>|Order Field Not In Result Set|  |
| <a name=\"149\">149</a>|Operation Failed|  |
| <a name=\"150\">150</a>|Elastic Search Error|  |
| <a name=\"151\">151</a>|Invalid Parameter Value|  |
| <a name=\"153\">153</a>|Command Processing Failure|  |
| <a name=\"154\">154</a>|Entity State Construction Failure|  |
| <a name=\"155\">155</a>|Entity Timeline Does Not Exist|  |
| <a name=\"156\">156</a>|Concurrency Conflict Failure|  |
| <a name=\"157\">157</a>|Invalid Request|  |
| <a name=\"158\">158</a>|Event Publish Unknown|  |
| <a name=\"159\">159</a>|Event Query Failure|  |
| <a name=\"160\">160</a>|Blob Did Not Exist|  |
| <a name=\"162\">162</a>|Sub System Request Failure|  |
| <a name=\"163\">163</a>|Sub System Configuration Failure|  |
| <a name=\"165\">165</a>|Failed To Delete|  |
| <a name=\"166\">166</a>|Upsert Client Instrument Failure|  |
| <a name=\"167\">167</a>|Illegal As At Interval|  |
| <a name=\"168\">168</a>|Illegal Bitemporal Query|  |
| <a name=\"169\">169</a>|Invalid Alternate Id|  |
| <a name=\"170\">170</a>|Cannot Add Source Portfolio Property Explicitly|  |
| <a name=\"171\">171</a>|Entity Already Exists In Group|  |
| <a name=\"173\">173</a>|Entity With Id Already Exists|  |
| <a name=\"174\">174</a>|Derived Portfolio Details Do Not Exist|  |
| <a name=\"176\">176</a>|Portfolio With Name Already Exists|  |
| <a name=\"177\">177</a>|Invalid Transactions|  |
| <a name=\"178\">178</a>|Reference Portfolio Not Found|  |
| <a name=\"179\">179</a>|Duplicate Id|  |
| <a name=\"180\">180</a>|Command Retrieval Failure|  |
| <a name=\"181\">181</a>|Data Filter Application Failure|  |
| <a name=\"182\">182</a>|Search Failed|  |
| <a name=\"183\">183</a>|Movements Engine Configuration Key Failure|  |
| <a name=\"184\">184</a>|Fx Rate Source Not Found|  |
| <a name=\"185\">185</a>|Accrual Source Not Found|  |
| <a name=\"186\">186</a>|Access Denied|  |
| <a name=\"187\">187</a>|Invalid Identity Token|  |
| <a name=\"188\">188</a>|Invalid Request Headers|  |
| <a name=\"189\">189</a>|Price Not Found|  |
| <a name=\"190\">190</a>|Invalid Sub Holding Keys Provided|  |
| <a name=\"191\">191</a>|Duplicate Sub Holding Keys Provided|  |
| <a name=\"192\">192</a>|Cut Definition Not Found|  |
| <a name=\"193\">193</a>|Cut Definition Invalid|  |
| <a name=\"194\">194</a>|Time Variant Property Deletion Date Unspecified|  |
| <a name=\"195\">195</a>|Perpetual Property Deletion Date Specified|  |
| <a name=\"196\">196</a>|Time Variant Property Upsert Date Unspecified|  |
| <a name=\"197\">197</a>|Perpetual Property Upsert Date Specified|  |
| <a name=\"200\">200</a>|Invalid Unit For Data Type|  |
| <a name=\"201\">201</a>|Invalid Type For Data Type|  |
| <a name=\"202\">202</a>|Invalid Value For Data Type|  |
| <a name=\"203\">203</a>|Unit Not Defined For Data Type|  |
| <a name=\"204\">204</a>|Units Not Supported On Data Type|  |
| <a name=\"205\">205</a>|Cannot Specify Units On Data Type|  |
| <a name=\"206\">206</a>|Unit Schema Inconsistent With Data Type|  |
| <a name=\"207\">207</a>|Unit Definition Not Specified|  |
| <a name=\"208\">208</a>|Duplicate Unit Definitions Specified|  |
| <a name=\"209\">209</a>|Invalid Units Definition|  |
| <a name=\"210\">210</a>|Invalid Instrument Identifier Unit|  |
| <a name=\"211\">211</a>|Holdings Adjustment Does Not Exist|  |
| <a name=\"212\">212</a>|Could Not Build Excel Url|  |
| <a name=\"213\">213</a>|Could Not Get Excel Version|  |
| <a name=\"214\">214</a>|Instrument By Code Not Found|  |
| <a name=\"215\">215</a>|Entity Schema Does Not Exist|  |
| <a name=\"216\">216</a>|Feature Not Supported On Portfolio Type|  |
| <a name=\"217\">217</a>|Quote Not Found|  |
| <a name=\"218\">218</a>|Invalid Quote Identifier|  |
| <a name=\"219\">219</a>|Invalid Metric For Data Type|  |
| <a name=\"220\">220</a>|Invalid Instrument Definition|  |
| <a name=\"221\">221</a>|Instrument Upsert Failure|  |
| <a name=\"222\">222</a>|Reference Portfolio Request Not Supported|  |
| <a name=\"223\">223</a>|Transaction Portfolio Request Not Supported|  |
| <a name=\"224\">224</a>|Invalid Property Value Assignment|  |
| <a name=\"230\">230</a>|Transaction Type Not Found|  |
| <a name=\"231\">231</a>|Transaction Type Duplication|  |
| <a name=\"232\">232</a>|Portfolio Does Not Exist At Given Date|  |
| <a name=\"233\">233</a>|Query Parser Failure|  |
| <a name=\"234\">234</a>|Duplicate Constituent|  |
| <a name=\"235\">235</a>|Unresolved Instrument Constituent|  |
| <a name=\"236\">236</a>|Unresolved Instrument In Transition|  |
| <a name=\"237\">237</a>|Missing Side Definitions|  |
| <a name=\"299\">299</a>|Invalid Recipe|  |
| <a name=\"300\">300</a>|Missing Recipe|  |
| <a name=\"301\">301</a>|Dependencies|  |
| <a name=\"304\">304</a>|Portfolio Preprocess Failure|  |
| <a name=\"310\">310</a>|Valuation Engine Failure|  |
| <a name=\"311\">311</a>|Task Factory Failure|  |
| <a name=\"312\">312</a>|Task Evaluation Failure|  |
| <a name=\"313\">313</a>|Task Generation Failure|  |
| <a name=\"314\">314</a>|Engine Configuration Failure|  |
| <a name=\"315\">315</a>|Model Specification Failure|  |
| <a name=\"320\">320</a>|Market Data Key Failure|  |
| <a name=\"321\">321</a>|Market Resolver Failure|  |
| <a name=\"322\">322</a>|Market Data Failure|  |
| <a name=\"330\">330</a>|Curve Failure|  |
| <a name=\"331\">331</a>|Volatility Surface Failure|  |
| <a name=\"332\">332</a>|Volatility Cube Failure|  |
| <a name=\"350\">350</a>|Instrument Failure|  |
| <a name=\"351\">351</a>|Cash Flows Failure|  |
| <a name=\"352\">352</a>|Reference Data Failure|  |
| <a name=\"360\">360</a>|Aggregation Failure|  |
| <a name=\"361\">361</a>|Aggregation Measure Failure|  |
| <a name=\"370\">370</a>|Result Retrieval Failure|  |
| <a name=\"371\">371</a>|Result Processing Failure|  |
| <a name=\"372\">372</a>|Vendor Result Processing Failure|  |
| <a name=\"373\">373</a>|Vendor Result Mapping Failure|  |
| <a name=\"374\">374</a>|Vendor Library Unauthorised|  |
| <a name=\"375\">375</a>|Vendor Connectivity Error|  |
| <a name=\"376\">376</a>|Vendor Interface Error|  |
| <a name=\"377\">377</a>|Vendor Pricing Failure|  |
| <a name=\"378\">378</a>|Vendor Translation Failure|  |
| <a name=\"379\">379</a>|Vendor Key Mapping Failure|  |
| <a name=\"380\">380</a>|Vendor Reflection Failure|  |
| <a name=\"381\">381</a>|Vendor Process Failure|  |
| <a name=\"382\">382</a>|Vendor System Failure|  |
| <a name=\"390\">390</a>|Attempt To Upsert Duplicate Quotes|  |
| <a name=\"391\">391</a>|Corporate Action Source Does Not Exist|  |
| <a name=\"392\">392</a>|Corporate Action Source Already Exists|  |
| <a name=\"393\">393</a>|Instrument Identifier Already In Use|  |
| <a name=\"394\">394</a>|Properties Not Found|  |
| <a name=\"395\">395</a>|Batch Operation Aborted|  |
| <a name=\"400\">400</a>|Invalid Iso4217 Currency Code|  |
| <a name=\"401\">401</a>|Cannot Assign Instrument Identifier To Currency|  |
| <a name=\"402\">402</a>|Cannot Assign Currency Identifier To Non Currency|  |
| <a name=\"403\">403</a>|Currency Instrument Cannot Be Deleted|  |
| <a name=\"404\">404</a>|Currency Instrument Cannot Have Economic Definition|  |
| <a name=\"405\">405</a>|Currency Instrument Cannot Have Lookthrough Portfolio|  |
| <a name=\"406\">406</a>|Cannot Create Currency Instrument With Multiple Identifiers|  |
| <a name=\"407\">407</a>|Specified Currency Is Undefined|  |
| <a name=\"410\">410</a>|Index Does Not Exist|  |
| <a name=\"411\">411</a>|Sort Field Does Not Exist|  |
| <a name=\"413\">413</a>|Negative Pagination Parameters|  |
| <a name=\"414\">414</a>|Invalid Search Syntax|  |
| <a name=\"415\">415</a>|Filter Execution Timeout|  |
| <a name=\"420\">420</a>|Side Definition Inconsistent|  |
| <a name=\"450\">450</a>|Invalid Quote Access Metadata Rule|  |
| <a name=\"451\">451</a>|Access Metadata Not Found|  |
| <a name=\"452\">452</a>|Invalid Access Metadata Identifier|  |
| <a name=\"460\">460</a>|Standard Resource Not Found|  |
| <a name=\"461\">461</a>|Standard Resource Conflict|  |
| <a name=\"462\">462</a>|Calendar Not Found|  |
| <a name=\"463\">463</a>|Date In A Calendar Not Found|  |
| <a name=\"464\">464</a>|Invalid Date Source Data|  |
| <a name=\"465\">465</a>|Invalid Timezone|  |
| <a name=\"601\">601</a>|Person Identifier Already In Use|  |
| <a name=\"602\">602</a>|Person Not Found|  |
| <a name=\"603\">603</a>|Cannot Set Identifier|  |
| <a name=\"617\">617</a>|Invalid Recipe Specification In Request|  |
| <a name=\"618\">618</a>|Inline Recipe Deserialisation Failure|  |
| <a name=\"619\">619</a>|Identifier Types Not Set For Entity|  |
| <a name=\"620\">620</a>|Cannot Delete All Client Defined Identifiers|  |
| <a name=\"650\">650</a>|The Order requested was not found.|  |
| <a name=\"654\">654</a>|The Allocation requested was not found.|  |
| <a name=\"655\">655</a>|Cannot build the fx forward target with the given holdings.|  |
| <a name=\"656\">656</a>|Group does not contain expected entities.|  |
| <a name=\"665\">665</a>|Destination directory not found|  |
| <a name=\"667\">667</a>|Relation definition already exists|  |
| <a name=\"672\">672</a>|Could not retrieve file contents|  |
| <a name=\"673\">673</a>|Missing entitlements for entities in Group|  |
| <a name=\"674\">674</a>|Next Best Action not found|  |
| <a name=\"676\">676</a>|Relation definition not defined|  |
| <a name=\"677\">677</a>|Invalid entity identifier for relation|  |
| <a name=\"681\">681</a>|Sorting by specified field not supported|One or more of the provided fields to order by were either invalid or not supported. |
| <a name=\"682\">682</a>|Too many fields to sort by|The number of fields to sort the data by exceeds the number allowed by the endpoint |
| <a name=\"684\">684</a>|Sequence Not Found|  |
| <a name=\"685\">685</a>|Sequence Already Exists|  |
| <a name=\"686\">686</a>|Non-cycling sequence has been exhausted|  |
| <a name=\"687\">687</a>|Legal Entity Identifier Already In Use|  |
| <a name=\"688\">688</a>|Legal Entity Not Found|  |
| <a name=\"689\">689</a>|The supplied pagination token is invalid|  |
| <a name=\"690\">690</a>|Property Type Is Not Supported|  |
| <a name=\"691\">691</a>|Multiple Tax-lots For Currency Type Is Not Supported|  |
| <a name=\"692\">692</a>|This endpoint does not support impersonation|  |
| <a name=\"693\">693</a>|Entity type is not supported for Relationship|  |
| <a name=\"694\">694</a>|Relationship Validation Failure|  |
| <a name=\"695\">695</a>|Relationship Not Found|  |
| <a name=\"697\">697</a>|Derived Property Formula No Longer Valid|  |
| <a name=\"698\">698</a>|Story is not available|  |
| <a name=\"703\">703</a>|Corporate Action Does Not Exist|  |
| <a name=\"720\">720</a>|The provided sort and filter combination is not valid|  |
| <a name=\"721\">721</a>|A2B generation failed|  |
| <a name=\"722\">722</a>|Aggregated Return Calculation Failure|  |
| <a name=\"723\">723</a>|Custom Entity Definition Identifier Already In Use|  |
| <a name=\"724\">724</a>|Custom Entity Definition Not Found|  |
| <a name=\"725\">725</a>|The Placement requested was not found.|  |
| <a name=\"726\">726</a>|The Execution requested was not found.|  |
| <a name=\"727\">727</a>|The Block requested was not found.|  |
| <a name=\"728\">728</a>|The Participation requested was not found.|  |
| <a name=\"729\">729</a>|The Package requested was not found.|  |
| <a name=\"730\">730</a>|The OrderInstruction requested was not found.|  |
| <a name=\"732\">732</a>|Custom Entity not found.|  |
| <a name=\"733\">733</a>|Custom Entity Identifier already in use.|  |
| <a name=\"735\">735</a>|Calculation Failed.|  |
| <a name=\"736\">736</a>|An expected key on HttpResponse is missing.|  |
| <a name=\"737\">737</a>|A required fee detail is missing.|  |
| <a name=\"738\">738</a>|Zero rows were returned from Luminesce|  |
| <a name=\"739\">739</a>|Provided Weekend Mask was invalid|  |
| <a name=\"742\">742</a>|Custom Entity fields do not match the definition|  |
| <a name=\"746\">746</a>|The provided sequence is not valid.|  |
| <a name=\"751\">751</a>|The type of the Custom Entity is different than the type provided in the definition.|  |
| <a name=\"752\">752</a>|Luminesce process returned an error.|  |
| <a name=\"753\">753</a>|File name or content incompatible with operation.|  |
| <a name=\"755\">755</a>|Schema of response from Drive is not as expected.|  |
| <a name=\"757\">757</a>|Schema of response from Luminesce is not as expected.|  |
| <a name=\"758\">758</a>|Luminesce timed out.|  |


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.11.3916
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonExperimentalClientCodegen
For more information, please visit [https://www.finbourne.com](https://www.finbourne.com)

## Requirements.

Python &gt;&#x3D;3.9
v3.9 is needed so one can combine classmethod and property decorators to define
object schema properties as classes

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import luisd
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import luisd
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import luisd
from pprint import pprint
from luisd.api import aggregation_api
from luisd.model.configuration_recipe import ConfigurationRecipe
from luisd.model.create_recipe_request import CreateRecipeRequest
from luisd.model.inline_valuation_request import InlineValuationRequest
from luisd.model.list_aggregation_response import ListAggregationResponse
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_aggregation_query import ResourceListOfAggregationQuery
from luisd.model.valuation_request import ValuationRequest
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = luisd.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with luisd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aggregation_api.AggregationApi(api_client)
    scope = "z" # str, none_type | The scope of the portfolio
code = "z" # str, none_type | The code of the portfolio
create_recipe_request = CreateRecipeRequest(
        recipe_creation_market_data_scopes=[
            "recipe_creation_market_data_scopes_example",
        ],
        recipe_id=ResourceId(
            scope="scope_example",
            code="code_example",
        ),
        inline_recipe=ConfigurationRecipe(
            scope="z",
            code="z",
            market=MarketContext(
                market_rules=[
                    MarketDataKeyRule(
                        key="key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        quote_type="Price",
                        field="field_example",
                        quote_interval="quote_interval_example",
                        as_at=isoparse('1970-01-01T00:00:00.00Z'),
                        price_source="price_source_example",
                        mask="mask_example",
                    ),
                ],
                suppliers=MarketContextSuppliers(
                    commodity="commodity_example",
                    credit="credit_example",
                    equity="equity_example",
                    fx="fx_example",
                    rates="rates_example",
                ),
                options=MarketOptions(
                    default_supplier="default_supplier_example",
                    default_instrument_code_type="default_instrument_code_type_example",
                    default_scope="z",
                    attempt_to_infer_missing_fx=True,
                    calendar_scope="z",
                    convention_scope="z",
                ),
            ),
            pricing=PricingContext(
                model_rules=[
                    VendorModelRule(
                        supplier="Lusid",
                        model_name="model_name_example",
                        instrument_type="instrument_type_example",
                        parameters="parameters_example",
                        model_options=ModelOptions(),
                        instrument_id="instrument_id_example",
                    ),
                ],
                model_choice=dict(
                    "key": ModelSelection(
                        library="Lusid",
                        model="SimpleStatic",
                    ),
                ),
                options=PricingOptions(
                    model_selection=ModelSelection(
                        library="Lusid",
                        model="SimpleStatic",
                    ),
                    use_instrument_type_to_determine_pricer=True,
                    allow_any_instruments_with_sec_uid_to_price_off_lookup=True,
                    allow_partially_successful_evaluation=True,
                    produce_separate_result_for_linear_otc_legs=True,
                    enable_use_of_cached_unit_results=True,
                    window_valuation_on_instrument_start_end=True,
                    remove_contingent_cashflows_in_payment_diary=True,
                    use_child_sub_holding_keys_for_portfolio_expansion=True,
                    validate_domestic_and_quote_currencies_are_consistent=True,
                ),
                result_data_rules=[
                    ResultDataKeyRule(
                        resource_key="resource_key_example",
                        supplier="supplier_example",
                        data_scope="z",
                        document_code="document_code_example",
                        quote_interval="quote_interval_example",
                        as_at=isoparse('1970-01-01T00:00:00.00Z'),
                    ),
                ],
            ),
            aggregation=AggregationContext(
                options=AggregationOptions(
                    use_ansi_like_syntax=True,
                    allow_partial_entitlement_success=True,
                ),
            ),
            inherited_recipes=[
                ResourceId(
                    scope="scope_example",
                    code="code_example",
                ),
            ],
            description="",
            holding=HoldingContext(
                tax_lot_level_holdings=True,
            ),
        ),
        as_at=isoparse('1970-01-01T00:00:00.00Z'),
        effective_at="effective_at_example",
    ) # CreateRecipeRequest | The request specifying the parameters to generating the recipe (optional)

    try:
        # [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
        api_response = api_instance.generate_configuration_recipe(scopecodecreate_recipe_request=create_recipe_request)
        pprint(api_response)
    except luisd.ApiException as e:
        print("Exception when calling AggregationApi->generate_configuration_recipe: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://www.lusid.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AggregationApi* | [**generate_configuration_recipe**](docs/AggregationApi.md#generate_configuration_recipe) | **POST** /api/aggregation/{scope}/{code}/$generateconfigurationrecipe | [EXPERIMENTAL] GenerateConfigurationRecipe: Generates a recipe sufficient to perform valuations for the given portfolio.
*AggregationApi* | [**get_queryable_keys**](docs/AggregationApi.md#get_queryable_keys) | **GET** /api/results/queryable/keys | [EXPERIMENTAL] GetQueryableKeys: Query the set of supported \&quot;addresses\&quot; that can be queried from the aggregation endpoint.
*AggregationApi* | [**get_valuation**](docs/AggregationApi.md#get_valuation) | **POST** /api/aggregation/$valuation | [BETA] GetValuation: Perform valuation for a list of portfolios and/or portfolio groups
*AggregationApi* | [**get_valuation_of_weighted_instruments**](docs/AggregationApi.md#get_valuation_of_weighted_instruments) | **POST** /api/aggregation/$valuationinlined | [BETA] GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio
*AllocationsApi* | [**delete_allocation**](docs/AllocationsApi.md#delete_allocation) | **DELETE** /api/allocations/{scope}/{code} | [EARLY ACCESS] DeleteAllocation: Delete allocation
*AllocationsApi* | [**get_allocation**](docs/AllocationsApi.md#get_allocation) | **GET** /api/allocations/{scope}/{code} | [EARLY ACCESS] GetAllocation: Get Allocation
*AllocationsApi* | [**list_allocations**](docs/AllocationsApi.md#list_allocations) | **GET** /api/allocations | [EARLY ACCESS] ListAllocations: List Allocations
*AllocationsApi* | [**upsert_allocations**](docs/AllocationsApi.md#upsert_allocations) | **POST** /api/allocations | [EARLY ACCESS] UpsertAllocations: Upsert Allocations
*ApplicationMetadataApi* | [**get_excel_addin**](docs/ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/metadata/downloads/exceladdin | [EARLY ACCESS] GetExcelAddin: Download Excel Addin
*ApplicationMetadataApi* | [**get_lusid_versions**](docs/ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/metadata/versions | [EARLY ACCESS] GetLusidVersions: Get LUSID versions
*ApplicationMetadataApi* | [**list_access_controlled_resources**](docs/ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | [EARLY ACCESS] ListAccessControlledResources: Get resources available for access control
*BlocksApi* | [**delete_block**](docs/BlocksApi.md#delete_block) | **DELETE** /api/blocks/{scope}/{code} | [EXPERIMENTAL] DeleteBlock: Delete block
*BlocksApi* | [**get_block**](docs/BlocksApi.md#get_block) | **GET** /api/blocks/{scope}/{code} | [EXPERIMENTAL] GetBlock: Get Block
*BlocksApi* | [**list_blocks**](docs/BlocksApi.md#list_blocks) | **GET** /api/blocks | [EXPERIMENTAL] ListBlocks: List Blocks
*BlocksApi* | [**upsert_blocks**](docs/BlocksApi.md#upsert_blocks) | **POST** /api/blocks | [EXPERIMENTAL] UpsertBlocks: Upsert Block
*CalendarsApi* | [**add_business_days_to_date**](docs/CalendarsApi.md#add_business_days_to_date) | **POST** /api/calendars/businessday/{scope}/add | [EXPERIMENTAL] AddBusinessDaysToDate: Adds the requested number of Business Days to the provided date.
*CalendarsApi* | [**add_date_to_calendar**](docs/CalendarsApi.md#add_date_to_calendar) | **PUT** /api/calendars/generic/{scope}/{code}/dates | [BETA] AddDateToCalendar: Add a date to a calendar
*CalendarsApi* | [**create_calendar**](docs/CalendarsApi.md#create_calendar) | **POST** /api/calendars/generic | [BETA] CreateCalendar: Create a calendar in its generic form
*CalendarsApi* | [**delete_calendar**](docs/CalendarsApi.md#delete_calendar) | **DELETE** /api/calendars/generic/{scope}/{code} | [BETA] DeleteCalendar: Delete a calendar
*CalendarsApi* | [**delete_date_from_calendar**](docs/CalendarsApi.md#delete_date_from_calendar) | **DELETE** /api/calendars/generic/{scope}/{code}/dates/{dateId} | [BETA] DeleteDateFromCalendar: Remove a date from a calendar
*CalendarsApi* | [**generate_schedule**](docs/CalendarsApi.md#generate_schedule) | **POST** /api/calendars/schedule/{scope} | [EXPERIMENTAL] GenerateSchedule: Generate an ordered schedule of dates.
*CalendarsApi* | [**get_calendar**](docs/CalendarsApi.md#get_calendar) | **GET** /api/calendars/generic/{scope}/{code} | [BETA] GetCalendar: Get a calendar in its generic form
*CalendarsApi* | [**get_dates**](docs/CalendarsApi.md#get_dates) | **GET** /api/calendars/generic/{scope}/{code}/dates | [BETA] GetDates: Get dates for a specific calendar
*CalendarsApi* | [**is_business_date_time**](docs/CalendarsApi.md#is_business_date_time) | **GET** /api/calendars/businessday/{scope}/{code} | [BETA] IsBusinessDateTime: Check whether a DateTime is a \&quot;Business DateTime\&quot;
*CalendarsApi* | [**list_calendars**](docs/CalendarsApi.md#list_calendars) | **GET** /api/calendars/generic | [BETA] ListCalendars: List Calendars
*CalendarsApi* | [**list_calendars_in_scope**](docs/CalendarsApi.md#list_calendars_in_scope) | **GET** /api/calendars/generic/{scope} | [BETA] ListCalendarsInScope: List all calenders in a specified scope
*CalendarsApi* | [**update_calendar**](docs/CalendarsApi.md#update_calendar) | **POST** /api/calendars/generic/{scope}/{code} | [BETA] UpdateCalendar: Update a calendar
*ComplexMarketDataApi* | [**delete_complex_market_data**](docs/ComplexMarketDataApi.md#delete_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$delete | [EARLY ACCESS] DeleteComplexMarketData: Delete one or more items of complex market data, assuming they are present.
*ComplexMarketDataApi* | [**get_complex_market_data**](docs/ComplexMarketDataApi.md#get_complex_market_data) | **POST** /api/complexmarketdata/{scope}/$get | [EARLY ACCESS] GetComplexMarketData: Get complex market data
*ComplexMarketDataApi* | [**list_complex_market_data**](docs/ComplexMarketDataApi.md#list_complex_market_data) | **GET** /api/complexmarketdata | [EXPERIMENTAL] ListComplexMarketData: List the set of ComplexMarketData
*ComplexMarketDataApi* | [**upsert_complex_market_data**](docs/ComplexMarketDataApi.md#upsert_complex_market_data) | **POST** /api/complexmarketdata/{scope} | [EARLY ACCESS] UpsertComplexMarketData: Upsert a set of complex market data items. This creates or updates the data in Lusid.
*ComplianceApi* | [**get_compliance_run**](docs/ComplianceApi.md#get_compliance_run) | **GET** /api/compliance/{runId} | [EXPERIMENTAL] GetComplianceRun: Get the details of a single compliance run.
*ComplianceApi* | [**list_compliance_runs**](docs/ComplianceApi.md#list_compliance_runs) | **GET** /api/compliance | [EXPERIMENTAL] ListComplianceRuns: List historical compliance runs.
*ComplianceApi* | [**run_compliance_check**](docs/ComplianceApi.md#run_compliance_check) | **POST** /api/compliance/run | [EXPERIMENTAL] RunComplianceCheck: Kick off the compliance check process
*ConfigurationRecipeApi* | [**delete_configuration_recipe**](docs/ConfigurationRecipeApi.md#delete_configuration_recipe) | **DELETE** /api/recipes/{scope}/{code} | [EXPERIMENTAL] DeleteConfigurationRecipe: Delete a Configuration Recipe, assuming that it is present.
*ConfigurationRecipeApi* | [**get_configuration_recipe**](docs/ConfigurationRecipeApi.md#get_configuration_recipe) | **GET** /api/recipes/{scope}/{code} | [EXPERIMENTAL] GetConfigurationRecipe: Get Configuration Recipe
*ConfigurationRecipeApi* | [**list_configuration_recipes**](docs/ConfigurationRecipeApi.md#list_configuration_recipes) | **GET** /api/recipes | [EXPERIMENTAL] ListConfigurationRecipes: List the set of Configuration Recipes
*ConfigurationRecipeApi* | [**upsert_configuration_recipe**](docs/ConfigurationRecipeApi.md#upsert_configuration_recipe) | **POST** /api/recipes | [EXPERIMENTAL] UpsertConfigurationRecipe: Upsert a Configuration Recipe. This creates or updates the data in Lusid.
*ConventionsApi* | [**delete_cds_flow_conventions**](docs/ConventionsApi.md#delete_cds_flow_conventions) | **DELETE** /api/conventions/credit/conventions/{scope}/{code} | [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
*ConventionsApi* | [**delete_flow_conventions**](docs/ConventionsApi.md#delete_flow_conventions) | **DELETE** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
*ConventionsApi* | [**delete_index_convention**](docs/ConventionsApi.md#delete_index_convention) | **DELETE** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
*ConventionsApi* | [**get_cds_flow_conventions**](docs/ConventionsApi.md#get_cds_flow_conventions) | **GET** /api/conventions/credit/conventions/{scope}/{code} | [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
*ConventionsApi* | [**get_flow_conventions**](docs/ConventionsApi.md#get_flow_conventions) | **GET** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] GetFlowConventions: Get Flow Conventions
*ConventionsApi* | [**get_index_convention**](docs/ConventionsApi.md#get_index_convention) | **GET** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] GetIndexConvention: Get Index Convention
*ConventionsApi* | [**list_cds_flow_conventions**](docs/ConventionsApi.md#list_cds_flow_conventions) | **GET** /api/conventions/credit/conventions | [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
*ConventionsApi* | [**list_flow_conventions**](docs/ConventionsApi.md#list_flow_conventions) | **GET** /api/conventions/rates/flowconventions | [BETA] ListFlowConventions: List the set of Flow Conventions
*ConventionsApi* | [**list_index_convention**](docs/ConventionsApi.md#list_index_convention) | **GET** /api/conventions/rates/indexconventions | [BETA] ListIndexConvention: List the set of Index Conventions
*ConventionsApi* | [**upsert_cds_flow_conventions**](docs/ConventionsApi.md#upsert_cds_flow_conventions) | **POST** /api/conventions/credit/conventions | [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
*ConventionsApi* | [**upsert_flow_conventions**](docs/ConventionsApi.md#upsert_flow_conventions) | **POST** /api/conventions/rates/flowconventions | [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
*ConventionsApi* | [**upsert_index_convention**](docs/ConventionsApi.md#upsert_index_convention) | **POST** /api/conventions/rates/indexconventions | [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.
*CorporateActionSourcesApi* | [**batch_upsert_corporate_actions**](docs/CorporateActionSourcesApi.md#batch_upsert_corporate_actions) | **POST** /api/corporateactionsources/{scope}/{code}/corporateactions | [BETA] BatchUpsertCorporateActions: Upsert corporate actions
*CorporateActionSourcesApi* | [**create_corporate_action_source**](docs/CorporateActionSourcesApi.md#create_corporate_action_source) | **POST** /api/corporateactionsources | [BETA] CreateCorporateActionSource: Create corporate action source
*CorporateActionSourcesApi* | [**delete_corporate_action_source**](docs/CorporateActionSourcesApi.md#delete_corporate_action_source) | **DELETE** /api/corporateactionsources/{scope}/{code} | [BETA] DeleteCorporateActionSource: Delete a corporate action source
*CorporateActionSourcesApi* | [**delete_corporate_actions**](docs/CorporateActionSourcesApi.md#delete_corporate_actions) | **DELETE** /api/corporateactionsources/{scope}/{code}/corporateactions | [EXPERIMENTAL] DeleteCorporateActions: Delete corporate actions
*CorporateActionSourcesApi* | [**get_corporate_actions**](docs/CorporateActionSourcesApi.md#get_corporate_actions) | **GET** /api/corporateactionsources/{scope}/{code}/corporateactions | [BETA] GetCorporateActions: Get corporate actions
*CorporateActionSourcesApi* | [**list_corporate_action_sources**](docs/CorporateActionSourcesApi.md#list_corporate_action_sources) | **GET** /api/corporateactionsources | [BETA] ListCorporateActionSources: List corporate action sources
*CounterpartiesApi* | [**delete_counterparty_agreement**](docs/CounterpartiesApi.md#delete_counterparty_agreement) | **DELETE** /api/counterparties/counterpartyagreements/{scope}/{code} | [EXPERIMENTAL] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
*CounterpartiesApi* | [**delete_credit_support_annex**](docs/CounterpartiesApi.md#delete_credit_support_annex) | **DELETE** /api/counterparties/creditsupportannexes/{scope}/{code} | [EXPERIMENTAL] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
*CounterpartiesApi* | [**get_counterparty_agreement**](docs/CounterpartiesApi.md#get_counterparty_agreement) | **GET** /api/counterparties/counterpartyagreements/{scope}/{code} | [EXPERIMENTAL] GetCounterpartyAgreement: Get Counterparty Agreement
*CounterpartiesApi* | [**get_credit_support_annex**](docs/CounterpartiesApi.md#get_credit_support_annex) | **GET** /api/counterparties/creditsupportannexes/{scope}/{code} | [EXPERIMENTAL] GetCreditSupportAnnex: Get Credit Support Annex
*CounterpartiesApi* | [**list_counterparty_agreements**](docs/CounterpartiesApi.md#list_counterparty_agreements) | **GET** /api/counterparties/counterpartyagreements | [EXPERIMENTAL] ListCounterpartyAgreements: List the set of Counterparty Agreements
*CounterpartiesApi* | [**list_credit_support_annexes**](docs/CounterpartiesApi.md#list_credit_support_annexes) | **GET** /api/counterparties/creditsupportannexes | [EXPERIMENTAL] ListCreditSupportAnnexes: List the set of Credit Support Annexes
*CounterpartiesApi* | [**upsert_counterparty_agreement**](docs/CounterpartiesApi.md#upsert_counterparty_agreement) | **POST** /api/counterparties/counterpartyagreements | [EXPERIMENTAL] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
*CounterpartiesApi* | [**upsert_credit_support_annex**](docs/CounterpartiesApi.md#upsert_credit_support_annex) | **POST** /api/counterparties/creditsupportannexes | [EXPERIMENTAL] UpsertCreditSupportAnnex: Upsert Credit Support Annex
*CustomEntitiesApi* | [**get_custom_entity**](docs/CustomEntitiesApi.md#get_custom_entity) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue} | [EXPERIMENTAL] GetCustomEntity: Get CustomEntity
*CustomEntitiesApi* | [**get_custom_entity_relationships**](docs/CustomEntitiesApi.md#get_custom_entity_relationships) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/relationships | [EXPERIMENTAL] GetCustomEntityRelationships: Get Relationships for Custom Entity
*CustomEntitiesApi* | [**list_custom_entities**](docs/CustomEntitiesApi.md#list_custom_entities) | **GET** /api/customentities/{entityType} | [EXPERIMENTAL] ListCustomEntities: List Custom Entities
*CustomEntitiesApi* | [**upsert_custom_entity**](docs/CustomEntitiesApi.md#upsert_custom_entity) | **POST** /api/customentities/{entityType} | [EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity
*CustomEntityDefinitionsApi* | [**create_custom_entity_definition**](docs/CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **POST** /api/customentities/entitytypes | [EXPERIMENTAL] CreateCustomEntityDefinition: Create a new CustomEntityDefinition
*CustomEntityDefinitionsApi* | [**get_definition**](docs/CustomEntityDefinitionsApi.md#get_definition) | **GET** /api/customentities/entitytypes/{entityType} | [EXPERIMENTAL] GetDefinition: Get CustomEntityDefinition
*CutLabelDefinitionsApi* | [**create_cut_label_definition**](docs/CutLabelDefinitionsApi.md#create_cut_label_definition) | **POST** /api/systemconfiguration/cutlabels | [EARLY ACCESS] CreateCutLabelDefinition: Create a Cut Label
*CutLabelDefinitionsApi* | [**delete_cut_label_definition**](docs/CutLabelDefinitionsApi.md#delete_cut_label_definition) | **DELETE** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] DeleteCutLabelDefinition: Delete a Cut Label
*CutLabelDefinitionsApi* | [**get_cut_label_definition**](docs/CutLabelDefinitionsApi.md#get_cut_label_definition) | **GET** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] GetCutLabelDefinition: Get a Cut Label
*CutLabelDefinitionsApi* | [**list_cut_label_definitions**](docs/CutLabelDefinitionsApi.md#list_cut_label_definitions) | **GET** /api/systemconfiguration/cutlabels | [EARLY ACCESS] ListCutLabelDefinitions: List Existing Cut Labels
*CutLabelDefinitionsApi* | [**update_cut_label_definition**](docs/CutLabelDefinitionsApi.md#update_cut_label_definition) | **PUT** /api/systemconfiguration/cutlabels/{code} | [EARLY ACCESS] UpdateCutLabelDefinition: Update a Cut Label
*DataTypesApi* | [**create_data_type**](docs/DataTypesApi.md#create_data_type) | **POST** /api/datatypes | [BETA] CreateDataType: Create data type definition
*DataTypesApi* | [**get_data_type**](docs/DataTypesApi.md#get_data_type) | **GET** /api/datatypes/{scope}/{code} | [EARLY ACCESS] GetDataType: Get data type definition
*DataTypesApi* | [**get_units_from_data_type**](docs/DataTypesApi.md#get_units_from_data_type) | **GET** /api/datatypes/{scope}/{code}/units | [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
*DataTypesApi* | [**list_data_type_summaries**](docs/DataTypesApi.md#list_data_type_summaries) | **GET** /api/datatypes | [EXPERIMENTAL] ListDataTypeSummaries: List all data type summaries, without the reference data
*DataTypesApi* | [**list_data_types**](docs/DataTypesApi.md#list_data_types) | **GET** /api/datatypes/{scope} | [EARLY ACCESS] ListDataTypes: List data types
*DataTypesApi* | [**update_data_type**](docs/DataTypesApi.md#update_data_type) | **PUT** /api/datatypes/{scope}/{code} | [EXPERIMENTAL] UpdateDataType: Update data type definition
*DataTypesApi* | [**update_reference_values**](docs/DataTypesApi.md#update_reference_values) | **PUT** /api/datatypes/{scope}/{code}/referencedatavalues | [EXPERIMENTAL] UpdateReferenceValues: Update reference data on a data type
*DerivedTransactionPortfoliosApi* | [**create_derived_portfolio**](docs/DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/derivedtransactionportfolios/{scope} | [EARLY ACCESS] CreateDerivedPortfolio: Create derived portfolio
*DerivedTransactionPortfoliosApi* | [**delete_derived_portfolio_details**](docs/DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details
*EntitiesApi* | [**get_portfolio_changes**](docs/EntitiesApi.md#get_portfolio_changes) | **GET** /api/entities/changes/portfolios | [EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.
*ExecutionsApi* | [**delete_execution**](docs/ExecutionsApi.md#delete_execution) | **DELETE** /api/executions/{scope}/{code} | [EXPERIMENTAL] DeleteExecution: Delete execution
*ExecutionsApi* | [**get_execution**](docs/ExecutionsApi.md#get_execution) | **GET** /api/executions/{scope}/{code} | [EXPERIMENTAL] GetExecution: Get Execution
*ExecutionsApi* | [**list_executions**](docs/ExecutionsApi.md#list_executions) | **GET** /api/executions | [EXPERIMENTAL] ListExecutions: List Executions
*ExecutionsApi* | [**upsert_executions**](docs/ExecutionsApi.md#upsert_executions) | **POST** /api/executions | [EXPERIMENTAL] UpsertExecutions: Upsert Execution
*FeesAndCommissionsApi* | [**get_applicable_fees**](docs/FeesAndCommissionsApi.md#get_applicable_fees) | **GET** /api/feesandcommissions | [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
*FeesAndCommissionsApi* | [**list_all_fees**](docs/FeesAndCommissionsApi.md#list_all_fees) | **GET** /api/feesandcommissions/rules | [EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.
*InstrumentsApi* | [**delete_instrument**](docs/InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] DeleteInstrument: Delete instrument
*InstrumentsApi* | [**delete_instrument_properties**](docs/InstrumentsApi.md#delete_instrument_properties) | **POST** /api/instruments/{identifierType}/{identifier}/properties/$delete | [EXPERIMENTAL] DeleteInstrumentProperties: Delete instrument properties
*InstrumentsApi* | [**get_instrument**](docs/InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | GetInstrument: Get instrument
*InstrumentsApi* | [**get_instrument_identifier_types**](docs/InstrumentsApi.md#get_instrument_identifier_types) | **GET** /api/instruments/identifierTypes | [EARLY ACCESS] GetInstrumentIdentifierTypes: Get instrument identifier types
*InstrumentsApi* | [**get_instrument_properties**](docs/InstrumentsApi.md#get_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties | [EXPERIMENTAL] GetInstrumentProperties: Get instrument properties
*InstrumentsApi* | [**get_instrument_property_time_series**](docs/InstrumentsApi.md#get_instrument_property_time_series) | **GET** /api/instruments/{identifierType}/{identifier}/properties/time-series | [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
*InstrumentsApi* | [**get_instruments**](docs/InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | GetInstruments: Get instruments
*InstrumentsApi* | [**list_instrument_properties**](docs/InstrumentsApi.md#list_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties/list | [EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)
*InstrumentsApi* | [**list_instruments**](docs/InstrumentsApi.md#list_instruments) | **GET** /api/instruments | [EARLY ACCESS] ListInstruments: List instruments
*InstrumentsApi* | [**update_instrument_identifier**](docs/InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] UpdateInstrumentIdentifier: Update instrument identifier
*InstrumentsApi* | [**upsert_instruments**](docs/InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | UpsertInstruments: Upsert instruments
*InstrumentsApi* | [**upsert_instruments_properties**](docs/InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | UpsertInstrumentsProperties: Upsert instruments properties
*LegalEntitiesApi* | [**delete_legal_entity**](docs/LegalEntitiesApi.md#delete_legal_entity) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] DeleteLegalEntity: Delete Legal Entity
*LegalEntitiesApi* | [**delete_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#delete_legal_entity_access_metadata) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteLegalEntityAccessMetadata: Delete a Legal Entity Access Metadata entry
*LegalEntitiesApi* | [**delete_legal_entity_identifiers**](docs/LegalEntitiesApi.md#delete_legal_entity_identifiers) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] DeleteLegalEntityIdentifiers: Delete Legal Entity Identifiers
*LegalEntitiesApi* | [**delete_legal_entity_properties**](docs/LegalEntitiesApi.md#delete_legal_entity_properties) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] DeleteLegalEntityProperties: Delete Legal Entity Properties
*LegalEntitiesApi* | [**get_all_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#get_all_legal_entity_access_metadata) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllLegalEntityAccessMetadata: Get Access Metadata rules for a Legal Entity
*LegalEntitiesApi* | [**get_legal_entity**](docs/LegalEntitiesApi.md#get_legal_entity) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EARLY ACCESS] GetLegalEntity: Get Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_access_metadata_by_key**](docs/LegalEntitiesApi.md#get_legal_entity_access_metadata_by_key) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetLegalEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_property_time_series**](docs/LegalEntitiesApi.md#get_legal_entity_property_time_series) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EXPERIMENTAL] GetLegalEntityPropertyTimeSeries: Get Legal Entity Property Time Series
*LegalEntitiesApi* | [**get_legal_entity_relations**](docs/LegalEntitiesApi.md#get_legal_entity_relations) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relations | [EXPERIMENTAL] GetLegalEntityRelations: Get Relations for Legal Entity
*LegalEntitiesApi* | [**get_legal_entity_relationships**](docs/LegalEntitiesApi.md#get_legal_entity_relationships) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/relationships | [EXPERIMENTAL] GetLegalEntityRelationships: Get Relationships for Legal Entity
*LegalEntitiesApi* | [**list_legal_entities**](docs/LegalEntitiesApi.md#list_legal_entities) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode} | [EARLY ACCESS] ListLegalEntities: List Legal Entities
*LegalEntitiesApi* | [**set_legal_entity_identifiers**](docs/LegalEntitiesApi.md#set_legal_entity_identifiers) | **POST** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] SetLegalEntityIdentifiers: Set Legal Entity Identifiers
*LegalEntitiesApi* | [**upsert_legal_entity**](docs/LegalEntitiesApi.md#upsert_legal_entity) | **POST** /api/legalentities | [EARLY ACCESS] UpsertLegalEntity: Upsert Legal Entity
*LegalEntitiesApi* | [**upsert_legal_entity_access_metadata**](docs/LegalEntitiesApi.md#upsert_legal_entity_access_metadata) | **PUT** /api/legalentities/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertLegalEntityAccessMetadata: Upsert a Legal Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*OrderGraphApi* | [**list_order_graph_blocks**](docs/OrderGraphApi.md#list_order_graph_blocks) | **GET** /api/ordergraph/blocks | [EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
*OrderGraphApi* | [**list_order_graph_placements**](docs/OrderGraphApi.md#list_order_graph_placements) | **GET** /api/ordergraph/placements | [EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.
*OrderInstructionsApi* | [**delete_order_instruction**](docs/OrderInstructionsApi.md#delete_order_instruction) | **DELETE** /api/orderinstructions/{scope}/{code} | [EXPERIMENTAL] DeleteOrderInstruction: Delete orderInstruction
*OrderInstructionsApi* | [**get_order_instruction**](docs/OrderInstructionsApi.md#get_order_instruction) | **GET** /api/orderinstructions/{scope}/{code} | [EXPERIMENTAL] GetOrderInstruction: Get OrderInstruction
*OrderInstructionsApi* | [**list_order_instructions**](docs/OrderInstructionsApi.md#list_order_instructions) | **GET** /api/orderinstructions | [EXPERIMENTAL] ListOrderInstructions: List OrderInstructions
*OrderInstructionsApi* | [**upsert_order_instructions**](docs/OrderInstructionsApi.md#upsert_order_instructions) | **POST** /api/orderinstructions | [EXPERIMENTAL] UpsertOrderInstructions: Upsert OrderInstruction
*OrdersApi* | [**delete_order**](docs/OrdersApi.md#delete_order) | **DELETE** /api/orders/{scope}/{code} | [EARLY ACCESS] DeleteOrder: Delete order
*OrdersApi* | [**get_order**](docs/OrdersApi.md#get_order) | **GET** /api/orders/{scope}/{code} | [EARLY ACCESS] GetOrder: Get Order
*OrdersApi* | [**list_orders**](docs/OrdersApi.md#list_orders) | **GET** /api/orders | [EARLY ACCESS] ListOrders: List Orders
*OrdersApi* | [**upsert_orders**](docs/OrdersApi.md#upsert_orders) | **POST** /api/orders | [EARLY ACCESS] UpsertOrders: Upsert Order
*PackagesApi* | [**delete_package**](docs/PackagesApi.md#delete_package) | **DELETE** /api/packages/{scope}/{code} | [EXPERIMENTAL] DeletePackage: Delete package
*PackagesApi* | [**get_package**](docs/PackagesApi.md#get_package) | **GET** /api/packages/{scope}/{code} | [EXPERIMENTAL] GetPackage: Get Package
*PackagesApi* | [**list_packages**](docs/PackagesApi.md#list_packages) | **GET** /api/packages | [EXPERIMENTAL] ListPackages: List Packages
*PackagesApi* | [**upsert_packages**](docs/PackagesApi.md#upsert_packages) | **POST** /api/packages | [EXPERIMENTAL] UpsertPackages: Upsert Package
*ParticipationsApi* | [**delete_participation**](docs/ParticipationsApi.md#delete_participation) | **DELETE** /api/participations/{scope}/{code} | [EXPERIMENTAL] DeleteParticipation: Delete participation
*ParticipationsApi* | [**get_participation**](docs/ParticipationsApi.md#get_participation) | **GET** /api/participations/{scope}/{code} | [EXPERIMENTAL] GetParticipation: Get Participation
*ParticipationsApi* | [**list_participations**](docs/ParticipationsApi.md#list_participations) | **GET** /api/participations | [EXPERIMENTAL] ListParticipations: List Participations
*ParticipationsApi* | [**upsert_participations**](docs/ParticipationsApi.md#upsert_participations) | **POST** /api/participations | [EXPERIMENTAL] UpsertParticipations: Upsert Participation
*PersonsApi* | [**delete_person**](docs/PersonsApi.md#delete_person) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] DeletePerson: Delete person
*PersonsApi* | [**delete_person_access_metadata**](docs/PersonsApi.md#delete_person_access_metadata) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeletePersonAccessMetadata: Delete a Person Access Metadata entry
*PersonsApi* | [**delete_person_identifiers**](docs/PersonsApi.md#delete_person_identifiers) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] DeletePersonIdentifiers: Delete Person Identifiers
*PersonsApi* | [**delete_person_properties**](docs/PersonsApi.md#delete_person_properties) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] DeletePersonProperties: Delete Person Properties
*PersonsApi* | [**get_all_person_access_metadata**](docs/PersonsApi.md#get_all_person_access_metadata) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EARLY ACCESS] GetAllPersonAccessMetadata: Get Access Metadata rules for a Person
*PersonsApi* | [**get_person**](docs/PersonsApi.md#get_person) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] GetPerson: Get Person
*PersonsApi* | [**get_person_access_metadata_by_key**](docs/PersonsApi.md#get_person_access_metadata_by_key) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPersonAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Person
*PersonsApi* | [**get_person_property_time_series**](docs/PersonsApi.md#get_person_property_time_series) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EXPERIMENTAL] GetPersonPropertyTimeSeries: Get Person Property Time Series
*PersonsApi* | [**get_person_relations**](docs/PersonsApi.md#get_person_relations) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [EXPERIMENTAL] GetPersonRelations: Get Relations for Person
*PersonsApi* | [**get_person_relationships**](docs/PersonsApi.md#get_person_relationships) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relationships | [EXPERIMENTAL] GetPersonRelationships: Get Relationships for Person
*PersonsApi* | [**list_persons**](docs/PersonsApi.md#list_persons) | **GET** /api/persons/{idTypeScope}/{idTypeCode} | [EXPERIMENTAL] ListPersons: List Persons
*PersonsApi* | [**set_person_identifiers**](docs/PersonsApi.md#set_person_identifiers) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] SetPersonIdentifiers: Set Person Identifiers
*PersonsApi* | [**set_person_properties**](docs/PersonsApi.md#set_person_properties) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] SetPersonProperties: Set Person Properties
*PersonsApi* | [**upsert_person**](docs/PersonsApi.md#upsert_person) | **POST** /api/persons | [EXPERIMENTAL] UpsertPerson: Upsert Person
*PersonsApi* | [**upsert_person_access_metadata**](docs/PersonsApi.md#upsert_person_access_metadata) | **PUT** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPersonAccessMetadata: Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*PlacementsApi* | [**delete_placement**](docs/PlacementsApi.md#delete_placement) | **DELETE** /api/placements/{scope}/{code} | [EXPERIMENTAL] DeletePlacement: Delete placement
*PlacementsApi* | [**get_placement**](docs/PlacementsApi.md#get_placement) | **GET** /api/placements/{scope}/{code} | [EXPERIMENTAL] GetPlacement: Get Placement
*PlacementsApi* | [**list_placements**](docs/PlacementsApi.md#list_placements) | **GET** /api/placements | [EXPERIMENTAL] ListPlacements: List Placements
*PlacementsApi* | [**upsert_placements**](docs/PlacementsApi.md#upsert_placements) | **POST** /api/placements | [EXPERIMENTAL] UpsertPlacements: Upsert Placement
*PortfolioGroupsApi* | [**add_portfolio_to_group**](docs/PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group
*PortfolioGroupsApi* | [**add_sub_group_to_group**](docs/PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] AddSubGroupToGroup: Add sub group to group
*PortfolioGroupsApi* | [**build_transactions_for_portfolio_group**](docs/PortfolioGroupsApi.md#build_transactions_for_portfolio_group) | **POST** /api/portfoliogroups/{scope}/{code}/transactions/$build | [EARLY ACCESS] BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group
*PortfolioGroupsApi* | [**create_portfolio_group**](docs/PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/portfoliogroups/{scope} | [EARLY ACCESS] CreatePortfolioGroup: Create portfolio group
*PortfolioGroupsApi* | [**delete_group_properties**](docs/PortfolioGroupsApi.md#delete_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeleteGroupProperties: Delete group properties
*PortfolioGroupsApi* | [**delete_key_from_portfolio_group_access_metadata**](docs/PortfolioGroupsApi.md#delete_key_from_portfolio_group_access_metadata) | **DELETE** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry
*PortfolioGroupsApi* | [**delete_portfolio_from_group**](docs/PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group
*PortfolioGroupsApi* | [**delete_portfolio_group**](docs/PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group
*PortfolioGroupsApi* | [**delete_sub_group_from_group**](docs/PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group
*PortfolioGroupsApi* | [**get_a2_b_data_for_portfolio_group**](docs/PortfolioGroupsApi.md#get_a2_b_data_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/a2b | [EXPERIMENTAL] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group
*PortfolioGroupsApi* | [**get_group_properties**](docs/PortfolioGroupsApi.md#get_group_properties) | **GET** /api/portfoliogroups/{scope}/{code}/properties | [EARLY ACCESS] GetGroupProperties: Get group properties
*PortfolioGroupsApi* | [**get_holdings_for_portfolio_group**](docs/PortfolioGroupsApi.md#get_holdings_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/holdings | [EARLY ACCESS] GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group**](docs/PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] GetPortfolioGroup: Get portfolio group
*PortfolioGroupsApi* | [**get_portfolio_group_access_metadata_by_key**](docs/PortfolioGroupsApi.md#get_portfolio_group_access_metadata_by_key) | **GET** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_commands**](docs/PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/portfoliogroups/{scope}/{code}/commands | [EARLY ACCESS] GetPortfolioGroupCommands: Get portfolio group commands
*PortfolioGroupsApi* | [**get_portfolio_group_expansion**](docs/PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion
*PortfolioGroupsApi* | [**get_portfolio_group_metadata**](docs/PortfolioGroupsApi.md#get_portfolio_group_metadata) | **GET** /api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_property_time_series**](docs/PortfolioGroupsApi.md#get_portfolio_group_property_time_series) | **GET** /api/portfoliogroups/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property
*PortfolioGroupsApi* | [**get_portfolio_group_relations**](docs/PortfolioGroupsApi.md#get_portfolio_group_relations) | **GET** /api/portfoliogroups/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group
*PortfolioGroupsApi* | [**get_portfolio_group_relationships**](docs/PortfolioGroupsApi.md#get_portfolio_group_relationships) | **GET** /api/portfoliogroups/{scope}/{code}/relationships | [EXPERIMENTAL] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group
*PortfolioGroupsApi* | [**get_transactions_for_portfolio_group**](docs/PortfolioGroupsApi.md#get_transactions_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/transactions | [EARLY ACCESS] GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group
*PortfolioGroupsApi* | [**list_portfolio_groups**](docs/PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/portfoliogroups/{scope} | [EARLY ACCESS] ListPortfolioGroups: List portfolio groups
*PortfolioGroupsApi* | [**update_portfolio_group**](docs/PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group
*PortfolioGroupsApi* | [**upsert_group_properties**](docs/PortfolioGroupsApi.md#upsert_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertGroupProperties: Upsert group properties
*PortfolioGroupsApi* | [**upsert_portfolio_group_access_metadata**](docs/PortfolioGroupsApi.md#upsert_portfolio_group_access_metadata) | **PUT** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
*PortfoliosApi* | [**delete_key_from_portfolio_access_metadata**](docs/PortfoliosApi.md#delete_key_from_portfolio_access_metadata) | **DELETE** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule
*PortfoliosApi* | [**delete_portfolio**](docs/PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | DeletePortfolio: Delete portfolio
*PortfoliosApi* | [**delete_portfolio_properties**](docs/PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | DeletePortfolioProperties: Delete portfolio properties
*PortfoliosApi* | [**delete_portfolio_returns**](docs/PortfoliosApi.md#delete_portfolio_returns) | **DELETE** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$delete | [EARLY ACCESS] DeletePortfolioReturns: Delete Returns
*PortfoliosApi* | [**get_portfolio**](docs/PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | GetPortfolio: Get portfolio
*PortfoliosApi* | [**get_portfolio_aggregate_returns**](docs/PortfoliosApi.md#get_portfolio_aggregate_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/aggregated | [EXPERIMENTAL] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).
*PortfoliosApi* | [**get_portfolio_aggregated_returns**](docs/PortfoliosApi.md#get_portfolio_aggregated_returns) | **POST** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$aggregated | [EARLY ACCESS] GetPortfolioAggregatedReturns: Aggregated Returns
*PortfoliosApi* | [**get_portfolio_commands**](docs/PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | [EARLY ACCESS] GetPortfolioCommands: Get portfolio commands
*PortfoliosApi* | [**get_portfolio_metadata**](docs/PortfoliosApi.md#get_portfolio_metadata) | **GET** /api/portfolios/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioMetadata: Get access metadata rules for a portfolio
*PortfoliosApi* | [**get_portfolio_properties**](docs/PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | GetPortfolioProperties: Get portfolio properties
*PortfoliosApi* | [**get_portfolio_property_time_series**](docs/PortfoliosApi.md#get_portfolio_property_time_series) | **GET** /api/portfolios/{scope}/{code}/properties/time-series | [EXPERIMENTAL] GetPortfolioPropertyTimeSeries: Get portfolio property time series
*PortfoliosApi* | [**get_portfolio_relations**](docs/PortfoliosApi.md#get_portfolio_relations) | **GET** /api/portfolios/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations
*PortfoliosApi* | [**get_portfolio_relationships**](docs/PortfoliosApi.md#get_portfolio_relationships) | **GET** /api/portfolios/{scope}/{code}/relationships | [EXPERIMENTAL] GetPortfolioRelationships: Get portfolio relationships
*PortfoliosApi* | [**get_portfolio_returns**](docs/PortfoliosApi.md#get_portfolio_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] GetPortfolioReturns: Get Returns
*PortfoliosApi* | [**get_portfolios_access_metadata_by_key**](docs/PortfoliosApi.md#get_portfolios_access_metadata_by_key) | **GET** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object
*PortfoliosApi* | [**list_portfolio_properties**](docs/PortfoliosApi.md#list_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties/list | [EXPERIMENTAL] ListPortfolioProperties: Get portfolio properties
*PortfoliosApi* | [**list_portfolios**](docs/PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | ListPortfolios: List portfolios
*PortfoliosApi* | [**list_portfolios_for_scope**](docs/PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | ListPortfoliosForScope: List portfolios for scope
*PortfoliosApi* | [**update_portfolio**](docs/PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | UpdatePortfolio: Update portfolio
*PortfoliosApi* | [**upsert_portfolio_access_metadata**](docs/PortfoliosApi.md#upsert_portfolio_access_metadata) | **PUT** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
*PortfoliosApi* | [**upsert_portfolio_properties**](docs/PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | UpsertPortfolioProperties: Upsert portfolio properties
*PortfoliosApi* | [**upsert_portfolio_returns**](docs/PortfoliosApi.md#upsert_portfolio_returns) | **POST** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] UpsertPortfolioReturns: Upsert Returns
*PropertyDefinitionsApi* | [**create_derived_property_definition**](docs/PropertyDefinitionsApi.md#create_derived_property_definition) | **POST** /api/propertydefinitions/derived | [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
*PropertyDefinitionsApi* | [**create_property_definition**](docs/PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/propertydefinitions | CreatePropertyDefinition: Create property definition
*PropertyDefinitionsApi* | [**delete_property_definition**](docs/PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/propertydefinitions/{domain}/{scope}/{code} | DeletePropertyDefinition: Delete property definition
*PropertyDefinitionsApi* | [**get_multiple_property_definitions**](docs/PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/propertydefinitions | GetMultiplePropertyDefinitions: Get multiple property definitions
*PropertyDefinitionsApi* | [**get_property_definition**](docs/PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/propertydefinitions/{domain}/{scope}/{code} | GetPropertyDefinition: Get property definition
*PropertyDefinitionsApi* | [**update_property_definition**](docs/PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/propertydefinitions/{domain}/{scope}/{code} | UpdatePropertyDefinition: Update property definition
*QuotesApi* | [**delete_quote_access_metadata_rule**](docs/QuotesApi.md#delete_quote_access_metadata_rule) | **DELETE** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] DeleteQuoteAccessMetadataRule: Delete a Quote Access Metadata Rule
*QuotesApi* | [**delete_quotes**](docs/QuotesApi.md#delete_quotes) | **POST** /api/quotes/{scope}/$delete | [EARLY ACCESS] DeleteQuotes: Delete quotes
*QuotesApi* | [**get_quotes**](docs/QuotesApi.md#get_quotes) | **POST** /api/quotes/{scope}/$get | [EARLY ACCESS] GetQuotes: Get quotes
*QuotesApi* | [**get_quotes_access_metadata_rule**](docs/QuotesApi.md#get_quotes_access_metadata_rule) | **GET** /api/metadata/quotes/rules | [EXPERIMENTAL] GetQuotesAccessMetadataRule: Get a quote access metadata rule
*QuotesApi* | [**list_quotes**](docs/QuotesApi.md#list_quotes) | **GET** /api/quotes/{scope}/$deprecated | [DEPRECATED] ListQuotes: List quotes
*QuotesApi* | [**list_quotes_access_metadata_rules**](docs/QuotesApi.md#list_quotes_access_metadata_rules) | **GET** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] ListQuotesAccessMetadataRules: List all quote access metadata rules in a scope
*QuotesApi* | [**list_quotes_for_scope**](docs/QuotesApi.md#list_quotes_for_scope) | **GET** /api/quotes/{scope} | [EARLY ACCESS] ListQuotesForScope: List quotes for scope
*QuotesApi* | [**upsert_quote_access_metadata_rule**](docs/QuotesApi.md#upsert_quote_access_metadata_rule) | **POST** /api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] UpsertQuoteAccessMetadataRule: Upsert a Quote Access Metadata Rule. This creates or updates the data in LUSID.
*QuotesApi* | [**upsert_quotes**](docs/QuotesApi.md#upsert_quotes) | **POST** /api/quotes/{scope} | [EARLY ACCESS] UpsertQuotes: Upsert quotes
*ReconciliationsApi* | [**reconcile_generic**](docs/ReconciliationsApi.md#reconcile_generic) | **POST** /api/portfolios/$reconcileGeneric | [EXPERIMENTAL] ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are &#x27;empty&#x27; or null or zero.
*ReconciliationsApi* | [**reconcile_holdings**](docs/ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
*ReconciliationsApi* | [**reconcile_holdings_preview**](docs/ReconciliationsApi.md#reconcile_holdings_preview) | **POST** /api/portfolios/preview/$reconcileholdings | [EXPERIMENTAL] ReconcileHoldingsPreview: Reconcile portfolio holdings with given tolerance
*ReconciliationsApi* | [**reconcile_inline**](docs/ReconciliationsApi.md#reconcile_inline) | **POST** /api/portfolios/$reconcileInline | [BETA] ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
*ReconciliationsApi* | [**reconcile_valuation**](docs/ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | [BETA] ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
*ReferencePortfolioApi* | [**create_reference_portfolio**](docs/ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/referenceportfolios/{scope} | CreateReferencePortfolio: Create reference portfolio
*ReferencePortfolioApi* | [**get_reference_portfolio_constituents**](docs/ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/referenceportfolios/{scope}/{code}/constituents | GetReferencePortfolioConstituents: Get reference portfolio constituents
*ReferencePortfolioApi* | [**list_constituents_adjustments**](docs/ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/referenceportfolios/{scope}/{code}/constituentsadjustments | ListConstituentsAdjustments: List constituents adjustments
*ReferencePortfolioApi* | [**upsert_reference_portfolio_constituents**](docs/ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/referenceportfolios/{scope}/{code}/constituents | UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents
*RelationDefinitionsApi* | [**create_relation_definition**](docs/RelationDefinitionsApi.md#create_relation_definition) | **POST** /api/relationdefinitions | [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
*RelationDefinitionsApi* | [**get_relation_definition**](docs/RelationDefinitionsApi.md#get_relation_definition) | **GET** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationDefinition: Get relation definition
*RelationsApi* | [**create_relation**](docs/RelationsApi.md#create_relation) | **POST** /api/relations/{scope}/{code} | [EXPERIMENTAL] CreateRelation: Create Relation
*RelationsApi* | [**delete_relation**](docs/RelationsApi.md#delete_relation) | **POST** /api/relations/{scope}/{code}/$delete | [EXPERIMENTAL] DeleteRelation: Delete a relation
*RelationshipDefinitionsApi* | [**create_relationship_definition**](docs/RelationshipDefinitionsApi.md#create_relationship_definition) | **POST** /api/relationshipdefinitions | [EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition
*RelationshipDefinitionsApi* | [**get_relationship_definition**](docs/RelationshipDefinitionsApi.md#get_relationship_definition) | **GET** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
*RelationshipDefinitionsApi* | [**list_relationship_definitions**](docs/RelationshipDefinitionsApi.md#list_relationship_definitions) | **GET** /api/relationshipdefinitions | [EXPERIMENTAL] ListRelationshipDefinitions: List relationship definitions
*RelationshipDefinitionsApi* | [**update_relationship_definition**](docs/RelationshipDefinitionsApi.md#update_relationship_definition) | **PUT** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition
*RelationshipsApi* | [**create_relationship**](docs/RelationshipsApi.md#create_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships | [EXPERIMENTAL] CreateRelationship: Create Relationship
*RelationshipsApi* | [**delete_relationship**](docs/RelationshipsApi.md#delete_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EXPERIMENTAL] DeleteRelationship: Delete Relationship
*SchemasApi* | [**get_entity_schema**](docs/SchemasApi.md#get_entity_schema) | **GET** /api/schemas/entities/{entity} | [BETA] GetEntitySchema: Get schema
*SchemasApi* | [**get_property_schema**](docs/SchemasApi.md#get_property_schema) | **GET** /api/schemas/properties | [BETA] GetPropertySchema: Get property schema
*SchemasApi* | [**get_value_types**](docs/SchemasApi.md#get_value_types) | **GET** /api/schemas/types | [BETA] GetValueTypes: Get value types
*SchemasApi* | [**list_entities**](docs/SchemasApi.md#list_entities) | **GET** /api/schemas/entities | [BETA] ListEntities: List entities
*ScopesApi* | [**list_scopes**](docs/ScopesApi.md#list_scopes) | **GET** /api/scopes | [EARLY ACCESS] ListScopes: List Scopes
*SearchApi* | [**instruments_search**](docs/SearchApi.md#instruments_search) | **POST** /api/search/instruments | [EXPERIMENTAL] InstrumentsSearch: Instruments search
*SearchApi* | [**search_portfolio_groups**](docs/SearchApi.md#search_portfolio_groups) | **GET** /api/search/portfoliogroups | [EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups
*SearchApi* | [**search_portfolios**](docs/SearchApi.md#search_portfolios) | **GET** /api/search/portfolios | [EARLY ACCESS] SearchPortfolios: Search Portfolios
*SearchApi* | [**search_properties**](docs/SearchApi.md#search_properties) | **GET** /api/search/propertydefinitions | [EARLY ACCESS] SearchProperties: Search Property Definitions
*SequencesApi* | [**create_sequence**](docs/SequencesApi.md#create_sequence) | **POST** /api/sequences/{scope} | [EXPERIMENTAL] CreateSequence: Create a new sequence
*SequencesApi* | [**get_sequence**](docs/SequencesApi.md#get_sequence) | **GET** /api/sequences/{scope}/{code} | [EXPERIMENTAL] GetSequence: Get a specified sequence
*SequencesApi* | [**list_sequences**](docs/SequencesApi.md#list_sequences) | **GET** /api/sequences | [EXPERIMENTAL] ListSequences: List Sequences
*SequencesApi* | [**next**](docs/SequencesApi.md#next) | **GET** /api/sequences/{scope}/{code}/next | [EXPERIMENTAL] Next: Get next values from sequence
*StructuredResultDataApi* | [**create_data_map**](docs/StructuredResultDataApi.md#create_data_map) | **POST** /api/unitresults/datamap/{scope} | [EXPERIMENTAL] CreateDataMap: Create data map
*StructuredResultDataApi* | [**delete_structured_result_data**](docs/StructuredResultDataApi.md#delete_structured_result_data) | **POST** /api/unitresults/{scope}/$delete | [EXPERIMENTAL] DeleteStructuredResultData: Delete structured result data
*StructuredResultDataApi* | [**get_data_map**](docs/StructuredResultDataApi.md#get_data_map) | **POST** /api/unitresults/datamap/{scope}/$get | [EXPERIMENTAL] GetDataMap: Get data map
*StructuredResultDataApi* | [**get_structured_result_data**](docs/StructuredResultDataApi.md#get_structured_result_data) | **POST** /api/unitresults/{scope}/$get | [EXPERIMENTAL] GetStructuredResultData: Get structured result data
*StructuredResultDataApi* | [**get_virtual_document**](docs/StructuredResultDataApi.md#get_virtual_document) | **POST** /api/unitresults/virtualdocument/{scope}/$get | [EXPERIMENTAL] GetVirtualDocument: Get Virtual Documents
*StructuredResultDataApi* | [**upsert_structured_result_data**](docs/StructuredResultDataApi.md#upsert_structured_result_data) | **POST** /api/unitresults/{scope} | [BETA] UpsertStructuredResultData: Upsert structured result data
*SystemConfigurationApi* | [**create_configuration_transaction_type**](docs/SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactions/type | [EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type
*SystemConfigurationApi* | [**create_side_definition**](docs/SystemConfigurationApi.md#create_side_definition) | **POST** /api/systemconfiguration/transactions/side | [EXPERIMENTAL] CreateSideDefinition: Create side definition
*SystemConfigurationApi* | [**delete_transaction_configuration_source**](docs/SystemConfigurationApi.md#delete_transaction_configuration_source) | **DELETE** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source
*SystemConfigurationApi* | [**get_transaction_configuration_source**](docs/SystemConfigurationApi.md#get_transaction_configuration_source) | **GET** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source
*SystemConfigurationApi* | [**list_configuration_transaction_types**](docs/SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactions | [EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types
*SystemConfigurationApi* | [**set_configuration_transaction_types**](docs/SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactions | [EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types
*SystemConfigurationApi* | [**set_transaction_configuration_source**](docs/SystemConfigurationApi.md#set_transaction_configuration_source) | **PUT** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source
*TransactionPortfoliosApi* | [**adjust_holdings**](docs/TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings | AdjustHoldings: Adjust holdings
*TransactionPortfoliosApi* | [**build_transactions**](docs/TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | BuildTransactions: Build transactions
*TransactionPortfoliosApi* | [**cancel_adjust_holdings**](docs/TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings | CancelAdjustHoldings: Cancel adjust holdings
*TransactionPortfoliosApi* | [**cancel_transactions**](docs/TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | CancelTransactions: Cancel transactions
*TransactionPortfoliosApi* | [**create_portfolio**](docs/TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | CreatePortfolio: Create portfolio
*TransactionPortfoliosApi* | [**delete_properties_from_transaction**](docs/TransactionPortfoliosApi.md#delete_properties_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | DeletePropertiesFromTransaction: Delete properties from transaction
*TransactionPortfoliosApi* | [**get_a2_b_data**](docs/TransactionPortfoliosApi.md#get_a2_b_data) | **GET** /api/transactionportfolios/{scope}/{code}/a2b | [EXPERIMENTAL] GetA2BData: Get A2B data
*TransactionPortfoliosApi* | [**get_a2_b_movements**](docs/TransactionPortfoliosApi.md#get_a2_b_movements) | **GET** /api/transactionportfolios/{scope}/{code}/a2bmovements | [EXPERIMENTAL] GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
*TransactionPortfoliosApi* | [**get_bucketed_cash_flows**](docs/TransactionPortfoliosApi.md#get_bucketed_cash_flows) | **POST** /api/transactionportfolios/{scope}/{code}/bucketedCashFlows | [EXPERIMENTAL] GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
*TransactionPortfoliosApi* | [**get_details**](docs/TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | GetDetails: Get details
*TransactionPortfoliosApi* | [**get_holdings**](docs/TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | GetHoldings: Get holdings
*TransactionPortfoliosApi* | [**get_holdings_adjustment**](docs/TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | GetHoldingsAdjustment: Get holdings adjustment
*TransactionPortfoliosApi* | [**get_holdings_with_orders**](docs/TransactionPortfoliosApi.md#get_holdings_with_orders) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsWithOrders | [EXPERIMENTAL] GetHoldingsWithOrders: Get holdings with orders
*TransactionPortfoliosApi* | [**get_portfolio_cash_flows**](docs/TransactionPortfoliosApi.md#get_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/cashflows | [BETA] GetPortfolioCashFlows: Get portfolio cash flows
*TransactionPortfoliosApi* | [**get_portfolio_cash_ladder**](docs/TransactionPortfoliosApi.md#get_portfolio_cash_ladder) | **GET** /api/transactionportfolios/{scope}/{code}/cashladder | [EXPERIMENTAL] GetPortfolioCashLadder: Get portfolio cash ladder
*TransactionPortfoliosApi* | [**get_portfolio_cash_statement**](docs/TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **GET** /api/transactionportfolios/{scope}/{code}/cashstatement | [EARLY ACCESS] GetPortfolioCashStatement: Get portfolio cash statement
*TransactionPortfoliosApi* | [**get_transactions**](docs/TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | GetTransactions: Get transactions
*TransactionPortfoliosApi* | [**get_upsertable_portfolio_cash_flows**](docs/TransactionPortfoliosApi.md#get_upsertable_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/upsertablecashflows | [BETA] GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
*TransactionPortfoliosApi* | [**list_holdings_adjustments**](docs/TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | ListHoldingsAdjustments: List holdings adjustments
*TransactionPortfoliosApi* | [**patch_portfolio_details**](docs/TransactionPortfoliosApi.md#patch_portfolio_details) | **PATCH** /api/transactionportfolios/{scope}/{code}/details | [EXPERIMENTAL] PatchPortfolioDetails: Patch portfolio details
*TransactionPortfoliosApi* | [**resolve_instrument**](docs/TransactionPortfoliosApi.md#resolve_instrument) | **POST** /api/transactionportfolios/{scope}/{code}/$resolve | [EARLY ACCESS] ResolveInstrument: Resolve instrument
*TransactionPortfoliosApi* | [**set_holdings**](docs/TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings | SetHoldings: Set holdings
*TransactionPortfoliosApi* | [**upsert_portfolio_details**](docs/TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | UpsertPortfolioDetails: Upsert portfolio details
*TransactionPortfoliosApi* | [**upsert_transaction_properties**](docs/TransactionPortfoliosApi.md#upsert_transaction_properties) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | UpsertTransactionProperties: Upsert transaction properties
*TransactionPortfoliosApi* | [**upsert_transactions**](docs/TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | UpsertTransactions: Upsert transactions
*TranslationApi* | [**translate_instrument_definitions**](docs/TranslationApi.md#translate_instrument_definitions) | **POST** /api/translation/instrumentdefinitions | [EXPERIMENTAL] TranslateInstrumentDefinitions: Translate instruments

## Documentation For Models

 - [A2BBreakdown](docs/A2BBreakdown.md)
 - [A2BCategory](docs/A2BCategory.md)
 - [A2BDataRecord](docs/A2BDataRecord.md)
 - [A2BMovementRecord](docs/A2BMovementRecord.md)
 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [AccessMetadataValue](docs/AccessMetadataValue.md)
 - [AccountingMethod](docs/AccountingMethod.md)
 - [ActionId](docs/ActionId.md)
 - [AddBusinessDaysToDateRequest](docs/AddBusinessDaysToDateRequest.md)
 - [AddBusinessDaysToDateResponse](docs/AddBusinessDaysToDateResponse.md)
 - [AdjustHolding](docs/AdjustHolding.md)
 - [AdjustHoldingRequest](docs/AdjustHoldingRequest.md)
 - [AggregateSpec](docs/AggregateSpec.md)
 - [AggregatedReturn](docs/AggregatedReturn.md)
 - [AggregatedReturnsRequest](docs/AggregatedReturnsRequest.md)
 - [AggregationContext](docs/AggregationContext.md)
 - [AggregationMeasureFailureDetail](docs/AggregationMeasureFailureDetail.md)
 - [AggregationOp](docs/AggregationOp.md)
 - [AggregationOptions](docs/AggregationOptions.md)
 - [AggregationQuery](docs/AggregationQuery.md)
 - [AggregationType](docs/AggregationType.md)
 - [Allocation](docs/Allocation.md)
 - [AllocationRequest](docs/AllocationRequest.md)
 - [AllocationSetRequest](docs/AllocationSetRequest.md)
 - [AnnulQuotesResponse](docs/AnnulQuotesResponse.md)
 - [AnnulSingleStructuredDataResponse](docs/AnnulSingleStructuredDataResponse.md)
 - [AnnulStructuredDataResponse](docs/AnnulStructuredDataResponse.md)
 - [AssetClass](docs/AssetClass.md)
 - [AtomValue](docs/AtomValue.md)
 - [AtomValue0D](docs/AtomValue0D.md)
 - [AtomValue0DAllOf](docs/AtomValue0DAllOf.md)
 - [AtomValueDecimal](docs/AtomValueDecimal.md)
 - [AtomValueDecimalAllOf](docs/AtomValueDecimalAllOf.md)
 - [AtomValueInt](docs/AtomValueInt.md)
 - [AtomValueIntAllOf](docs/AtomValueIntAllOf.md)
 - [AtomValueString](docs/AtomValueString.md)
 - [AtomValueStringAllOf](docs/AtomValueStringAllOf.md)
 - [AtomValueType](docs/AtomValueType.md)
 - [Basket](docs/Basket.md)
 - [BasketAllOf](docs/BasketAllOf.md)
 - [BasketIdentifier](docs/BasketIdentifier.md)
 - [Block](docs/Block.md)
 - [BlockRequest](docs/BlockRequest.md)
 - [BlockSetRequest](docs/BlockSetRequest.md)
 - [Bond](docs/Bond.md)
 - [BondAllOf](docs/BondAllOf.md)
 - [BucketedCashFlowRequest](docs/BucketedCashFlowRequest.md)
 - [BucketedCashFlowResponse](docs/BucketedCashFlowResponse.md)
 - [CalculationInfo](docs/CalculationInfo.md)
 - [CalculationMethod](docs/CalculationMethod.md)
 - [Calendar](docs/Calendar.md)
 - [CalendarDate](docs/CalendarDate.md)
 - [CapFloor](docs/CapFloor.md)
 - [CapFloorAllOf](docs/CapFloorAllOf.md)
 - [CashLadderRecord](docs/CashLadderRecord.md)
 - [CashPerpetual](docs/CashPerpetual.md)
 - [CashPerpetualAllOf](docs/CashPerpetualAllOf.md)
 - [CdsFlowConventions](docs/CdsFlowConventions.md)
 - [CdsIndex](docs/CdsIndex.md)
 - [CdsIndexAllOf](docs/CdsIndexAllOf.md)
 - [CdsProtectionDetailSpecification](docs/CdsProtectionDetailSpecification.md)
 - [CdsRestructuringType](docs/CdsRestructuringType.md)
 - [CdsSeniority](docs/CdsSeniority.md)
 - [Change](docs/Change.md)
 - [CompletePortfolio](docs/CompletePortfolio.md)
 - [CompleteRelation](docs/CompleteRelation.md)
 - [CompleteRelationship](docs/CompleteRelationship.md)
 - [ComplexMarketData](docs/ComplexMarketData.md)
 - [ComplexMarketDataId](docs/ComplexMarketDataId.md)
 - [ComplianceRuleResult](docs/ComplianceRuleResult.md)
 - [ComplianceRun](docs/ComplianceRun.md)
 - [Compounding](docs/Compounding.md)
 - [ConfigurationRecipe](docs/ConfigurationRecipe.md)
 - [ConfigurationRecipeSnippet](docs/ConfigurationRecipeSnippet.md)
 - [ConstituentsAdjustmentHeader](docs/ConstituentsAdjustmentHeader.md)
 - [ContractForDifference](docs/ContractForDifference.md)
 - [ContractForDifferenceAllOf](docs/ContractForDifferenceAllOf.md)
 - [CorporateAction](docs/CorporateAction.md)
 - [CorporateActionSource](docs/CorporateActionSource.md)
 - [CorporateActionTransition](docs/CorporateActionTransition.md)
 - [CorporateActionTransitionComponent](docs/CorporateActionTransitionComponent.md)
 - [CorporateActionTransitionComponentRequest](docs/CorporateActionTransitionComponentRequest.md)
 - [CorporateActionTransitionRequest](docs/CorporateActionTransitionRequest.md)
 - [CounterpartyAgreement](docs/CounterpartyAgreement.md)
 - [CounterpartyRiskInformation](docs/CounterpartyRiskInformation.md)
 - [CounterpartySignatory](docs/CounterpartySignatory.md)
 - [CreateCalendarRequest](docs/CreateCalendarRequest.md)
 - [CreateCorporateActionSourceRequest](docs/CreateCorporateActionSourceRequest.md)
 - [CreateCutLabelDefinitionRequest](docs/CreateCutLabelDefinitionRequest.md)
 - [CreateDataMapRequest](docs/CreateDataMapRequest.md)
 - [CreateDataTypeRequest](docs/CreateDataTypeRequest.md)
 - [CreateDateRequest](docs/CreateDateRequest.md)
 - [CreateDerivedPropertyDefinitionRequest](docs/CreateDerivedPropertyDefinitionRequest.md)
 - [CreateDerivedTransactionPortfolioRequest](docs/CreateDerivedTransactionPortfolioRequest.md)
 - [CreatePortfolioDetails](docs/CreatePortfolioDetails.md)
 - [CreatePortfolioGroupRequest](docs/CreatePortfolioGroupRequest.md)
 - [CreatePropertyDefinitionRequest](docs/CreatePropertyDefinitionRequest.md)
 - [CreateRecipeRequest](docs/CreateRecipeRequest.md)
 - [CreateReferencePortfolioRequest](docs/CreateReferencePortfolioRequest.md)
 - [CreateRelationDefinitionRequest](docs/CreateRelationDefinitionRequest.md)
 - [CreateRelationRequest](docs/CreateRelationRequest.md)
 - [CreateRelationshipDefinitionRequest](docs/CreateRelationshipDefinitionRequest.md)
 - [CreateRelationshipRequest](docs/CreateRelationshipRequest.md)
 - [CreateSequenceRequest](docs/CreateSequenceRequest.md)
 - [CreateTransactionPortfolioRequest](docs/CreateTransactionPortfolioRequest.md)
 - [CreateUnitDefinition](docs/CreateUnitDefinition.md)
 - [CreditDefaultSwap](docs/CreditDefaultSwap.md)
 - [CreditDefaultSwapAllOf](docs/CreditDefaultSwapAllOf.md)
 - [CreditRating](docs/CreditRating.md)
 - [CreditSpreadCurveData](docs/CreditSpreadCurveData.md)
 - [CreditSpreadCurveDataAllOf](docs/CreditSpreadCurveDataAllOf.md)
 - [CreditSupportAnnex](docs/CreditSupportAnnex.md)
 - [CrossCurrencySwap](docs/CrossCurrencySwap.md)
 - [CrossCurrencySwapAllOf](docs/CrossCurrencySwapAllOf.md)
 - [CurrencyAndAmount](docs/CurrencyAndAmount.md)
 - [CustomEntityDefinition](docs/CustomEntityDefinition.md)
 - [CustomEntityDefinitionRequest](docs/CustomEntityDefinitionRequest.md)
 - [CustomEntityField](docs/CustomEntityField.md)
 - [CustomEntityFieldDefinition](docs/CustomEntityFieldDefinition.md)
 - [CustomEntityIdRequest](docs/CustomEntityIdRequest.md)
 - [CustomEntityIdResponse](docs/CustomEntityIdResponse.md)
 - [CustomEntityRequest](docs/CustomEntityRequest.md)
 - [CustomEntityResponse](docs/CustomEntityResponse.md)
 - [CutLabelDefinition](docs/CutLabelDefinition.md)
 - [CutLocalTime](docs/CutLocalTime.md)
 - [DataDefinition](docs/DataDefinition.md)
 - [DataMapKey](docs/DataMapKey.md)
 - [DataMapping](docs/DataMapping.md)
 - [DataType](docs/DataType.md)
 - [DataTypeSummary](docs/DataTypeSummary.md)
 - [DataTypeValueRange](docs/DataTypeValueRange.md)
 - [DateAttributes](docs/DateAttributes.md)
 - [DateRange](docs/DateRange.md)
 - [DateTimeComparisonType](docs/DateTimeComparisonType.md)
 - [DayOfWeek](docs/DayOfWeek.md)
 - [DeleteInstrumentPropertiesResponse](docs/DeleteInstrumentPropertiesResponse.md)
 - [DeleteInstrumentResponse](docs/DeleteInstrumentResponse.md)
 - [DeleteRelationRequest](docs/DeleteRelationRequest.md)
 - [DeleteRelationshipRequest](docs/DeleteRelationshipRequest.md)
 - [DeletedEntityResponse](docs/DeletedEntityResponse.md)
 - [DeliveryType](docs/DeliveryType.md)
 - [DiscountFactorCurveData](docs/DiscountFactorCurveData.md)
 - [DiscountFactorCurveDataAllOf](docs/DiscountFactorCurveDataAllOf.md)
 - [DiscountingMethod](docs/DiscountingMethod.md)
 - [EmptyModelOptions](docs/EmptyModelOptions.md)
 - [EmptyModelOptionsAllOf](docs/EmptyModelOptionsAllOf.md)
 - [Equity](docs/Equity.md)
 - [EquityAllOf](docs/EquityAllOf.md)
 - [EquityAllOfIdentifiers](docs/EquityAllOfIdentifiers.md)
 - [EquityOption](docs/EquityOption.md)
 - [EquityOptionAllOf](docs/EquityOptionAllOf.md)
 - [EquitySwap](docs/EquitySwap.md)
 - [EquitySwapAllOf](docs/EquitySwapAllOf.md)
 - [EquityVolSurfaceData](docs/EquityVolSurfaceData.md)
 - [EquityVolSurfaceDataAllOf](docs/EquityVolSurfaceDataAllOf.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [ExchangeTradedOption](docs/ExchangeTradedOption.md)
 - [ExchangeTradedOptionAllOf](docs/ExchangeTradedOptionAllOf.md)
 - [ExchangeTradedOptionContractDetails](docs/ExchangeTradedOptionContractDetails.md)
 - [Execution](docs/Execution.md)
 - [ExecutionRequest](docs/ExecutionRequest.md)
 - [ExecutionSetRequest](docs/ExecutionSetRequest.md)
 - [ExoticInstrument](docs/ExoticInstrument.md)
 - [ExoticInstrumentAllOf](docs/ExoticInstrumentAllOf.md)
 - [ExpandedGroup](docs/ExpandedGroup.md)
 - [FeeCalculationDetails](docs/FeeCalculationDetails.md)
 - [FieldDefinition](docs/FieldDefinition.md)
 - [FieldSchema](docs/FieldSchema.md)
 - [FieldValue](docs/FieldValue.md)
 - [FileResponse](docs/FileResponse.md)
 - [FixedLeg](docs/FixedLeg.md)
 - [FixedLegAllOf](docs/FixedLegAllOf.md)
 - [FixedLegAllOfOverrides](docs/FixedLegAllOfOverrides.md)
 - [FloatingLeg](docs/FloatingLeg.md)
 - [FloatingLegAllOf](docs/FloatingLegAllOf.md)
 - [FlowConventionName](docs/FlowConventionName.md)
 - [FlowConventions](docs/FlowConventions.md)
 - [ForwardRateAgreement](docs/ForwardRateAgreement.md)
 - [ForwardRateAgreementAllOf](docs/ForwardRateAgreementAllOf.md)
 - [FundingLeg](docs/FundingLeg.md)
 - [FundingLegAllOf](docs/FundingLegAllOf.md)
 - [Future](docs/Future.md)
 - [FutureAllOf](docs/FutureAllOf.md)
 - [FuturesContractDetails](docs/FuturesContractDetails.md)
 - [FxForward](docs/FxForward.md)
 - [FxForwardAllOf](docs/FxForwardAllOf.md)
 - [FxForwardCurveByQuoteReference](docs/FxForwardCurveByQuoteReference.md)
 - [FxForwardCurveByQuoteReferenceAllOf](docs/FxForwardCurveByQuoteReferenceAllOf.md)
 - [FxForwardCurveData](docs/FxForwardCurveData.md)
 - [FxForwardCurveDataAllOf](docs/FxForwardCurveDataAllOf.md)
 - [FxForwardModelOptions](docs/FxForwardModelOptions.md)
 - [FxForwardModelOptionsAllOf](docs/FxForwardModelOptionsAllOf.md)
 - [FxForwardPipsCurveData](docs/FxForwardPipsCurveData.md)
 - [FxForwardPipsCurveDataAllOf](docs/FxForwardPipsCurveDataAllOf.md)
 - [FxForwardTenorCurveData](docs/FxForwardTenorCurveData.md)
 - [FxForwardTenorCurveDataAllOf](docs/FxForwardTenorCurveDataAllOf.md)
 - [FxForwardTenorPipsCurveData](docs/FxForwardTenorPipsCurveData.md)
 - [FxForwardTenorPipsCurveDataAllOf](docs/FxForwardTenorPipsCurveDataAllOf.md)
 - [FxOption](docs/FxOption.md)
 - [FxOptionAllOf](docs/FxOptionAllOf.md)
 - [FxSwap](docs/FxSwap.md)
 - [FxSwapAllOf](docs/FxSwapAllOf.md)
 - [FxVolSurfaceData](docs/FxVolSurfaceData.md)
 - [GetCdsFlowConventionsResponse](docs/GetCdsFlowConventionsResponse.md)
 - [GetComplexMarketDataResponse](docs/GetComplexMarketDataResponse.md)
 - [GetCounterpartyAgreementResponse](docs/GetCounterpartyAgreementResponse.md)
 - [GetCreditSupportAnnexResponse](docs/GetCreditSupportAnnexResponse.md)
 - [GetDataMapResponse](docs/GetDataMapResponse.md)
 - [GetFlowConventionsResponse](docs/GetFlowConventionsResponse.md)
 - [GetIndexConventionResponse](docs/GetIndexConventionResponse.md)
 - [GetInstrumentsResponse](docs/GetInstrumentsResponse.md)
 - [GetQuotesResponse](docs/GetQuotesResponse.md)
 - [GetRecipeResponse](docs/GetRecipeResponse.md)
 - [GetReferencePortfolioConstituentsResponse](docs/GetReferencePortfolioConstituentsResponse.md)
 - [GetStructuredResultDataResponse](docs/GetStructuredResultDataResponse.md)
 - [GetVirtualDocumentResponse](docs/GetVirtualDocumentResponse.md)
 - [GroupedResultOfAddressKey](docs/GroupedResultOfAddressKey.md)
 - [HoldingAdjustment](docs/HoldingAdjustment.md)
 - [HoldingContext](docs/HoldingContext.md)
 - [HoldingsAdjustment](docs/HoldingsAdjustment.md)
 - [HoldingsAdjustmentHeader](docs/HoldingsAdjustmentHeader.md)
 - [IDataRecord](docs/IDataRecord.md)
 - [IUnitDefinitionDto](docs/IUnitDefinitionDto.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [IdentifierPartSchema](docs/IdentifierPartSchema.md)
 - [IndexConvention](docs/IndexConvention.md)
 - [IndexModelOptions](docs/IndexModelOptions.md)
 - [IndexModelOptionsAllOf](docs/IndexModelOptionsAllOf.md)
 - [IndustryClassifier](docs/IndustryClassifier.md)
 - [InlineValuationRequest](docs/InlineValuationRequest.md)
 - [InlineValuationsReconciliationRequest](docs/InlineValuationsReconciliationRequest.md)
 - [Instrument](docs/Instrument.md)
 - [InstrumentCashFlow](docs/InstrumentCashFlow.md)
 - [InstrumentDefinition](docs/InstrumentDefinition.md)
 - [InstrumentDefinitionFormat](docs/InstrumentDefinitionFormat.md)
 - [InstrumentIdTypeDescriptor](docs/InstrumentIdTypeDescriptor.md)
 - [InstrumentIdValue](docs/InstrumentIdValue.md)
 - [InstrumentLeg](docs/InstrumentLeg.md)
 - [InstrumentLegAllOf](docs/InstrumentLegAllOf.md)
 - [InstrumentMatch](docs/InstrumentMatch.md)
 - [InstrumentProperties](docs/InstrumentProperties.md)
 - [InstrumentSearchProperty](docs/InstrumentSearchProperty.md)
 - [InstrumentType](docs/InstrumentType.md)
 - [InterestRateSwap](docs/InterestRateSwap.md)
 - [InterestRateSwapAllOf](docs/InterestRateSwapAllOf.md)
 - [InterestRateSwaption](docs/InterestRateSwaption.md)
 - [InterestRateSwaptionAllOf](docs/InterestRateSwaptionAllOf.md)
 - [IrVolCubeData](docs/IrVolCubeData.md)
 - [IrVolCubeDataAllOf](docs/IrVolCubeDataAllOf.md)
 - [IsBusinessDayResponse](docs/IsBusinessDayResponse.md)
 - [LabelValueSet](docs/LabelValueSet.md)
 - [LegDefinition](docs/LegDefinition.md)
 - [LegalEntity](docs/LegalEntity.md)
 - [LevelStep](docs/LevelStep.md)
 - [Link](docs/Link.md)
 - [ListAggregationReconciliation](docs/ListAggregationReconciliation.md)
 - [ListAggregationResponse](docs/ListAggregationResponse.md)
 - [ListComplexMarketDataWithMetaDataResponse](docs/ListComplexMarketDataWithMetaDataResponse.md)
 - [LusidInstrument](docs/LusidInstrument.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [MarketContext](docs/MarketContext.md)
 - [MarketContextSuppliers](docs/MarketContextSuppliers.md)
 - [MarketDataKeyRule](docs/MarketDataKeyRule.md)
 - [MarketDataType](docs/MarketDataType.md)
 - [MarketIdentifier](docs/MarketIdentifier.md)
 - [MarketObservableType](docs/MarketObservableType.md)
 - [MarketOptions](docs/MarketOptions.md)
 - [MarketQuote](docs/MarketQuote.md)
 - [MetricValue](docs/MetricValue.md)
 - [ModelOptions](docs/ModelOptions.md)
 - [ModelOptionsType](docs/ModelOptionsType.md)
 - [ModelProperty](docs/ModelProperty.md)
 - [ModelSelection](docs/ModelSelection.md)
 - [MovementType](docs/MovementType.md)
 - [Multiplier](docs/Multiplier.md)
 - [NextValueInSequenceResponse](docs/NextValueInSequenceResponse.md)
 - [NumericComparisonType](docs/NumericComparisonType.md)
 - [OpaqueMarketData](docs/OpaqueMarketData.md)
 - [OpaqueMarketDataAllOf](docs/OpaqueMarketDataAllOf.md)
 - [OpaqueModelOptions](docs/OpaqueModelOptions.md)
 - [OpaqueModelOptionsAllOf](docs/OpaqueModelOptionsAllOf.md)
 - [OperandType](docs/OperandType.md)
 - [Operation](docs/Operation.md)
 - [Operator](docs/Operator.md)
 - [OptionType](docs/OptionType.md)
 - [Order](docs/Order.md)
 - [OrderBySpec](docs/OrderBySpec.md)
 - [OrderGraphBlock](docs/OrderGraphBlock.md)
 - [OrderGraphPlacement](docs/OrderGraphPlacement.md)
 - [OrderGraphSynopsis](docs/OrderGraphSynopsis.md)
 - [OrderInstruction](docs/OrderInstruction.md)
 - [OrderInstructionRequest](docs/OrderInstructionRequest.md)
 - [OrderInstructionSetRequest](docs/OrderInstructionSetRequest.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [OrderSetRequest](docs/OrderSetRequest.md)
 - [OtcConfirmation](docs/OtcConfirmation.md)
 - [OutputTransaction](docs/OutputTransaction.md)
 - [Package](docs/Package.md)
 - [PackageRequest](docs/PackageRequest.md)
 - [PackageSetRequest](docs/PackageSetRequest.md)
 - [PagedResourceListOfAllocation](docs/PagedResourceListOfAllocation.md)
 - [PagedResourceListOfBlock](docs/PagedResourceListOfBlock.md)
 - [PagedResourceListOfCalendar](docs/PagedResourceListOfCalendar.md)
 - [PagedResourceListOfComplianceRuleResult](docs/PagedResourceListOfComplianceRuleResult.md)
 - [PagedResourceListOfComplianceRun](docs/PagedResourceListOfComplianceRun.md)
 - [PagedResourceListOfCorporateActionSource](docs/PagedResourceListOfCorporateActionSource.md)
 - [PagedResourceListOfCustomEntityResponse](docs/PagedResourceListOfCustomEntityResponse.md)
 - [PagedResourceListOfCutLabelDefinition](docs/PagedResourceListOfCutLabelDefinition.md)
 - [PagedResourceListOfDataTypeSummary](docs/PagedResourceListOfDataTypeSummary.md)
 - [PagedResourceListOfExecution](docs/PagedResourceListOfExecution.md)
 - [PagedResourceListOfInstrument](docs/PagedResourceListOfInstrument.md)
 - [PagedResourceListOfLegalEntity](docs/PagedResourceListOfLegalEntity.md)
 - [PagedResourceListOfOrder](docs/PagedResourceListOfOrder.md)
 - [PagedResourceListOfOrderGraphBlock](docs/PagedResourceListOfOrderGraphBlock.md)
 - [PagedResourceListOfOrderGraphPlacement](docs/PagedResourceListOfOrderGraphPlacement.md)
 - [PagedResourceListOfOrderInstruction](docs/PagedResourceListOfOrderInstruction.md)
 - [PagedResourceListOfPackage](docs/PagedResourceListOfPackage.md)
 - [PagedResourceListOfParticipation](docs/PagedResourceListOfParticipation.md)
 - [PagedResourceListOfPerson](docs/PagedResourceListOfPerson.md)
 - [PagedResourceListOfPlacement](docs/PagedResourceListOfPlacement.md)
 - [PagedResourceListOfPortfolioGroupSearchResult](docs/PagedResourceListOfPortfolioGroupSearchResult.md)
 - [PagedResourceListOfPortfolioSearchResult](docs/PagedResourceListOfPortfolioSearchResult.md)
 - [PagedResourceListOfPropertyDefinitionSearchResult](docs/PagedResourceListOfPropertyDefinitionSearchResult.md)
 - [PagedResourceListOfRelationshipDefinition](docs/PagedResourceListOfRelationshipDefinition.md)
 - [PagedResourceListOfSequenceDefinition](docs/PagedResourceListOfSequenceDefinition.md)
 - [Participation](docs/Participation.md)
 - [ParticipationRequest](docs/ParticipationRequest.md)
 - [ParticipationSetRequest](docs/ParticipationSetRequest.md)
 - [PerformanceReturn](docs/PerformanceReturn.md)
 - [PerformanceReturnsMetric](docs/PerformanceReturnsMetric.md)
 - [PeriodType](docs/PeriodType.md)
 - [PerpetualEntityState](docs/PerpetualEntityState.md)
 - [PerpetualProperty](docs/PerpetualProperty.md)
 - [Person](docs/Person.md)
 - [Placement](docs/Placement.md)
 - [PlacementRequest](docs/PlacementRequest.md)
 - [PlacementSetRequest](docs/PlacementSetRequest.md)
 - [Portfolio](docs/Portfolio.md)
 - [PortfolioCashFlow](docs/PortfolioCashFlow.md)
 - [PortfolioCashLadder](docs/PortfolioCashLadder.md)
 - [PortfolioDetails](docs/PortfolioDetails.md)
 - [PortfolioEntityId](docs/PortfolioEntityId.md)
 - [PortfolioGroup](docs/PortfolioGroup.md)
 - [PortfolioGroupProperties](docs/PortfolioGroupProperties.md)
 - [PortfolioGroupSearchResult](docs/PortfolioGroupSearchResult.md)
 - [PortfolioHolding](docs/PortfolioHolding.md)
 - [PortfolioProperties](docs/PortfolioProperties.md)
 - [PortfolioReconciliationRequest](docs/PortfolioReconciliationRequest.md)
 - [PortfolioSearchResult](docs/PortfolioSearchResult.md)
 - [PortfolioType](docs/PortfolioType.md)
 - [PortfoliosReconciliationRequest](docs/PortfoliosReconciliationRequest.md)
 - [PortfoliosReconciliationRequestPreview](docs/PortfoliosReconciliationRequestPreview.md)
 - [Premium](docs/Premium.md)
 - [PricingContext](docs/PricingContext.md)
 - [PricingModel](docs/PricingModel.md)
 - [PricingOptions](docs/PricingOptions.md)
 - [ProcessedCommand](docs/ProcessedCommand.md)
 - [PropertyDefinition](docs/PropertyDefinition.md)
 - [PropertyDefinitionSearchResult](docs/PropertyDefinitionSearchResult.md)
 - [PropertyDefinitionType](docs/PropertyDefinitionType.md)
 - [PropertyDomain](docs/PropertyDomain.md)
 - [PropertyFilter](docs/PropertyFilter.md)
 - [PropertyInterval](docs/PropertyInterval.md)
 - [PropertyLifeTime](docs/PropertyLifeTime.md)
 - [PropertySchema](docs/PropertySchema.md)
 - [PropertyType](docs/PropertyType.md)
 - [PropertyValue](docs/PropertyValue.md)
 - [Quote](docs/Quote.md)
 - [QuoteAccessMetadataRule](docs/QuoteAccessMetadataRule.md)
 - [QuoteAccessMetadataRuleId](docs/QuoteAccessMetadataRuleId.md)
 - [QuoteId](docs/QuoteId.md)
 - [QuoteInstrumentIdType](docs/QuoteInstrumentIdType.md)
 - [QuoteSeriesId](docs/QuoteSeriesId.md)
 - [QuoteType](docs/QuoteType.md)
 - [RealisedGainLoss](docs/RealisedGainLoss.md)
 - [ReconcileDateTimeRule](docs/ReconcileDateTimeRule.md)
 - [ReconcileDateTimeRuleAllOf](docs/ReconcileDateTimeRuleAllOf.md)
 - [ReconcileNumericRule](docs/ReconcileNumericRule.md)
 - [ReconcileNumericRuleAllOf](docs/ReconcileNumericRuleAllOf.md)
 - [ReconcileStringRule](docs/ReconcileStringRule.md)
 - [ReconcileStringRuleAllOf](docs/ReconcileStringRuleAllOf.md)
 - [ReconciliationBreak](docs/ReconciliationBreak.md)
 - [ReconciliationLeftRightAddressKeyPair](docs/ReconciliationLeftRightAddressKeyPair.md)
 - [ReconciliationLine](docs/ReconciliationLine.md)
 - [ReconciliationRequest](docs/ReconciliationRequest.md)
 - [ReconciliationResponse](docs/ReconciliationResponse.md)
 - [ReconciliationRule](docs/ReconciliationRule.md)
 - [ReconciliationRuleType](docs/ReconciliationRuleType.md)
 - [ReferenceData](docs/ReferenceData.md)
 - [ReferencePortfolioConstituent](docs/ReferencePortfolioConstituent.md)
 - [ReferencePortfolioConstituentRequest](docs/ReferencePortfolioConstituentRequest.md)
 - [ReferencePortfolioWeightType](docs/ReferencePortfolioWeightType.md)
 - [RelatedEntity](docs/RelatedEntity.md)
 - [Relation](docs/Relation.md)
 - [RelationDefinition](docs/RelationDefinition.md)
 - [Relationship](docs/Relationship.md)
 - [RelationshipDefinition](docs/RelationshipDefinition.md)
 - [Repo](docs/Repo.md)
 - [RepoAllOf](docs/RepoAllOf.md)
 - [ResourceId](docs/ResourceId.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [ResourceListOfAccessMetadataValueOf](docs/ResourceListOfAccessMetadataValueOf.md)
 - [ResourceListOfAggregatedReturn](docs/ResourceListOfAggregatedReturn.md)
 - [ResourceListOfAggregationQuery](docs/ResourceListOfAggregationQuery.md)
 - [ResourceListOfAllocation](docs/ResourceListOfAllocation.md)
 - [ResourceListOfBlock](docs/ResourceListOfBlock.md)
 - [ResourceListOfCalendarDate](docs/ResourceListOfCalendarDate.md)
 - [ResourceListOfChange](docs/ResourceListOfChange.md)
 - [ResourceListOfConstituentsAdjustmentHeader](docs/ResourceListOfConstituentsAdjustmentHeader.md)
 - [ResourceListOfCorporateAction](docs/ResourceListOfCorporateAction.md)
 - [ResourceListOfDataType](docs/ResourceListOfDataType.md)
 - [ResourceListOfExecution](docs/ResourceListOfExecution.md)
 - [ResourceListOfFeeCalculationDetails](docs/ResourceListOfFeeCalculationDetails.md)
 - [ResourceListOfGetCdsFlowConventionsResponse](docs/ResourceListOfGetCdsFlowConventionsResponse.md)
 - [ResourceListOfGetCounterpartyAgreementResponse](docs/ResourceListOfGetCounterpartyAgreementResponse.md)
 - [ResourceListOfGetCreditSupportAnnexResponse](docs/ResourceListOfGetCreditSupportAnnexResponse.md)
 - [ResourceListOfGetFlowConventionsResponse](docs/ResourceListOfGetFlowConventionsResponse.md)
 - [ResourceListOfGetIndexConventionResponse](docs/ResourceListOfGetIndexConventionResponse.md)
 - [ResourceListOfGetRecipeResponse](docs/ResourceListOfGetRecipeResponse.md)
 - [ResourceListOfHoldingsAdjustmentHeader](docs/ResourceListOfHoldingsAdjustmentHeader.md)
 - [ResourceListOfIUnitDefinitionDto](docs/ResourceListOfIUnitDefinitionDto.md)
 - [ResourceListOfInstrumentCashFlow](docs/ResourceListOfInstrumentCashFlow.md)
 - [ResourceListOfInstrumentIdTypeDescriptor](docs/ResourceListOfInstrumentIdTypeDescriptor.md)
 - [ResourceListOfListComplexMarketDataWithMetaDataResponse](docs/ResourceListOfListComplexMarketDataWithMetaDataResponse.md)
 - [ResourceListOfOrder](docs/ResourceListOfOrder.md)
 - [ResourceListOfOrderInstruction](docs/ResourceListOfOrderInstruction.md)
 - [ResourceListOfPackage](docs/ResourceListOfPackage.md)
 - [ResourceListOfParticipation](docs/ResourceListOfParticipation.md)
 - [ResourceListOfPerformanceReturn](docs/ResourceListOfPerformanceReturn.md)
 - [ResourceListOfPlacement](docs/ResourceListOfPlacement.md)
 - [ResourceListOfPortfolio](docs/ResourceListOfPortfolio.md)
 - [ResourceListOfPortfolioCashFlow](docs/ResourceListOfPortfolioCashFlow.md)
 - [ResourceListOfPortfolioCashLadder](docs/ResourceListOfPortfolioCashLadder.md)
 - [ResourceListOfPortfolioGroup](docs/ResourceListOfPortfolioGroup.md)
 - [ResourceListOfProcessedCommand](docs/ResourceListOfProcessedCommand.md)
 - [ResourceListOfProperty](docs/ResourceListOfProperty.md)
 - [ResourceListOfPropertyDefinition](docs/ResourceListOfPropertyDefinition.md)
 - [ResourceListOfPropertyInterval](docs/ResourceListOfPropertyInterval.md)
 - [ResourceListOfQuote](docs/ResourceListOfQuote.md)
 - [ResourceListOfQuoteAccessMetadataRule](docs/ResourceListOfQuoteAccessMetadataRule.md)
 - [ResourceListOfReconciliationBreak](docs/ResourceListOfReconciliationBreak.md)
 - [ResourceListOfRelation](docs/ResourceListOfRelation.md)
 - [ResourceListOfRelationship](docs/ResourceListOfRelationship.md)
 - [ResourceListOfScopeDefinition](docs/ResourceListOfScopeDefinition.md)
 - [ResourceListOfString](docs/ResourceListOfString.md)
 - [ResourceListOfTransaction](docs/ResourceListOfTransaction.md)
 - [ResourceListOfValueType](docs/ResourceListOfValueType.md)
 - [ResultDataKeyRule](docs/ResultDataKeyRule.md)
 - [ResultDataSchema](docs/ResultDataSchema.md)
 - [ScalingMethodology](docs/ScalingMethodology.md)
 - [Schema](docs/Schema.md)
 - [ScopeDefinition](docs/ScopeDefinition.md)
 - [SequenceDefinition](docs/SequenceDefinition.md)
 - [SetLegalEntityIdentifiersRequest](docs/SetLegalEntityIdentifiersRequest.md)
 - [SetPersonIdentifiersRequest](docs/SetPersonIdentifiersRequest.md)
 - [SetPersonPropertiesRequest](docs/SetPersonPropertiesRequest.md)
 - [SetTransactionConfigurationAlias](docs/SetTransactionConfigurationAlias.md)
 - [SetTransactionConfigurationSourceRequest](docs/SetTransactionConfigurationSourceRequest.md)
 - [SideConfigurationData](docs/SideConfigurationData.md)
 - [SideConfigurationDataRequest](docs/SideConfigurationDataRequest.md)
 - [SimpleInstrument](docs/SimpleInstrument.md)
 - [SimpleInstrumentAllOf](docs/SimpleInstrumentAllOf.md)
 - [SortOrder](docs/SortOrder.md)
 - [StepSchedule](docs/StepSchedule.md)
 - [Stream](docs/Stream.md)
 - [StringComparisonType](docs/StringComparisonType.md)
 - [StructuredResultData](docs/StructuredResultData.md)
 - [StructuredResultDataId](docs/StructuredResultDataId.md)
 - [TargetTaxLot](docs/TargetTaxLot.md)
 - [TargetTaxLotRequest](docs/TargetTaxLotRequest.md)
 - [TermDeposit](docs/TermDeposit.md)
 - [TermDepositAllOf](docs/TermDepositAllOf.md)
 - [Tolerance](docs/Tolerance.md)
 - [ToleranceEnum](docs/ToleranceEnum.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionConfigurationData](docs/TransactionConfigurationData.md)
 - [TransactionConfigurationDataRequest](docs/TransactionConfigurationDataRequest.md)
 - [TransactionConfigurationMovementData](docs/TransactionConfigurationMovementData.md)
 - [TransactionConfigurationMovementDataRequest](docs/TransactionConfigurationMovementDataRequest.md)
 - [TransactionConfigurationTypeAlias](docs/TransactionConfigurationTypeAlias.md)
 - [TransactionPrice](docs/TransactionPrice.md)
 - [TransactionPriceType](docs/TransactionPriceType.md)
 - [TransactionPropertyMapping](docs/TransactionPropertyMapping.md)
 - [TransactionPropertyMappingRequest](docs/TransactionPropertyMappingRequest.md)
 - [TransactionQueryMode](docs/TransactionQueryMode.md)
 - [TransactionQueryParameters](docs/TransactionQueryParameters.md)
 - [TransactionRequest](docs/TransactionRequest.md)
 - [TransactionRoles](docs/TransactionRoles.md)
 - [TransactionSetConfigurationData](docs/TransactionSetConfigurationData.md)
 - [TransactionSetConfigurationDataRequest](docs/TransactionSetConfigurationDataRequest.md)
 - [TransactionStatus](docs/TransactionStatus.md)
 - [TranslateInstrumentDefinitionsRequest](docs/TranslateInstrumentDefinitionsRequest.md)
 - [TranslateInstrumentDefinitionsResponse](docs/TranslateInstrumentDefinitionsResponse.md)
 - [TypedResourceId](docs/TypedResourceId.md)
 - [UnitSchema](docs/UnitSchema.md)
 - [UnmatchedHoldingMethod](docs/UnmatchedHoldingMethod.md)
 - [UpdateCalendarRequest](docs/UpdateCalendarRequest.md)
 - [UpdateCutLabelDefinitionRequest](docs/UpdateCutLabelDefinitionRequest.md)
 - [UpdateDataTypeRequest](docs/UpdateDataTypeRequest.md)
 - [UpdateInstrumentIdentifierRequest](docs/UpdateInstrumentIdentifierRequest.md)
 - [UpdatePortfolioGroupRequest](docs/UpdatePortfolioGroupRequest.md)
 - [UpdatePortfolioRequest](docs/UpdatePortfolioRequest.md)
 - [UpdatePropertyDefinitionRequest](docs/UpdatePropertyDefinitionRequest.md)
 - [UpdateRelationshipDefinitionRequest](docs/UpdateRelationshipDefinitionRequest.md)
 - [UpdateUnitRequest](docs/UpdateUnitRequest.md)
 - [UpsertCdsFlowConventionsRequest](docs/UpsertCdsFlowConventionsRequest.md)
 - [UpsertComplexMarketDataRequest](docs/UpsertComplexMarketDataRequest.md)
 - [UpsertCorporateActionRequest](docs/UpsertCorporateActionRequest.md)
 - [UpsertCorporateActionsResponse](docs/UpsertCorporateActionsResponse.md)
 - [UpsertCounterpartyAgreementRequest](docs/UpsertCounterpartyAgreementRequest.md)
 - [UpsertCreditSupportAnnexRequest](docs/UpsertCreditSupportAnnexRequest.md)
 - [UpsertFlowConventionsRequest](docs/UpsertFlowConventionsRequest.md)
 - [UpsertIndexConventionRequest](docs/UpsertIndexConventionRequest.md)
 - [UpsertInstrumentPropertiesResponse](docs/UpsertInstrumentPropertiesResponse.md)
 - [UpsertInstrumentPropertyRequest](docs/UpsertInstrumentPropertyRequest.md)
 - [UpsertInstrumentsResponse](docs/UpsertInstrumentsResponse.md)
 - [UpsertLegalEntityAccessMetadataRequest](docs/UpsertLegalEntityAccessMetadataRequest.md)
 - [UpsertLegalEntityRequest](docs/UpsertLegalEntityRequest.md)
 - [UpsertPersonAccessMetadataRequest](docs/UpsertPersonAccessMetadataRequest.md)
 - [UpsertPersonRequest](docs/UpsertPersonRequest.md)
 - [UpsertPortfolioAccessMetadataRequest](docs/UpsertPortfolioAccessMetadataRequest.md)
 - [UpsertPortfolioGroupAccessMetadataRequest](docs/UpsertPortfolioGroupAccessMetadataRequest.md)
 - [UpsertPortfolioTransactionsResponse](docs/UpsertPortfolioTransactionsResponse.md)
 - [UpsertQuoteAccessMetadataRuleRequest](docs/UpsertQuoteAccessMetadataRuleRequest.md)
 - [UpsertQuoteRequest](docs/UpsertQuoteRequest.md)
 - [UpsertQuotesResponse](docs/UpsertQuotesResponse.md)
 - [UpsertRecipeRequest](docs/UpsertRecipeRequest.md)
 - [UpsertReferencePortfolioConstituentsRequest](docs/UpsertReferencePortfolioConstituentsRequest.md)
 - [UpsertReferencePortfolioConstituentsResponse](docs/UpsertReferencePortfolioConstituentsResponse.md)
 - [UpsertReturnsResponse](docs/UpsertReturnsResponse.md)
 - [UpsertSingleStructuredDataResponse](docs/UpsertSingleStructuredDataResponse.md)
 - [UpsertStructuredDataResponse](docs/UpsertStructuredDataResponse.md)
 - [UpsertStructuredResultDataRequest](docs/UpsertStructuredResultDataRequest.md)
 - [UpsertTransactionPropertiesResponse](docs/UpsertTransactionPropertiesResponse.md)
 - [User](docs/User.md)
 - [ValuationRequest](docs/ValuationRequest.md)
 - [ValuationSchedule](docs/ValuationSchedule.md)
 - [ValuationsReconciliationRequest](docs/ValuationsReconciliationRequest.md)
 - [ValueType](docs/ValueType.md)
 - [VendorLibrary](docs/VendorLibrary.md)
 - [VendorModelRule](docs/VendorModelRule.md)
 - [Version](docs/Version.md)
 - [VersionSummaryDto](docs/VersionSummaryDto.md)
 - [VersionedResourceListOfA2BDataRecord](docs/VersionedResourceListOfA2BDataRecord.md)
 - [VersionedResourceListOfA2BMovementRecord](docs/VersionedResourceListOfA2BMovementRecord.md)
 - [VersionedResourceListOfOutputTransaction](docs/VersionedResourceListOfOutputTransaction.md)
 - [VersionedResourceListOfPortfolioHolding](docs/VersionedResourceListOfPortfolioHolding.md)
 - [VersionedResourceListOfTransaction](docs/VersionedResourceListOfTransaction.md)
 - [VersionedResourceListWithWarningsOfPortfolioHolding](docs/VersionedResourceListWithWarningsOfPortfolioHolding.md)
 - [VirtualDocument](docs/VirtualDocument.md)
 - [VirtualDocumentRow](docs/VirtualDocumentRow.md)
 - [Warning](docs/Warning.md)
 - [WeekendMask](docs/WeekendMask.md)
 - [WeightedInstrument](docs/WeightedInstrument.md)
 - [WeightedInstruments](docs/WeightedInstruments.md)
 - [YieldCurveData](docs/YieldCurveData.md)
 - [YieldCurveDataAllOf](docs/YieldCurveDataAllOf.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## oauth2

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://lusid.okta.com/oauth2/default/v1/authorize
- **Scopes**: N/A


## Author

info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com
info@finbourne.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in luisd.apis and luisd.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from luisd.api.default_api import DefaultApi`
- `from luisd.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import luisd
from luisd.apis import *
from luisd.models import *
```
