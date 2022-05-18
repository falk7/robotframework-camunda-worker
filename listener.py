from robot.libraries.BuiltIn import BuiltIn

ROBOT_LISTENER_API_VERSION = 2


class getVariablesListener:
    ROBOT_LISTENER_API_VERSION = 2
    def __init__(self) -> None:
        self.camunda_result = {}

    def end_suite(self, name, attributes):
        self.camunda_result[name] = attributes

    def log_file(self, path):
        self.log_path = path
        
