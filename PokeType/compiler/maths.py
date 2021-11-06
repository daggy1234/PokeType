from rply import ParserGenerator
from PokeType.ast import Add, Sub, Div, Mul

class Maths():

	def __init__(self, pg: ParserGenerator) -> None:
		@pg.production('expression : expression ADD expression')
		@pg.production('expression : expression SUB expression')
		@pg.production('expression : expression MUL expression')
		@pg.production('expression : expression DIV expression')
		def expression_binop(p):
		    left = p[0]
		    right = p[2]
		    if p[1].gettokentype() == 'ADD':
		        return Add(left, right)
		    elif p[1].gettokentype() == 'SUB':
		        return Sub(left, right)
		    elif p[1].gettokentype() == 'MUL':
		        return Mul(left, right)
		    elif p[1].gettokentype() == 'DIV':
		        return Div(left, right)
		    else:
		        raise AssertionError('Oops, this should not be possible!')