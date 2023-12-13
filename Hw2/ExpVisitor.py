# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw2/Exp.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpParser import ExpParser
else:
    from ExpParser import ExpParser

# This class defines a complete generic visitor for a parse tree produced by ExpParser.

class ExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpParser#file.
    def visitFile(self, ctx:ExpParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#varDecl.
    def visitVarDecl(self, ctx:ExpParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#type.
    def visitType(self, ctx:ExpParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#functionDecl.
    def visitFunctionDecl(self, ctx:ExpParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#formalParameters.
    def visitFormalParameters(self, ctx:ExpParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#formalParameter.
    def visitFormalParameter(self, ctx:ExpParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#block.
    def visitBlock(self, ctx:ExpParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#stat.
    def visitStat(self, ctx:ExpParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#expr.
    def visitExpr(self, ctx:ExpParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpParser#exprList.
    def visitExprList(self, ctx:ExpParser.ExprListContext):
        return self.visitChildren(ctx)



del ExpParser