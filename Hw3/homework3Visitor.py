# Generated from C:/Users/persianNB/Desktop/CompilerDesign/Hw3/homework3.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .homework3Parser import homework3Parser
else:
    from homework3Parser import homework3Parser

# This class defines a complete generic visitor for a parse tree produced by homework3Parser.

class homework3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by homework3Parser#start.
    def visitStart(self, ctx:homework3Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by homework3Parser#email.
    def visitEmail(self, ctx:homework3Parser.EmailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by homework3Parser#nationalNum.
    def visitNationalNum(self, ctx:homework3Parser.NationalNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by homework3Parser#postalCode.
    def visitPostalCode(self, ctx:homework3Parser.PostalCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by homework3Parser#float.
    def visitFloat(self, ctx:homework3Parser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by homework3Parser#versionOfSFTW.
    def visitVersionOfSFTW(self, ctx:homework3Parser.VersionOfSFTWContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by homework3Parser#url.
    def visitUrl(self, ctx:homework3Parser.UrlContext):
        return self.visitChildren(ctx)



del homework3Parser