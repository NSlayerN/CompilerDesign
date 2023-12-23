# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw4/Pass.g4 by ANTLR 4.13.1
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
        4,1,6,8,2,0,7,0,1,0,4,0,4,8,0,11,0,12,0,5,1,0,0,0,1,0,0,0,7,0,3,
        1,0,0,0,2,4,5,1,0,0,3,2,1,0,0,0,4,5,1,0,0,0,5,3,1,0,0,0,5,6,1,0,
        0,0,6,1,1,0,0,0,1,5
    ]

class PassParser ( Parser ):

    grammarFileName = "Pass.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "CHAR", "DIGIT", "UPPERCASE", "LOWERCASE", 
                      "SYMBOL", "WS" ]

    RULE_password = 0

    ruleNames =  [ "password" ]

    EOF = Token.EOF
    CHAR=1
    DIGIT=2
    UPPERCASE=3
    LOWERCASE=4
    SYMBOL=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PasswordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PassParser.CHAR)
            else:
                return self.getToken(PassParser.CHAR, i)

        def getRuleIndex(self):
            return PassParser.RULE_password

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassword" ):
                listener.enterPassword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassword" ):
                listener.exitPassword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassword" ):
                return visitor.visitPassword(self)
            else:
                return visitor.visitChildren(self)




    def password(self):

        localctx = PassParser.PasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_password)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(PassParser.CHAR)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





