
from json import dumps

class Setting:
  def __init__(self):
    self.sharetime = ''
    self.price = ''
    self.over_price = ''


class ReturnValue:
  def __init__(self, status, msg, value):
    self.status = status
    self.msg = msg
    self.value = value
  
  def __repr__(self):
    test = {"status":self.status, "msg":self.msg, "value":self.value}
    return dumps(test)