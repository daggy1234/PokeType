from rply import LexerGenerator
from rply.lexer import Lexer
from typing import Dict, List
from .tokens import tokens, ignore_tokens


class PokeLexer:
	lexer: LexerGenerator
	tokens: Dict[str, str]
	ignore_tokens: List[str]

	def __init__(self):
		self.lexer = LexerGenerator()
		self.tokens = tokens
		self.ignore_tokens = ignore_tokens

	def add_tokens(self):
		for key, value in self.tokens.items():
			self.lexer.add(key, value)
		for item in self.ignore_tokens:
			self.lexer.ignore(item)

	def get_token_list(self) -> List[str]:
		toks = []
		for key in self.tokens.keys():
			toks.append(key)
		return toks

	def get_lexer(self):
		self.add_tokens()
		return self.lexer.build()

