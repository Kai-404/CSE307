# Zhongkai Ye 111314836

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class NumberNode(Node):
    def __init__(self, v):
        if('.' in v):
            self.value = float(v)
        elif('e'in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

class StringNode(Node):
    def __init__(self, v):
        self.value = str(v)

    def evaluate(self):
        return self.value

class PrintNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):
        self.value = self.value.evaluate()
        if(self.value == None):
            return
        if(isinstance(self.value, str)):
            print("'"+self.value+"'")
        else: 
            print(self.value)

class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op =='**'):
            return self.v1.evaluate() ** self.v2.evaluate()
        elif (self.op =='div'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op =='mod'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op =='in'):
            if (not (isinstance(self.v2.evaluate(), str) or isinstance(self.v2.evaluate(), list))):
                print("SEMANTIC ERROR")
                return
            return (self.v1.evaluate() in self.v2.evaluate())
        elif (self.op =='::'):
            if ((not isinstance(self.v2.evaluate(), list))):
                print("SEMANTIC ERROR")
                return
            return [self.v1.evaluate()]+self.v2.evaluate()
        elif (self.op == '<'):
            # if (not(isinstance(self.v2.evaluate(), str) and isinstance(self.v1.evaluate(), str))) and (not (isinstance(self.v2, NumberNode) or isinstance(self.v1, NumberNode))):
            #     print("SEMANTIC ERROR")
            #     return
            return self.v1.evaluate() < self.v2.evaluate()
        elif (self.op == '<='):
            return self.v1.evaluate() <= self.v2.evaluate()
        elif (self.op == '=='):
            return self.v1.evaluate() == self.v2.evaluate()
        elif (self.op =='<>'):
            return self.v1.evaluate() != self.v2.evaluate()
        elif (self.op =='>'):
            return self.v1.evaluate() > self.v2.evaluate()
        elif (self.op =='>='):
            return self.v1.evaluate() >= self.v2.evaluate()

        elif (self.op =='andalso'):
            # if (not (isinstance(self.v2.evaluate(), bool) and isinstance(self.v2.evaluate(), bool))):
            #     print("SEMANTIC ERROR")
            #     return
            return (self.v1.evaluate() and self.v2.evaluate())
        elif (self.op =='orelse'):
            # if (not (isinstance(self.v2.evaluate(), bool) and isinstance(self.v2.evaluate(), bool))):
            #     print("SEMANTIC ERROR")
            #     return
            return (self.v1.evaluate() or self.v2.evaluate())


class NotopNode(Node):
    def __init__(self,v1):
        self.v1 = v1

    def evaluate(self):
        if not isinstance(self.v1.evaluate(), bool):
            print("SEMANTIC ERROR")
            return
        return (not self.v1.evaluate())


class TupleNode(Node):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        a = (self.v1.evaluate(),)
        if (isinstance(self.v2, ExtendTupleNode)):
            a= a + (self.v2.evaluate())
        else:
            a= a+(self.v2.evaluate(),)
        return a


class ExtendTupleNode(Node):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        a = (self.v1.evaluate(),)
        if (isinstance(self.v2, ExtendTupleNode)):
            a= a + (self.v2.evaluate())
        else:
            a= a+(self.v2.evaluate(),)
        return a


class ListNode(Node):
    def __init__(self,v1):
        self.v1 = v1
        
    def evaluate(self):

        if(self.v1==None):
            a = []
            return a  
        else:
            a = []   
            if (isinstance(self.v1, ExtendListNode)):
                a.extend(self.v1.evaluate())
            else:
                a.append(self.v1.evaluate())
        return a


class ExtendListNode(Node):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        a = [self.v1.evaluate()]
        if (isinstance(self.v2, ExtendListNode)):
            a.extend(self.v2.evaluate())
            
        else:
            a.append(self.v2.evaluate())
        return a

class BooleanNode(Node):
    def __init__(self,v1):
        if(v1 == "True"):
            self.v1 = bool(v1)
        else:
            self.v1 = bool()

    def evaluate(self):
        return self.v1

class IndexTupleNode(Node):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        a = self.v1.evaluate()
        b = self.v2.evaluate()

        if (not isinstance(a,int)):
            print("SEMANTIC ERROR")
            return
        if (not isinstance(b, tuple)):
            print("SEMANTIC ERROR")
            return
        if (a<1 or a>len(b)):
            print("SEMANTIC ERROR")
            return
        a = a-1
        return b[a]

class IndexListNode(Node):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        a = self.v1.evaluate()
        b = self.v2.evaluate()

        if (not (isinstance(a,list) or isinstance(a,str))):
            print("SEMANTIC ERROR")
            return
        if (not isinstance(b, int)):
            print("SEMANTIC ERROR")
            return
        if (b<0 or b>(len(a)-1)):
            print("SEMANTIC ERROR")
            return
        return a[b]



tokens = (
    'PRINT','LPAREN', 'RPAREN', 'SEMICOLON', 'SQUOTE', 'DQUOTE','COMMA','LSBRACKET',"RSBRACKET",
    'STRING', 'NUMBER', 'TRUE', 'FALSE',
    'PLUS','MINUS','TIMES','DIVIDE','UMINUS','POWER','INDEXTUPLE','DIV', 'MOD','IN','CONS',
    'SMALLER','SMALLEROREQUAL','EQUAL','NOTEQUAL','BIGGER','BIGGEROREQUAL',
    'NOT', 'AND','OR'
    )

# Tokens
# t_PRINT    = 'print'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_SEMICOLON =r';'
t_LSBRACKET =r'\['
t_RSBRACKET =r'\]'
t_TRUE =r'True'
t_FALSE =r'False'
t_POWER =r'\*\*'
t_INDEXTUPLE =r'\#'
t_DIV =r'div'
t_MOD =r'mod'
t_IN =r'in'
t_CONS =r'::'

t_SMALLER =r'<'
t_SMALLEROREQUAL =r'<='
t_EQUAL =r'=='
t_NOTEQUAL =r'<>'
t_BIGGER =r'>'
t_BIGGEROREQUAL =r'>='

t_NOT =r'not'
t_AND =r'andalso'
t_OR =r'orelse'

t_SQUOTE = r'\''
t_DQUOTE = r'\"'
t_COMMA = r','

def t_NUMBER(t):
    #r'(-?\d*(\d\.|\.\d)\d* | \d+)| (-?\d*(\d\.|\.\d)\d* | \d+[e]-?\d+)'
    r'((-?\d*(\d\.|\.\d)\d* | \d+) [e]-?\d+)|(-?\d*(\d\.|\.\d)\d* | \d+)'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    #r'(\'|\")(\w|\s)*(\'|\")'
    r'(\'(\w|\s|\.|!|@|\#|\$|%|\^|&|\*)*\')|(\"(\w|\s|\.|!|@|\#|\$|%|\^|&|\*)*\")'
    t.value = StringNode((t.value)[1:len((t.value))-1])
    return t
    
    

# Ignored characters
t_ignore = " \t"

def t_error(t):
    return
    #print("Syntax error at '%s'" % t.value)
    
# Build the lexer
import ply.lex as lex
lex.lex(debug=False)

# Parsing rules
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left','SMALLER','SMALLEROREQUAL','EQUAL','NOTEQUAL','BIGGER','BIGGEROREQUAL'),
    ('right','CONS'),
    ('left','IN'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','DIV','MOD'),
    ('left', 'INDEXTUPLE'),
    ('right', 'UMINUS','POWER')
    )

def p_print_smt(t):
    """
    print_smt : expression SEMICOLON
    """
    t[0] = PrintNode(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression 
                  | expression MINUS expression 
                  | expression TIMES expression 
                  | expression DIVIDE expression
                  | expression POWER expression 
                  | expression DIV expression
                  | expression MOD expression 
                  | expression IN expression
                  | expression CONS expression
                  | expression SMALLER expression 
                  | expression SMALLEROREQUAL expression
                  | expression EQUAL expression 
                  | expression NOTEQUAL expression
                  | expression BIGGER expression 
                  | expression BIGGEROREQUAL expression
                  | expression AND expression
                  | expression OR expression'''
    t[0] = BopNode(t[2], t[1], t[3])

def p_expression_notop(t):
    '''expression : NOT expression'''
    t[0] = NotopNode(t[2])

def p_expression_uminus(t):
    '''expression : MINUS expression %prec UMINUS'''
    t[0] = BopNode(t[1], NumberNode("0"), t[2])

def p_expression_indextuple(t):
    '''expression : INDEXTUPLE expression expression'''
    t[0] = IndexTupleNode(t[2],t[3])

def p_expression_indexlist(t):
    '''expression : expression LSBRACKET expression RSBRACKET'''
    t[0] = IndexListNode(t[1],t[3])
    
def p_expression_factor(t):
    '''expression : factor '''
    t[0] = t[1]

def p_factor_number(t):
    '''factor : NUMBER'''
    t[0] = t[1]

def p_factor_booleantrue(t):
    '''factor : TRUE'''
    t[0] = BooleanNode(t[1])

def p_factor_booleanfalse(t):
    '''factor : FALSE'''
    t[0] = BooleanNode(t[1])

def p_expression_group(t):
    '''expression : LPAREN expression RPAREN'''
    t[0] = t[2]    

def p_expression_tuple(t):
    '''expression : LPAREN expression COMMA tupexp RPAREN'''
    t[0] = TupleNode(t[2],t[4])

def p_tupexp_moretup(t):
    '''tupexp : expression COMMA tupexp'''
    t[0] = ExtendTupleNode(t[1],t[3])

def p_tupexp_expression(t):
    '''tupexp : expression'''
    t[0] = t[1]

def p_expression_list(t):
    '''expression : LSBRACKET listexp RSBRACKET'''
    t[0] = ListNode(t[2])

def p_expression_emptylist(t):
    '''expression : LSBRACKET RSBRACKET'''
    t[0] = ListNode(None)

def p_listexp_expression(t):
    '''listexp : expression'''
    t[0] = t[1]

def p_listexp_morelist(t):
    '''listexp : listexp COMMA listexp'''
    t[0] = ExtendListNode(t[1],t[3])


def p_factor_string(t):
    ''' factor : STRING'''
    t[0] = t[1]

def p_error(t):
    return
    #print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()
yacc.yacc(debug=False)
yacc.yacc(errorlog=yacc.NullLogger())

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""

for line in fd:
    code = line.strip()

    try:
        lex.input(code)
        # while True:
        #     token = lex.token()
        #     if not token: break
        #     print(token)
        ast = yacc.parse(code)
        ast.execute()
    except Exception:
        print("SYNTAX ERROR")

        ##
