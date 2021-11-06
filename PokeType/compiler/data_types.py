from rply import ParserGenerator
from PokeType.ast import Number, Boolean

class DataTypes():
	def __init__(self, pg: ParserGenerator) -> None:
		
		@pg.production('expression : NUMBER')
		def expression_number(p):
			return Number(int(p[0].getstr()))

		@pg.production('expression : BOOLEAN')
		def expression_number(p):
			b_val = p[0].getstr()

			if b_val == "true":
				return Boolean(True)
			else:
				return Boolean(False)


		