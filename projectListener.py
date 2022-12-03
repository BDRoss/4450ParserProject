# Generated from project.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .projectParser import projectParser
else:
    from projectParser import projectParser

# This class defines a complete listener for a parse tree produced by projectParser.
class projectListener(ParseTreeListener):

    # Enter a parse tree produced by projectParser#start.
    def enterStart(self, ctx:projectParser.StartContext):
        pass

    # Exit a parse tree produced by projectParser#start.
    def exitStart(self, ctx:projectParser.StartContext):
        pass


    # Enter a parse tree produced by projectParser#value.
    def enterValue(self, ctx:projectParser.ValueContext):
        pass

    # Exit a parse tree produced by projectParser#value.
    def exitValue(self, ctx:projectParser.ValueContext):
        pass


    # Enter a parse tree produced by projectParser#variableDef.
    def enterVariableDef(self, ctx:projectParser.VariableDefContext):
        pass

    # Exit a parse tree produced by projectParser#variableDef.
    def exitVariableDef(self, ctx:projectParser.VariableDefContext):
        pass


    # Enter a parse tree produced by projectParser#identifier.
    def enterIdentifier(self, ctx:projectParser.IdentifierContext):
        pass

    # Exit a parse tree produced by projectParser#identifier.
    def exitIdentifier(self, ctx:projectParser.IdentifierContext):
        pass



del projectParser