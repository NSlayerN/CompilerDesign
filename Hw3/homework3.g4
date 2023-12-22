grammar homework3;

start : (email | nationalNum | postalCode | float | versionOfSFTW | url)+ EOF;

EMAIL : USER ('.' USER)* '@' DOMAIN('.'DOMAIN)+;  //email structure
fragment USER   : [a-zA-Z0-9]+; //in user we can only use letter and numbers and '.'
fragment DOMAIN : [a-zA-Z0-9-]+; // '-' example=>  mail@master-info.com

/////////////////////////////////////////////////////////////////////////

NATIONALNUMBER : DIGIT+; //National number created by intiger numbers!

////////////////////////////////////////////////////////////////////////

POSTALCODE : DIGIT DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT DIGIT DIGIT DIGIT;
//this is structure of postal code in our country IRAN

///////////////////////////////////////////////////////////////////////

FLOAT : DIGIT* '.' DIGIT+;

///////////////////////////////////////////////////////////////////////

VERSION : DIGIT+ '.' DIGIT+ '.' DIGIT+;

//////////////////////////////////////////////////////////////////////

URLADDRESS : SCHEME '://' HOST '.' HOST (':' PORT)? ;
fragment SCHEME : [a-zA-Z0-9]+; //like https or http or anything else
fragment HOST   : [a-zA-Z0-9]+;
fragment PORT   : [0-9]+;


//Lexical Rules
email         : EMAIL;
nationalNum   : NATIONALNUMBER;
postalCode    : POSTALCODE;
float         : FLOAT;
versionOfSFTW : VERSION;
url           : URLADDRESS;
DIGIT : [0-9] ;
WS :[ \t\r\n]+ -> skip ;
