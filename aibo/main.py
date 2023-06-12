from aibo.functions.fetch import Functions
from typing import Dict


class Aibo:
    def __init__(self, token) -> None:
        self.token = token
        self.function = Functions(token)

    def aibo_control(self, API_NAME: str, arguments: Dict = None) -> Dict:
        """Main method for controlling aibo!!

        Args:
            API_NAME: aibo_control(API_NAME = "xxxxxx")
            arguments (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """

        self.function.get_result_on_completion(API_NAME, arguments)