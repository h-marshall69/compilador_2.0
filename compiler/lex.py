import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'COMMENT',
    'FLOAT',
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'COMMA',
    'ID',
]

reserved = [
    'IF',
    'THEN',
    'ELSE',
    'WHILE',
    'WHERE',
    'BIGINT',
    'CREATE',
    'INSERT',
    'TABLE',
    'SELECT',
    'DELETE',
    'FOR',
    'FROM',
    'PRINT'
]

tokens = tokens + reserved
    
# Regular expression rules for simple tokens
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_EQUAL         = r'\='
t_COMMA         = r','

t_IF            = r'IF'
t_THEN          = r'THEN'
t_ELSE          = r'ELSE'
t_WHILE         = r'WHILE'
t_BIGINT        = r'BIGINT'
t_CREATE        = r'CREATE'
t_INSERT        = r'INSERT'
t_TABLE         = r'TABLE'
t_SELECT        = r'SELECT'
t_DELETE        = r'DELETE'
t_FOR           = r'FOR'
t_FROM          = r'FROM'
t_PRINT         = r'PRINT'


def t_COMMENT(t):
    r'\#.*'
    pass

# A regular expression rule with some action code
def t_FLOAT(t):
	r'[\d]+[.][\d]+'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# A regular expression for detecting the string in double codes
def t_STRING(t):
	r'(\")[a-zA-Z]+[a-zA-Z0-9]*(\")'
	t.value = str(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.value = t.value.upper()
        t.type = t.value
        return t
    
    return t

# Build the lexer
#lexer = lex.lex()


'''

# Test it out
data = 'INSERTd xm.insert(23)'


# Give the lexer some input
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
'''