from rply import ParserGenerator
from PokeType.ast import Lesser, Greater, Equal, NotEqual

class Compare():

	def __init__(self, pg: ParserGenerator) -> None:
		@pg.production('expression : expression GREATER expression')
		@pg.production('expression : expression LESSER expression')
		@pg.production('expression : expression EQUAL expression')
		@pg.production('expression : expression NOTEQUAL expression')
		def expression_equal(p):
		    left = p[0]
		    right = p[2]
		    if p[1].gettokentype() == 'GREATER':
		        return Greater(left, right)
		    elif p[1].gettokentype() == 'LESSER':
		        return Lesser(left, right)
		    elif p[1].gettokentype() == 'EQUAL':
		        return Equal(left, right)
		    elif p[1].gettokentype() == 'NOTEQUAL':
		        return NotEqual(left, right)
		    else:
		        raise AssertionError('Oops, this should not be possible!')