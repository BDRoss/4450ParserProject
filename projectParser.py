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
        4,1,26,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,2,1,
        2,3,2,44,8,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,3,2,53,8,2,1,2,1,2,3,
        2,57,8,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,3,2,68,8,2,
        1,3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,3,3,78,8,3,1,3,3,3,81,8,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,1,
        4,3,4,97,8,4,1,4,3,4,100,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,
        110,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,9,
        6,1,7,1,7,1,7,5,7,127,8,7,10,7,12,7,130,9,7,5,7,132,8,7,10,7,12,
        7,135,9,7,1,8,1,8,5,8,139,8,8,10,8,12,8,142,9,8,1,8,3,8,145,8,8,
        1,9,1,9,5,9,149,8,9,10,9,12,9,152,9,9,3,9,154,8,9,1,9,3,9,157,8,
        9,1,9,1,9,1,9,5,9,162,8,9,10,9,12,9,165,9,9,3,9,167,8,9,1,9,3,9,
        170,8,9,1,9,5,9,173,8,9,10,9,12,9,176,9,9,1,10,1,10,1,10,1,10,1,
        10,1,10,3,10,184,8,10,1,10,5,10,187,8,10,10,10,12,10,190,9,10,1,
        10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,218,0,25,1,0,0,0,2,39,
        1,0,0,0,4,41,1,0,0,0,6,69,1,0,0,0,8,84,1,0,0,0,10,104,1,0,0,0,12,
        113,1,0,0,0,14,133,1,0,0,0,16,136,1,0,0,0,18,156,1,0,0,0,20,177,
        1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,
        0,0,30,40,5,1,0,0,31,40,3,20,10,0,32,40,3,4,2,0,33,40,3,18,9,0,34,
        40,3,6,3,0,35,40,3,8,4,0,36,40,3,10,5,0,37,40,3,12,6,0,38,40,5,24,
        0,0,39,30,1,0,0,0,39,31,1,0,0,0,39,32,1,0,0,0,39,33,1,0,0,0,39,34,
        1,0,0,0,39,35,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,
        40,3,1,0,0,0,41,43,5,2,0,0,42,44,5,3,0,0,43,42,1,0,0,0,43,44,1,0,
        0,0,44,45,1,0,0,0,45,47,3,18,9,0,46,48,5,4,0,0,47,46,1,0,0,0,47,
        48,1,0,0,0,48,49,1,0,0,0,49,62,3,16,8,0,50,52,5,5,0,0,51,53,5,3,
        0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,56,3,18,9,0,55,
        57,5,4,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,3,16,
        8,0,59,61,1,0,0,0,60,50,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,
        1,0,0,0,63,67,1,0,0,0,64,62,1,0,0,0,65,66,5,6,0,0,66,68,3,16,8,0,
        67,65,1,0,0,0,67,68,1,0,0,0,68,5,1,0,0,0,69,77,5,7,0,0,70,78,3,18,
        9,0,71,73,5,22,0,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,
        75,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,77,70,1,0,0,0,77,74,1,0,0,
        0,78,80,1,0,0,0,79,81,5,4,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,
        1,0,0,0,82,83,3,16,8,0,83,7,1,0,0,0,84,85,5,8,0,0,85,86,5,20,0,0,
        86,99,5,9,0,0,87,100,5,20,0,0,88,96,5,10,0,0,89,91,5,22,0,0,90,89,
        1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,97,1,0,0,0,
        94,92,1,0,0,0,95,97,5,20,0,0,96,92,1,0,0,0,96,95,1,0,0,0,97,98,1,
        0,0,0,98,100,5,11,0,0,99,87,1,0,0,0,99,88,1,0,0,0,100,101,1,0,0,
        0,101,102,5,12,0,0,102,103,3,16,8,0,103,9,1,0,0,0,104,105,5,13,0,
        0,105,106,5,20,0,0,106,107,5,3,0,0,107,109,3,14,7,0,108,110,5,4,
        0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,112,3,16,
        8,0,112,11,1,0,0,0,113,114,5,20,0,0,114,115,5,3,0,0,115,116,3,14,
        7,0,116,120,5,11,0,0,117,119,5,24,0,0,118,117,1,0,0,0,119,122,1,
        0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,13,1,0,0,0,122,120,1,0,
        0,0,123,128,5,20,0,0,124,125,5,14,0,0,125,127,5,20,0,0,126,124,1,
        0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,132,1,
        0,0,0,130,128,1,0,0,0,131,123,1,0,0,0,132,135,1,0,0,0,133,131,1,
        0,0,0,133,134,1,0,0,0,134,15,1,0,0,0,135,133,1,0,0,0,136,140,5,25,
        0,0,137,139,3,2,1,0,138,137,1,0,0,0,139,142,1,0,0,0,140,138,1,0,
        0,0,140,141,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,143,145,5,26,
        0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,17,1,0,0,0,146,154,5,20,
        0,0,147,149,5,22,0,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,
        0,0,150,151,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,153,146,1,0,
        0,0,153,150,1,0,0,0,154,157,1,0,0,0,155,157,5,16,0,0,156,153,1,0,
        0,0,156,155,1,0,0,0,157,158,1,0,0,0,158,169,5,19,0,0,159,167,5,20,
        0,0,160,162,5,22,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,
        0,0,163,164,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,166,159,1,0,
        0,0,166,163,1,0,0,0,167,170,1,0,0,0,168,170,5,16,0,0,169,166,1,0,
        0,0,169,168,1,0,0,0,170,174,1,0,0,0,171,173,5,24,0,0,172,171,1,0,
        0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,19,1,0,0,
        0,176,174,1,0,0,0,177,178,5,20,0,0,178,183,5,17,0,0,179,184,5,20,
        0,0,180,184,5,18,0,0,181,184,5,22,0,0,182,184,3,12,6,0,183,179,1,
        0,0,0,183,180,1,0,0,0,183,181,1,0,0,0,183,182,1,0,0,0,184,188,1,
        0,0,0,185,187,5,24,0,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,
        0,0,0,188,189,1,0,0,0,189,21,1,0,0,0,190,188,1,0,0,0,29,25,39,43,
        47,52,56,62,67,74,77,80,92,96,99,109,120,128,133,140,144,150,153,
        156,163,166,169,174,183,188
    ]

class projectParser ( Parser ):

    grammarFileName = "project.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pass'", "'if'", "'('", "'):'", "'elif'", 
                     "'else:'", "'while('", "'for'", "'in'", "'range('", 
                     "')'", "':'", "'def'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ARITHMETIC", 
                      "ASSIGN", "OPERATORS", "CONDITIONAL", "IDENTIFIER", 
                      "LETTERS", "DIGITS", "COMMENT", "NEWLINE", "INDENT", 
                      "DEDENT" ]

    RULE_start = 0
    RULE_value = 1
    RULE_ifelse = 2
    RULE_whileLoop = 3
    RULE_forLoop = 4
    RULE_functionDeclare = 5
    RULE_functionCall = 6
    RULE_args = 7
    RULE_block = 8
    RULE_expression = 9
    RULE_variableDef = 10

    ruleNames =  [ "start", "value", "ifelse", "whileLoop", "forLoop", "functionDeclare", 
                   "functionCall", "args", "block", "expression", "variableDef" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    WS=15
    ARITHMETIC=16
    ASSIGN=17
    OPERATORS=18
    CONDITIONAL=19
    IDENTIFIER=20
    LETTERS=21
    DIGITS=22
    COMMENT=23
    NEWLINE=24
    INDENT=25
    DEDENT=26

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 22618502) != 0:
                self.state = 22
                self.value()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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


        def forLoop(self):
            return self.getTypedRuleContext(projectParser.ForLoopContext,0)


        def functionDeclare(self):
            return self.getTypedRuleContext(projectParser.FunctionDeclareContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(projectParser.FunctionCallContext,0)


        def NEWLINE(self):
            return self.getToken(projectParser.NEWLINE, 0)

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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(projectParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.variableDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.ifelse()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.functionDeclare()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 37
                self.functionCall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 38
                self.match(projectParser.NEWLINE)
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
            self.state = 41
            self.match(projectParser.T__1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 42
                self.match(projectParser.T__2)


            self.state = 45
            self.expression()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 46
                self.match(projectParser.T__3)


            self.state = 49
            self.block()
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.match(projectParser.T__4)
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==3:
                        self.state = 51
                        self.match(projectParser.T__2)


                    self.state = 54
                    self.expression()
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==4:
                        self.state = 55
                        self.match(projectParser.T__3)


                    self.state = 58
                    self.block() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 65
                self.match(projectParser.T__5)
                self.state = 66
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
            self.state = 69
            self.match(projectParser.T__6)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 70
                self.expression()
                pass

            elif la_ == 2:
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22:
                    self.state = 71
                    self.match(projectParser.DIGITS)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 79
                self.match(projectParser.T__3)


            self.state = 82
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.IDENTIFIER)
            else:
                return self.getToken(projectParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(projectParser.BlockContext,0)


        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.DIGITS)
            else:
                return self.getToken(projectParser.DIGITS, i)

        def getRuleIndex(self):
            return projectParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = projectParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(projectParser.T__7)
            self.state = 85
            self.match(projectParser.IDENTIFIER)
            self.state = 86
            self.match(projectParser.T__8)
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 87
                self.match(projectParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.state = 88
                self.match(projectParser.T__9)
                self.state = 96
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 22]:
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==22:
                        self.state = 89
                        self.match(projectParser.DIGITS)
                        self.state = 94
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                elif token in [20]:
                    self.state = 95
                    self.match(projectParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 98
                self.match(projectParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 101
            self.match(projectParser.T__11)
            self.state = 102
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(projectParser.IDENTIFIER, 0)

        def args(self):
            return self.getTypedRuleContext(projectParser.ArgsContext,0)


        def block(self):
            return self.getTypedRuleContext(projectParser.BlockContext,0)


        def getRuleIndex(self):
            return projectParser.RULE_functionDeclare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclare" ):
                listener.enterFunctionDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclare" ):
                listener.exitFunctionDeclare(self)




    def functionDeclare(self):

        localctx = projectParser.FunctionDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(projectParser.T__12)
            self.state = 105
            self.match(projectParser.IDENTIFIER)
            self.state = 106
            self.match(projectParser.T__2)
            self.state = 107
            self.args()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 108
                self.match(projectParser.T__3)


            self.state = 111
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(projectParser.IDENTIFIER, 0)

        def args(self):
            return self.getTypedRuleContext(projectParser.ArgsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.NEWLINE)
            else:
                return self.getToken(projectParser.NEWLINE, i)

        def getRuleIndex(self):
            return projectParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = projectParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(projectParser.IDENTIFIER)
            self.state = 114
            self.match(projectParser.T__2)
            self.state = 115
            self.args()
            self.state = 116
            self.match(projectParser.T__10)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 117
                    self.match(projectParser.NEWLINE) 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.IDENTIFIER)
            else:
                return self.getToken(projectParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return projectParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = projectParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 123
                self.match(projectParser.IDENTIFIER)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 124
                    self.match(projectParser.T__13)
                    self.state = 125
                    self.match(projectParser.IDENTIFIER)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(projectParser.ValueContext)
            else:
                return self.getTypedRuleContext(projectParser.ValueContext,i)


        def DEDENT(self):
            return self.getToken(projectParser.DEDENT, 0)

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
        self.enterRule(localctx, 16, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(projectParser.INDENT)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 137
                    self.value() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 143
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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(projectParser.NEWLINE)
            else:
                return self.getToken(projectParser.NEWLINE, i)

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
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 22]:
                self.state = 153
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 146
                    self.match(projectParser.IDENTIFIER)
                    pass
                elif token in [19, 22]:
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==22:
                        self.state = 147
                        self.match(projectParser.DIGITS)
                        self.state = 152
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [16]:
                self.state = 155
                self.match(projectParser.ARITHMETIC)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 158
            self.match(projectParser.CONDITIONAL)
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 166
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 159
                    self.match(projectParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 160
                            self.match(projectParser.DIGITS) 
                        self.state = 165
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                    pass


                pass

            elif la_ == 2:
                self.state = 168
                self.match(projectParser.ARITHMETIC)
                pass


            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 171
                    self.match(projectParser.NEWLINE) 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def functionCall(self):
            return self.getTypedRuleContext(projectParser.FunctionCallContext,0)


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
        self.enterRule(localctx, 20, self.RULE_variableDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(projectParser.IDENTIFIER)
            self.state = 178
            self.match(projectParser.ASSIGN)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 179
                self.match(projectParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 180
                self.match(projectParser.OPERATORS)
                pass

            elif la_ == 3:
                self.state = 181
                self.match(projectParser.DIGITS)
                pass

            elif la_ == 4:
                self.state = 182
                self.functionCall()
                pass


            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    self.match(projectParser.NEWLINE) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





