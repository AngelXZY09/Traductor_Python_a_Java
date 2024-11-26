# Generated from TraduceJava.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5\62\n\5\r\5\16\5")
        buf.write("\63\3\6\6\6\67\n\6\r\6\16\68\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17L")
        buf.write("\n\17\r\17\16\17M\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2")
        buf.write("\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2S\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\3\37\3\2\2\2\5#\3\2\2\2\7*\3\2\2\2\t\61\3\2\2\2\13")
        buf.write("\66\3\2\2\2\r:\3\2\2\2\17<\3\2\2\2\21>\3\2\2\2\23@\3\2")
        buf.write("\2\2\25B\3\2\2\2\27D\3\2\2\2\31F\3\2\2\2\33H\3\2\2\2\35")
        buf.write("K\3\2\2\2\37 \7f\2\2 !\7g\2\2!\"\7h\2\2\"\4\3\2\2\2#$")
        buf.write("\7t\2\2$%\7g\2\2%&\7v\2\2&\'\7w\2\2\'(\7t\2\2()\7p\2\2")
        buf.write(")\6\3\2\2\2*+\7r\2\2+,\7t\2\2,-\7k\2\2-.\7p\2\2./\7v\2")
        buf.write("\2/\b\3\2\2\2\60\62\t\2\2\2\61\60\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\61\3\2\2\2\63\64\3\2\2\2\64\n\3\2\2\2\65\67\t\3")
        buf.write("\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29")
        buf.write("\f\3\2\2\2:;\7-\2\2;\16\3\2\2\2<=\7?\2\2=\20\3\2\2\2>")
        buf.write("?\7,\2\2?\22\3\2\2\2@A\7/\2\2A\24\3\2\2\2BC\7*\2\2C\26")
        buf.write("\3\2\2\2DE\7+\2\2E\30\3\2\2\2FG\7<\2\2G\32\3\2\2\2HI\7")
        buf.write(".\2\2I\34\3\2\2\2JL\t\4\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2")
        buf.write("\2\2MN\3\2\2\2NO\3\2\2\2OP\b\17\2\2P\36\3\2\2\2\6\2\63")
        buf.write("8M\3\b\2\2")
        return buf.getvalue()


class TraduceJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    PRINT = 3
    ID = 4
    NUMBER = 5
    PLUS = 6
    ASSIGN = 7
    MUL = 8
    SUB = 9
    LPAREN = 10
    RPAREN = 11
    COLON = 12
    COMMA = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'print'", "'+'", "'='", "'*'", "'-'", 
            "'('", "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "PRINT", "ID", "NUMBER", "PLUS", "ASSIGN", 
            "MUL", "SUB", "LPAREN", "RPAREN", "COLON", "COMMA", "WS" ]

    ruleNames = [ "DEF", "RETURN", "PRINT", "ID", "NUMBER", "PLUS", "ASSIGN", 
                  "MUL", "SUB", "LPAREN", "RPAREN", "COLON", "COMMA", "WS" ]

    grammarFileName = "TraduceJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


