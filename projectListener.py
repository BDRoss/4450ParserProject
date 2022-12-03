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


    # Enter a parse tree produced by projectParser#ifelse.
    def enterIfelse(self, ctx:projectParser.IfelseContext):
        pass

    # Exit a parse tree produced by projectParser#ifelse.
    def exitIfelse(self, ctx:projectParser.IfelseContext):
        pass


    # Enter a parse tree produced by projectParser#whileLoop.
    def enterWhileLoop(self, ctx:projectParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by projectParser#whileLoop.
    def exitWhileLoop(self, ctx:projectParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by projectParser#forLoop.
    def enterForLoop(self, ctx:projectParser.ForLoopContext):
        pass

    # Exit a parse tree produced by projectParser#forLoop.
    def exitForLoop(self, ctx:projectParser.ForLoopContext):
        pass


    # Enter a parse tree produced by projectParser#block.
    def enterBlock(self, ctx:projectParser.BlockContext):
        pass

    # Exit a parse tree produced by projectParser#block.
    def exitBlock(self, ctx:projectParser.BlockContext):
        pass


    # Enter a parse tree produced by projectParser#expression.
    def enterExpression(self, ctx:projectParser.ExpressionContext):
        pass

    # Exit a parse tree produced by projectParser#expression.
    def exitExpression(self, ctx:projectParser.ExpressionContext):
        pass


    # Enter a parse tree produced by projectParser#variableDef.
    def enterVariableDef(self, ctx:projectParser.VariableDefContext):
        pass

    # Exit a parse tree produced by projectParser#variableDef.
    def exitVariableDef(self, ctx:projectParser.VariableDefContext):
        pass



del projectParser