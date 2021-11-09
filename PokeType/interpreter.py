from typing import Any, Tuple, Union
from poketype.lexer import PokeLexer
from poketype.compiler import PokeParser
from poketype.lexer.tokens import data_type_tokens, tokens_normal
from poketype.errors import SyntaxError
from rply.errors import LexingError, ParsingError

class PokeType:

	def __init__(self) -> None:
	    self.lexer = PokeLexer().get_lexer()
	    self.parser = PokeParser().get_compiler()

	def eval(self, code: str) -> Union[str, int]:
		self.check_syntax(code)
		return (self.parser.parse(self.lexer.lex(code))).eval()

	def compile(self, code: str) -> str:
		self.check_syntax(code)
		code_str = ""
		for tok in self.lexer.lex(code):
			tok_type = tok.gettokentype()
			if tok_type in data_type_tokens:
				if tok_type == "BOOLEAN":
					code_str += str(tok.value == "true")
				else:
					code_str += str(tok.value)
			elif tokens_normal.get(tok_type):
				code_str += tokens_normal[tok_type]
			else:
				raise ValueError("Unknown token")
		return code_str

	def compile_and_eval(self, code: str) -> Any:
		return eval(self.compile(code))

	def _check_syntax(self, code: str) -> Tuple[bool, str]:
		try:
			self.parser.parse(self.lexer.lex(code))
		except LexingError as e:
			return (False, f"Unkown Symbol `{code[e.source_pos.idx]}` caused error. Line {e.source_pos.lineno}, Column {e.source_pos.colno}")
		except ParsingError as e:
			return (False, f"Incorrect usage of symbol `{code[e.source_pos.idx]}` caused error. Line {e.source_pos.lineno}, Column {e.source_pos.colno}")
		else:
			return (True, "")

	def check_syntax(self, code: str):
		stat, out = self._check_syntax(code)
		if not stat:
			raise SyntaxError(out)
		


	def __repr__(self) -> str:
	      return "<PokeType.Interpreter>"