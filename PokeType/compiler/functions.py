from PokeType.ast.types import Number
from rply import ParserGenerator
from PokeType.ast import Abs, Log

class Functions():
	def __init__(self, pg: ParserGenerator) -> None:
		@pg.production('expression : LOG OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : LOG OPEN_PARENE expression CLOSE_PARENE')
		def function(p):
			return Log(p[2].value)

		@pg.production('expression : ABS OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : ABS OPEN_PARENE expression CLOSE_PARENE')
		def abs(p):
			return Abs(p[2].value)

		@pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : OPEN_PARENE expression CLOSE_PARENE')
		def parens(p):
			out = (p[1]).eval()
			if isinstance(out, int):
				return Number(out)
			else:
				raise ValueError(f'Error evaluating {p}')