# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
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
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
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
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    NoneClass,
    BoolClass,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from luisd.model.instrument_search_property import InstrumentSearchProperty
from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.instrument_match import InstrumentMatch
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails

from . import path

# query params


class MasteredEffectiveAtSchema(
    _SchemaTypeChecker(typing.Union[NoneClass, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _configuration: typing.Optional[Configuration] = None,
    ) -> 'MasteredEffectiveAtSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
MasteredOnlySchema = BoolSchema


class ScopeSchema(
    _SchemaValidator(
        max_length=64,
        min_length=1,
        regex=[{
            'pattern': r'^[a-zA-Z0-9\-_]+$',  # noqa: E501
        }],
    ),
    _SchemaTypeChecker(typing.Union[NoneClass, str, ]),
    StrBase,
    NoneBase,
    Schema
):

    def __new__(
        cls,
        *args: typing.Union[str, None, ],
        _configuration: typing.Optional[Configuration] = None,
    ) -> 'ScopeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'masteredEffectiveAt': MasteredEffectiveAtSchema,
        'masteredOnly': MasteredOnlySchema,
        'scope': ScopeSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_mastered_effective_at = api_client.QueryParameter(
    name="masteredEffectiveAt",
    style=api_client.ParameterStyle.FORM,
    schema=MasteredEffectiveAtSchema,
    explode=True,
)
request_query_mastered_only = api_client.QueryParameter(
    name="masteredOnly",
    style=api_client.ParameterStyle.FORM,
    schema=MasteredOnlySchema,
    explode=True,
)
request_query_scope = api_client.QueryParameter(
    name="scope",
    style=api_client.ParameterStyle.FORM,
    schema=ScopeSchema,
    explode=True,
)
# body param


class SchemaForRequestBodyApplicationJsonPatchjson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentSearchProperty']:
        return InstrumentSearchProperty


class SchemaForRequestBodyApplicationJson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentSearchProperty']:
        return InstrumentSearchProperty


class SchemaForRequestBodyTextJson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentSearchProperty']:
        return InstrumentSearchProperty


class SchemaForRequestBodyApplicationJson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentSearchProperty']:
        return InstrumentSearchProperty


request_body_instrument_search_property = api_client.RequestBody(
    content={
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'oauth2',
]


class SchemaFor200ResponseBodyTextPlain(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentMatch']:
        return InstrumentMatch


class SchemaFor200ResponseBodyApplicationJson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentMatch']:
        return InstrumentMatch


class SchemaFor200ResponseBodyTextJson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['InstrumentMatch']:
        return InstrumentMatch


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


class BaseApi(api_client.Api):

    def _instruments_search(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson],
        query_params: RequestQueryParams = frozendict(),
        content_type: str = 'application/json-patch+json',
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
        [EXPERIMENTAL] InstrumentsSearch: Instruments search
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_mastered_effective_at,
            request_query_mastered_only,
            request_query_scope,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_instrument_search_property.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
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


class InstrumentsSearch(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def instruments_search(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson],
        query_params: RequestQueryParams = frozendict(),
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._instruments_search(
            body=body,
            query_params=query_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson],
        query_params: RequestQueryParams = frozendict(),
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._instruments_search(
            body=body,
            query_params=query_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


