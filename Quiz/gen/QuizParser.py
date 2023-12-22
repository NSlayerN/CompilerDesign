# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Quiz/Quiz.g4 by ANTLR 4.13.1
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
        4,1,12,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,9,
        2,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,56,
        8,4,1,4,0,2,2,4,5,0,2,4,6,8,0,0,59,0,10,1,0,0,0,2,14,1,0,0,0,4,28,
        1,0,0,0,6,47,1,0,0,0,8,55,1,0,0,0,10,11,5,9,0,0,11,12,5,8,0,0,12,
        13,3,2,1,0,13,1,1,0,0,0,14,15,6,1,-1,0,15,16,3,4,2,0,16,25,1,0,0,
        0,17,18,10,3,0,0,18,19,5,3,0,0,19,24,3,4,2,0,20,21,10,2,0,0,21,22,
        5,4,0,0,22,24,3,4,2,0,23,17,1,0,0,0,23,20,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,25,1,0,0,0,28,29,6,2,
        -1,0,29,30,3,6,3,0,30,39,1,0,0,0,31,32,10,3,0,0,32,33,5,5,0,0,33,
        38,3,6,3,0,34,35,10,2,0,0,35,36,5,6,0,0,36,38,3,6,3,0,37,31,1,0,
        0,0,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,5,
        1,0,0,0,41,39,1,0,0,0,42,43,3,8,4,0,43,44,5,7,0,0,44,45,3,6,3,0,
        45,48,1,0,0,0,46,48,3,8,4,0,47,42,1,0,0,0,47,46,1,0,0,0,48,7,1,0,
        0,0,49,50,5,1,0,0,50,51,3,2,1,0,51,52,5,2,0,0,52,56,1,0,0,0,53,56,
        5,10,0,0,54,56,5,9,0,0,55,49,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,
        56,9,1,0,0,0,6,23,25,37,39,47,55
    ]

class QuizParser ( Parser ):

    grammarFileName = "Quiz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "MULT", "DIVIDE", "EXPO", "ASSIGN", "Id", "Number", 
                      "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_fact = 3
    RULE_exponent = 4

    ruleNames =  [ "start", "expr", "term", "fact", "exponent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PLUS=3
    MINUS=4
    MULT=5
    DIVIDE=6
    EXPO=7
    ASSIGN=8
    Id=9
    Number=10
    WS=11
    NEWLINE=12

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

        def Id(self):
            return self.getToken(QuizParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(QuizParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(QuizParser.ExprContext,0)


        def getRuleIndex(self):
            return QuizParser.RULE_start

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

        localctx = QuizParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(QuizParser.Id)
            self.state = 11
            self.match(QuizParser.ASSIGN)
            self.state = 12
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(QuizParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(QuizParser.ExprContext,0)


        def PLUS(self):
            return self.getToken(QuizParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(QuizParser.MINUS, 0)

        def getRuleIndex(self):
            return QuizParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QuizParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = QuizParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        self.match(QuizParser.PLUS)
                        self.state = 19
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = QuizParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 21
                        self.match(QuizParser.MINUS)
                        self.state = 22
                        self.term(0)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(QuizParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(QuizParser.TermContext,0)


        def MULT(self):
            return self.getToken(QuizParser.MULT, 0)

        def DIVIDE(self):
            return self.getToken(QuizParser.DIVIDE, 0)

        def getRuleIndex(self):
            return QuizParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QuizParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = QuizParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        self.match(QuizParser.MULT)
                        self.state = 33
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = QuizParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(QuizParser.DIVIDE)
                        self.state = 36
                        self.fact()
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponent(self):
            return self.getTypedRuleContext(QuizParser.ExponentContext,0)


        def EXPO(self):
            return self.getToken(QuizParser.EXPO, 0)

        def fact(self):
            return self.getTypedRuleContext(QuizParser.FactContext,0)


        def getRuleIndex(self):
            return QuizParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = QuizParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.exponent()
                self.state = 43
                self.match(QuizParser.EXPO)
                self.state = 44
                self.fact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.exponent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(QuizParser.ExprContext,0)


        def Number(self):
            return self.getToken(QuizParser.Number, 0)

        def Id(self):
            return self.getToken(QuizParser.Id, 0)

        def getRuleIndex(self):
            return QuizParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = QuizParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exponent)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(QuizParser.T__0)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(QuizParser.T__1)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(QuizParser.Number)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(QuizParser.Id)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




