grammar Pass;

password: CHAR+;

CHAR: (UPPERCASE | LOWERCASE | DIGIT | SYMBOL | EOF);

DIGIT: [0-9];
UPPERCASE: [A-Z];
LOWERCASE :[a-z];
SYMBOL: [ !@#$%^&*()-=_+{}\]|[;':",.<>?/];

// Skip spaces
WS: [\t\r\n]+ -> skip;