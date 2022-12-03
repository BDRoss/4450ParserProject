grammar project;
start : (value)* EOF;
value : variableDef;
WS : [ \t] + -> skip; //Apparently \r\n aren't whitespace, because variables aren't working with them in there
variableDef : IDENTIFIER ASSIGN (IDENTIFIER | OPERATORS | DIGITS)(NEWLINE | EOF);
ASSIGN : ('+=' | '-=' | '*=' | '/=' | '=');
OPERATORS : ('+' | '-' | '*' | '/' | '%');
IDENTIFIER : (LETTERS | '_') (LETTERS | '_' | DIGITS)*;
LETTERS : ([a-z]+ | [A-Z]+);
DIGITS : ([0-9]+);
NEWLINE : ('\r'? '\n' ' '*);
