# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw2/Exp.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpParser import ExpParser
else:
    from ExpParser import ExpParser

# This class defines a complete listener for a parse tree produced by ExpParser.
class ExpListener(ParseTreeListener):

    # Enter a parse tree produced by ExpParser#file.
    def enterFile(self, ctx:ExpParser.FileContext):
        pass

    # Exit a parse tree produced by ExpParser#file.
    def exitFile(self, ctx:ExpParser.FileContext):
        pass


    # Enter a parse tree produced by ExpParser#varDecl.
    def enterVarDecl(self, ctx:ExpParser.VarDeclContext):
        pass

    # Exit a parse tree produced by ExpParser#varDecl.
    def exitVarDecl(self, ctx:ExpParser.VarDeclContext):
        pass


    # Enter a parse tree produced by ExpParser#type.
    def enterType(self, ctx:ExpParser.TypeContext):
        pass

    # Exit a parse tree produced by ExpParser#type.
    def exitType(self, ctx:ExpParser.TypeContext):
        pass


    # Enter a parse tree produced by ExpParser#functionDecl.
    def enterFunctionDecl(self, ctx:ExpParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by ExpParser#functionDecl.
    def exitFunctionDecl(self, ctx:ExpParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by ExpParser#formalParameters.
    def enterFormalParameters(self, ctx:ExpParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by ExpParser#formalParameters.
    def exitFormalParameters(self, ctx:ExpParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by ExpParser#formalParameter.
    def enterFormalParameter(self, ctx:ExpParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by ExpParser#formalParameter.
    def exitFormalParameter(self, ctx:ExpParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by ExpParser#block.
    def enterBlock(self, ctx:ExpParser.BlockContext):
        pass

    # Exit a parse tree produced by ExpParser#block.
    def exitBlock(self, ctx:ExpParser.BlockContext):
        pass


    # Enter a parse tree produced by ExpParser#stat.
    def enterStat(self, ctx:ExpParser.StatContext):
        pass

    # Exit a parse tree produced by ExpParser#stat.
    def exitStat(self, ctx:ExpParser.StatContext):
        pass


    # Enter a parse tree produced by ExpParser#expr.
    def enterExpr(self, ctx:ExpParser.ExprContext):
        pass

    # Exit a parse tree produced by ExpParser#expr.
    def exitExpr(self, ctx:ExpParser.ExprContext):
        pass


    # Enter a parse tree produced by ExpParser#exprList.
    def enterExprList(self, ctx:ExpParser.ExprListContext):
        pass

    # Exit a parse tree produced by ExpParser#exprList.
    def exitExprList(self, ctx:ExpParser.ExprListContext):
        pass



del ExpParser