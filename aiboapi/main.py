from typing import Dict
from aiboapi.functions.fetch import Functions

class Aibo:
    def __init__(self, token) -> None:
        self.function = Functions(token)

    def get_devices(self) -> str:
        device_id = self.function.get_devices()
        return device_id

    def ask_action(self, API_NAME: str, arguments:str = '{}') -> Dict:
        """Main method for controlling aibo!!

        Args:
            API_NAME: ask_action(API_NAME = "xxxxxx")
            arguments (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """

        result = self.function.get_result_on_completion(API_NAME, arguments = None)
        return result