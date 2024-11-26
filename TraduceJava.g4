grammar TraduceJava;

DEF       : 'def';
RETURN    : 'return';
PRINT     : 'print';
ID        : [a-zA-Z]+;
NUMBER    : [0-9]+;
PLUS      : '+';
ASSIGN    : '=';
MUL       : '*';
SUB       : '-';
LPAREN    : '(';
RPAREN    : ')';
COLON     : ':';
COMMA     : ',';

WS        : [ \t\r\n]+ -> skip;

// Entry points
programa: (function | print_statement | function_call)+ ;

// Function definition
function: DEF ID LPAREN parameters RPAREN COLON statements;

// Parameters
parameters: ID (COMMA ID)*;

// Statements
statements: statement*;

// Statement types
statement: assignment | return_statement | print_statement;

// Assignment statement
assignment: ID ASSIGN expression;

// Return statement
return_statement: RETURN expression;

// Print statement
print_statement: PRINT LPAREN expression RPAREN;

// Function call
function_call: ID LPAREN arguments RPAREN;

// Arguments for function calls
arguments: expression (COMMA expression)*;

// Expressions
expression: term (SUB term)*;
term: factor (MUL factor)*;
factor: ID | NUMBER | LPAREN expression RPAREN | function_call;  // Permite llamadas a función en expresiones
