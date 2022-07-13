#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from .source_schema import ClariSchemas
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator


"""
TODO: Most comments in this class are instructive and should be deleted after the source is implemented.

This file provides a stubbed example of how to use the Airbyte CDK to develop both a source connector which supports full refresh or and an
incremental syncs from an HTTP API.

The various TODOs are both implementation hints and steps - fulfilling all the TODOs should be sufficient to implement one basic and one incremental
stream from a source. This pattern is the same one used by Airbyte internally to implement connectors.

The approach here is not authoritative, and devs are free to use their own judgement.

There are additional required TODOs in the files within the integration_tests folder and the spec.yaml file.
"""


# Basic full refresh stream
class ClariForecastStream(HttpStream, ABC):

    def __init__(self, config: Mapping[str, Any], **kwargs):
        super().__init__(kwargs["authenticator"])
        self.config = config
        self.schemas = ClariSchemas().get_schemas()
        self.header = {}
        self.params = {}
        self.response_data = {}

    def request_headers(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, Any] = None, next_page_token: Mapping[str, Any] = None
    ) -> Mapping[str, Any]:
        return {"apikey": self.config["apikey"]}

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        return None

    def request_params(
        self,
        stream_state: Mapping[str, Any],
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        """
        TODO: Override this method to define any query parameters to be set. Remove this method if you don't need to define request params.
        Usually contains common params e.g. pagination size etc.
        """
        for key_value in self.config.keys():
            if key_value not in ["apikey", "basePath","typesToExport"]:
                self.params.update({key_value: self.config[key_value]})
        
        if self.config["typesToExport"] == "default":
            pass
        elif self.config["typesToExport"] == "quota":
            self.params.update({"typesToExport": "quota"})
        
        return self.params

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        """
        TODO: Override this method to define how a response is parsed.
        :return an iterable containing each record in the response
        """
        if not self.response_data:
            self.response_data = response.json()
        else:
            pass
        return self.response_data

class Entries(ClariForecastStream):

    # primary key is not available in clari.
    primary_key = None

    def __init(self, config: Mapping[str, Any], **kwargs):
        super().__init__()
        self.config = config

    @property
    def url_base(self) -> str:
        return f"https://api.clari.com/{self.config.get('basePath', ' ')}/forecast/"
    
    def get_json_schema(self) -> Mapping[str, Any]:
        return self.schemas[f"{self.config['typesToExport']}_entries"]

    def path(self, **kwargs):
        return "forecast"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_data = super().parse_response(response, **kwargs)
        return response_data.get("entries", [])


class Users(ClariForecastStream):

    # primary key is not available in clari.
    primary_key = None

    def __init(self, config: Mapping[str, Any], **kwargs):
        super().__init__()

    @property
    def url_base(self) -> str:
        return f"https://api.clari.com/{self.config.get('basePath', ' ')}/forecast/"
    
    def get_json_schema(self) -> Mapping[str, Any]:
        return self.schemas[f"{self.config['typesToExport']}_users"]

    def path(self, **kwargs):
        return "forecast"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_data = super().parse_response(response, **kwargs)
        return response_data.get("users", [])


class Fields(ClariForecastStream):

    # primary key is not available in clari.
    primary_key = None

    def __init(self, config: Mapping[str, Any], **kwargs):
        super().__init__()

    @property
    def url_base(self) -> str:
        return f"https://api.clari.com/{self.config.get('basePath', ' ')}/forecast/"
    
    def get_json_schema(self) -> Mapping[str, Any]:
        return self.schemas[f"{self.config['typesToExport']}_fields"]

    def path(self, **kwargs):
        return "forecast"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_data = super().parse_response(response, **kwargs)
        return response_data.get("fields", [])


class Timeperiods(ClariForecastStream):

    # primary key is not available in clari.
    primary_key = None

    def __init(self, config: Mapping[str, Any], **kwargs):
        super().__init__()

    @property
    def url_base(self) -> str:
        return f"https://api.clari.com/{self.config.get('basePath', ' ')}/forecast/"
    
    def get_json_schema(self) -> Mapping[str, Any]:
        return self.schemas[f"{self.config['typesToExport']}_timeperiods"]

    def path(self, **kwargs):
        return "forecast"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_data = super().parse_response(response, **kwargs)
        return response_data.get("timePeriods", [])


class Timeframes(ClariForecastStream):

    # primary key is not available in clari.
    primary_key = None

    def __init(self, config: Mapping[str, Any], **kwargs):
        super().__init__()

    @property
    def url_base(self) -> str:
        return f"https://api.clari.com/{self.config.get('basePath', ' ')}/forecast/"
    
    def get_json_schema(self) -> Mapping[str, Any]:
        return self.schemas[f"{self.config['typesToExport']}_timeframes"]

    def path(self, **kwargs):
        return "forecast"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_data = super().parse_response(response, **kwargs)
        return response_data.get("timeFrames", [])

# Source
class SourceClariForecast(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        """
        TODO: Implement a connection check to validate that the user-provided config can be used to connect to the underlying API

        See https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-stripe/source_stripe/source.py#L232
        for an example.

        :param config:  the user-input config object conforming to the connector's spec.yaml
        :param logger:  logger object
        :return Tuple[bool, any]: (True, None) if the input config can be used to connect to the API successfully, (False, error) otherwise.
        """
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """
        TODO: Replace the streams below with your own streams.

        :param config: A Mapping of the user input configuration as defined in the connector spec.
        """
        # TODO remove the authenticator if not required.
        # auth = TokenAuthenticator(token="api_key")  # Oauth2Authenticator is also available if you need oauth support
        auth = TokenAuthenticator(token=config["apikey"])
        streams = [
            Entries(config, authenticator=auth),
            Users(config, authenticator=auth),
            Fields(config, authenticator=auth),
            Timeperiods(config, authenticator=auth),
            Timeframes(config, authenticator=auth)
        ]
        return streams
