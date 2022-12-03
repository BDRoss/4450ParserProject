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
value : variableDef | ifelse | expression;
WS : [ ] + -> skip; //Apparently \r\n aren't whitespace, because variables aren't working with them in there
ifelse : (('if') '('? expression '):'? block) (('elif') '('? expression '):'? block)* (('else:') block)?;
block : INDENT (value+ ) NEWLINE? DEDENT?;
expression : ((IDENTIFIER | DIGITS*) CONDITIONAL (IDENTIFIER | DIGITS*));
variableDef : IDENTIFIER ASSIGN (IDENTIFIER | OPERATORS | DIGITS) NEWLINE*;
ASSIGN : ('+=' | '-=' | '*=' | '/=' | '=');
OPERATORS : ('+' | '-' | '*' | '/' | '%'| 'AND'| 'OR'| 'NOT'| 'and'| 'or'| 'not');
CONDITIONAL : ('<' | '<='| '>'| '>='| '=='| '!=');
IDENTIFIER : (LETTERS | '_') (LETTERS | '_' | DIGITS)*;
LETTERS : ([a-z]+ | [A-Z]+);
DIGITS : ([0-9]+);
NEWLINE : (('\r'? '\n' '\t'* ' '*) | ('\n' '\t'* ' '*));
