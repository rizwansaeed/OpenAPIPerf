# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
from urllib3._collections import HTTPHeaderDict

from luisd import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from luisd.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    InstantiationMetadata,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.resource_list_of_fee_calculation_details import ResourceListOfFeeCalculationDetails

# query params


class InstrumentIdentifierTypeSchema(
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'InstrumentIdentifierTypeSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class InstrumentIdentifierSchema(
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'InstrumentIdentifierSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class PortfolioScopeSchema(
    _SchemaValidator(
        max_length=64,
        min_length=1,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }],
    ),
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'PortfolioScopeSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class PortfolioCodeSchema(
    _SchemaValidator(
        max_length=64,
        min_length=1,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }],
    ),
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'PortfolioCodeSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class AdditionalSearchKeysSchema(
    _SchemaTypeChecker(typing.Union[tuple, none_type, ]),
    ListBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'AdditionalSearchKeysSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class FileNameSchema(
    _SchemaValidator(
        regex=[{
            'pattern': r'^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$',  # noqa: E501
        }],
    ),
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'FileNameSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'instrumentIdentifierType': InstrumentIdentifierTypeSchema,
        'instrumentIdentifier': InstrumentIdentifierSchema,
        'portfolioScope': PortfolioScopeSchema,
        'portfolioCode': PortfolioCodeSchema,
        'additionalSearchKeys': AdditionalSearchKeysSchema,
        'fileName': FileNameSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_instrument_identifier_type = api_client.QueryParameter(
    name="instrumentIdentifierType",
    style=api_client.ParameterStyle.FORM,
    schema=InstrumentIdentifierTypeSchema,
    explode=True,
)
request_query_instrument_identifier = api_client.QueryParameter(
    name="instrumentIdentifier",
    style=api_client.ParameterStyle.FORM,
    schema=InstrumentIdentifierSchema,
    explode=True,
)
request_query_portfolio_scope = api_client.QueryParameter(
    name="portfolioScope",
    style=api_client.ParameterStyle.FORM,
    schema=PortfolioScopeSchema,
    explode=True,
)
request_query_portfolio_code = api_client.QueryParameter(
    name="portfolioCode",
    style=api_client.ParameterStyle.FORM,
    schema=PortfolioCodeSchema,
    explode=True,
)
request_query_additional_search_keys = api_client.QueryParameter(
    name="additionalSearchKeys",
    style=api_client.ParameterStyle.FORM,
    schema=AdditionalSearchKeysSchema,
    explode=True,
)
request_query_file_name = api_client.QueryParameter(
    name="fileName",
    style=api_client.ParameterStyle.FORM,
    schema=FileNameSchema,
    explode=True,
)
_path = '/api/feesandcommissions'
_method = 'GET'
_auth = [
    'oauth2',
]
SchemaFor200ResponseBodyTextPlain = ResourceListOfFeeCalculationDetails
SchemaFor200ResponseBodyApplicationJson = ResourceListOfFeeCalculationDetails
SchemaFor200ResponseBodyTextJson = ResourceListOfFeeCalculationDetails


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyTextPlain,
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyTextJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
    },
)
SchemaFor400ResponseBodyTextPlain = LusidValidationProblemDetails
SchemaFor400ResponseBodyApplicationJson = LusidValidationProblemDetails
SchemaFor400ResponseBodyTextJson = LusidValidationProblemDetails


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyTextPlain,
        SchemaFor400ResponseBodyApplicationJson,
        SchemaFor400ResponseBodyTextJson,
    ]
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = LusidProblemDetails


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'text/plain',
    'application/json',
    'text/json',
)


class GetApplicableFees(api_client.Api):

    def get_applicable_fees(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)

        _query_params = []
        for parameter in (
            request_query_instrument_identifier_type,
            request_query_instrument_identifier,
            request_query_portfolio_scope,
            request_query_portfolio_code,
            request_query_additional_search_keys,
            request_query_file_name,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _query_params.extend(serialized_data)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            query_params=tuple(_query_params),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                default_response = _status_code_to_response.get('default')
                if default_response:
                    api_response = default_response.deserialize(response, self.api_client.configuration)
                else:
                    api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
