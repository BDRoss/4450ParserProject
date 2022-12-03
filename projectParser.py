# Generated from project.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        3,2,28,8,2,1,2,1,2,3,2,32,8,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,
        3,2,42,8,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,3,2,53,8,
        2,1,3,1,3,4,3,57,8,3,11,3,12,3,58,1,3,3,3,62,8,3,1,3,3,3,65,8,3,
        1,4,1,4,5,4,69,8,4,10,4,12,4,72,9,4,3,4,74,8,4,1,4,1,4,1,4,5,4,79,
        8,4,10,4,12,4,82,9,4,3,4,84,8,4,1,5,1,5,1,5,1,5,5,5,90,8,5,10,5,
        12,5,93,9,5,1,5,0,0,6,0,2,4,6,8,10,0,1,3,0,8,8,10,10,12,12,105,0,
        15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,54,1,0,0,0,8,73,1,0,0,0,10,
        85,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,
        0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,
        0,0,0,20,24,3,10,5,0,21,24,3,4,2,0,22,24,3,8,4,0,23,20,1,0,0,0,23,
        21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,27,5,1,0,0,26,28,5,2,0,
        0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,31,3,8,4,0,30,32,
        5,3,0,0,31,30,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,3,6,3,0,
        34,47,1,0,0,0,35,37,5,4,0,0,36,38,5,2,0,0,37,36,1,0,0,0,37,38,1,
        0,0,0,38,39,1,0,0,0,39,41,3,8,4,0,40,42,5,3,0,0,41,40,1,0,0,0,41,
        42,1,0,0,0,42,43,1,0,0,0,43,44,3,6,3,0,44,46,1,0,0,0,45,35,1,0,0,
        0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,52,1,0,0,0,49,47,
        1,0,0,0,50,51,5,5,0,0,51,53,3,6,3,0,52,50,1,0,0,0,52,53,1,0,0,0,
        53,5,1,0,0,0,54,56,5,14,0,0,55,57,3,2,1,0,56,55,1,0,0,0,57,58,1,
        0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,62,5,13,0,0,61,
        60,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,65,5,15,0,0,64,63,1,0,
        0,0,64,65,1,0,0,0,65,7,1,0,0,0,66,74,5,10,0,0,67,69,5,12,0,0,68,
        67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,74,1,0,0,
        0,72,70,1,0,0,0,73,66,1,0,0,0,73,70,1,0,0,0,74,75,1,0,0,0,75,83,
        5,9,0,0,76,84,5,10,0,0,77,79,5,12,0,0,78,77,1,0,0,0,79,82,1,0,0,
        0,80,78,1,0,0,0,80,81,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,83,76,
        1,0,0,0,83,80,1,0,0,0,84,9,1,0,0,0,85,86,5,10,0,0,86,87,5,7,0,0,
        87,91,7,0,0,0,88,90,5,13,0,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,
        0,0,0,91,92,1,0,0,0,92,11,1,0,0,0,93,91,1,0,0,0,16,15,23,27,31,37,
        41,47,52,58,61,64,70,73,80,83,91
    ]

class projectParser ( Parser ):

    grammarFileName = "project.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "'):'", "'elif'", "'else:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WS", "ASSIGN", "OPERATORS", 
                      "CONDITIONAL", "IDENTIFIER", "LETTERS", "DIGITS", 
                      "NEWLINE", "INDENT", "DEDENT" ]

    RULE_start = 0
    RULE_value = 1
    RULE_ifelse = 2
    RULE_block = 3
    RULE_expression = 4
    RULE_variableDef = 5

    ruleNames =  [ "start", "value", "ifelse", "block", "expression", "variableDef" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    WS=6
    ASSIGN=7
    OPERATORS=8
    CONDITIONAL=9
    IDENTIFIER=10
    LETTERS=11
    DIGITS=12
    NEWLINE=13
    INDENT=14
    DEDENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(projectParser.EOF, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projectParser.ValueContext)
            else:
                return self.getTypedRuleContext(projectParser.ValueContext,i)


        def getRuleIndex(self):
            return projectParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = projectParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 5634) != 0:
                self.state = 12
                self.value()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(projectParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDef(self):
            return self.getTypedRuleContext(projectParser.VariableDefContext,0)


        def ifelse(self):
            return self.getTypedRuleContext(projectParser.IfelseContext,0)


        def expression(self):
            return self.getTypedRuleContext(projectParser.ExpressionContext,0)


        def getRuleIndex(self):
            return projectParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = projectParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.variableDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.ifelse()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(projectParser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projectParser.BlockContext)
            else:
                return self.getTypedRuleContext(projectParser.BlockContext,i)


        def getRuleIndex(self):
            return projectParser.RULE_ifelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)




    def ifelse(self):

        localctx = projectParser.IfelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifelse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(projectParser.T__0)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 26
                self.match(projectParser.T__1)


            self.state = 29
            self.expression()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 30
                self.match(projectParser.T__2)


            self.state = 33
            self.block()
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 35
                    self.match(projectParser.T__3)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==2:
                        self.state = 36
                        self.match(projectParser.T__1)


                    self.state = 39
                    self.expression()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==3:
                        self.state = 40
                        self.match(projectParser.T__2)


                    self.state = 43
                    self.block() 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 50
                self.match(projectParser.T__4)
                self.state = 51
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(projectParser.INDENT, 0)

        def NEWLINE(self):
            return self.getToken(projectParser.NEWLINE, 0)

        def DEDENT(self):
            return self.getToken(projectParser.DEDENT, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projectParser.ValueContext)
            else:
                return self.getTypedRuleContext(projectParser.ValueContext,i)


        def getRuleIndex(self):
            return projectParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = projectParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(projectParser.INDENT)

            self.state = 56 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 55
                    self.value()

                else:
                    raise NoViableAltException(self)
                self.state = 58 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 60
                self.match(projectParser.NEWLINE)


            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(projectParser.DEDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONDITIONAL(self):
            return self.getToken(projectParser.CONDITIONAL, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.IDENTIFIER)
            else:
                return self.getToken(projectParser.IDENTIFIER, i)

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.DIGITS)
            else:
                return self.getToken(projectParser.DIGITS, i)

        def getRuleIndex(self):
            return projectParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = projectParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 66
                self.match(projectParser.IDENTIFIER)
                pass
            elif token in [9, 12]:
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 67
                    self.match(projectParser.DIGITS)
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 75
            self.match(projectParser.CONDITIONAL)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(projectParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 77
                        self.match(projectParser.DIGITS) 
                    self.state = 82
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.IDENTIFIER)
            else:
                return self.getToken(projectParser.IDENTIFIER, i)

        def ASSIGN(self):
            return self.getToken(projectParser.ASSIGN, 0)

        def OPERATORS(self):
            return self.getToken(projectParser.OPERATORS, 0)

        def DIGITS(self):
            return self.getToken(projectParser.DIGITS, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.NEWLINE)
            else:
                return self.getToken(projectParser.NEWLINE, i)

        def getRuleIndex(self):
            return projectParser.RULE_variableDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDef" ):
                listener.enterVariableDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDef" ):
                listener.exitVariableDef(self)




    def variableDef(self):

        localctx = projectParser.VariableDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(projectParser.IDENTIFIER)
            self.state = 86
            self.match(projectParser.ASSIGN)
            self.state = 87
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 5376) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.match(projectParser.NEWLINE) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





