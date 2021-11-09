from poketype.ast.types import Number, Boolean
from rply import ParserGenerator
from poketype.ast import Abs, Log, Exponent

class Functions():
	def __init__(self, pg: ParserGenerator) -> None:
		@pg.production('expression : LOG OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : LOG OPEN_PARENE expression CLOSE_PARENE')
		def function(p):
			return Log(p[2])

		@pg.production('expression : ABS OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : ABS OPEN_PARENE expression CLOSE_PARENE')
		def abs(p):
			return Abs(p[2])

		@pg.production('expression : expression EXP OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : expression EXP OPEN_PARENE expression CLOSE_PARENE')
		def exp(p):
			return Exponent(p[0], p[3])

		@pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
		@pg.production('expression : OPEN_PARENE expression CLOSE_PARENE')
		def parens(p):
			out = (p[1]).eval()
			if isinstance(out, int):
				return Number(out)
			elif isinstance(out, str):
				if out == "true":
					return Boolean(True)
				elif out == "false":
					return Boolean(False)
				else:
					raise ValueError(f'Error evaluating {p}')

			else:
				raise ValueError(f'Error evaluating {p}')