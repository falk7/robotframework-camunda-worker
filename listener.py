from robot.libraries.BuiltIn import BuiltIn

ROBOT_LISTENER_API_VERSION = 2


class getVariablesListener:
  ROBOT_LISTENER_API_VERSION = 2
  def end_test(self, name, attributes):
    self.variables = BuiltIn().get_variables()
