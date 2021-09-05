from datetime import datetime
from logging import getLogger

class Loggable:
  """Directly interacts with the logging module"""

  def __init__(self, id, class_name):
    """
    Keyword arguments:
      class_name -- str -- the name of the descendant class.
      id -- str -- the logger object id in the logging module.
    """
    self._class_name = class_name
    self._log_id = id

  def _debug(self, function_name, message):
    to_log = "%s -- %s - %s() - DEBUG - %s" % (str(datetime.now()), self._class_name, function_name, message)
    getLogger(self._log_id).debug(to_log)

  def _error(self, function_name, message):
    to_log = "%s -- %s - %s() - ERROR - %s" % (str(datetime.now()), self._class_name, function_name, message)
    getLogger(self._log_id).error(to_log)

  def _info(self, function_name, message):
    to_log = "%s -- %s - %s() - INFO - %s" % (str(datetime.now()), self._class_name, function_name, message)
    getLogger(self._log_id).info(to_log)