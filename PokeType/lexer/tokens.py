tokens = {
	# Start With Datatypes
	"NUMBER": r"\d+",
	"BOOLEAN": r"true(?!\w)|false(?!\w)",
	# Arithmetic
	"ADD": r"\🔥",
	"SUB": r"\🌊",
	"MUL": r"\🪨",
	"DIV": r"\💨",
	"FLOORDIV": r"\⚡",
	"MODULO": r"\☠️",

	# Comparison
	"GREATER": r"\✊",
	"LESSER": r"\🔮",
	"EQUAL": r"\✨",
	"NOTEQUAL": r"\👻",
	"LESSEQUAL": r"\🐉",
	"GREATEQUAL": r"\🏝️",
	# Context
	"OPEN_PAREN": r"\(",
    "CLOSE_PAREN": r"\)",
    "OPEN_PARENE": r"\🧚",
    "CLOSE_PARENE": r"\🌌",
    "NEG": r"\-",
    # Funcs
    "ABS": r"\❄️",
    "LOG": r"\⛓",
    "EXP": r"\🐛"
}

ignore_tokens = [
	r'\s+',
]

data_type_tokens = ["NUMBER", "BOOLEAN"]

tokens_normal = {
	# Arithmetic
	"ADD": "+",
	"SUB": "-",
	"MUL": "*",
	"DIV": "/",
	"FLOORDIV": "//",
	"MODULO": "%",

	# Comparison
	"GREATER": ">",
	"LESSER": "<",
	"EQUAL": "==",
	"NOTEQUAL": "!=",
	"LESSEQUAL": "<=",
	"GREATEQUAL": ">=",
	# Context
	"OPEN_PAREN": "(",
    "CLOSE_PAREN": ")",
    "OPEN_PARENE": "(",
    "CLOSE_PARENE": ")",
    "NEG": "-",

    # Functions
    "EXP": "**",
    "ABS": "abs",
    "LOG": "__import__('math').log"

}