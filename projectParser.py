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
        4,1,7,22,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,2,2,0,3,4,
        6,6,1,1,7,7,19,0,9,1,0,0,0,2,14,1,0,0,0,4,16,1,0,0,0,6,8,3,2,1,0,
        7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,
        11,9,1,0,0,0,12,13,5,0,0,1,13,1,1,0,0,0,14,15,3,4,2,0,15,3,1,0,0,
        0,16,17,5,4,0,0,17,18,5,2,0,0,18,19,7,0,0,0,19,20,7,1,0,0,20,5,1,
        0,0,0,1,9
    ]

class projectParser ( Parser ):

    grammarFileName = "project.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "WS", "ASSIGN", "OPERATORS", "IDENTIFIER", 
                      "LETTERS", "DIGITS", "NEWLINE" ]

    RULE_start = 0
    RULE_value = 1
    RULE_variableDef = 2

    ruleNames =  [ "start", "value", "variableDef" ]

    EOF = Token.EOF
    WS=1
    ASSIGN=2
    OPERATORS=3
    IDENTIFIER=4
    LETTERS=5
    DIGITS=6
    NEWLINE=7

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
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 6
                self.value()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
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
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.variableDef()
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

        def NEWLINE(self):
            return self.getToken(projectParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(projectParser.EOF, 0)

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
        self.enterRule(localctx, 4, self.RULE_variableDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(projectParser.IDENTIFIER)
            self.state = 17
            self.match(projectParser.ASSIGN)
            self.state = 18
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 88) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 19
            _la = self._input.LA(1)
            if not(_la==-1 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





