# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw4/Pass.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PassParser import PassParser
else:
    from PassParser import PassParser

# This class defines a complete listener for a parse tree produced by PassParser.
class PassListener(ParseTreeListener):

    # Enter a parse tree produced by PassParser#password.
    def enterPassword(self, ctx:PassParser.PasswordContext):
        pass

    # Exit a parse tree produced by PassParser#password.
    def exitPassword(self, ctx:PassParser.PasswordContext):
        pass



del PassParser