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
        4,1,7,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,2,1,2,
        1,3,1,3,5,3,30,8,3,10,3,12,3,33,9,3,1,3,0,0,4,0,2,4,6,0,3,1,1,7,
        7,2,0,1,1,5,5,2,0,1,1,5,6,34,0,11,1,0,0,0,2,16,1,0,0,0,4,18,1,0,
        0,0,6,27,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,
        0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,
        1,0,0,0,16,17,3,4,2,0,17,3,1,0,0,0,18,19,3,6,3,0,19,23,5,3,0,0,20,
        24,5,4,0,0,21,24,3,6,3,0,22,24,5,6,0,0,23,20,1,0,0,0,23,21,1,0,0,
        0,23,22,1,0,0,0,24,25,1,0,0,0,25,26,7,0,0,0,26,5,1,0,0,0,27,31,7,
        1,0,0,28,30,7,2,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,7,1,0,0,0,33,31,1,0,0,0,3,11,23,31
    ]

class projectParser ( Parser ):

    grammarFileName = "project.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "ASSIGN", "OPERATORS", 
                      "LETTERS", "DIGITS", "NEWLINE" ]

    RULE_start = 0
    RULE_value = 1
    RULE_variableDef = 2
    RULE_identifier = 3

    ruleNames =  [ "start", "value", "variableDef", "identifier" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    ASSIGN=3
    OPERATORS=4
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
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==5:
                self.state = 8
                self.value()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
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
            self.state = 16
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projectParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(projectParser.IdentifierContext,i)


        def ASSIGN(self):
            return self.getToken(projectParser.ASSIGN, 0)

        def NEWLINE(self):
            return self.getToken(projectParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(projectParser.EOF, 0)

        def OPERATORS(self):
            return self.getToken(projectParser.OPERATORS, 0)

        def DIGITS(self):
            return self.getToken(projectParser.DIGITS, 0)

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
            self.state = 18
            self.identifier()
            self.state = 19
            self.match(projectParser.ASSIGN)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 20
                self.match(projectParser.OPERATORS)
                pass
            elif token in [1, 5]:
                self.state = 21
                self.identifier()
                pass
            elif token in [6]:
                self.state = 22
                self.match(projectParser.DIGITS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 25
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTERS(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.LETTERS)
            else:
                return self.getToken(projectParser.LETTERS, i)

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.DIGITS)
            else:
                return self.getToken(projectParser.DIGITS, i)

        def getRuleIndex(self):
            return projectParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = projectParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==1 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 98) != 0:
                self.state = 28
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 98) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





