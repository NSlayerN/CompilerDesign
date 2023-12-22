# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw3/homework3.g4 by ANTLR 4.13.1
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
        4,1,8,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,0,1,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,
        0,0,37,0,20,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,30,1,0,0,0,8,32,
        1,0,0,0,10,34,1,0,0,0,12,36,1,0,0,0,14,21,3,2,1,0,15,21,3,4,2,0,
        16,21,3,6,3,0,17,21,3,8,4,0,18,21,3,10,5,0,19,21,3,12,6,0,20,14,
        1,0,0,0,20,15,1,0,0,0,20,16,1,0,0,0,20,17,1,0,0,0,20,18,1,0,0,0,
        20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,1,
        0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,5,1,0,0,27,3,1,0,0,0,28,29,
        5,2,0,0,29,5,1,0,0,0,30,31,5,3,0,0,31,7,1,0,0,0,32,33,5,4,0,0,33,
        9,1,0,0,0,34,35,5,5,0,0,35,11,1,0,0,0,36,37,5,6,0,0,37,13,1,0,0,
        0,2,20,22
    ]

class homework3Parser ( Parser ):

    grammarFileName = "homework3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "EMAIL", "NATIONALNUMBER", "POSTALCODE", 
                      "FLOAT", "VERSION", "URLADDRESS", "DIGIT", "WS" ]

    RULE_start = 0
    RULE_email = 1
    RULE_nationalNum = 2
    RULE_postalCode = 3
    RULE_float = 4
    RULE_versionOfSFTW = 5
    RULE_url = 6

    ruleNames =  [ "start", "email", "nationalNum", "postalCode", "float", 
                   "versionOfSFTW", "url" ]

    EOF = Token.EOF
    EMAIL=1
    NATIONALNUMBER=2
    POSTALCODE=3
    FLOAT=4
    VERSION=5
    URLADDRESS=6
    DIGIT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(homework3Parser.EOF, 0)

        def email(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(homework3Parser.EmailContext)
            else:
                return self.getTypedRuleContext(homework3Parser.EmailContext,i)


        def nationalNum(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(homework3Parser.NationalNumContext)
            else:
                return self.getTypedRuleContext(homework3Parser.NationalNumContext,i)


        def postalCode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(homework3Parser.PostalCodeContext)
            else:
                return self.getTypedRuleContext(homework3Parser.PostalCodeContext,i)


        def float_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(homework3Parser.FloatContext)
            else:
                return self.getTypedRuleContext(homework3Parser.FloatContext,i)


        def versionOfSFTW(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(homework3Parser.VersionOfSFTWContext)
            else:
                return self.getTypedRuleContext(homework3Parser.VersionOfSFTWContext,i)


        def url(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(homework3Parser.UrlContext)
            else:
                return self.getTypedRuleContext(homework3Parser.UrlContext,i)


        def getRuleIndex(self):
            return homework3Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = homework3Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 14
                    self.email()
                    pass
                elif token in [2]:
                    self.state = 15
                    self.nationalNum()
                    pass
                elif token in [3]:
                    self.state = 16
                    self.postalCode()
                    pass
                elif token in [4]:
                    self.state = 17
                    self.float_()
                    pass
                elif token in [5]:
                    self.state = 18
                    self.versionOfSFTW()
                    pass
                elif token in [6]:
                    self.state = 19
                    self.url()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                    break

            self.state = 24
            self.match(homework3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMAIL(self):
            return self.getToken(homework3Parser.EMAIL, 0)

        def getRuleIndex(self):
            return homework3Parser.RULE_email

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmail" ):
                listener.enterEmail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmail" ):
                listener.exitEmail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmail" ):
                return visitor.visitEmail(self)
            else:
                return visitor.visitChildren(self)




    def email(self):

        localctx = homework3Parser.EmailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_email)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(homework3Parser.EMAIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NationalNumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NATIONALNUMBER(self):
            return self.getToken(homework3Parser.NATIONALNUMBER, 0)

        def getRuleIndex(self):
            return homework3Parser.RULE_nationalNum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNationalNum" ):
                listener.enterNationalNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNationalNum" ):
                listener.exitNationalNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNationalNum" ):
                return visitor.visitNationalNum(self)
            else:
                return visitor.visitChildren(self)




    def nationalNum(self):

        localctx = homework3Parser.NationalNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nationalNum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(homework3Parser.NATIONALNUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostalCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSTALCODE(self):
            return self.getToken(homework3Parser.POSTALCODE, 0)

        def getRuleIndex(self):
            return homework3Parser.RULE_postalCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostalCode" ):
                listener.enterPostalCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostalCode" ):
                listener.exitPostalCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostalCode" ):
                return visitor.visitPostalCode(self)
            else:
                return visitor.visitChildren(self)




    def postalCode(self):

        localctx = homework3Parser.PostalCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_postalCode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(homework3Parser.POSTALCODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(homework3Parser.FLOAT, 0)

        def getRuleIndex(self):
            return homework3Parser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = homework3Parser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(homework3Parser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionOfSFTWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION(self):
            return self.getToken(homework3Parser.VERSION, 0)

        def getRuleIndex(self):
            return homework3Parser.RULE_versionOfSFTW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersionOfSFTW" ):
                listener.enterVersionOfSFTW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersionOfSFTW" ):
                listener.exitVersionOfSFTW(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersionOfSFTW" ):
                return visitor.visitVersionOfSFTW(self)
            else:
                return visitor.visitChildren(self)




    def versionOfSFTW(self):

        localctx = homework3Parser.VersionOfSFTWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_versionOfSFTW)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(homework3Parser.VERSION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URLADDRESS(self):
            return self.getToken(homework3Parser.URLADDRESS, 0)

        def getRuleIndex(self):
            return homework3Parser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = homework3Parser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(homework3Parser.URLADDRESS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





