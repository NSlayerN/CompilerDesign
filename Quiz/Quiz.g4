grammar Quiz;

start Id '=' expr EOF;
// we have to write from lowest precedence to most precedence
expr : expr '+' term | expr '-' term | term; // minus and plus have same precedence

term : term '*' fact | term '/' fact | fact; // * and / have same precedence

fact : exponent '^' fact | exponent; // we have to consider assocativity of ^

exponent : '('expr')' | Number | Id ;

//Lexical rule

PLUS:  '+';
MINUS: '-';
MULT:  '*';
DIVIDE:'/';
EXPO:  '^';
ASSIGN:'=';

Id: IDENTIFIER;
Number: NUMBER;

fragment IDENTIFIER: [a-zA-Z][a-zA-Z]*;
fragment NUMBER: [0-9]+;

WS: [\t\r]+ -> channel(HIDDEN);
NEWLINE: '\n' -> skip;
