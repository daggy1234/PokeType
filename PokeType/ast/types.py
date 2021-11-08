from typing import Any, TypeVar
from rply.token import BaseBox


class BaseType(BaseBox):
	def __init__(self,value ,d_type: str) -> None:
		self.value: T = value
		self.type = d_type

	def get_type(self) -> str:
		return f"<PokeType.{self.type}>"

	def eval(self):
		return self.value


class Number(BaseType):
	def __init__(self, value: int) -> None:
	    super().__init__(value, "number")

class NegNumber(BaseType):
	def __init__(self, value: int) -> None:
	    super().__init__(value, "number")

class Boolean(BaseType):
	def __init__(self, value: int) -> None:
	    super().__init__(value, "bool")