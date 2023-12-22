# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Quiz/Quiz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QuizParser import QuizParser
else:
    from QuizParser import QuizParser

# This class defines a complete listener for a parse tree produced by QuizParser.
class QuizListener(ParseTreeListener):

    # Enter a parse tree produced by QuizParser#start.
    def enterStart(self, ctx:QuizParser.StartContext):
        pass

    # Exit a parse tree produced by QuizParser#start.
    def exitStart(self, ctx:QuizParser.StartContext):
        pass


    # Enter a parse tree produced by QuizParser#expr.
    def enterExpr(self, ctx:QuizParser.ExprContext):
        pass

    # Exit a parse tree produced by QuizParser#expr.
    def exitExpr(self, ctx:QuizParser.ExprContext):
        pass


    # Enter a parse tree produced by QuizParser#term.
    def enterTerm(self, ctx:QuizParser.TermContext):
        pass

    # Exit a parse tree produced by QuizParser#term.
    def exitTerm(self, ctx:QuizParser.TermContext):
        pass


    # Enter a parse tree produced by QuizParser#fact.
    def enterFact(self, ctx:QuizParser.FactContext):
        pass

    # Exit a parse tree produced by QuizParser#fact.
    def exitFact(self, ctx:QuizParser.FactContext):
        pass


    # Enter a parse tree produced by QuizParser#exponent.
    def enterExponent(self, ctx:QuizParser.ExponentContext):
        pass

    # Exit a parse tree produced by QuizParser#exponent.
    def exitExponent(self, ctx:QuizParser.ExponentContext):
        pass



del QuizParser