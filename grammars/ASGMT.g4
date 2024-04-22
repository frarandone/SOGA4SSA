grammar ASGMT; 

assignment: symvars '=' add;

add: add_term (('+')? add_term)*?;
add_term: (term '*')? term;

term: NUM | sub? symvars | sub? gm | sub? poisson;
symvars : IDV | idd;
idd : IDV '[' (NUM | IDV) ']';
gm: 'gm(' list ',' list ',' list ')';
poisson: 'poisson('  prate ',' psupp ',' ppar ')';
prate: NUM | symvars;                                                                                                            
psupp: NUM;
ppar: 'disc'|'nbin'|'mom1'|'mom2';
list: '[' NUM (',' NUM)*? ']';

sub: '-';

IDV : ALPHA (ALPHA|DIGIT)*;
NUM : ('-')? DIGIT+ ('.' DIGIT*)?;

COMM : '/*' .*? '*/' -> skip;
WS : (' '|'\t'|'\r'|'\n') -> skip;

fragment 
ALPHA : [a-zA-Z];
DIGIT : [0-9];