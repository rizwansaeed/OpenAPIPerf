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

from luisd.model.lusid_problem_details import LusidProblemDetails
from luisd.model.resource_list_of_participation import ResourceListOfParticipation
from luisd.model.lusid_validation_problem_details import LusidValidationProblemDetails
from luisd.model.participation_set_request import ParticipationSetRequest

from . import path

# body param
SchemaForRequestBodyApplicationJsonPatchjson = ParticipationSetRequest
SchemaForRequestBodyApplicationJson = ParticipationSetRequest
SchemaForRequestBodyTextJson = ParticipationSetRequest
SchemaForRequestBodyApplicationJson = ParticipationSetRequest


request_body_participation_set_request = api_client.RequestBody(
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
)
_auth = [
    'oauth2',
]
SchemaFor201ResponseBodyTextPlain = ResourceListOfParticipation
SchemaFor201ResponseBodyApplicationJson = ResourceListOfParticipation
SchemaFor201ResponseBodyTextJson = ResourceListOfParticipation


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor201ResponseBodyTextPlain,
        SchemaFor201ResponseBodyApplicationJson,
        SchemaFor201ResponseBodyTextJson,
    ]
    headers: Unset = unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextPlain),
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextJson),
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
    '201': _response_for_201,
    '400': _response_for_400,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'text/plain',
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _upsert_participations(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] = unset,
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        [EXPERIMENTAL] UpsertParticipations: Upsert Participation
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not unset:
            serialized_data = request_body_participation_set_request.serialize(body, content_type)
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


class UpsertParticipations(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def upsert_participations(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] = unset,
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._upsert_participations(
            body=body,
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
        body: typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] = unset,
        content_type: str = 'application/json-patch+json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._upsert_participations(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


