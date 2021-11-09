# PokeType

A simple mathematical expression evaluator that uses Pokemon types to replace symbols.

## Syntax

### Reference

| Symbol | Math Equivalent | Pokemon Type |
|--------|-----------------|--------------|
| **🔥**    | +               |    Fire      |
| **🌊**    | -               |    Water     |
| **🪨**    | *               |    Rock      |
| **💨**    | /               |    Flying    |
| **⚡**     | //              |    Electric  |
| **☠️**    | %               |    Poison    |
| **✊**    | >               |   Fighting   |
| **🔮**    | <               |    Psychic   |
| **✨**    | ==              |    Normal    |
| **👻**    | != 			  |     Ghost 	 |
| **🧚**    | (               |    Fairy     |
| **🌌**    | )               |    Dark      |
| **❄️()**  | abs()           |    Ice       |
| **⛓()**  | log()			  | 	Steel    |
| **🌿**    | \|              |    Grass     |
| **🐉**    | >=              |    Dragon    |
| **🏝️**    | <=              |    Ground    |
| **🐛()**  | ^()			  |     Bug      |



### Symbols Needed

Ran out of pokemon types, need help representing:
`>>>`
`<<<`


### Data Types

- Numbers
- Boolean: "true" or "false"

## Examples

### Basic Arithmetic

Addition:

```pt
1 🔥 1
```

Subtraction:

```pt
1 🌊 1
```

### Comparisons/Boolean

Checking if numbers are equal:

```pt
1 ✨ 1
```
Is `true` >= `false`:

```pt
true 🐉 false
```

### Functions

For Absolute of `-2`:

```pt
❄️🧚-2🌌
```
```pt
❄️(-2)
```

## Interpreter/Compiler

Using the installed python `poketype` package!

### Syntax Checking

Check if PokeType expression is valid

```py
from poketype import PokeType

pt = PokeType()
pt.check_syntax('code')

```

### Interpret

Run code, and print output.

```py
from poketype import PokeType

pt = PokeType()
print(pt.eval('code'))

```

### Compile

Turn PokeType to python code

```py
from poketype import PokeType

pt = PokeType()
print(pt.compile('code')) #Python
```

## Contributions

Open a PR! This is a WIP

[ ] CLI

[ ] API

[ ] More Interpreters

