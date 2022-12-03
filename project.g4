grammar project;

// Setup code fore open-source library antlr-denter that helps
// handle indent/dedenting
tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from projectParser import projectParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: projectLexer = lexer

    def pull_token(self):
        return super(projectLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, projectParser.INDENT, projectParser.DEDENT, 1)
    return self.denter.next_token()

}




start : (value)* EOF;
// Basic building block of code
value : variableDef | ifelse | expression;
WS : [ ] + -> skip; //Apparently \r\n aren't whitespace, because variables aren't working with them in there
// Allow for an arbitrary amount of elifs and a single else
ifelse : (('if') '('? expression '):'? block) (('elif') '('? expression '):'? block)* (('else:') block)?;
// define blocks of code, which can include nested values (and more blocks). Thanks, antlr-denter
block : INDENT (value+ ) NEWLINE? DEDENT?;
// handle expressions with variable identifiers
expression : ((IDENTIFIER | DIGITS*) CONDITIONAL (IDENTIFIER | DIGITS*));
// define variables with an identifier, a type of assignation, and arithmetic or value (or another variable)
// should probably take another look to make sure you can do var + var, or digit + var or vice/versa, I don't think it's right as of now
variableDef : IDENTIFIER ASSIGN (IDENTIFIER | OPERATORS | DIGITS) NEWLINE*;
// Just lists of possible defined symbols
ASSIGN : ('+=' | '-=' | '*=' | '/=' | '=');
OPERATORS : ('+' | '-' | '*' | '/' | '%');
CONDITIONAL : ('<' | '<='| '>'| '>='| '=='| '!=' | 'AND' | 'OR' | 'NOT' | 'and' | 'or' | 'not');
// Rule for variable names/identifiers, cannot start with a number
IDENTIFIER : (LETTERS | '_') (LETTERS | '_' | DIGITS)*;
// Easier than typing it out, plus ANTLR got mad when [a-z] was directly in a rule
LETTERS : ([a-z]+ | [A-Z]+);
// same
DIGITS : ([0-9]+);
NEWLINE : (('\r'? '\n' '\t'* ' '*) | ('\n' '\t'* ' '*));
