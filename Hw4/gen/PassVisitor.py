# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw4/Pass.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PassParser import PassParser
else:
    from PassParser import PassParser

# This class defines a complete generic visitor for a parse tree produced by PassParser.

class PassVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PassParser#password.
    def visitPassword(self, ctx:PassParser.PasswordContext):
        return self.visitChildren(ctx)



del PassParser