from rply import ParserGenerator
from poketype.lexer import PokeLexer
from .data_types import DataTypes
from .maths import Maths
from .compare import Compare
from .functions import Functions

class PokeParser():

	def __init__(self) -> None:
	    self.parser = ParserGenerator(PokeLexer().get_token_list())
	    self.parse_all()
	    self.compiler = self.parser.build()

	def parse_all(self):
		DataTypes(self.parser)
		Maths(self.parser)
		Compare(self.parser)
		Functions(self.parser)

	def get_compiler(self):
		return self.compiler

