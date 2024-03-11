from requests import Response
import json

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannnot find cookie with name {cookie_name} in last responce"
        return response.cookies[cookie_name]
    
    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannnot find header with name {headers_name} in last responce"
        return response.cookies[headers_name]
    
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderERROR:
            assert False, f"Response is not in json format. response text in {response.text}"

        assert name in response_as_dict, f"Response name dosen't have name {name}"
        return response_as_dict[name]