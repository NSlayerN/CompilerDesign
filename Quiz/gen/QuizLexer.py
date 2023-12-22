# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Quiz/Quiz.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,72,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,10,1,10,5,10,52,8,10,10,10,12,10,55,9,10,1,
        11,4,11,58,8,11,11,11,12,11,59,1,12,4,12,63,8,12,11,12,12,12,64,
        1,12,1,12,1,13,1,13,1,13,1,13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,0,23,0,25,11,27,12,1,0,3,2,0,65,90,97,122,1,
        0,48,57,2,0,9,9,13,13,72,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,31,
        1,0,0,0,5,33,1,0,0,0,7,35,1,0,0,0,9,37,1,0,0,0,11,39,1,0,0,0,13,
        41,1,0,0,0,15,43,1,0,0,0,17,45,1,0,0,0,19,47,1,0,0,0,21,49,1,0,0,
        0,23,57,1,0,0,0,25,62,1,0,0,0,27,68,1,0,0,0,29,30,5,40,0,0,30,2,
        1,0,0,0,31,32,5,41,0,0,32,4,1,0,0,0,33,34,5,43,0,0,34,6,1,0,0,0,
        35,36,5,45,0,0,36,8,1,0,0,0,37,38,5,42,0,0,38,10,1,0,0,0,39,40,5,
        47,0,0,40,12,1,0,0,0,41,42,5,94,0,0,42,14,1,0,0,0,43,44,5,61,0,0,
        44,16,1,0,0,0,45,46,3,21,10,0,46,18,1,0,0,0,47,48,3,23,11,0,48,20,
        1,0,0,0,49,53,7,0,0,0,50,52,7,0,0,0,51,50,1,0,0,0,52,55,1,0,0,0,
        53,51,1,0,0,0,53,54,1,0,0,0,54,22,1,0,0,0,55,53,1,0,0,0,56,58,7,
        1,0,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,
        24,1,0,0,0,61,63,7,2,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,
        0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,6,12,0,0,67,26,1,0,0,0,68,69,
        5,10,0,0,69,70,1,0,0,0,70,71,6,13,1,0,71,28,1,0,0,0,4,0,53,59,64,
        2,0,1,0,6,0,0
    ]

class QuizLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    PLUS = 3
    MINUS = 4
    MULT = 5
    DIVIDE = 6
    EXPO = 7
    ASSIGN = 8
    Id = 9
    Number = 10
    WS = 11
    NEWLINE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'^'", "'='", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MULT", "DIVIDE", "EXPO", "ASSIGN", "Id", "Number", 
            "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "PLUS", "MINUS", "MULT", "DIVIDE", "EXPO", 
                  "ASSIGN", "Id", "Number", "IDENTIFIER", "NUMBER", "WS", 
                  "NEWLINE" ]

    grammarFileName = "Quiz.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


