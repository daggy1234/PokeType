from rply.token import BaseBox
import math

class FuncOp(BaseBox):
    def __init__(self, value):
        self.value = value

class Log(FuncOp):
    def eval(self):
        return math.log(self.value.eval())

class Abs(FuncOp):
    def eval(self):
        return abs(self.value.eval())