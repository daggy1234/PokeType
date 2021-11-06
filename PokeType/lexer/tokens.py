tokens = {
	# Start With Datatypes
	"NUMBER": r"\d+",
	"BOOLEAN": r"true(?!\w)|false(?!\w)",
	# Arithmetic
	"ADD": r"\♨",
	"SUB": r"\≋",
	"MUL": r"\ᨏ",
	"DIV": r"\༄",
}

ignore_tokens = [
	r'\s+',
	r'//.*'
	r"/\*([\n\r]|.)*\*/"
]