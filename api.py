import requests
import validators
from typing import TypedDict, Self, Any, List, Union, cast 


class ApiResponseElementType(TypedDict):
    id: str
    symbol: str
    name: str
    current_price: Union[float, int]
    market_cap: Union[float, int]


ApiResponseType = List[ApiResponseElementType]


class FetchRequest:
    def __test_api_url(self: Self, api_to_fetch: str):
        if not isinstance(api_to_fetch, str):
            raise ValueError("please send a url as str")
        if not validators.url(api_to_fetch):
            raise ValueError("please send url")
        return api_to_fetch
    
    def __test_api_status(self: Self, status_code: int):
        if not isinstance(status_code, int):
            raise ValueError("please send integer")
        if 200 <= status_code < 300:
            return True

    def get(self:Self, api_to_fetch:str):
        self.api_to_fetch = self.__test_api_url(api_to_fetch)
        response = requests.get(self.api_to_fetch)
        response_json: ApiResponseType = cast(ApiResponseType, response.json())
        if self.__test_api_status(response.status_code):
            return response