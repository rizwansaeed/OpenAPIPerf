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
from luisd.model.resource_list_of_property import ResourceListOfProperty

# query params


class EffectiveAtSchema(
    _SchemaValidator(
        max_length=256,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_\+:\.]+$',  # noqa: E501
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
    ) -> 'EffectiveAtSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class AsAtSchema(
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    DateTimeBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'AsAtSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class PageSchema(
    _SchemaValidator(
        max_length=500,
        min_length=1,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\+\/]*={0,3}$',  # noqa: E501
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
    ) -> 'PageSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class LimitSchema(
    _SchemaValidator(
        inclusive_maximum=5000,
        inclusive_minimum=1,
    ),
    _SchemaTypeChecker(typing.Union[none_type, decimal.Decimal, ]),
    Int32Base,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'LimitSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class ScopeSchema(
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
    ) -> 'ScopeSchema':
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
        'effectiveAt': EffectiveAtSchema,
        'asAt': AsAtSchema,
        'page': PageSchema,
        'limit': LimitSchema,
        'scope': ScopeSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_effective_at = api_client.QueryParameter(
    name="effectiveAt",
    style=api_client.ParameterStyle.FORM,
    schema=EffectiveAtSchema,
    explode=True,
)
request_query_as_at = api_client.QueryParameter(
    name="asAt",
    style=api_client.ParameterStyle.FORM,
    schema=AsAtSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_scope = api_client.QueryParameter(
    name="scope",
    style=api_client.ParameterStyle.FORM,
    schema=ScopeSchema,
    explode=True,
)
# path params


class IdentifierTypeSchema(
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'IdentifierTypeSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )


class IdentifierSchema(
    _SchemaTypeChecker(typing.Union[none_type, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
    ) -> 'IdentifierSchema':
        return super().__new__(
            cls,
            *args,
            _instantiation_metadata=_instantiation_metadata,
        )
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'identifierType': IdentifierTypeSchema,
        'identifier': IdentifierSchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_identifier_type = api_client.PathParameter(
    name="identifierType",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdentifierTypeSchema,
    required=True,
)
request_path_identifier = api_client.PathParameter(
    name="identifier",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdentifierSchema,
    required=True,
)
_path = '/api/instruments/{identifierType}/{identifier}/properties/list'
_method = 'GET'
_auth = [
    'oauth2',
]
SchemaFor200ResponseBodyTextPlain = ResourceListOfProperty
SchemaFor200ResponseBodyApplicationJson = ResourceListOfProperty
SchemaFor200ResponseBodyTextJson = ResourceListOfProperty


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


class ListInstrumentProperties(api_client.Api):

    def list_instrument_properties(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
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
        [EXPERIMENTAL] ListInstrumentProperties: Get instrument properties (with Pagination)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)

        _path_params = {}
        for parameter in (
            request_path_identifier_type,
            request_path_identifier,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        _query_params = []
        for parameter in (
            request_query_effective_at,
            request_query_as_at,
            request_query_page,
            request_query_limit,
            request_query_scope,
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
            path_params=_path_params,
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
