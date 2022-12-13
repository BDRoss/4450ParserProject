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
value : 'pass' | variableDef | ifelse | expression | whileLoop | forLoop | functionDeclare | functionCall | NEWLINE;
WS : [ ] + -> skip; //Apparently \r\n aren't whitespace, because variables aren't working with them in there
// Allow for an arbitrary amount of elifs and a single else
//ifelse : ((('if') '('? expression '):'? block) ('elif' '('? expression '):'? block)* (('else:') block)?);
ifelse : (('if') '('? expression '):'? block ('elif' '('? expression '):'? block)* (('else:') block)?);
// WHILE
whileLoop : ('while(' (expression | DIGITS*) '):'? block);
// for loops of the form for (var in (expression?))
forLoop : ('for' IDENTIFIER 'in' (IDENTIFIER | 'range(' (DIGITS* | IDENTIFIER) ')') ':' block) ;
// function declare should probably be def identifier(args) block - need to define args, I think
functionDeclare : 'def' IDENTIFIER '(' args '):'? block;
// calls easier, identifier(args), should allow assignment to have functionCall on right side
functionCall : IDENTIFIER '(' args ')' NEWLINE*;
// args for functions, can just be an undetermined number of IDENTIFIERS
args : (IDENTIFIER (','IDENTIFIER)*)*;
// define blocks of code, which can include nested values (and more blocks). Thanks, antlr-denter
block : INDENT (value)* DEDENT?;
// handle expressions with variable identifiers - want this to be able to handle all expressions, in the general sense
expression : (((IDENTIFIER | DIGITS*) | ARITHMETIC) CONDITIONAL ((IDENTIFIER | DIGITS*) | ARITHMETIC)) NEWLINE*;
// define variables with an identifier, a type of assignation, and arithmetic or value (or another variable)
// should probably take another look to make sure you can do var + var, or digit + var or vice/versa, I don't think it's right as of now
variableDef : IDENTIFIER ASSIGN (IDENTIFIER | OPERATORS | DIGITS | functionCall) NEWLINE*;
// Adding arithmetic support
ARITHMETIC : ((IDENTIFIER | (DIGITS)*) OPERATORS (IDENTIFIER | (DIGITS)*)) NEWLINE*;
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
// Implement comments - . is any token, followed by a newline to end comment
// . operator was too greedy (couldn't exclude any character) so now the rule just looks for anything that isn't \n
COMMENT : '#' (~('\n'))* NEWLINE -> skip;
NEWLINE : (('\r'? '\n' ' '* '\t'*) | ('\n' ' '* '\t'*));

