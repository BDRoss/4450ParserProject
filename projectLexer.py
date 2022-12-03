# Generated from project.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from projectParser import projectParser


def serializedATN():
    return [
        4,0,21,225,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,
        11,4,11,89,8,11,11,11,12,11,90,1,11,1,11,1,12,1,12,5,12,97,8,12,
        10,12,12,12,100,9,12,3,12,102,8,12,1,12,1,12,1,12,5,12,107,8,12,
        10,12,12,12,110,9,12,3,12,112,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,123,8,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,153,8,15,1,16,1,16,
        3,16,157,8,16,1,16,1,16,1,16,5,16,162,8,16,10,16,12,16,165,9,16,
        1,17,4,17,168,8,17,11,17,12,17,169,1,17,4,17,173,8,17,11,17,12,17,
        174,3,17,177,8,17,1,18,4,18,180,8,18,11,18,12,18,181,1,19,1,19,5,
        19,186,8,19,10,19,12,19,189,9,19,1,19,1,19,1,19,1,19,1,20,3,20,196,
        8,20,1,20,1,20,5,20,200,8,20,10,20,12,20,203,9,20,1,20,5,20,206,
        8,20,10,20,12,20,209,9,20,1,20,1,20,5,20,213,8,20,10,20,12,20,216,
        9,20,1,20,5,20,219,8,20,10,20,12,20,222,9,20,3,20,224,8,20,0,0,21,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,1,0,6,1,0,32,32,
        4,0,37,37,42,43,45,45,47,47,1,0,97,122,1,0,65,90,1,0,48,57,1,0,10,
        10,259,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,
        0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,
        0,0,41,1,0,0,0,1,43,1,0,0,0,3,46,1,0,0,0,5,48,1,0,0,0,7,51,1,0,0,
        0,9,56,1,0,0,0,11,62,1,0,0,0,13,69,1,0,0,0,15,73,1,0,0,0,17,76,1,
        0,0,0,19,83,1,0,0,0,21,85,1,0,0,0,23,88,1,0,0,0,25,101,1,0,0,0,27,
        122,1,0,0,0,29,124,1,0,0,0,31,152,1,0,0,0,33,156,1,0,0,0,35,176,
        1,0,0,0,37,179,1,0,0,0,39,183,1,0,0,0,41,223,1,0,0,0,43,44,5,105,
        0,0,44,45,5,102,0,0,45,2,1,0,0,0,46,47,5,40,0,0,47,4,1,0,0,0,48,
        49,5,41,0,0,49,50,5,58,0,0,50,6,1,0,0,0,51,52,5,101,0,0,52,53,5,
        108,0,0,53,54,5,105,0,0,54,55,5,102,0,0,55,8,1,0,0,0,56,57,5,101,
        0,0,57,58,5,108,0,0,58,59,5,115,0,0,59,60,5,101,0,0,60,61,5,58,0,
        0,61,10,1,0,0,0,62,63,5,119,0,0,63,64,5,104,0,0,64,65,5,105,0,0,
        65,66,5,108,0,0,66,67,5,101,0,0,67,68,5,40,0,0,68,12,1,0,0,0,69,
        70,5,102,0,0,70,71,5,111,0,0,71,72,5,114,0,0,72,14,1,0,0,0,73,74,
        5,105,0,0,74,75,5,110,0,0,75,16,1,0,0,0,76,77,5,114,0,0,77,78,5,
        97,0,0,78,79,5,110,0,0,79,80,5,103,0,0,80,81,5,101,0,0,81,82,5,40,
        0,0,82,18,1,0,0,0,83,84,5,41,0,0,84,20,1,0,0,0,85,86,5,58,0,0,86,
        22,1,0,0,0,87,89,7,0,0,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,
        0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,6,11,0,0,93,24,1,0,0,0,94,102,
        3,33,16,0,95,97,3,37,18,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,
        0,0,98,99,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,101,94,1,0,0,0,101,
        98,1,0,0,0,102,103,1,0,0,0,103,111,3,29,14,0,104,112,3,33,16,0,105,
        107,3,37,18,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,
        109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,104,1,0,0,0,111,
        108,1,0,0,0,112,26,1,0,0,0,113,114,5,43,0,0,114,123,5,61,0,0,115,
        116,5,45,0,0,116,123,5,61,0,0,117,118,5,42,0,0,118,123,5,61,0,0,
        119,120,5,47,0,0,120,123,5,61,0,0,121,123,5,61,0,0,122,113,1,0,0,
        0,122,115,1,0,0,0,122,117,1,0,0,0,122,119,1,0,0,0,122,121,1,0,0,
        0,123,28,1,0,0,0,124,125,7,1,0,0,125,30,1,0,0,0,126,153,5,60,0,0,
        127,128,5,60,0,0,128,153,5,61,0,0,129,153,5,62,0,0,130,131,5,62,
        0,0,131,153,5,61,0,0,132,133,5,61,0,0,133,153,5,61,0,0,134,135,5,
        33,0,0,135,153,5,61,0,0,136,137,5,65,0,0,137,138,5,78,0,0,138,153,
        5,68,0,0,139,140,5,79,0,0,140,153,5,82,0,0,141,142,5,78,0,0,142,
        143,5,79,0,0,143,153,5,84,0,0,144,145,5,97,0,0,145,146,5,110,0,0,
        146,153,5,100,0,0,147,148,5,111,0,0,148,153,5,114,0,0,149,150,5,
        110,0,0,150,151,5,111,0,0,151,153,5,116,0,0,152,126,1,0,0,0,152,
        127,1,0,0,0,152,129,1,0,0,0,152,130,1,0,0,0,152,132,1,0,0,0,152,
        134,1,0,0,0,152,136,1,0,0,0,152,139,1,0,0,0,152,141,1,0,0,0,152,
        144,1,0,0,0,152,147,1,0,0,0,152,149,1,0,0,0,153,32,1,0,0,0,154,157,
        3,35,17,0,155,157,5,95,0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,163,
        1,0,0,0,158,162,3,35,17,0,159,162,5,95,0,0,160,162,3,37,18,0,161,
        158,1,0,0,0,161,159,1,0,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,
        161,1,0,0,0,163,164,1,0,0,0,164,34,1,0,0,0,165,163,1,0,0,0,166,168,
        7,2,0,0,167,166,1,0,0,0,168,169,1,0,0,0,169,167,1,0,0,0,169,170,
        1,0,0,0,170,177,1,0,0,0,171,173,7,3,0,0,172,171,1,0,0,0,173,174,
        1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,177,1,0,0,0,176,167,
        1,0,0,0,176,172,1,0,0,0,177,36,1,0,0,0,178,180,7,4,0,0,179,178,1,
        0,0,0,180,181,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,38,1,0,
        0,0,183,187,5,35,0,0,184,186,8,5,0,0,185,184,1,0,0,0,186,189,1,0,
        0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,
        0,0,190,191,3,41,20,0,191,192,1,0,0,0,192,193,6,19,0,0,193,40,1,
        0,0,0,194,196,5,13,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,
        0,0,0,197,201,5,10,0,0,198,200,5,9,0,0,199,198,1,0,0,0,200,203,1,
        0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,207,1,0,0,0,203,201,1,
        0,0,0,204,206,5,32,0,0,205,204,1,0,0,0,206,209,1,0,0,0,207,205,1,
        0,0,0,207,208,1,0,0,0,208,224,1,0,0,0,209,207,1,0,0,0,210,214,5,
        10,0,0,211,213,5,9,0,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,
        0,0,0,214,215,1,0,0,0,215,220,1,0,0,0,216,214,1,0,0,0,217,219,5,
        32,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,
        0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,223,195,1,0,0,0,223,210,1,
        0,0,0,224,42,1,0,0,0,22,0,90,98,101,108,111,122,152,156,161,163,
        169,174,176,181,187,195,201,207,214,220,223,1,6,0,0
    ]

class projectLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    WS = 12
    ARITHMETIC = 13
    ASSIGN = 14
    OPERATORS = 15
    CONDITIONAL = 16
    IDENTIFIER = 17
    LETTERS = 18
    DIGITS = 19
    COMMENT = 20
    NEWLINE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'('", "'):'", "'elif'", "'else:'", "'while('", "'for'", 
            "'in'", "'range('", "')'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ARITHMETIC", "ASSIGN", "OPERATORS", "CONDITIONAL", "IDENTIFIER", 
            "LETTERS", "DIGITS", "COMMENT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "WS", "ARITHMETIC", "ASSIGN", 
                  "OPERATORS", "CONDITIONAL", "IDENTIFIER", "LETTERS", "DIGITS", 
                  "COMMENT", "NEWLINE" ]

    grammarFileName = "project.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: projectLexer = lexer

        def pull_token(self):
            return super(projectLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NEWLINE, projectParser.INDENT, projectParser.DEDENT, 1)
        return self.denter.next_token()



