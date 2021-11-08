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
	"GREATER": r"\✊",
	"LESSER": r"\🔮",
	"EQUAL": r"\✨",
	"NOTEQUAL": r"\👻",
	# Context
	"OPEN_PAREN": r"\(",
    "CLOSE_PAREN": r"\)",
    "OPEN_PARENE": r"\🧚",
    "CLOSE_PARENE": r"\🌌",
    "NEG": r"\-",
    # Funcs
    "ABS": r"\❄️",
    "LOG": r"\⛓"
}

ignore_tokens = [
	r'\s+',
]