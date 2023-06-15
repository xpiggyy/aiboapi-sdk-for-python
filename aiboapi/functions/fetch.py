import requests
from typing import Dict
import json
import time
import sys


#test file

class Functions:
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

    def send_request(self, API_NAME: str, arguments: Dict = None) -> Dict:
        headers = self.headers
        endpoint = (
            "https://public.api.aibo.com/v1/devices/"
            + self.device_Id
            + "/capabilities/"
            + API_NAME
            + "/execute"
        )
        if arguments:
            data = '{"arguments":' + arguments + "}"
        else:
            data = "{}"
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

    def get_result_on_completion(self, API_NAME: str, arguments: Dict = None) -> Dict:
        while True:
            send_request_response = self.send_request(API_NAME, arguments)
            send_request_execution_Id = send_request_response["execution_Id"]
            send_request_status = send_request_response["status"]
            if (
                send_request_status == "ACCEPTED"
                or send_request_status == "IN_PROGRESS"
            ):
                time.sleep(3)
                break
            else:
                time.sleep(1.5)
                return False
        time.sleep(3)
        while True:
            send_get_request_response = self.send_get_request(send_request_execution_Id)
            send_get_request_status = send_get_request_response["status"]
            if send_get_request_status == "SUCCEEDED":
                break
            else:
                time.sleep(1.5)
                return False
        return send_get_request_response["result"]
