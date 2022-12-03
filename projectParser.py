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
        4,1,18,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,3,2,31,8,2,1,2,1,2,3,2,35,8,2,1,2,1,2,1,2,1,2,3,2,41,
        8,2,1,2,1,2,3,2,45,8,2,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,
        2,3,2,56,8,2,1,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,3,3,66,8,3,
        1,3,3,3,69,8,3,1,3,1,3,1,4,1,4,4,4,75,8,4,11,4,12,4,76,1,4,3,4,80,
        8,4,1,4,3,4,83,8,4,1,5,1,5,5,5,87,8,5,10,5,12,5,90,9,5,3,5,92,8,
        5,1,5,3,5,95,8,5,1,5,1,5,1,5,5,5,100,8,5,10,5,12,5,103,9,5,3,5,105,
        8,5,1,5,3,5,108,8,5,1,6,1,6,1,6,1,6,4,6,114,8,6,11,6,12,6,115,1,
        6,0,0,7,0,2,4,6,8,10,12,0,1,3,0,10,10,12,12,14,14,133,0,17,1,0,0,
        0,2,26,1,0,0,0,4,28,1,0,0,0,6,57,1,0,0,0,8,72,1,0,0,0,10,94,1,0,
        0,0,12,109,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,
        15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,
        1,21,1,1,0,0,0,22,27,3,12,6,0,23,27,3,4,2,0,24,27,3,10,5,0,25,27,
        3,6,3,0,26,22,1,0,0,0,26,23,1,0,0,0,26,24,1,0,0,0,26,25,1,0,0,0,
        27,3,1,0,0,0,28,30,5,1,0,0,29,31,5,2,0,0,30,29,1,0,0,0,30,31,1,0,
        0,0,31,32,1,0,0,0,32,34,3,10,5,0,33,35,5,3,0,0,34,33,1,0,0,0,34,
        35,1,0,0,0,35,36,1,0,0,0,36,37,3,8,4,0,37,50,1,0,0,0,38,40,5,4,0,
        0,39,41,5,2,0,0,40,39,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,44,
        3,10,5,0,43,45,5,3,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,
        46,47,3,8,4,0,47,49,1,0,0,0,48,38,1,0,0,0,49,52,1,0,0,0,50,48,1,
        0,0,0,50,51,1,0,0,0,51,55,1,0,0,0,52,50,1,0,0,0,53,54,5,5,0,0,54,
        56,3,8,4,0,55,53,1,0,0,0,55,56,1,0,0,0,56,5,1,0,0,0,57,65,5,6,0,
        0,58,66,3,10,5,0,59,61,5,14,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,65,58,1,0,0,0,
        65,62,1,0,0,0,66,68,1,0,0,0,67,69,5,3,0,0,68,67,1,0,0,0,68,69,1,
        0,0,0,69,70,1,0,0,0,70,71,3,8,4,0,71,7,1,0,0,0,72,74,5,17,0,0,73,
        75,3,2,1,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,
        0,77,79,1,0,0,0,78,80,5,16,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,
        1,0,0,0,81,83,5,18,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,9,1,0,0,0,
        84,92,5,12,0,0,85,87,5,14,0,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,
        1,0,0,0,88,89,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,84,1,0,0,0,
        91,88,1,0,0,0,92,95,1,0,0,0,93,95,5,8,0,0,94,91,1,0,0,0,94,93,1,
        0,0,0,95,96,1,0,0,0,96,107,5,11,0,0,97,105,5,12,0,0,98,100,5,14,
        0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,
        102,105,1,0,0,0,103,101,1,0,0,0,104,97,1,0,0,0,104,101,1,0,0,0,105,
        108,1,0,0,0,106,108,5,8,0,0,107,104,1,0,0,0,107,106,1,0,0,0,108,
        11,1,0,0,0,109,110,5,12,0,0,110,111,5,9,0,0,111,113,7,0,0,0,112,
        114,5,16,0,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,13,1,0,0,0,21,17,26,30,34,40,44,50,55,62,65,68,76,
        79,82,88,91,94,101,104,107,115
    ]

class projectParser ( Parser ):

    grammarFileName = "project.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "'):'", "'elif'", "'else:'", 
                     "'while('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ARITHMETIC", 
                      "ASSIGN", "OPERATORS", "CONDITIONAL", "IDENTIFIER", 
                      "LETTERS", "DIGITS", "COMMENT", "NEWLINE", "INDENT", 
                      "DEDENT" ]

    RULE_start = 0
    RULE_value = 1
    RULE_ifelse = 2
    RULE_whileLoop = 3
    RULE_block = 4
    RULE_expression = 5
    RULE_variableDef = 6

    ruleNames =  [ "start", "value", "ifelse", "whileLoop", "block", "expression", 
                   "variableDef" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WS=7
    ARITHMETIC=8
    ASSIGN=9
    OPERATORS=10
    CONDITIONAL=11
    IDENTIFIER=12
    LETTERS=13
    DIGITS=14
    COMMENT=15
    NEWLINE=16
    INDENT=17
    DEDENT=18

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 22850) != 0:
                self.state = 14
                self.value()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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


        def whileLoop(self):
            return self.getTypedRuleContext(projectParser.WhileLoopContext,0)


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
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.variableDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.ifelse()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.whileLoop()
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
            self.state = 28
            self.match(projectParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 29
                self.match(projectParser.T__1)


            self.state = 32
            self.expression()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 33
                self.match(projectParser.T__2)


            self.state = 36
            self.block()
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 38
                    self.match(projectParser.T__3)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==2:
                        self.state = 39
                        self.match(projectParser.T__1)


                    self.state = 42
                    self.expression()
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==3:
                        self.state = 43
                        self.match(projectParser.T__2)


                    self.state = 46
                    self.block() 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 53
                self.match(projectParser.T__4)
                self.state = 54
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(projectParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(projectParser.ExpressionContext,0)


        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.DIGITS)
            else:
                return self.getToken(projectParser.DIGITS, i)

        def getRuleIndex(self):
            return projectParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = projectParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(projectParser.T__5)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 58
                self.expression()
                pass

            elif la_ == 2:
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 59
                    self.match(projectParser.DIGITS)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 67
                self.match(projectParser.T__2)


            self.state = 70
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
        self.enterRule(localctx, 8, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(projectParser.INDENT)

            self.state = 74 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 73
                    self.value()

                else:
                    raise NoViableAltException(self)
                self.state = 76 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(projectParser.NEWLINE)


            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 81
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

        def ARITHMETIC(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.ARITHMETIC)
            else:
                return self.getToken(projectParser.ARITHMETIC, i)

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
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 14]:
                self.state = 91
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 84
                    self.match(projectParser.IDENTIFIER)
                    pass
                elif token in [11, 14]:
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==14:
                        self.state = 85
                        self.match(projectParser.DIGITS)
                        self.state = 90
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [8]:
                self.state = 93
                self.match(projectParser.ARITHMETIC)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 96
            self.match(projectParser.CONDITIONAL)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.match(projectParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 101
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 98
                            self.match(projectParser.DIGITS) 
                        self.state = 103
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                    pass


                pass

            elif la_ == 2:
                self.state = 106
                self.match(projectParser.ARITHMETIC)
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
        self.enterRule(localctx, 12, self.RULE_variableDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(projectParser.IDENTIFIER)
            self.state = 110
            self.match(projectParser.ASSIGN)
            self.state = 111
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 21504) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 113 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 112
                    self.match(projectParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 115 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





