import requests
import json
from typing import Dict
import time
import sys


class Aibo:
    def __init__(self, token) -> None:
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.get(
            "https://public.api.aibo.com/v1/devices", headers=self.headers
        )
        assert response.status_code == requests.codes.ok, sys.exit(
            "SyntaxError: invalid token!"
        )
        response_text = json.loads(response.text)
        self.device_Id = response_text["devices"][0]["deviceId"]

    def get_devices(self) -> str:
        device_id = self.device_Id
        return device_id

    def send_request(self, API_NAME: str, arguments) -> Dict:
        headers = self.headers
        endpoint = (
            "https://public.api.aibo.com/v1/devices/"
            + self.device_Id
            + "/capabilities/"
            + API_NAME
            + "/execute"
        )
        data = arguments
        print(data)
        response = requests.post(endpoint, headers=headers, data=data)
        response_text = json.loads(response.text)
        execution_Id = response_text["executionId"]
        status = response_text["status"]
        return {"status": status, "execution_Id": execution_Id}

    def send_get_request(self, execution_Id: str) -> Dict:
        headers = self.headers
        endpoint = f"https://public.api.aibo.com/v1/executions/{execution_Id}"
        response = requests.get(endpoint, headers=headers)
        response_text = json.loads(response.text)
        new_execution_Id = response_text["executionId"]
        new_status = response_text["status"]
        result = response_text["result"]
        return {
            "status": new_status,
            "execution_Id": new_execution_Id,
            "result": result,
        }

    def ask_action(self, API_NAME: str, arguments: str = '{}') -> Dict:
        while True:
            print('send_request......')
            send_request_response = self.send_request(API_NAME, arguments)
            send_request_execution_Id = send_request_response["execution_Id"]
            send_request_status = send_request_response["status"]
            if (
                send_request_status == "ACCEPTED"
                or send_request_status == "IN_PROGRESS"
            ):
                print(send_request_status)
                print('send_requested!!')
                break
            else:
                print('send_request')
                time.sleep(1.5)
        print('send_get_request.....')
        while True:
            send_get_request_response = self.send_get_request(send_request_execution_Id)
            send_get_request_status = send_get_request_response["status"]
            if send_get_request_status == "SUCCEEDED":
                return send_get_request_response["result"]
            else:
                time.sleep(2.5)
                print('send_get_request.....')


token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjExMSJ9.eyJzdWIiOiIxMTg3MGFmNS00MGI1LTRkNDAtOTM5MC0xN2NlYTA2ZjQ1ZDgiLCJleHAiOjE2ODY4ODg5OTEsImlzcyI6Imh0dHBzOi8vcHVibGljLmFwaS5haWJvLmNvbSIsImF1ZCI6IjQ1LjU0NzA2MTA2NzUyMDgxOTIiLCJqdGkiOiIwYjQxOThmNC1jOWRiLTQxMDMtODRjNi00N2E3ODVhMzgwNjkiLCJpYXQiOjE2ODY4MDI1OTF9.ffJP_nxdB3sm6nAD4ENw8gw1fqsiU2n6fNYXmP3QrCXc3I3y7mMB70Rw3TXL_nuwcRdbgtxjXlE8F9J-k_-szNtYS5x-HlGGoB2tIGTqZzR8FBJc6EJU8pAPYq8-2pqbxKezkgPF5gsbheRroqqAO9clugozqxT7BPElmVXEDAR84mdtiCIzH0E-2Zb-N0GNJQuIi1jFAFzE4ZNF0JdCnYF0xcUJWqOl81QepK4ShtRcucPig1w8LEbp-IIQTLgZ1oqz8i0eDKEg3wl_4hRFBnCRXDfrC65FA26eAqlOVtadXVD1qjQt7wELVXH3o26Zfo3IFm3b40fQLPMfIzYX4g'
a = Aibo(token)
print(a.ask_action(API_NAME='play_motion',arguments='{"arguments":{"Category":"bark","Mode":"NONE"}}'))
print(a.ask_action(API_NAME='play_motion',arguments='{"arguments":{"Category":"bark","Mode":"NONE"}}'))
print(a.ask_action(API_NAME='play_motion',arguments='{"arguments":{"Category":"bark","Mode":"NONE"}}'))
print(a.ask_action(API_NAME='play_motion',arguments='{"arguments":{"Category":"bark","Mode":"NONE"}}'))
print(a.ask_action(API_NAME='play_motion',arguments='{"arguments":{"Category":"bark","Mode":"NONE"}}'))
print(a.ask_action(API_NAME='play_motion',arguments='{"arguments":{"Category":"bark","Mode":"NONE"}}'))
