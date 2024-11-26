# Generated from TraduceJava.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\6\2 \n\2\r\2\16\2!\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3\5")
        buf.write("\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\6\5\6=\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\7\13S\n\13\f\13\16\13V\13\13\3")
        buf.write("\f\3\f\3\f\7\f[\n\f\f\f\16\f^\13\f\3\r\3\r\3\r\7\rc\n")
        buf.write("\r\f\r\16\rf\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16o\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\2\2\2p\2\37\3\2\2\2\4#\3\2\2\2\6+\3\2\2\2\b\66\3\2\2")
        buf.write("\2\n<\3\2\2\2\f>\3\2\2\2\16B\3\2\2\2\20E\3\2\2\2\22J\3")
        buf.write("\2\2\2\24O\3\2\2\2\26W\3\2\2\2\30_\3\2\2\2\32n\3\2\2\2")
        buf.write("\34 \5\4\3\2\35 \5\20\t\2\36 \5\22\n\2\37\34\3\2\2\2\37")
        buf.write("\35\3\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2")
        buf.write("\2\2\"\3\3\2\2\2#$\7\3\2\2$%\7\6\2\2%&\7\f\2\2&\'\5\6")
        buf.write("\4\2\'(\7\r\2\2()\7\16\2\2)*\5\b\5\2*\5\3\2\2\2+\60\7")
        buf.write("\6\2\2,-\7\17\2\2-/\7\6\2\2.,\3\2\2\2/\62\3\2\2\2\60.")
        buf.write("\3\2\2\2\60\61\3\2\2\2\61\7\3\2\2\2\62\60\3\2\2\2\63\65")
        buf.write("\5\n\6\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\67\t\3\2\2\28\66\3\2\2\29=\5\f\7\2:=\5\16\b\2")
        buf.write(";=\5\20\t\2<9\3\2\2\2<:\3\2\2\2<;\3\2\2\2=\13\3\2\2\2")
        buf.write(">?\7\6\2\2?@\7\t\2\2@A\5\26\f\2A\r\3\2\2\2BC\7\4\2\2C")
        buf.write("D\5\26\f\2D\17\3\2\2\2EF\7\5\2\2FG\7\f\2\2GH\5\26\f\2")
        buf.write("HI\7\r\2\2I\21\3\2\2\2JK\7\6\2\2KL\7\f\2\2LM\5\24\13\2")
        buf.write("MN\7\r\2\2N\23\3\2\2\2OT\5\26\f\2PQ\7\17\2\2QS\5\26\f")
        buf.write("\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\25\3\2\2\2")
        buf.write("VT\3\2\2\2W\\\5\30\r\2XY\7\13\2\2Y[\5\30\r\2ZX\3\2\2\2")
        buf.write("[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\27\3\2\2\2^\\\3\2\2")
        buf.write("\2_d\5\32\16\2`a\7\n\2\2ac\5\32\16\2b`\3\2\2\2cf\3\2\2")
        buf.write("\2db\3\2\2\2de\3\2\2\2e\31\3\2\2\2fd\3\2\2\2go\7\6\2\2")
        buf.write("ho\7\7\2\2ij\7\f\2\2jk\5\26\f\2kl\7\r\2\2lo\3\2\2\2mo")
        buf.write("\5\22\n\2ng\3\2\2\2nh\3\2\2\2ni\3\2\2\2nm\3\2\2\2o\33")
        buf.write("\3\2\2\2\13\37!\60\66<T\\dn")
        return buf.getvalue()


class TraduceJavaParser ( Parser ):

    grammarFileName = "TraduceJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "<INVALID>", 
                     "<INVALID>", "'+'", "'='", "'*'", "'-'", "'('", "')'", 
                     "':'", "','" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "ID", "NUMBER", 
                      "PLUS", "ASSIGN", "MUL", "SUB", "LPAREN", "RPAREN", 
                      "COLON", "COMMA", "WS" ]

    RULE_programa = 0
    RULE_function = 1
    RULE_parameters = 2
    RULE_statements = 3
    RULE_statement = 4
    RULE_assignment = 5
    RULE_return_statement = 6
    RULE_print_statement = 7
    RULE_function_call = 8
    RULE_arguments = 9
    RULE_expression = 10
    RULE_term = 11
    RULE_factor = 12

    ruleNames =  [ "programa", "function", "parameters", "statements", "statement", 
                   "assignment", "return_statement", "print_statement", 
                   "function_call", "arguments", "expression", "term", "factor" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    ID=4
    NUMBER=5
    PLUS=6
    ASSIGN=7
    MUL=8
    SUB=9
    LPAREN=10
    RPAREN=11
    COLON=12
    COMMA=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.FunctionContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.FunctionContext,i)


        def print_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.Print_statementContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.Print_statementContext,i)


        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.Function_callContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.Function_callContext,i)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = TraduceJavaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TraduceJavaParser.DEF]:
                    self.state = 26
                    self.function()
                    pass
                elif token in [TraduceJavaParser.PRINT]:
                    self.state = 27
                    self.print_statement()
                    pass
                elif token in [TraduceJavaParser.ID]:
                    self.state = 28
                    self.function_call()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TraduceJavaParser.DEF) | (1 << TraduceJavaParser.PRINT) | (1 << TraduceJavaParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(TraduceJavaParser.DEF, 0)

        def ID(self):
            return self.getToken(TraduceJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TraduceJavaParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(TraduceJavaParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(TraduceJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(TraduceJavaParser.COLON, 0)

        def statements(self):
            return self.getTypedRuleContext(TraduceJavaParser.StatementsContext,0)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = TraduceJavaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(TraduceJavaParser.DEF)
            self.state = 34
            self.match(TraduceJavaParser.ID)
            self.state = 35
            self.match(TraduceJavaParser.LPAREN)
            self.state = 36
            self.parameters()
            self.state = 37
            self.match(TraduceJavaParser.RPAREN)
            self.state = 38
            self.match(TraduceJavaParser.COLON)
            self.state = 39
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TraduceJavaParser.ID)
            else:
                return self.getToken(TraduceJavaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TraduceJavaParser.COMMA)
            else:
                return self.getToken(TraduceJavaParser.COMMA, i)

        def getRuleIndex(self):
            return TraduceJavaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = TraduceJavaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(TraduceJavaParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TraduceJavaParser.COMMA:
                self.state = 42
                self.match(TraduceJavaParser.COMMA)
                self.state = 43
                self.match(TraduceJavaParser.ID)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = TraduceJavaParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self.statement() 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(TraduceJavaParser.AssignmentContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(TraduceJavaParser.Return_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(TraduceJavaParser.Print_statementContext,0)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TraduceJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TraduceJavaParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.assignment()
                pass
            elif token in [TraduceJavaParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.return_statement()
                pass
            elif token in [TraduceJavaParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.print_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TraduceJavaParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TraduceJavaParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(TraduceJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = TraduceJavaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(TraduceJavaParser.ID)
            self.state = 61
            self.match(TraduceJavaParser.ASSIGN)
            self.state = 62
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TraduceJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(TraduceJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = TraduceJavaParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(TraduceJavaParser.RETURN)
            self.state = 65
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Print_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(TraduceJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(TraduceJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TraduceJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(TraduceJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return TraduceJavaParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)




    def print_statement(self):

        localctx = TraduceJavaParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(TraduceJavaParser.PRINT)
            self.state = 68
            self.match(TraduceJavaParser.LPAREN)
            self.state = 69
            self.expression()
            self.state = 70
            self.match(TraduceJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TraduceJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TraduceJavaParser.LPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(TraduceJavaParser.ArgumentsContext,0)


        def RPAREN(self):
            return self.getToken(TraduceJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return TraduceJavaParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = TraduceJavaParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(TraduceJavaParser.ID)
            self.state = 73
            self.match(TraduceJavaParser.LPAREN)
            self.state = 74
            self.arguments()
            self.state = 75
            self.match(TraduceJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TraduceJavaParser.COMMA)
            else:
                return self.getToken(TraduceJavaParser.COMMA, i)

        def getRuleIndex(self):
            return TraduceJavaParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = TraduceJavaParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.expression()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TraduceJavaParser.COMMA:
                self.state = 78
                self.match(TraduceJavaParser.COMMA)
                self.state = 79
                self.expression()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.TermContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.TermContext,i)


        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(TraduceJavaParser.SUB)
            else:
                return self.getToken(TraduceJavaParser.SUB, i)

        def getRuleIndex(self):
            return TraduceJavaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = TraduceJavaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.term()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TraduceJavaParser.SUB:
                self.state = 86
                self.match(TraduceJavaParser.SUB)
                self.state = 87
                self.term()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraduceJavaParser.FactorContext)
            else:
                return self.getTypedRuleContext(TraduceJavaParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(TraduceJavaParser.MUL)
            else:
                return self.getToken(TraduceJavaParser.MUL, i)

        def getRuleIndex(self):
            return TraduceJavaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = TraduceJavaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.factor()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TraduceJavaParser.MUL:
                self.state = 94
                self.match(TraduceJavaParser.MUL)
                self.state = 95
                self.factor()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TraduceJavaParser.ID, 0)

        def NUMBER(self):
            return self.getToken(TraduceJavaParser.NUMBER, 0)

        def LPAREN(self):
            return self.getToken(TraduceJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TraduceJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(TraduceJavaParser.RPAREN, 0)

        def function_call(self):
            return self.getTypedRuleContext(TraduceJavaParser.Function_callContext,0)


        def getRuleIndex(self):
            return TraduceJavaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = TraduceJavaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(TraduceJavaParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(TraduceJavaParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(TraduceJavaParser.LPAREN)
                self.state = 104
                self.expression()
                self.state = 105
                self.match(TraduceJavaParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





