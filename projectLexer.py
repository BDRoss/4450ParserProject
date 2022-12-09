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
        4,0,24,248,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,1,13,1,13,1,14,4,14,106,8,14,11,14,12,14,107,1,14,1,14,1,15,
        1,15,5,15,114,8,15,10,15,12,15,117,9,15,3,15,119,8,15,1,15,1,15,
        1,15,5,15,124,8,15,10,15,12,15,127,9,15,3,15,129,8,15,1,15,5,15,
        132,8,15,10,15,12,15,135,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,146,8,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,176,8,18,1,19,1,19,3,19,
        180,8,19,1,19,1,19,1,19,5,19,185,8,19,10,19,12,19,188,9,19,1,20,
        4,20,191,8,20,11,20,12,20,192,1,20,4,20,196,8,20,11,20,12,20,197,
        3,20,200,8,20,1,21,4,21,203,8,21,11,21,12,21,204,1,22,1,22,5,22,
        209,8,22,10,22,12,22,212,9,22,1,22,1,22,1,22,1,22,1,23,3,23,219,
        8,23,1,23,1,23,5,23,223,8,23,10,23,12,23,226,9,23,1,23,5,23,229,
        8,23,10,23,12,23,232,9,23,1,23,1,23,5,23,236,8,23,10,23,12,23,239,
        9,23,1,23,5,23,242,8,23,10,23,12,23,245,9,23,3,23,247,8,23,0,0,24,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,
        1,0,6,1,0,32,32,4,0,37,37,42,43,45,45,47,47,1,0,97,122,1,0,65,90,
        1,0,48,57,1,0,10,10,283,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,
        1,0,0,0,1,49,1,0,0,0,3,54,1,0,0,0,5,57,1,0,0,0,7,59,1,0,0,0,9,62,
        1,0,0,0,11,67,1,0,0,0,13,73,1,0,0,0,15,80,1,0,0,0,17,84,1,0,0,0,
        19,87,1,0,0,0,21,94,1,0,0,0,23,96,1,0,0,0,25,98,1,0,0,0,27,102,1,
        0,0,0,29,105,1,0,0,0,31,118,1,0,0,0,33,145,1,0,0,0,35,147,1,0,0,
        0,37,175,1,0,0,0,39,179,1,0,0,0,41,199,1,0,0,0,43,202,1,0,0,0,45,
        206,1,0,0,0,47,246,1,0,0,0,49,50,5,112,0,0,50,51,5,97,0,0,51,52,
        5,115,0,0,52,53,5,115,0,0,53,2,1,0,0,0,54,55,5,105,0,0,55,56,5,102,
        0,0,56,4,1,0,0,0,57,58,5,40,0,0,58,6,1,0,0,0,59,60,5,41,0,0,60,61,
        5,58,0,0,61,8,1,0,0,0,62,63,5,101,0,0,63,64,5,108,0,0,64,65,5,105,
        0,0,65,66,5,102,0,0,66,10,1,0,0,0,67,68,5,101,0,0,68,69,5,108,0,
        0,69,70,5,115,0,0,70,71,5,101,0,0,71,72,5,58,0,0,72,12,1,0,0,0,73,
        74,5,119,0,0,74,75,5,104,0,0,75,76,5,105,0,0,76,77,5,108,0,0,77,
        78,5,101,0,0,78,79,5,40,0,0,79,14,1,0,0,0,80,81,5,102,0,0,81,82,
        5,111,0,0,82,83,5,114,0,0,83,16,1,0,0,0,84,85,5,105,0,0,85,86,5,
        110,0,0,86,18,1,0,0,0,87,88,5,114,0,0,88,89,5,97,0,0,89,90,5,110,
        0,0,90,91,5,103,0,0,91,92,5,101,0,0,92,93,5,40,0,0,93,20,1,0,0,0,
        94,95,5,41,0,0,95,22,1,0,0,0,96,97,5,58,0,0,97,24,1,0,0,0,98,99,
        5,100,0,0,99,100,5,101,0,0,100,101,5,102,0,0,101,26,1,0,0,0,102,
        103,5,44,0,0,103,28,1,0,0,0,104,106,7,0,0,0,105,104,1,0,0,0,106,
        107,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,
        110,6,14,0,0,110,30,1,0,0,0,111,119,3,39,19,0,112,114,3,43,21,0,
        113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,
        116,119,1,0,0,0,117,115,1,0,0,0,118,111,1,0,0,0,118,115,1,0,0,0,
        119,120,1,0,0,0,120,128,3,35,17,0,121,129,3,39,19,0,122,124,3,43,
        21,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,
        0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,121,1,0,0,0,128,125,1,0,
        0,0,129,133,1,0,0,0,130,132,3,47,23,0,131,130,1,0,0,0,132,135,1,
        0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,32,1,0,0,0,135,133,1,0,
        0,0,136,137,5,43,0,0,137,146,5,61,0,0,138,139,5,45,0,0,139,146,5,
        61,0,0,140,141,5,42,0,0,141,146,5,61,0,0,142,143,5,47,0,0,143,146,
        5,61,0,0,144,146,5,61,0,0,145,136,1,0,0,0,145,138,1,0,0,0,145,140,
        1,0,0,0,145,142,1,0,0,0,145,144,1,0,0,0,146,34,1,0,0,0,147,148,7,
        1,0,0,148,36,1,0,0,0,149,176,5,60,0,0,150,151,5,60,0,0,151,176,5,
        61,0,0,152,176,5,62,0,0,153,154,5,62,0,0,154,176,5,61,0,0,155,156,
        5,61,0,0,156,176,5,61,0,0,157,158,5,33,0,0,158,176,5,61,0,0,159,
        160,5,65,0,0,160,161,5,78,0,0,161,176,5,68,0,0,162,163,5,79,0,0,
        163,176,5,82,0,0,164,165,5,78,0,0,165,166,5,79,0,0,166,176,5,84,
        0,0,167,168,5,97,0,0,168,169,5,110,0,0,169,176,5,100,0,0,170,171,
        5,111,0,0,171,176,5,114,0,0,172,173,5,110,0,0,173,174,5,111,0,0,
        174,176,5,116,0,0,175,149,1,0,0,0,175,150,1,0,0,0,175,152,1,0,0,
        0,175,153,1,0,0,0,175,155,1,0,0,0,175,157,1,0,0,0,175,159,1,0,0,
        0,175,162,1,0,0,0,175,164,1,0,0,0,175,167,1,0,0,0,175,170,1,0,0,
        0,175,172,1,0,0,0,176,38,1,0,0,0,177,180,3,41,20,0,178,180,5,95,
        0,0,179,177,1,0,0,0,179,178,1,0,0,0,180,186,1,0,0,0,181,185,3,41,
        20,0,182,185,5,95,0,0,183,185,3,43,21,0,184,181,1,0,0,0,184,182,
        1,0,0,0,184,183,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,
        1,0,0,0,187,40,1,0,0,0,188,186,1,0,0,0,189,191,7,2,0,0,190,189,1,
        0,0,0,191,192,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,200,1,
        0,0,0,194,196,7,3,0,0,195,194,1,0,0,0,196,197,1,0,0,0,197,195,1,
        0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,190,1,0,0,0,199,195,1,
        0,0,0,200,42,1,0,0,0,201,203,7,4,0,0,202,201,1,0,0,0,203,204,1,0,
        0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,44,1,0,0,0,206,210,5,35,
        0,0,207,209,8,5,0,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,1,0,
        0,0,210,211,1,0,0,0,211,213,1,0,0,0,212,210,1,0,0,0,213,214,3,47,
        23,0,214,215,1,0,0,0,215,216,6,22,0,0,216,46,1,0,0,0,217,219,5,13,
        0,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,224,5,10,
        0,0,221,223,5,9,0,0,222,221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,
        0,0,224,225,1,0,0,0,225,230,1,0,0,0,226,224,1,0,0,0,227,229,5,32,
        0,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,
        0,0,231,247,1,0,0,0,232,230,1,0,0,0,233,237,5,10,0,0,234,236,5,9,
        0,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,
        0,0,238,243,1,0,0,0,239,237,1,0,0,0,240,242,5,32,0,0,241,240,1,0,
        0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,247,1,0,
        0,0,245,243,1,0,0,0,246,218,1,0,0,0,246,233,1,0,0,0,247,48,1,0,0,
        0,23,0,107,115,118,125,128,133,145,175,179,184,186,192,197,199,204,
        210,218,224,230,237,243,246,1,6,0,0
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
    T__11 = 12
    T__12 = 13
    T__13 = 14
    WS = 15
    ARITHMETIC = 16
    ASSIGN = 17
    OPERATORS = 18
    CONDITIONAL = 19
    IDENTIFIER = 20
    LETTERS = 21
    DIGITS = 22
    COMMENT = 23
    NEWLINE = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'pass'", "'if'", "'('", "'):'", "'elif'", "'else:'", "'while('", 
            "'for'", "'in'", "'range('", "')'", "':'", "'def'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ARITHMETIC", "ASSIGN", "OPERATORS", "CONDITIONAL", "IDENTIFIER", 
            "LETTERS", "DIGITS", "COMMENT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "WS", "ARITHMETIC", "ASSIGN", "OPERATORS", "CONDITIONAL", 
                  "IDENTIFIER", "LETTERS", "DIGITS", "COMMENT", "NEWLINE" ]

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



