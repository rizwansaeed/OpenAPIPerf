# coding: utf-8

"""
    LUSID API

    # Introduction  This page documents the [LUSID APIs](https://www.lusid.com/api/swagger), which allows authorised clients to query and update their data within the LUSID platform.  SDKs to interact with the LUSID APIs are available in the following languages and frameworks:  * [C#](https://github.com/finbourne/lusid-sdk-csharp) * [Java](https://github.com/finbourne/lusid-sdk-java) * [JavaScript](https://github.com/finbourne/lusid-sdk-js) * [Python](https://github.com/finbourne/lusid-sdk-python) * [Angular](https://github.com/finbourne/lusid-sdk-angular)  The LUSID platform is made up of a number of sub-applications. You can find the API / swagger documentation by following the links in the table below.   | Application | Description | API / Swagger Documentation | | ----- | ----- | ---- | | LUSID | Open, API-first, developer-friendly investment data platform. | [Swagger](https://www.lusid.com/api/swagger/index.html) | | Web app | User-facing front end for LUSID. | [Swagger](https://www.lusid.com/app/swagger/index.html) | | Scheduler | Automated job scheduler. | [Swagger](https://www.lusid.com/scheduler2/swagger/index.html) | | Insights |Monitoring and troubleshooting service. | [Swagger](https://www.lusid.com/insights/swagger/index.html) | | Identity | Identity management for LUSID (in conjuction with Access) | [Swagger](https://www.lusid.com/identity/swagger/index.html) | | Access | Access control for LUSID (in conjunction with Identity) | [Swagger](https://www.lusid.com/access/swagger/index.html) | | Drive | Secure file repository and manager for collaboration. | [Swagger](https://www.lusid.com/drive/swagger/index.html) | | Luminesce | Data virtualisation service (query data from multiple providers, including LUSID) | [Swagger](https://www.lusid.com/honeycomb/swagger/index.html) | | Notification | Notification service. | [Swagger](https://www.lusid.com/notifications/swagger/index.html) | | Configuration | File store for secrets and other sensitive information. | [Swagger](https://www.lusid.com/configuration/swagger/index.html) |   # Error Codes  | Code|Name|Description | | ---|---|--- | | <a name=\"-10\">-10</a>|Server Configuration Error|  | | <a name=\"-1\">-1</a>|Unknown error|An unexpected error was encountered on our side. | | <a name=\"102\">102</a>|Version Not Found|  | | <a name=\"103\">103</a>|Api Rate Limit Violation|  | | <a name=\"104\">104</a>|Instrument Not Found|  | | <a name=\"105\">105</a>|Property Not Found|  | | <a name=\"106\">106</a>|Portfolio Recursion Depth|  | | <a name=\"108\">108</a>|Group Not Found|  | | <a name=\"109\">109</a>|Portfolio Not Found|  | | <a name=\"110\">110</a>|Property Schema Not Found|  | | <a name=\"111\">111</a>|Portfolio Ancestry Not Found|  | | <a name=\"112\">112</a>|Portfolio With Id Already Exists|  | | <a name=\"113\">113</a>|Orphaned Portfolio|  | | <a name=\"119\">119</a>|Missing Base Claims|  | | <a name=\"121\">121</a>|Property Not Defined|  | | <a name=\"122\">122</a>|Cannot Delete System Property|  | | <a name=\"123\">123</a>|Cannot Modify Immutable Property Field|  | | <a name=\"124\">124</a>|Property Already Exists|  | | <a name=\"125\">125</a>|Invalid Property Life Time|  | | <a name=\"126\">126</a>|Property Constraint Style Excludes Properties|  | | <a name=\"127\">127</a>|Cannot Modify Default Data Type|  | | <a name=\"128\">128</a>|Group Already Exists|  | | <a name=\"129\">129</a>|No Such Data Type|  | | <a name=\"130\">130</a>|Undefined Value For Data Type|  | | <a name=\"131\">131</a>|Unsupported Value Type Defined On Data Type|  | | <a name=\"132\">132</a>|Validation Error|  | | <a name=\"133\">133</a>|Loop Detected In Group Hierarchy|  | | <a name=\"134\">134</a>|Undefined Acceptable Values|  | | <a name=\"135\">135</a>|Sub Group Already Exists|  | | <a name=\"138\">138</a>|Price Source Not Found|  | | <a name=\"139\">139</a>|Analytic Store Not Found|  | | <a name=\"141\">141</a>|Analytic Store Already Exists|  | | <a name=\"143\">143</a>|Client Instrument Already Exists|  | | <a name=\"144\">144</a>|Duplicate In Parameter Set|  | | <a name=\"147\">147</a>|Results Not Found|  | | <a name=\"148\">148</a>|Order Field Not In Result Set|  | | <a name=\"149\">149</a>|Operation Failed|  | | <a name=\"150\">150</a>|Elastic Search Error|  | | <a name=\"151\">151</a>|Invalid Parameter Value|  | | <a name=\"153\">153</a>|Command Processing Failure|  | | <a name=\"154\">154</a>|Entity State Construction Failure|  | | <a name=\"155\">155</a>|Entity Timeline Does Not Exist|  | | <a name=\"156\">156</a>|Concurrency Conflict Failure|  | | <a name=\"157\">157</a>|Invalid Request|  | | <a name=\"158\">158</a>|Event Publish Unknown|  | | <a name=\"159\">159</a>|Event Query Failure|  | | <a name=\"160\">160</a>|Blob Did Not Exist|  | | <a name=\"162\">162</a>|Sub System Request Failure|  | | <a name=\"163\">163</a>|Sub System Configuration Failure|  | | <a name=\"165\">165</a>|Failed To Delete|  | | <a name=\"166\">166</a>|Upsert Client Instrument Failure|  | | <a name=\"167\">167</a>|Illegal As At Interval|  | | <a name=\"168\">168</a>|Illegal Bitemporal Query|  | | <a name=\"169\">169</a>|Invalid Alternate Id|  | | <a name=\"170\">170</a>|Cannot Add Source Portfolio Property Explicitly|  | | <a name=\"171\">171</a>|Entity Already Exists In Group|  | | <a name=\"173\">173</a>|Entity With Id Already Exists|  | | <a name=\"174\">174</a>|Derived Portfolio Details Do Not Exist|  | | <a name=\"176\">176</a>|Portfolio With Name Already Exists|  | | <a name=\"177\">177</a>|Invalid Transactions|  | | <a name=\"178\">178</a>|Reference Portfolio Not Found|  | | <a name=\"179\">179</a>|Duplicate Id|  | | <a name=\"180\">180</a>|Command Retrieval Failure|  | | <a name=\"181\">181</a>|Data Filter Application Failure|  | | <a name=\"182\">182</a>|Search Failed|  | | <a name=\"183\">183</a>|Movements Engine Configuration Key Failure|  | | <a name=\"184\">184</a>|Fx Rate Source Not Found|  | | <a name=\"185\">185</a>|Accrual Source Not Found|  | | <a name=\"186\">186</a>|Access Denied|  | | <a name=\"187\">187</a>|Invalid Identity Token|  | | <a name=\"188\">188</a>|Invalid Request Headers|  | | <a name=\"189\">189</a>|Price Not Found|  | | <a name=\"190\">190</a>|Invalid Sub Holding Keys Provided|  | | <a name=\"191\">191</a>|Duplicate Sub Holding Keys Provided|  | | <a name=\"192\">192</a>|Cut Definition Not Found|  | | <a name=\"193\">193</a>|Cut Definition Invalid|  | | <a name=\"194\">194</a>|Time Variant Property Deletion Date Unspecified|  | | <a name=\"195\">195</a>|Perpetual Property Deletion Date Specified|  | | <a name=\"196\">196</a>|Time Variant Property Upsert Date Unspecified|  | | <a name=\"197\">197</a>|Perpetual Property Upsert Date Specified|  | | <a name=\"200\">200</a>|Invalid Unit For Data Type|  | | <a name=\"201\">201</a>|Invalid Type For Data Type|  | | <a name=\"202\">202</a>|Invalid Value For Data Type|  | | <a name=\"203\">203</a>|Unit Not Defined For Data Type|  | | <a name=\"204\">204</a>|Units Not Supported On Data Type|  | | <a name=\"205\">205</a>|Cannot Specify Units On Data Type|  | | <a name=\"206\">206</a>|Unit Schema Inconsistent With Data Type|  | | <a name=\"207\">207</a>|Unit Definition Not Specified|  | | <a name=\"208\">208</a>|Duplicate Unit Definitions Specified|  | | <a name=\"209\">209</a>|Invalid Units Definition|  | | <a name=\"210\">210</a>|Invalid Instrument Identifier Unit|  | | <a name=\"211\">211</a>|Holdings Adjustment Does Not Exist|  | | <a name=\"212\">212</a>|Could Not Build Excel Url|  | | <a name=\"213\">213</a>|Could Not Get Excel Version|  | | <a name=\"214\">214</a>|Instrument By Code Not Found|  | | <a name=\"215\">215</a>|Entity Schema Does Not Exist|  | | <a name=\"216\">216</a>|Feature Not Supported On Portfolio Type|  | | <a name=\"217\">217</a>|Quote Not Found|  | | <a name=\"218\">218</a>|Invalid Quote Identifier|  | | <a name=\"219\">219</a>|Invalid Metric For Data Type|  | | <a name=\"220\">220</a>|Invalid Instrument Definition|  | | <a name=\"221\">221</a>|Instrument Upsert Failure|  | | <a name=\"222\">222</a>|Reference Portfolio Request Not Supported|  | | <a name=\"223\">223</a>|Transaction Portfolio Request Not Supported|  | | <a name=\"224\">224</a>|Invalid Property Value Assignment|  | | <a name=\"230\">230</a>|Transaction Type Not Found|  | | <a name=\"231\">231</a>|Transaction Type Duplication|  | | <a name=\"232\">232</a>|Portfolio Does Not Exist At Given Date|  | | <a name=\"233\">233</a>|Query Parser Failure|  | | <a name=\"234\">234</a>|Duplicate Constituent|  | | <a name=\"235\">235</a>|Unresolved Instrument Constituent|  | | <a name=\"236\">236</a>|Unresolved Instrument In Transition|  | | <a name=\"237\">237</a>|Missing Side Definitions|  | | <a name=\"299\">299</a>|Invalid Recipe|  | | <a name=\"300\">300</a>|Missing Recipe|  | | <a name=\"301\">301</a>|Dependencies|  | | <a name=\"304\">304</a>|Portfolio Preprocess Failure|  | | <a name=\"310\">310</a>|Valuation Engine Failure|  | | <a name=\"311\">311</a>|Task Factory Failure|  | | <a name=\"312\">312</a>|Task Evaluation Failure|  | | <a name=\"313\">313</a>|Task Generation Failure|  | | <a name=\"314\">314</a>|Engine Configuration Failure|  | | <a name=\"315\">315</a>|Model Specification Failure|  | | <a name=\"320\">320</a>|Market Data Key Failure|  | | <a name=\"321\">321</a>|Market Resolver Failure|  | | <a name=\"322\">322</a>|Market Data Failure|  | | <a name=\"330\">330</a>|Curve Failure|  | | <a name=\"331\">331</a>|Volatility Surface Failure|  | | <a name=\"332\">332</a>|Volatility Cube Failure|  | | <a name=\"350\">350</a>|Instrument Failure|  | | <a name=\"351\">351</a>|Cash Flows Failure|  | | <a name=\"352\">352</a>|Reference Data Failure|  | | <a name=\"360\">360</a>|Aggregation Failure|  | | <a name=\"361\">361</a>|Aggregation Measure Failure|  | | <a name=\"370\">370</a>|Result Retrieval Failure|  | | <a name=\"371\">371</a>|Result Processing Failure|  | | <a name=\"372\">372</a>|Vendor Result Processing Failure|  | | <a name=\"373\">373</a>|Vendor Result Mapping Failure|  | | <a name=\"374\">374</a>|Vendor Library Unauthorised|  | | <a name=\"375\">375</a>|Vendor Connectivity Error|  | | <a name=\"376\">376</a>|Vendor Interface Error|  | | <a name=\"377\">377</a>|Vendor Pricing Failure|  | | <a name=\"378\">378</a>|Vendor Translation Failure|  | | <a name=\"379\">379</a>|Vendor Key Mapping Failure|  | | <a name=\"380\">380</a>|Vendor Reflection Failure|  | | <a name=\"381\">381</a>|Vendor Process Failure|  | | <a name=\"382\">382</a>|Vendor System Failure|  | | <a name=\"390\">390</a>|Attempt To Upsert Duplicate Quotes|  | | <a name=\"391\">391</a>|Corporate Action Source Does Not Exist|  | | <a name=\"392\">392</a>|Corporate Action Source Already Exists|  | | <a name=\"393\">393</a>|Instrument Identifier Already In Use|  | | <a name=\"394\">394</a>|Properties Not Found|  | | <a name=\"395\">395</a>|Batch Operation Aborted|  | | <a name=\"400\">400</a>|Invalid Iso4217 Currency Code|  | | <a name=\"401\">401</a>|Cannot Assign Instrument Identifier To Currency|  | | <a name=\"402\">402</a>|Cannot Assign Currency Identifier To Non Currency|  | | <a name=\"403\">403</a>|Currency Instrument Cannot Be Deleted|  | | <a name=\"404\">404</a>|Currency Instrument Cannot Have Economic Definition|  | | <a name=\"405\">405</a>|Currency Instrument Cannot Have Lookthrough Portfolio|  | | <a name=\"406\">406</a>|Cannot Create Currency Instrument With Multiple Identifiers|  | | <a name=\"407\">407</a>|Specified Currency Is Undefined|  | | <a name=\"410\">410</a>|Index Does Not Exist|  | | <a name=\"411\">411</a>|Sort Field Does Not Exist|  | | <a name=\"413\">413</a>|Negative Pagination Parameters|  | | <a name=\"414\">414</a>|Invalid Search Syntax|  | | <a name=\"415\">415</a>|Filter Execution Timeout|  | | <a name=\"420\">420</a>|Side Definition Inconsistent|  | | <a name=\"450\">450</a>|Invalid Quote Access Metadata Rule|  | | <a name=\"451\">451</a>|Access Metadata Not Found|  | | <a name=\"452\">452</a>|Invalid Access Metadata Identifier|  | | <a name=\"460\">460</a>|Standard Resource Not Found|  | | <a name=\"461\">461</a>|Standard Resource Conflict|  | | <a name=\"462\">462</a>|Calendar Not Found|  | | <a name=\"463\">463</a>|Date In A Calendar Not Found|  | | <a name=\"464\">464</a>|Invalid Date Source Data|  | | <a name=\"465\">465</a>|Invalid Timezone|  | | <a name=\"601\">601</a>|Person Identifier Already In Use|  | | <a name=\"602\">602</a>|Person Not Found|  | | <a name=\"603\">603</a>|Cannot Set Identifier|  | | <a name=\"617\">617</a>|Invalid Recipe Specification In Request|  | | <a name=\"618\">618</a>|Inline Recipe Deserialisation Failure|  | | <a name=\"619\">619</a>|Identifier Types Not Set For Entity|  | | <a name=\"620\">620</a>|Cannot Delete All Client Defined Identifiers|  | | <a name=\"650\">650</a>|The Order requested was not found.|  | | <a name=\"654\">654</a>|The Allocation requested was not found.|  | | <a name=\"655\">655</a>|Cannot build the fx forward target with the given holdings.|  | | <a name=\"656\">656</a>|Group does not contain expected entities.|  | | <a name=\"665\">665</a>|Destination directory not found|  | | <a name=\"667\">667</a>|Relation definition already exists|  | | <a name=\"672\">672</a>|Could not retrieve file contents|  | | <a name=\"673\">673</a>|Missing entitlements for entities in Group|  | | <a name=\"674\">674</a>|Next Best Action not found|  | | <a name=\"676\">676</a>|Relation definition not defined|  | | <a name=\"677\">677</a>|Invalid entity identifier for relation|  | | <a name=\"681\">681</a>|Sorting by specified field not supported|One or more of the provided fields to order by were either invalid or not supported. | | <a name=\"682\">682</a>|Too many fields to sort by|The number of fields to sort the data by exceeds the number allowed by the endpoint | | <a name=\"684\">684</a>|Sequence Not Found|  | | <a name=\"685\">685</a>|Sequence Already Exists|  | | <a name=\"686\">686</a>|Non-cycling sequence has been exhausted|  | | <a name=\"687\">687</a>|Legal Entity Identifier Already In Use|  | | <a name=\"688\">688</a>|Legal Entity Not Found|  | | <a name=\"689\">689</a>|The supplied pagination token is invalid|  | | <a name=\"690\">690</a>|Property Type Is Not Supported|  | | <a name=\"691\">691</a>|Multiple Tax-lots For Currency Type Is Not Supported|  | | <a name=\"692\">692</a>|This endpoint does not support impersonation|  | | <a name=\"693\">693</a>|Entity type is not supported for Relationship|  | | <a name=\"694\">694</a>|Relationship Validation Failure|  | | <a name=\"695\">695</a>|Relationship Not Found|  | | <a name=\"697\">697</a>|Derived Property Formula No Longer Valid|  | | <a name=\"698\">698</a>|Story is not available|  | | <a name=\"703\">703</a>|Corporate Action Does Not Exist|  | | <a name=\"720\">720</a>|The provided sort and filter combination is not valid|  | | <a name=\"721\">721</a>|A2B generation failed|  | | <a name=\"722\">722</a>|Aggregated Return Calculation Failure|  | | <a name=\"723\">723</a>|Custom Entity Definition Identifier Already In Use|  | | <a name=\"724\">724</a>|Custom Entity Definition Not Found|  | | <a name=\"725\">725</a>|The Placement requested was not found.|  | | <a name=\"726\">726</a>|The Execution requested was not found.|  | | <a name=\"727\">727</a>|The Block requested was not found.|  | | <a name=\"728\">728</a>|The Participation requested was not found.|  | | <a name=\"729\">729</a>|The Package requested was not found.|  | | <a name=\"730\">730</a>|The OrderInstruction requested was not found.|  | | <a name=\"732\">732</a>|Custom Entity not found.|  | | <a name=\"733\">733</a>|Custom Entity Identifier already in use.|  | | <a name=\"735\">735</a>|Calculation Failed.|  | | <a name=\"736\">736</a>|An expected key on HttpResponse is missing.|  | | <a name=\"737\">737</a>|A required fee detail is missing.|  | | <a name=\"738\">738</a>|Zero rows were returned from Luminesce|  | | <a name=\"739\">739</a>|Provided Weekend Mask was invalid|  | | <a name=\"742\">742</a>|Custom Entity fields do not match the definition|  | | <a name=\"746\">746</a>|The provided sequence is not valid.|  | | <a name=\"751\">751</a>|The type of the Custom Entity is different than the type provided in the definition.|  | | <a name=\"752\">752</a>|Luminesce process returned an error.|  | | <a name=\"753\">753</a>|File name or content incompatible with operation.|  | | <a name=\"755\">755</a>|Schema of response from Drive is not as expected.|  | | <a name=\"757\">757</a>|Schema of response from Luminesce is not as expected.|  | | <a name=\"758\">758</a>|Luminesce timed out.|  |   # noqa: E501

    The version of the OpenAPI document: 0.11.3916
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""

from collections import defaultdict
from datetime import date, datetime, timedelta  # noqa: F401
from dataclasses import dataclass
import functools
import decimal
import io
import os
import re
import tempfile
import typing

from dateutil.parser.isoparser import isoparser, _takes_ascii
from frozendict import frozendict

from luisd.exceptions import (
    ApiTypeError,
    ApiValueError,
)
from luisd.configuration import (
    Configuration,
)


class Unset(object):
    """
    An instance of this class is set as the default value for object type(dict) properties that are optional
    When a property has an unset value, that property will not be assigned in the dict
    """
    pass

unset = Unset()

none_type = type(None)
file_type = io.IOBase


class FileIO(io.FileIO):
    """
    A class for storing files
    Note: this class is not immutable
    """

    def __new__(cls, arg: typing.Union[io.FileIO, io.BufferedReader]):
        if isinstance(arg, (io.FileIO, io.BufferedReader)):
            arg.close()
            inst = super(FileIO, cls).__new__(cls, arg.name)
            super(FileIO, inst).__init__(arg.name)
            return inst
        raise ApiValueError('FileIO must be passed arg which contains the open file')


def update(d: dict, u: dict):
    """
    Adds u to d
    Where each dict is defaultdict(set)
    """
    for k, v in u.items():
        d[k] = d[k].union(v)
    return d


class InstantiationMetadata:
    """
    A class to store metadata that is needed when instantiating OpenApi Schema subclasses
    """
    def __init__(
        self,
        path_to_item: typing.Tuple[typing.Union[str, int], ...] = tuple(['args[0]']),
        from_server: bool = False,
        configuration: typing.Optional[Configuration] = None,
        base_classes: typing.FrozenSet[typing.Type] = frozenset(),
        path_to_schemas: typing.Optional[typing.Dict[str, typing.Set[typing.Type]]] = None,
    ):
        """
        Args:
            path_to_item: the path to the current data being instantiated.
                For {'a': [1]} if the code is handling, 1, then the path is ('args[0]', 'a', 0)
            from_server: whether or not this data came form the server
                True when receiving server data
                False when instantiating model with client side data not form the server
            configuration: the Configuration instance to use
                This is needed because in Configuration:
                - one can disable validation checking
            base_classes: when deserializing data that matches multiple schemas, this is used to store
                the schemas that have been traversed. This is used to stop processing when a cycle is seen.
            path_to_schemas: a dict that goes from path to a list of classes at each path location
        """
        self.path_to_item = path_to_item
        self.from_server = from_server
        self.configuration = configuration
        self.base_classes = base_classes
        if path_to_schemas is None:
            path_to_schemas = defaultdict(set)
        self.path_to_schemas = path_to_schemas

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if not isinstance(other, InstantiationMetadata):
            return False
        return self.__dict__ == other.__dict__


class ValidatorBase:
    @staticmethod
    def __is_json_validation_enabled(schema_keyword, configuration=None):
        """Returns true if JSON schema validation is enabled for the specified
        validation keyword. This can be used to skip JSON schema structural validation
        as requested in the configuration.

        Args:
            schema_keyword (string): the name of a JSON schema validation keyword.
            configuration (Configuration): the configuration class.
        """

        return (configuration is None or
            not hasattr(configuration, '_disabled_client_side_validations') or
            schema_keyword not in configuration._disabled_client_side_validations)

    @staticmethod
    def __raise_validation_error_message(value, constraint_msg, constraint_value, path_to_item, additional_txt=""):
        raise ApiValueError(
            "Invalid value `{value}`, {constraint_msg} `{constraint_value}`{additional_txt} at {path_to_item}".format(
                value=value,
                constraint_msg=constraint_msg,
                constraint_value=constraint_value,
                additional_txt=additional_txt,
                path_to_item=path_to_item,
            )
        )

    @classmethod
    def __check_str_validations(cls,
            validations, input_values,
            _instantiation_metadata: InstantiationMetadata):

        if (cls.__is_json_validation_enabled('maxLength', _instantiation_metadata.configuration) and
                'max_length' in validations and
                len(input_values) > validations['max_length']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="length must be less than or equal to",
                constraint_value=validations['max_length'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('minLength', _instantiation_metadata.configuration) and
                'min_length' in validations and
                len(input_values) < validations['min_length']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="length must be greater than or equal to",
                constraint_value=validations['min_length'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        checked_value = input_values
        if (cls.__is_json_validation_enabled('pattern', _instantiation_metadata.configuration) and
                'regex' in validations):
            for regex_dict in validations['regex']:
                flags = regex_dict.get('flags', 0)
                if not re.search(regex_dict['pattern'], checked_value, flags=flags):
                    if flags != 0:
                        # Don't print the regex flags if the flags are not
                        # specified in the OAS document.
                        cls.__raise_validation_error_message(
                            value=input_values,
                            constraint_msg="must match regular expression",
                            constraint_value=regex_dict['pattern'],
                            path_to_item=_instantiation_metadata.path_to_item,
                            additional_txt=" with flags=`{}`".format(flags)
                        )
                    cls.__raise_validation_error_message(
                        value=input_values,
                        constraint_msg="must match regular expression",
                        constraint_value=regex_dict['pattern'],
                        path_to_item=_instantiation_metadata.path_to_item
                    )

    @classmethod
    def __check_tuple_validations(
            cls, validations, input_values,
            _instantiation_metadata: InstantiationMetadata):

        if (cls.__is_json_validation_enabled('maxItems', _instantiation_metadata.configuration) and
                'max_items' in validations and
                len(input_values) > validations['max_items']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="number of items must be less than or equal to",
                constraint_value=validations['max_items'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('minItems', _instantiation_metadata.configuration) and
                'min_items' in validations and
                len(input_values) < validations['min_items']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="number of items must be greater than or equal to",
                constraint_value=validations['min_items'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('uniqueItems', _instantiation_metadata.configuration) and
                'unique_items' in validations and validations['unique_items'] and input_values):
            unique_items = []
            for item in input_values:
                if item not in unique_items:
                    unique_items.append(item)
            if len(input_values) > len(unique_items):
                cls.__raise_validation_error_message(
                    value=input_values,
                    constraint_msg="duplicate items were found, and the tuple must not contain duplicates because",
                    constraint_value='unique_items==True',
                    path_to_item=_instantiation_metadata.path_to_item
                )

    @classmethod
    def __check_dict_validations(
            cls, validations, input_values,
            _instantiation_metadata: InstantiationMetadata):

        if (cls.__is_json_validation_enabled('maxProperties', _instantiation_metadata.configuration) and
                'max_properties' in validations and
                len(input_values) > validations['max_properties']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="number of properties must be less than or equal to",
                constraint_value=validations['max_properties'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('minProperties', _instantiation_metadata.configuration) and
                'min_properties' in validations and
                len(input_values) < validations['min_properties']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="number of properties must be greater than or equal to",
                constraint_value=validations['min_properties'],
                path_to_item=_instantiation_metadata.path_to_item
            )

    @classmethod
    def __check_numeric_validations(
            cls, validations, input_values,
            _instantiation_metadata: InstantiationMetadata):

        if cls.__is_json_validation_enabled('multipleOf',
                                      _instantiation_metadata.configuration) and 'multiple_of' in validations:
            multiple_of_values = validations['multiple_of']
            for multiple_of_value in multiple_of_values:
                if (isinstance(input_values, decimal.Decimal) and
                        not (float(input_values) / multiple_of_value).is_integer()
                ):
                    # Note 'multipleOf' will be as good as the floating point arithmetic.
                    cls.__raise_validation_error_message(
                        value=input_values,
                        constraint_msg="value must be a multiple of",
                        constraint_value=multiple_of_value,
                        path_to_item=_instantiation_metadata.path_to_item
                    )

        checking_max_or_min_values = {'exclusive_maximum', 'inclusive_maximum', 'exclusive_minimum',
                                      'inclusive_minimum'}.isdisjoint(validations) is False
        if not checking_max_or_min_values:
            return
        max_val = input_values
        min_val = input_values

        if (cls.__is_json_validation_enabled('exclusiveMaximum', _instantiation_metadata.configuration) and
                'exclusive_maximum' in validations and
                max_val >= validations['exclusive_maximum']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="must be a value less than",
                constraint_value=validations['exclusive_maximum'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('maximum', _instantiation_metadata.configuration) and
                'inclusive_maximum' in validations and
                max_val > validations['inclusive_maximum']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="must be a value less than or equal to",
                constraint_value=validations['inclusive_maximum'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('exclusiveMinimum', _instantiation_metadata.configuration) and
                'exclusive_minimum' in validations and
                min_val <= validations['exclusive_minimum']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="must be a value greater than",
                constraint_value=validations['exclusive_maximum'],
                path_to_item=_instantiation_metadata.path_to_item
            )

        if (cls.__is_json_validation_enabled('minimum', _instantiation_metadata.configuration) and
                'inclusive_minimum' in validations and
                min_val < validations['inclusive_minimum']):
            cls.__raise_validation_error_message(
                value=input_values,
                constraint_msg="must be a value greater than or equal to",
                constraint_value=validations['inclusive_minimum'],
                path_to_item=_instantiation_metadata.path_to_item
            )

    @classmethod
    def _check_validations_for_types(
            cls,
            validations,
            input_values,
            _instantiation_metadata: InstantiationMetadata
    ):
        if isinstance(input_values, str):
            cls.__check_str_validations(validations, input_values, _instantiation_metadata)
        elif isinstance(input_values, tuple):
            cls.__check_tuple_validations(validations, input_values, _instantiation_metadata)
        elif isinstance(input_values, frozendict):
            cls.__check_dict_validations(validations, input_values, _instantiation_metadata)
        elif isinstance(input_values, decimal.Decimal):
            cls.__check_numeric_validations(validations, input_values, _instantiation_metadata)
        try:
            return super()._validate_validations_pass(input_values, _instantiation_metadata)
        except AttributeError:
            return True


class Validator(typing.Protocol):
    def _validate_validations_pass(
        cls,
        input_values,
        _instantiation_metadata: InstantiationMetadata
    ):
        pass


def _SchemaValidator(**validations: typing.Union[str, bool, None, int, float, list[dict[str, typing.Union[str, int, float]]]]) -> Validator:
    class SchemaValidator(ValidatorBase):
        @classmethod
        def _validate_validations_pass(
                cls,
                input_values,
                _instantiation_metadata: InstantiationMetadata
        ):
            cls._check_validations_for_types(validations, input_values, _instantiation_metadata)
            try:
                return super()._validate_validations_pass(input_values, _instantiation_metadata)
            except AttributeError:
                return True

    return SchemaValidator


class TypeChecker(typing.Protocol):
    @classmethod
    def _validate_type(
        cls, arg_simple_class: type
    ) -> typing.Tuple[type]:
        pass


def _SchemaTypeChecker(union_type_cls: typing.Union[typing.Any]) -> TypeChecker:
    if typing.get_origin(union_type_cls) is typing.Union:
        union_classes = typing.get_args(union_type_cls)
    else:
        # note: when a union of a single class is passed in, the union disappears
        union_classes = tuple([union_type_cls])
    """
    I want the type hint... union_type_cls
    and to use it as a base class but when I do, I get
    TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
    """
    class SchemaTypeChecker:
        @classmethod
        def _validate_type(cls, arg_simple_class: type):
            if arg_simple_class not in union_classes:
                return union_classes
            try:
                return super()._validate_type(arg_simple_class)
            except AttributeError:
                return tuple()

    return SchemaTypeChecker


class EnumMakerBase:
    @classmethod
    @property
    def _enum_by_value(
        cls
    ) -> type:
        enum_classes = {}
        if not hasattr(cls, "_enum_value_to_name"):
            return enum_classes
        for enum_value, enum_name in cls._enum_value_to_name.items():
            base_class = type(enum_value)
            if base_class is none_type:
                enum_classes[enum_value] = get_new_class(
                      "Dynamic" + cls.__name__, (cls, NoneClass))
                log_cache_usage(get_new_class)
            elif base_class is bool:
                enum_classes[enum_value] = get_new_class(
                      "Dynamic" + cls.__name__, (cls, BoolClass))
                log_cache_usage(get_new_class)
            else:
                enum_classes[enum_value] = get_new_class(
                    "Dynamic" + cls.__name__, (cls, Singleton, base_class))
                log_cache_usage(get_new_class)
        return enum_classes


class EnumMakerInterface(typing.Protocol):
    @classmethod
    @property
    def _enum_value_to_name(
        cls
    ) -> typing.Dict[typing.Union[str, decimal.Decimal, bool, none_type], str]:
        pass

    @classmethod
    @property
    def _enum_by_value(
        cls
    ) -> type:
        pass


def _SchemaEnumMaker(enum_value_to_name: typing.Dict[typing.Union[str, decimal.Decimal, bool, none_type], str]) -> EnumMakerInterface:
    class SchemaEnumMaker(EnumMakerBase):
        @classmethod
        @property
        def _enum_value_to_name(
                cls
        ) -> typing.Dict[typing.Union[str, decimal.Decimal, bool, none_type], str]:
            pass
            try:
                super_enum_value_to_name = super()._enum_value_to_name
            except AttributeError:
                return enum_value_to_name
            intersection = dict(enum_value_to_name.items() & super_enum_value_to_name.items())
            return intersection

    return SchemaEnumMaker


class Singleton:
    """
    Enums and singletons are the same
    The same instance is returned for a given key of (cls, arg)
    """
    # TODO use bidict to store this so boolean enums can move through it in reverse to get their own arg value?
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if not args:
            raise ValueError('arg must be passed')
        arg = args[0]
        key = (cls, arg)
        if key not in cls._instances:
            if arg in {None, True, False}:
                inst = super().__new__(cls)
                # inst._value = arg
                cls._instances[key] = inst
            else:
                cls._instances[key] = super().__new__(cls, arg)
        return cls._instances[key]

    def __repr__(self):
        return '({}, {})'.format(self.__class__.__name__, self)


class NoneClass(Singleton):
    @classmethod
    @property
    def NONE(cls):
        return cls(None)

    def is_none(self) -> bool:
        return True

    def __bool__(self) -> bool:
        return False


class BoolClass(Singleton):
    @classmethod
    @property
    def TRUE(cls):
        return cls(True)

    @classmethod
    @property
    def FALSE(cls):
        return cls(False)

    @functools.cache
    def __bool__(self) -> bool:
        for key, instance in self._instances.items():
            if self is instance:
                return key[1]
        raise ValueError('Unable to find the boolean value of this instance')

    def is_true(self):
        return bool(self)

    def is_false(self):
        return bool(self)


class BoolBase:
    pass


class NoneBase:
    pass


class StrBase:
    @property
    def as_str(self) -> str:
        return self

    @property
    def as_date(self) -> date:
        raise Exception('not implemented')

    @property
    def as_datetime(self) -> datetime:
        raise Exception('not implemented')

    @property
    def as_decimal(self) -> decimal.Decimal:
        raise Exception('not implemented')


class CustomIsoparser(isoparser):

    @_takes_ascii
    def parse_isodatetime(self, dt_str):
        components, pos = self._parse_isodate(dt_str)
        if len(dt_str) > pos:
            if self._sep is None or dt_str[pos:pos + 1] == self._sep:
                components += self._parse_isotime(dt_str[pos + 1:])
            else:
                raise ValueError('String contains unknown ISO components')

        if len(components) > 3 and components[3] == 24:
            components[3] = 0
            return datetime(*components) + timedelta(days=1)

        if len(components) <= 3:
            raise ValueError('Value is not a datetime')

        return datetime(*components)

    @_takes_ascii
    def parse_isodate(self, datestr):
        components, pos = self._parse_isodate(datestr)

        if len(datestr) > pos:
            raise ValueError('String contains invalid time components')

        if len(components) > 3:
            raise ValueError('String contains invalid time components')

        return date(*components)


DEFAULT_ISOPARSER = CustomIsoparser()


class DateBase(StrBase):
    @property
    @functools.cache
    def as_date(self) -> date:
        return DEFAULT_ISOPARSER.parse_isodate(self)

    @classmethod
    def _validate_format(cls, arg: typing.Optional[str], _instantiation_metadata: InstantiationMetadata):
        if isinstance(arg, str):
            try:
                DEFAULT_ISOPARSER.parse_isodate(arg)
                return True
            except ValueError:
                raise ApiValueError(
                    "Value does not conform to the required ISO-8601 date format. "
                    "Invalid value '{}' for type date at {}".format(arg, _instantiation_metadata.path_to_item)
                )

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        DateBase _validate
        """
        cls._validate_format(args[0], _instantiation_metadata=_instantiation_metadata)
        return super()._validate(*args, _instantiation_metadata=_instantiation_metadata)


class DateTimeBase:
    @property
    @functools.cache
    def as_datetime(self) -> datetime:
        return DEFAULT_ISOPARSER.parse_isodatetime(self)

    @classmethod
    def _validate_format(cls, arg: typing.Optional[str], _instantiation_metadata: InstantiationMetadata):
        if isinstance(arg, str):
            try:
                DEFAULT_ISOPARSER.parse_isodatetime(arg)
                return True
            except ValueError:
                raise ApiValueError(
                    "Value does not conform to the required ISO-8601 datetime format. "
                    "Invalid value '{}' for type datetime at {}".format(arg, _instantiation_metadata.path_to_item)
                )

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        DateTimeBase _validate
        """
        cls._validate_format(args[0], _instantiation_metadata=_instantiation_metadata)
        return super()._validate(*args, _instantiation_metadata=_instantiation_metadata)


class DecimalBase(StrBase):
    """
    A class for storing decimals that are sent over the wire as strings
    These schemas must remain based on StrBase rather than NumberBase
    because picking base classes must be deterministic
    """

    @property
    @functools.cache
    def as_decimal(self) -> decimal.Decimal:
        return decimal.Decimal(self)

    @classmethod
    def _validate_format(cls, arg: typing.Optional[str], _instantiation_metadata: InstantiationMetadata):
        if isinstance(arg, str):
            try:
                decimal.Decimal(arg)
                return True
            except decimal.InvalidOperation:
                raise ApiValueError(
                    "Value cannot be converted to a decimal. "
                    "Invalid value '{}' for type decimal at {}".format(arg, _instantiation_metadata.path_to_item)
                )

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        DecimalBase _validate
        """
        cls._validate_format(args[0], _instantiation_metadata=_instantiation_metadata)
        return super()._validate(*args, _instantiation_metadata=_instantiation_metadata)


class NumberBase:
    @property
    def as_int(self) -> int:
        try:
            return self._as_int
        except AttributeError:
            """
            Note: for some numbers like 9.0 they could be represented as an
            integer but our code chooses to store them as
            >>> Decimal('9.0').as_tuple()
            DecimalTuple(sign=0, digits=(9, 0), exponent=-1)
            so we can tell that the value came from a float and convert it back to a float
            during later serialization
            """
            if self.as_tuple().exponent < 0:
                # this could be represented as an integer but should be represented as a float
                # because that's what it was serialized from
                raise ApiValueError(f'{self} is not an integer')
            self._as_int = int(self)
            return self._as_int

    @property
    def as_float(self) -> float:
        try:
            return self._as_float
        except AttributeError:
            if self.as_tuple().exponent >= 0:
                raise ApiValueError(f'{self} is not an float')
            self._as_float = float(self)
            return self._as_float


class ListBase:
    @classmethod
    def _validate_items(cls, list_items, _instantiation_metadata: InstantiationMetadata):
        """
        Ensures that:
        - values passed in for items are valid
        Exceptions will be raised if:
        - invalid arguments were passed in

        Args:
            list_items: the input list of items

        Raises:
            ApiTypeError - for missing required arguments, or for invalid properties
        """

        # if we have definitions for an items schema, use it
        # otherwise accept anything
        item_cls = getattr(cls, '_items', AnyTypeSchema)
        path_to_schemas = defaultdict(set)
        for i, value in enumerate(list_items):
            if isinstance(value, item_cls):
                continue
            item_instantiation_metadata = InstantiationMetadata(
                from_server=_instantiation_metadata.from_server,
                configuration=_instantiation_metadata.configuration,
                path_to_item=_instantiation_metadata.path_to_item+(i,)
            )
            other_path_to_schemas = item_cls._validate(
                value, _instantiation_metadata=item_instantiation_metadata)
            update(path_to_schemas, other_path_to_schemas)
        return path_to_schemas

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        ListBase _validate
        We return dynamic classes of different bases depending upon the inputs
        This makes it so:
        - the returned instance is always a subclass of our defining schema
            - this allows us to check type based on whether an instance is a subclass of a schema
        - the returned instance is a serializable type (except for None, True, and False) which are enums

        Returns:
            new_cls (type): the new class

        Raises:
            ApiValueError: when a string can't be converted into a date or datetime and it must be one of those classes
            ApiTypeError: when the input type is not in the list of allowed spec types
        """
        arg = args[0]
        _path_to_schemas = super()._validate(*args, _instantiation_metadata=_instantiation_metadata)
        if not isinstance(arg, tuple):
            return _path_to_schemas
        if cls in _instantiation_metadata.base_classes:
            # we have already moved through this class so stop here
            return _path_to_schemas
        _instantiation_metadata.base_classes |= frozenset({cls})
        other_path_to_schemas = cls._validate_items(arg, _instantiation_metadata=_instantiation_metadata)
        update(_path_to_schemas, other_path_to_schemas)
        return _path_to_schemas

    @classmethod
    def _get_items(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        '''
        ListBase _get_items
        '''
        _instantiation_metadata = InstantiationMetadata() if _instantiation_metadata is None else _instantiation_metadata

        list_items = args[0]
        cast_items = []
        # if we have definitions for an items schema, use it
        # otherwise accept anything

        cls_item_cls = getattr(cls, '_items', AnyTypeSchema)
        for i, value in enumerate(list_items):
            item_path_to_item = _instantiation_metadata.path_to_item+(i,)
            if item_path_to_item in _instantiation_metadata.path_to_schemas:
                item_cls = _instantiation_metadata.path_to_schemas[item_path_to_item]
            else:
                item_cls = cls_item_cls

            if isinstance(value, item_cls):
                cast_items.append(value)
                continue
            item_instantiation_metadata = InstantiationMetadata(
                configuration=_instantiation_metadata.configuration,
                from_server=_instantiation_metadata.from_server,
                path_to_item=item_path_to_item,
                path_to_schemas=_instantiation_metadata.path_to_schemas,
            )

            if _instantiation_metadata.from_server:
                new_value = item_cls._from_openapi_data(value, _instantiation_metadata=item_instantiation_metadata)
            else:
                new_value = item_cls(value, _instantiation_metadata=item_instantiation_metadata)
            cast_items.append(new_value)

        return cast_items


class Discriminable:
    @classmethod
    def _ensure_discriminator_value_present(cls, disc_property_name: str, _instantiation_metadata: InstantiationMetadata, *args):
        if not args or args and disc_property_name not in args[0]:
            # The input data does not contain the discriminator property
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '{}' is missing at path: {}".format(disc_property_name, _instantiation_metadata.path_to_item)
            )

    @classmethod
    def _get_discriminated_class(cls, disc_property_name: str, disc_payload_value: str):
        """
        Used in schemas with discriminators
        """
        if not hasattr(cls, '_discriminator'):
            return None
        disc = cls._discriminator
        if disc_property_name not in disc:
            return None
        discriminated_cls = disc[disc_property_name].get(disc_payload_value)
        if discriminated_cls is not None:
            return discriminated_cls
        elif not hasattr(cls, '_composed_schemas'):
            return None
        # TODO stop traveling if a cycle is hit
        for allof_cls in cls._composed_schemas['allOf']:
            discriminated_cls = allof_cls._get_discriminated_class(
                disc_property_name=disc_property_name, disc_payload_value=disc_payload_value)
            if discriminated_cls is not None:
                return discriminated_cls
        for oneof_cls in cls._composed_schemas['oneOf']:
            discriminated_cls = oneof_cls._get_discriminated_class(
                disc_property_name=disc_property_name, disc_payload_value=disc_payload_value)
            if discriminated_cls is not None:
                return discriminated_cls
        for anyof_cls in cls._composed_schemas['anyOf']:
            discriminated_cls = anyof_cls._get_discriminated_class(
                disc_property_name=disc_property_name, disc_payload_value=disc_payload_value)
            if discriminated_cls is not None:
                return discriminated_cls
        return None


class DictBase(Discriminable):
    # subclass properties
    _required_property_names = set()

    @classmethod
    def _validate_arg_presence(cls, arg):
        """
        Ensures that:
        - all required arguments are passed in
        - the input variable names are valid
            - present in properties or
            - accepted because additionalProperties exists
        Exceptions will be raised if:
        - invalid arguments were passed in
            - a var_name is invalid if additionProperties == None and var_name not in _properties
        - required properties were not passed in

        Args:
            arg: the input dict

        Raises:
            ApiTypeError - for missing required arguments, or for invalid properties
        """
        seen_required_properties = set()
        invalid_arguments = []
        for property_name in arg:
            if property_name in cls._required_property_names:
                seen_required_properties.add(property_name)
            elif property_name in cls._property_names:
                continue
            elif cls._additional_properties:
                continue
            else:
                invalid_arguments.append(property_name)
        missing_required_arguments = list(cls._required_property_names - seen_required_properties)
        if missing_required_arguments:
            missing_required_arguments.sort()
            raise ApiTypeError(
                "{} is missing {} required argument{}: {}".format(
                    cls.__name__,
                    len(missing_required_arguments),
                    "s" if len(missing_required_arguments) > 1 else "",
                    missing_required_arguments
                )
            )
        if invalid_arguments:
            invalid_arguments.sort()
            raise ApiTypeError(
                "{} was passed {} invalid argument{}: {}".format(
                    cls.__name__,
                    len(invalid_arguments),
                    "s" if len(invalid_arguments) > 1 else "",
                    invalid_arguments
                )
            )

    @classmethod
    def _validate_args(cls, arg, _instantiation_metadata: InstantiationMetadata):
        """
        Ensures that:
        - values passed in for properties are valid
        Exceptions will be raised if:
        - invalid arguments were passed in

        Args:
            arg: the input dict

        Raises:
            ApiTypeError - for missing required arguments, or for invalid properties
        """
        path_to_schemas = defaultdict(set)
        for property_name, value in arg.items():
            if property_name in cls._required_property_names or property_name in cls._property_names:
                schema = getattr(cls, property_name)
            elif cls._additional_properties:
                schema = cls._additional_properties
            else:
                raise ApiTypeError('Unable to find schema for value={} in class={} at path_to_item={}'.format(
                    value, cls, _instantiation_metadata.path_to_item+(property_name,)
                ))
            if isinstance(value, schema):
                continue
            arg_instantiation_metadata = InstantiationMetadata(
                from_server=_instantiation_metadata.from_server,
                configuration=_instantiation_metadata.configuration,
                path_to_item=_instantiation_metadata.path_to_item+(property_name,)
            )
            other_path_to_schemas = schema._validate(value, _instantiation_metadata=arg_instantiation_metadata)
            update(path_to_schemas, other_path_to_schemas)
            _instantiation_metadata.path_to_schemas.update(arg_instantiation_metadata.path_to_schemas)
        return path_to_schemas

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        DictBase _validate
        We return dynamic classes of different bases depending upon the inputs
        This makes it so:
        - the returned instance is always a subclass of our defining schema
            - this allows us to check type based on whether an instance is a subclass of a schema
        - the returned instance is a serializable type (except for None, True, and False) which are enums

        Returns:
            new_cls (type): the new class

        Raises:
            ApiValueError: when a string can't be converted into a date or datetime and it must be one of those classes
            ApiTypeError: when the input type is not in the list of allowed spec types
        """
        if args and isinstance(args[0], cls):
            # an instance of the correct type was passed in
            return {}
        arg = args[0]
        _path_to_schemas = super()._validate(*args, _instantiation_metadata=_instantiation_metadata)
        if not isinstance(arg, frozendict):
            return _path_to_schemas
        cls._validate_arg_presence(args[0])
        other_path_to_schemas = cls._validate_args(args[0], _instantiation_metadata=_instantiation_metadata)
        update(_path_to_schemas, other_path_to_schemas)
        try:
            _discriminator = cls._discriminator
        except AttributeError:
            return _path_to_schemas
        # discriminator exists
        disc_prop_name = list(_discriminator.keys())[0]
        cls._ensure_discriminator_value_present(disc_prop_name, _instantiation_metadata, *args)
        discriminated_cls = cls._get_discriminated_class(
            disc_property_name=disc_prop_name, disc_payload_value=arg[disc_prop_name])
        if discriminated_cls is None:
            raise ApiValueError(
                "Invalid discriminator value was passed in to {}.{} Only the values {} are allowed at {}".format(
                    cls.__name__,
                    disc_prop_name,
                    list(_discriminator[disc_prop_name].keys()),
                    _instantiation_metadata.path_to_item + (disc_prop_name,)
                )
            )
        if discriminated_cls in _instantiation_metadata.base_classes:
            # we have already moved through this class so stop here
            return _path_to_schemas
        _instantiation_metadata.base_classes |= frozenset({cls})
        other_path_to_schemas = discriminated_cls._validate(*args, _instantiation_metadata=_instantiation_metadata)
        update(_path_to_schemas, other_path_to_schemas)
        return _path_to_schemas

    @classmethod
    @property
    def _additional_properties(cls):
        return AnyTypeSchema

    @classmethod
    @property
    @functools.cache
    def _property_names(cls):
        property_names = set()
        for var_name, var_value in cls.__dict__.items():
            # referenced models are classmethods
            is_classmethod = type(var_value) is classmethod
            if is_classmethod:
                property_names.add(var_name)
                continue
            is_class = type(var_value) is type
            if not is_class:
                continue
            if not issubclass(var_value, Schema):
                continue
            if var_name == '_additional_properties':
                continue
            property_names.add(var_name)
        property_names = list(property_names)
        property_names.sort()
        return tuple(property_names)

    @classmethod
    def _get_properties(cls, arg: typing.Dict[str, typing.Any], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        DictBase _get_properties, this is how properties are set
        These values already passed validation
        """
        dict_items = {}
        # if we have definitions for property schemas convert values using it
        # otherwise accept anything

        _instantiation_metadata = InstantiationMetadata() if _instantiation_metadata is None else _instantiation_metadata

        for property_name_js, value in arg.items():
            property_cls = getattr(cls, property_name_js, cls._additional_properties)
            property_path_to_item = _instantiation_metadata.path_to_item+(property_name_js,)
            stored_property_cls = _instantiation_metadata.path_to_schemas.get(property_path_to_item)
            if stored_property_cls:
                property_cls = stored_property_cls

            if isinstance(value, property_cls):
                dict_items[property_name_js] = value
                continue

            prop_instantiation_metadata = InstantiationMetadata(
                configuration=_instantiation_metadata.configuration,
                from_server=_instantiation_metadata.from_server,
                path_to_item=property_path_to_item,
                path_to_schemas=_instantiation_metadata.path_to_schemas,
            )
            if _instantiation_metadata.from_server:
                new_value = property_cls._from_openapi_data(value, _instantiation_metadata=prop_instantiation_metadata)
            else:
                new_value = property_cls(value, _instantiation_metadata=prop_instantiation_metadata)
            dict_items[property_name_js] = new_value
        return dict_items

    def __setattr__(self, name, value):
        if not isinstance(self, FileIO):
            raise AttributeError('property setting not supported on immutable instances')

    def __getattr__(self, name):
        if isinstance(self, frozendict):
            # if an attribute does not exist
            try:
                return self[name]
            except KeyError as ex:
                raise AttributeError(str(ex))
        return super().__getattr__(self, name)

    def __getattribute__(self, name):
        # if an attribute does exist (for example as a class property but not as an instance method)
        try:
            return self[name]
        except (KeyError, TypeError):
            return super().__getattribute__(name)


inheritable_primitive_types_set = {decimal.Decimal, str, tuple, frozendict, FileIO, bytes}


class Schema:
    """
    the base class of all swagger/openapi schemas/models

    ensures that:
    - payload passes required validations
    - payload is of allowed types
    - payload value is an allowed enum value
    """

    @staticmethod
    def __get_simple_class(input_value):
        """Returns an input_value's simple class that we will use for type checking

        Args:
            input_value (class/class_instance): the item for which we will return
                                                the simple class
        """
        if isinstance(input_value, tuple):
            return tuple
        elif isinstance(input_value, frozendict):
            return frozendict
        elif isinstance(input_value, none_type):
            return none_type
        elif isinstance(input_value, bytes):
            return bytes
        elif isinstance(input_value, (io.FileIO, io.BufferedReader)):
            return FileIO
        elif isinstance(input_value, bool):
            # this must be higher than the int check because
            # isinstance(True, int) == True
            return bool
        elif isinstance(input_value, int):
            return int
        elif isinstance(input_value, float):
            return float
        elif isinstance(input_value, datetime):
            # this must be higher than the date check because
            # isinstance(datetime_instance, date) == True
            return datetime
        elif isinstance(input_value, date):
            return date
        elif isinstance(input_value, str):
            return str
        return type(input_value)

    @staticmethod
    def __get_valid_classes_phrase(input_classes):
        """Returns a string phrase describing what types are allowed"""
        all_classes = list(input_classes)
        all_classes = sorted(all_classes, key=lambda cls: cls.__name__)
        all_class_names = [cls.__name__ for cls in all_classes]
        if len(all_class_names) == 1:
            return "is {0}".format(all_class_names[0])
        return "is one of [{0}]".format(", ".join(all_class_names))

    @classmethod
    def __type_error_message(
        cls, var_value=None, var_name=None, valid_classes=None, key_type=None
    ):
        """
        Keyword Args:
            var_value (any): the variable which has the type_error
            var_name (str): the name of the variable which has the typ error
            valid_classes (tuple): the accepted classes for current_item's
                                      value
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a tuple
        """
        key_or_value = "value"
        if key_type:
            key_or_value = "key"
        valid_classes_phrase = cls.__get_valid_classes_phrase(valid_classes)
        msg = "Invalid type. Required {1} type {2} and " "passed type was {3}".format(
            var_name,
            key_or_value,
            valid_classes_phrase,
            type(var_value).__name__,
        )
        return msg

    @classmethod
    def __get_type_error(cls, var_value, path_to_item, valid_classes, key_type=False):
        error_msg = cls.__type_error_message(
            var_name=path_to_item[-1],
            var_value=var_value,
            valid_classes=valid_classes,
            key_type=key_type,
        )
        return ApiTypeError(
            error_msg,
            path_to_item=path_to_item,
            valid_classes=valid_classes,
            key_type=key_type,
        )

    @classmethod
    def _class_by_base_class(cls, base_cls: type) -> type:
        cls_name = "Dynamic"+cls.__name__
        if base_cls is bool:
            new_cls = get_new_class(cls_name, (cls, BoolBase, BoolClass))
        elif base_cls is str:
            new_cls = get_new_class(cls_name, (cls, StrBase, str))
        elif base_cls is decimal.Decimal:
            new_cls = get_new_class(cls_name, (cls, NumberBase, decimal.Decimal))
        elif base_cls is tuple:
            new_cls =  get_new_class(cls_name, (cls, ListBase, tuple))
        elif base_cls is frozendict:
            new_cls = get_new_class(cls_name, (cls, DictBase, frozendict))
        elif base_cls is none_type:
            new_cls = get_new_class(cls_name, (cls, NoneBase, NoneClass))
        log_cache_usage(get_new_class)
        return new_cls

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        Schema _validate
        Runs all schema validation logic and
        returns a dynamic class of different bases depending upon the input
        This makes it so:
        - the returned instance is always a subclass of our defining schema
            - this allows us to check type based on whether an instance is a subclass of a schema
        - the returned instance is a serializable type (except for None, True, and False) which are enums

        Use cases:
        1. inheritable type: string/decimal.Decimal/frozendict/tuple
        2. enum value cases: 'hi', 1 -> no base_class set because the enum includes the base class
        3. uninheritable type: True/False/None -> no base_class because the base class is not inheritable
            _enum_by_value will handle this use case

        Required Steps:
        1. verify type of input is valid vs the allowed _types
        2. check validations that are applicable for this type of input
        3. if enums exist, check that the value exists in the enum

        Returns:
            path_to_schemas: a map of path to schemas

        Raises:
            ApiValueError: when a string can't be converted into a date or datetime and it must be one of those classes
            ApiTypeError: when the input type is not in the list of allowed spec types
        """
        arg = args[0]

        base_class = cls.__get_simple_class(arg)
        failed_type_check_classes = cls._validate_type(base_class)
        if failed_type_check_classes:
            raise cls.__get_type_error(
                arg,
                _instantiation_metadata.path_to_item,
                failed_type_check_classes,
                key_type=False,
            )
        if hasattr(cls, '_validate_validations_pass'):
            cls._validate_validations_pass(arg, _instantiation_metadata)
        path_to_schemas = defaultdict(set)
        path_to_schemas[_instantiation_metadata.path_to_item].add(cls)

        if hasattr(cls, "_enum_by_value"):
            cls._validate_enum_value(arg)
            return path_to_schemas

        if base_class is none_type or base_class is bool:
            return path_to_schemas

        path_to_schemas[_instantiation_metadata.path_to_item].add(base_class)
        return path_to_schemas

    @classmethod
    def _validate_enum_value(cls, arg):
        try:
            cls._enum_by_value[arg]
        except KeyError:
            raise ApiValueError("Invalid value {} passed in to {}, {}".format(arg, cls, cls._enum_value_to_name))

    @classmethod
    def __get_new_cls(cls, arg, _instantiation_metadata: InstantiationMetadata):
        """
        PATH 1 - make a new dynamic class and return an instance of that class
        We are making an instance of cls, but instead of making cls
        make a new class, new_cls
        which includes dynamic bases including cls
        return an instance of that new class
        """
        if (
        _instantiation_metadata.path_to_schemas and
        _instantiation_metadata.path_to_item in _instantiation_metadata.path_to_schemas):
            chosen_new_cls = _instantiation_metadata.path_to_schemas[_instantiation_metadata.path_to_item]
            return chosen_new_cls
        """
        Dict property + List Item Assignment Use cases:
        1. value is NOT an instance of the required schema class
            the value is validated by _validate
            _validate returns a key value pair
            where the key is the path to the item, and the value will be the required manufactured class
            made out of the matching schemas
        2. value is an instance of the the correct schema type
            the value is NOT validated by _validate, _validate only checks that the instance is of the correct schema type
            for this value, _validate does NOT return an entry for it in _path_to_schemas
            and in list/dict _get_items,_get_properties the value will be directly assigned
            because value is of the correct type, and validation was run earlier when the instance was created
        """
        _path_to_schemas = cls._validate(arg, _instantiation_metadata=_instantiation_metadata)
        # loop through it make a new class for each entry
        for path, schema_classes in _path_to_schemas.items():
            enum_schema = any(
                hasattr(this_cls, '_enum_by_value') for this_cls in schema_classes)
            inheritable_primitive_type = schema_classes.intersection(inheritable_primitive_types_set)
            chosen_schema_classes = schema_classes
            suffix = tuple()
            if inheritable_primitive_type:
                chosen_schema_classes = schema_classes - inheritable_primitive_types_set
                if not enum_schema:
                    # include the inheritable_primitive_type
                    suffix = tuple(inheritable_primitive_type)

            if len(chosen_schema_classes) == 1 and not suffix:
                mfg_cls = tuple(chosen_schema_classes)[0]
            else:
                x_schema = schema_descendents & chosen_schema_classes
                if x_schema:
                    x_schema = x_schema.pop()
                    if any(c is not x_schema and issubclass(c, x_schema) for c in chosen_schema_classes):
                        # needed to not have a mro error in get_new_class
                        chosen_schema_classes.remove(x_schema)
                used_classes = tuple(sorted(chosen_schema_classes, key=lambda a_cls: a_cls.__name__)) + suffix
                mfg_cls = get_new_class(class_name='DynamicSchema', bases=used_classes)

            if inheritable_primitive_type and not enum_schema:
                _instantiation_metadata.path_to_schemas[path] = mfg_cls
                continue

            # Use case: value is None, True, False, or an enum value
            value = arg
            for key in path[1:]:
                value = value[key]
            if hasattr(mfg_cls, '_enum_by_value'):
                mfg_cls = mfg_cls._enum_by_value[value]
            elif value in {True, False}:
                mfg_cls = mfg_cls._class_by_base_class(bool)
            elif value is None:
                mfg_cls = mfg_cls._class_by_base_class(none_type)
            else:
                raise ApiValueError('Unhandled case value={} bases={}'.format(value, mfg_cls.__bases__))
            _instantiation_metadata.path_to_schemas[path] = mfg_cls

        return _instantiation_metadata.path_to_schemas[_instantiation_metadata.path_to_item]

    @classmethod
    def __get_new_instance_without_conversion(cls, arg, _instantiation_metadata):
        # PATH 2 - we have a Dynamic class and we are making an instance of it
        if issubclass(cls, tuple):
            items = cls._get_items(arg, _instantiation_metadata=_instantiation_metadata)
            return super(Schema, cls).__new__(cls, items)
        elif issubclass(cls, frozendict):
            properties = cls._get_properties(arg, _instantiation_metadata=_instantiation_metadata)
            return super(Schema, cls).__new__(cls, properties)
        """
        str = openapi str, date, and datetime
        decimal.Decimal = openapi int and float
        FileIO = openapi binary type and the user inputs a file
        bytes = openapi binary type and the user inputs bytes
        """
        return super(Schema, cls).__new__(cls, arg)

    @classmethod
    def _from_openapi_data(
        cls,
        arg: typing.Union[
            str,
            date,
            datetime,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            'Schema',
            dict,
            frozendict,
            tuple,
            list,
            io.FileIO,
            io.BufferedReader,
            bytes
        ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata]
    ):
        arg = cast_to_allowed_types(arg, from_server=True)
        _instantiation_metadata = InstantiationMetadata(from_server=True) if _instantiation_metadata is None else _instantiation_metadata
        if not _instantiation_metadata.from_server:
            raise ApiValueError(
                'from_server must be True in this code path, if you need it to be False, use cls()'
            )
        new_cls = cls.__get_new_cls(arg, _instantiation_metadata)
        new_inst = new_cls.__get_new_instance_without_conversion(arg, _instantiation_metadata)
        return new_inst

    @staticmethod
    def __get_input_dict(*args, **kwargs) -> frozendict:
        input_dict = {}
        if args and isinstance(args[0], (dict, frozendict)):
            input_dict.update(args[0])
        if kwargs:
            input_dict.update(kwargs)
        return frozendict(input_dict)

    @staticmethod
    def __remove_unsets(kwargs):
        return {key: val for key, val in kwargs.items() if val is not unset}

    def __new__(cls, *args: typing.Union[dict, frozendict, list, tuple, decimal.Decimal, float, int, str, date, datetime, bool, None, 'Schema'], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None, **kwargs: typing.Union[dict, frozendict, list, tuple, decimal.Decimal, float, int, str, date, datetime, bool, None, 'Schema', Unset]):
        """
        Schema __new__

        Args:
            args (int/float/decimal.Decimal/str/list/tuple/dict/frozendict/bool/None): the value
            kwargs (str, int/float/decimal.Decimal/str/list/tuple/dict/frozendict/bool/None): dict values
            _instantiation_metadata: contains the needed from_server, configuration, path_to_item
        """
        kwargs = cls.__remove_unsets(kwargs)
        if not args and not kwargs:
            raise TypeError(
                'No input given. args or kwargs must be given.'
            )
        if not kwargs and args and not isinstance(args[0], dict):
            arg = args[0]
        else:
            arg = cls.__get_input_dict(*args, **kwargs)
        _instantiation_metadata = InstantiationMetadata() if _instantiation_metadata is None else _instantiation_metadata
        if _instantiation_metadata.from_server:
            raise ApiValueError(
                'from_server must be False in this code path, if you need it to be True, use cls._from_openapi_data()'
            )
        arg = cast_to_allowed_types(arg, from_server=_instantiation_metadata.from_server)
        new_cls = cls.__get_new_cls(arg, _instantiation_metadata)
        return new_cls.__get_new_instance_without_conversion(arg, _instantiation_metadata)

    def __init__(
        self,
        *args: typing.Union[
            dict, frozendict, list, tuple, decimal.Decimal, float, int, str, date, datetime, bool, None, 'Schema'],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Union[
            dict, frozendict, list, tuple, decimal.Decimal, float, int, str, date, datetime, bool, None, 'Schema', Unset
        ]
    ):
        """
        this is needed to fix 'Unexpected argument' warning in pycharm
        this code does nothing because all Schema instances are immutable
        this means that all input data is passed into and used in new, and after the new instance is made
        no new attributes are assigned and init is not used
        """
        pass


def cast_to_allowed_types(arg: typing.Union[str, date, datetime, decimal.Decimal, int, float, None, dict, frozendict, list, tuple, bytes, Schema], from_server=False) -> typing.Union[str, bytes, decimal.Decimal, None, frozendict, tuple, Schema]:
    """
    from_server=False date, datetime -> str
    int, float -> Decimal
    StrSchema will convert that to bytes and remember the encoding when we pass in str input
    """
    if isinstance(arg, (date, datetime)):
        if not from_server:
            return arg.isoformat()
        # ApiTypeError will be thrown later by _validate_type
        return arg
    elif isinstance(arg, bool):
        """
        this check must come before isinstance(arg, (int, float))
        because isinstance(True, int) is True
        """
        return arg
    elif isinstance(arg, decimal.Decimal):
        return arg
    elif isinstance(arg, int):
        return decimal.Decimal(arg)
    elif isinstance(arg, float):
        decimal_from_float = decimal.Decimal(arg)
        if decimal_from_float.as_integer_ratio()[1] == 1:
            # 9.0 -> Decimal('9.0')
            # 3.4028234663852886e+38 -> Decimal('340282346638528859811704183484516925440.0')
            return decimal.Decimal(str(decimal_from_float)+'.0')
        return decimal_from_float
    elif isinstance(arg, str):
        return arg
    elif isinstance(arg, bytes):
        return arg
    elif isinstance(arg, (io.FileIO, io.BufferedReader)):
        if arg.closed:
            raise ApiValueError('Invalid file state; file is closed and must be open')
        return arg
    elif type(arg) is list or type(arg) is tuple:
        return tuple([cast_to_allowed_types(item) for item in arg])
    elif type(arg) is dict or type(arg) is frozendict:
        return frozendict({key: cast_to_allowed_types(val) for key, val in arg.items() if val is not unset})
    elif arg is None:
        return arg
    elif isinstance(arg, Schema):
        return arg
    raise ValueError('Invalid type passed in got input={} type={}'.format(arg, type(arg)))


class ComposedBase(Discriminable):

    @classmethod
    def __get_allof_classes(cls, *args, _instantiation_metadata: InstantiationMetadata):
        path_to_schemas = defaultdict(set)
        for allof_cls in cls._composed_schemas['allOf']:
            if allof_cls in _instantiation_metadata.base_classes:
                continue
            other_path_to_schemas = allof_cls._validate(*args, _instantiation_metadata=_instantiation_metadata)
            update(path_to_schemas, other_path_to_schemas)
        return path_to_schemas

    @classmethod
    def __get_oneof_class(
        cls,
        *args,
        discriminated_cls,
        _instantiation_metadata: InstantiationMetadata,
        path_to_schemas: typing.Dict[typing.Tuple, typing.Set[typing.Type[Schema]]]
    ):
        oneof_classes = []
        chosen_oneof_cls = None
        original_base_classes = _instantiation_metadata.base_classes
        new_base_classes = _instantiation_metadata.base_classes
        path_to_schemas = defaultdict(set)
        for oneof_cls in cls._composed_schemas['oneOf']:
            if oneof_cls in path_to_schemas[_instantiation_metadata.path_to_item]:
                oneof_classes.append(oneof_cls)
                continue
            if isinstance(args[0], oneof_cls):
                # passed in instance is the correct type
                chosen_oneof_cls = oneof_cls
                oneof_classes.append(oneof_cls)
                continue
            _instantiation_metadata.base_classes = original_base_classes
            try:
                path_to_schemas = oneof_cls._validate(*args, _instantiation_metadata=_instantiation_metadata)
                new_base_classes = _instantiation_metadata.base_classes
            except (ApiValueError, ApiTypeError) as ex:
                if discriminated_cls is not None and oneof_cls is discriminated_cls:
                    raise ex
                continue
            chosen_oneof_cls = oneof_cls
            oneof_classes.append(oneof_cls)
        if not oneof_classes:
            raise ApiValueError(
                "Invalid inputs given to generate an instance of {}. None "
                "of the oneOf schemas matched the input data.".format(cls)
            )
        elif len(oneof_classes) > 1:
            raise ApiValueError(
                "Invalid inputs given to generate an instance of {}. Multiple "
                "oneOf schemas {} matched the inputs, but a max of one is allowed.".format(cls, oneof_classes)
            )
        _instantiation_metadata.base_classes = new_base_classes
        return path_to_schemas

    @classmethod
    def __get_anyof_classes(
        cls,
        *args,
        discriminated_cls,
        _instantiation_metadata: InstantiationMetadata
    ):
        anyof_classes = []
        chosen_anyof_cls = None
        original_base_classes = _instantiation_metadata.base_classes
        path_to_schemas = defaultdict(set)
        for anyof_cls in cls._composed_schemas['anyOf']:
            if anyof_cls in _instantiation_metadata.base_classes:
                continue
            if isinstance(args[0], anyof_cls):
                # passed in instance is the correct type
                chosen_anyof_cls = anyof_cls
                anyof_classes.append(anyof_cls)
                continue

            _instantiation_metadata.base_classes = original_base_classes
            try:
                other_path_to_schemas = anyof_cls._validate(*args, _instantiation_metadata=_instantiation_metadata)
            except (ApiValueError, ApiTypeError) as ex:
                if discriminated_cls is not None and anyof_cls is discriminated_cls:
                    raise ex
                continue
            original_base_classes = _instantiation_metadata.base_classes
            chosen_anyof_cls = anyof_cls
            anyof_classes.append(anyof_cls)
            update(path_to_schemas, other_path_to_schemas)
        if not anyof_classes:
            raise ApiValueError(
                "Invalid inputs given to generate an instance of {}. None "
                "of the anyOf schemas matched the input data.".format(cls)
            )
        return path_to_schemas

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        ComposedBase _validate
        We return dynamic classes of different bases depending upon the inputs
        This makes it so:
        - the returned instance is always a subclass of our defining schema
            - this allows us to check type based on whether an instance is a subclass of a schema
        - the returned instance is a serializable type (except for None, True, and False) which are enums

        Returns:
            new_cls (type): the new class

        Raises:
            ApiValueError: when a string can't be converted into a date or datetime and it must be one of those classes
            ApiTypeError: when the input type is not in the list of allowed spec types
        """
        if args and isinstance(args[0], Schema) and _instantiation_metadata.from_server is False:
            if isinstance(args[0], cls):
                # an instance of the correct type was passed in
                return {}
            raise ApiTypeError(
                'Incorrect type passed in, required type was {} and passed type was {} at {}'.format(
                    cls,
                    type(args[0]),
                    _instantiation_metadata.path_to_item
                )
            )

        # validation checking on types, validations, and enums
        path_to_schemas = super()._validate(*args, _instantiation_metadata=_instantiation_metadata)

        _instantiation_metadata.base_classes |= frozenset({cls})

        # process composed schema
        _discriminator = getattr(cls, '_discriminator', None)
        discriminated_cls = None
        if _discriminator and args and isinstance(args[0], frozendict):
            disc_property_name = list(_discriminator.keys())[0]
            cls._ensure_discriminator_value_present(disc_property_name, _instantiation_metadata, *args)
            # get discriminated_cls by looking at the dict in the current class
            discriminated_cls = cls._get_discriminated_class(
                disc_property_name=disc_property_name, disc_payload_value=args[0][disc_property_name])
            if discriminated_cls is None:
                raise ApiValueError(
                    "Invalid discriminator value '{}' was passed in to {}.{} Only the values {} are allowed at {}".format(
                        args[0][disc_property_name],
                        cls.__name__,
                        disc_property_name,
                        list(_discriminator[disc_property_name].keys()),
                        _instantiation_metadata.path_to_item + (disc_property_name,)
                    )
                )

        if cls._composed_schemas['allOf']:
            other_path_to_schemas = cls.__get_allof_classes(*args, _instantiation_metadata=_instantiation_metadata)
            update(path_to_schemas, other_path_to_schemas)
        if cls._composed_schemas['oneOf']:
            other_path_to_schemas = cls.__get_oneof_class(
                *args,
                discriminated_cls=discriminated_cls,
                _instantiation_metadata=_instantiation_metadata,
                path_to_schemas=path_to_schemas
            )
            update(path_to_schemas, other_path_to_schemas)
        if cls._composed_schemas['anyOf']:
            other_path_to_schemas = cls.__get_anyof_classes(
                *args,
                discriminated_cls=discriminated_cls,
                _instantiation_metadata=_instantiation_metadata
            )
            update(path_to_schemas, other_path_to_schemas)

        if discriminated_cls is not None:
            # TODO use an exception from this package here
            assert discriminated_cls in path_to_schemas[_instantiation_metadata.path_to_item]
        return path_to_schemas


# DictBase, ListBase, NumberBase, StrBase, BoolBase, NoneBase
class ComposedSchema(
    _SchemaTypeChecker(typing.Union[none_type, str, decimal.Decimal, bool, tuple, frozendict]),
    ComposedBase,
    DictBase,
    ListBase,
    NumberBase,
    StrBase,
    BoolBase,
    NoneBase,
    Schema
):

    # subclass properties
    _composed_schemas = {}

    @classmethod
    def _from_openapi_data(cls, *args: typing.Any, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None, **kwargs):
        if not args:
            if not kwargs:
                raise ApiTypeError('{} is missing required input data in args or kwargs'.format(cls.__name__))
            args = (kwargs, )
        return super()._from_openapi_data(args[0], _instantiation_metadata=_instantiation_metadata)


class ListSchema(
    _SchemaTypeChecker(typing.Union[tuple]),
    ListBase,
    Schema
):

    @classmethod
    def _from_openapi_data(cls, arg: typing.List[typing.Any], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, arg: typing.Union[list, tuple], **kwargs: InstantiationMetadata):
        return super().__new__(cls, arg, **kwargs)


class NoneSchema(
    _SchemaTypeChecker(typing.Union[none_type]),
    NoneBase,
    Schema
):

    @classmethod
    def _from_openapi_data(cls, arg: None, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, arg: None, **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class NumberSchema(
    _SchemaTypeChecker(typing.Union[decimal.Decimal]),
    NumberBase,
    Schema
):
    """
    This is used for type: number with no format
    Both integers AND floats are accepted
    """

    @classmethod
    def _from_openapi_data(cls, arg: typing.Union[int, float, decimal.Decimal], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, arg: typing.Union[decimal.Decimal, int, float], **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class IntBase(NumberBase):
    @property
    def as_int(self) -> int:
        try:
            return self._as_int
        except AttributeError:
            self._as_int = int(self)
            return self._as_int

    @classmethod
    def _validate_format(cls, arg: typing.Optional[decimal.Decimal], _instantiation_metadata: InstantiationMetadata):
        if isinstance(arg, decimal.Decimal):
            exponent = arg.as_tuple().exponent
            if exponent != 0:
                raise ApiValueError(
                    "Invalid value '{}' for type integer at {}".format(arg, _instantiation_metadata.path_to_item)
                )

    @classmethod
    def _validate(cls, *args, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        """
        IntBase _validate
        TODO what about types = (int, number) -> IntBase, NumberBase? We could drop int and keep number only
        """
        cls._validate_format(args[0], _instantiation_metadata=_instantiation_metadata)
        return super()._validate(*args, _instantiation_metadata=_instantiation_metadata)


class IntSchema(IntBase, NumberSchema):

    @classmethod
    def _from_openapi_data(cls, arg: int, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, arg: typing.Union[decimal.Decimal, int], **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class Int32Base(
    _SchemaValidator(
        inclusive_minimum=decimal.Decimal(-2147483648),
        inclusive_maximum=decimal.Decimal(2147483647)
    ),
):
    pass


class Int32Schema(
    Int32Base,
    IntSchema
):
    pass


class Int64Base(
    _SchemaValidator(
        inclusive_minimum=decimal.Decimal(-9223372036854775808),
        inclusive_maximum=decimal.Decimal(9223372036854775807)
    ),
):
    pass


class Int64Schema(
    Int64Base,
    IntSchema
):
    pass


class Float32Base(
    _SchemaValidator(
        inclusive_minimum=decimal.Decimal(-3.4028234663852886e+38),
        inclusive_maximum=decimal.Decimal(3.4028234663852886e+38)
    ),
):
    pass


class Float32Schema(
    Float32Base,
    NumberSchema
):

    @classmethod
    def _from_openapi_data(cls, arg: typing.Union[float, decimal.Decimal], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        # todo check format
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)


class Float64Base(
    _SchemaValidator(
        inclusive_minimum=decimal.Decimal(-1.7976931348623157E+308),
        inclusive_maximum=decimal.Decimal(1.7976931348623157E+308)
    ),
):
    pass


class Float64Schema(
    Float64Base,
    NumberSchema
):

    @classmethod
    def _from_openapi_data(cls, arg: typing.Union[float, decimal.Decimal], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        # todo check format
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)


class StrSchema(
    _SchemaTypeChecker(typing.Union[str]),
    StrBase,
    Schema
):
    """
    date + datetime string types must inherit from this class
    That is because one can validate a str payload as both:
    - type: string (format unset)
    - type: string, format: date
    """

    @classmethod
    def _from_openapi_data(cls, arg: typing.Union[str], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None) -> 'StrSchema':
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, arg: typing.Union[str, date, datetime], **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class DateSchema(DateBase, StrSchema):

    def __new__(cls, arg: typing.Union[str, datetime], **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class DateTimeSchema(DateTimeBase, StrSchema):

    def __new__(cls, arg: typing.Union[str, datetime], **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class DecimalSchema(DecimalBase, StrSchema):

    def __new__(cls, arg: typing.Union[str], **kwargs: typing.Union[InstantiationMetadata]):
        """
        Note: Decimals may not be passed in because cast_to_allowed_types is only invoked once for payloads
        which can be simple (str) or complex (dicts or lists with nested values)
        Because casting is only done once and recursively casts all values prior to validation then for a potential
        client side Decimal input if Decimal was accepted as an input in DecimalSchema then one would not know
        if one was using it for a StrSchema (where it should be cast to str) or one is using it for NumberSchema
        where it should stay as Decimal.
        """
        return super().__new__(cls, arg, **kwargs)


class BytesSchema(
    _SchemaTypeChecker(typing.Union[bytes]),
    Schema,
):
    """
    this class will subclass bytes and is immutable
    """
    def __new__(cls, arg: typing.Union[bytes], **kwargs: typing.Union[InstantiationMetadata]):
        return super(Schema, cls).__new__(cls, arg)


class FileSchema(
    _SchemaTypeChecker(typing.Union[FileIO]),
    Schema,
):
    """
    This class is NOT immutable
    Dynamic classes are built using it for example when AnyType allows in binary data
    Al other schema classes ARE immutable
    If one wanted to make this immutable one could make this a DictSchema with required properties:
    - data = BytesSchema (which would be an immutable bytes based schema)
    - file_name = StrSchema
    and cast_to_allowed_types would convert bytes and file instances into dicts containing data + file_name
    The downside would be that data would be stored in memory which one may not want to do for very large files

    The developer is responsible for closing this file and deleting it

    This class was kept as mutable:
    - to allow file reading and writing to disk
    - to be able to preserve file name info
    """

    def __new__(cls, arg: typing.Union[io.FileIO, io.BufferedReader], **kwargs: typing.Union[InstantiationMetadata]):
        return super(Schema, cls).__new__(cls, arg)


class BinaryBase:
    pass


class BinarySchema(
    _SchemaTypeChecker(typing.Union[bytes, FileIO]),
    ComposedBase,
    BinaryBase,
    Schema,
):

    @classmethod
    @property
    def _composed_schemas(cls):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
            'allOf': [],
            'oneOf': [
                BytesSchema,
                FileSchema,
            ],
            'anyOf': [
            ],
        }

    def __new__(cls, arg: typing.Union[io.FileIO, io.BufferedReader, bytes], **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg)


class BoolSchema(
    _SchemaTypeChecker(typing.Union[bool]),
    BoolBase,
    Schema
):

    @classmethod
    def _from_openapi_data(cls, arg: bool, _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, arg: bool, **kwargs: typing.Union[InstantiationMetadata]):
        return super().__new__(cls, arg, **kwargs)


class AnyTypeSchema(
    _SchemaTypeChecker(
        typing.Union[frozendict, tuple, decimal.Decimal, str, bool, none_type, bytes, FileIO]
    ),
    DictBase,
    ListBase,
    NumberBase,
    StrBase,
    BoolBase,
    NoneBase,
    Schema
):
    pass


class DictSchema(
    _SchemaTypeChecker(typing.Union[frozendict]),
    DictBase,
    Schema
):

    @classmethod
    def _from_openapi_data(cls, arg: typing.Dict[str, typing.Any], _instantiation_metadata: typing.Optional[InstantiationMetadata] = None):
        return super()._from_openapi_data(arg, _instantiation_metadata=_instantiation_metadata)

    def __new__(cls, *args: typing.Union[dict, frozendict], **kwargs: typing.Union[dict, frozendict, list, tuple, decimal.Decimal, float, int, str, date, datetime, bool, None, bytes, Schema, Unset, InstantiationMetadata]):
        return super().__new__(cls, *args, **kwargs)


schema_descendents = set([NoneSchema, DictSchema, ListSchema, NumberSchema, StrSchema, BoolSchema])


def deserialize_file(response_data, configuration, content_disposition=None):
    """Deserializes body to file

    Saves response body into a file in a temporary folder,
    using the filename from the `Content-Disposition` header if provided.

    Args:
        param response_data (str):  the file data to write
        configuration (Configuration): the instance to use to convert files

    Keyword Args:
        content_disposition (str):  the value of the Content-Disposition
            header

    Returns:
        (file_type): the deserialized file which is open
            The user is responsible for closing and reading the file
    """
    fd, path = tempfile.mkstemp(dir=configuration.temp_folder_path)
    os.close(fd)
    os.remove(path)

    if content_disposition:
        filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                             content_disposition).group(1)
        path = os.path.join(os.path.dirname(path), filename)

    with open(path, "wb") as f:
        if isinstance(response_data, str):
            # change str to bytes so we can write it
            response_data = response_data.encode('utf-8')
        f.write(response_data)

    f = open(path, "rb")
    return f


@functools.cache
def get_new_class(
    class_name: str,
    bases: typing.Tuple[typing.Type[typing.Union[Schema, typing.Any]], ...]
) -> typing.Type[Schema]:
    """
    Returns a new class that is made with the subclass bases
    """
    return type(class_name, bases, {})


LOG_CACHE_USAGE = False


def log_cache_usage(cache_fn):
    if LOG_CACHE_USAGE:
        print(cache_fn.__name__, cache_fn.cache_info())
