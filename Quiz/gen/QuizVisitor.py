# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Quiz/Quiz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QuizParser import QuizParser
else:
    from QuizParser import QuizParser

# This class defines a complete generic visitor for a parse tree produced by QuizParser.

class QuizVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QuizParser#start.
    def visitStart(self, ctx:QuizParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizParser#expr.
    def visitExpr(self, ctx:QuizParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizParser#term.
    def visitTerm(self, ctx:QuizParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizParser#fact.
    def visitFact(self, ctx:QuizParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizParser#exponent.
    def visitExponent(self, ctx:QuizParser.ExponentContext):
        return self.visitChildren(ctx)



del QuizParser