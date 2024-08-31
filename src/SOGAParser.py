# Generated from SOGA.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO
import numpy as np

def serializedATN():
    return [
        4,1,43,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,5,0,66,8,0,10,
        0,12,0,69,9,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,77,8,0,10,0,12,0,80,9,
        0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,99,8,3,1,4,1,4,1,4,1,4,1,5,5,5,106,8,5,10,5,12,5,109,9,
        5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,118,8,7,1,7,3,7,121,8,7,1,8,1,
        8,1,8,5,8,126,8,8,10,8,12,8,129,9,8,1,9,1,9,3,9,133,8,9,1,9,1,9,
        1,9,3,9,138,8,9,3,9,140,8,9,1,10,1,10,1,10,5,10,145,8,10,10,10,12,
        10,148,9,10,1,11,1,11,3,11,152,8,11,1,11,3,11,155,8,11,1,11,1,11,
        3,11,159,8,11,1,12,1,12,3,12,163,8,12,1,12,3,12,166,8,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,4,16,190,8,16,11,16,12,16,
        191,1,17,1,17,1,17,1,17,3,17,198,8,17,1,17,1,17,1,17,1,17,3,17,204,
        8,17,3,17,206,8,17,1,18,1,18,1,18,5,18,211,8,18,10,18,12,18,214,
        9,18,1,19,1,19,3,19,218,8,19,1,19,3,19,221,8,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,238,
        8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,249,8,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,258,8,23,1,24,1,24,1,24,
        1,24,3,24,264,8,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,3,26,273,8,
        26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,3,29,292,8,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,30,1,30,1,30,1,30,5,30,304,8,30,10,30,12,30,307,9,30,1,30,1,
        30,1,30,6,67,107,127,146,212,305,0,31,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,5,
        1,0,10,11,1,0,18,21,1,0,22,23,1,0,39,40,1,0,35,38,319,0,67,1,0,0,
        0,2,81,1,0,0,0,4,86,1,0,0,0,6,98,1,0,0,0,8,100,1,0,0,0,10,107,1,
        0,0,0,12,110,1,0,0,0,14,120,1,0,0,0,16,122,1,0,0,0,18,132,1,0,0,
        0,20,141,1,0,0,0,22,158,1,0,0,0,24,165,1,0,0,0,26,171,1,0,0,0,28,
        175,1,0,0,0,30,181,1,0,0,0,32,189,1,0,0,0,34,205,1,0,0,0,36,207,
        1,0,0,0,38,220,1,0,0,0,40,224,1,0,0,0,42,228,1,0,0,0,44,232,1,0,
        0,0,46,257,1,0,0,0,48,263,1,0,0,0,50,265,1,0,0,0,52,272,1,0,0,0,
        54,274,1,0,0,0,56,282,1,0,0,0,58,288,1,0,0,0,60,299,1,0,0,0,62,63,
        3,2,1,0,63,64,5,1,0,0,64,66,1,0,0,0,65,62,1,0,0,0,66,69,1,0,0,0,
        67,68,1,0,0,0,67,65,1,0,0,0,68,78,1,0,0,0,69,67,1,0,0,0,70,71,3,
        6,3,0,71,72,5,1,0,0,72,77,1,0,0,0,73,74,3,4,2,0,74,75,5,1,0,0,75,
        77,1,0,0,0,76,70,1,0,0,0,76,73,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,
        0,78,79,1,0,0,0,79,1,1,0,0,0,80,78,1,0,0,0,81,82,5,2,0,0,82,83,3,
        52,26,0,83,84,5,3,0,0,84,85,3,60,30,0,85,3,1,0,0,0,86,87,5,4,0,0,
        87,88,5,40,0,0,88,89,5,5,0,0,89,90,5,39,0,0,90,5,1,0,0,0,91,99,3,
        14,7,0,92,99,3,26,13,0,93,99,3,40,20,0,94,99,3,42,21,0,95,99,3,44,
        22,0,96,99,3,8,4,0,97,99,3,12,6,0,98,91,1,0,0,0,98,92,1,0,0,0,98,
        93,1,0,0,0,98,94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,
        0,99,7,1,0,0,0,100,101,5,6,0,0,101,102,3,10,5,0,102,103,5,7,0,0,
        103,9,1,0,0,0,104,106,9,0,0,0,105,104,1,0,0,0,106,109,1,0,0,0,107,
        108,1,0,0,0,107,105,1,0,0,0,108,11,1,0,0,0,109,107,1,0,0,0,110,111,
        5,8,0,0,111,13,1,0,0,0,112,113,3,52,26,0,113,117,5,3,0,0,114,118,
        3,16,8,0,115,118,3,20,10,0,116,118,3,24,12,0,117,114,1,0,0,0,117,
        115,1,0,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,121,5,9,0,0,120,
        112,1,0,0,0,120,119,1,0,0,0,121,15,1,0,0,0,122,127,3,18,9,0,123,
        124,7,0,0,0,124,126,3,18,9,0,125,123,1,0,0,0,126,129,1,0,0,0,127,
        128,1,0,0,0,127,125,1,0,0,0,128,17,1,0,0,0,129,127,1,0,0,0,130,133,
        5,40,0,0,131,133,3,50,25,0,132,130,1,0,0,0,132,131,1,0,0,0,133,139,
        1,0,0,0,134,137,5,12,0,0,135,138,5,40,0,0,136,138,3,50,25,0,137,
        135,1,0,0,0,137,136,1,0,0,0,138,140,1,0,0,0,139,134,1,0,0,0,139,
        140,1,0,0,0,140,19,1,0,0,0,141,146,3,22,11,0,142,143,7,0,0,0,143,
        145,3,22,11,0,144,142,1,0,0,0,145,148,1,0,0,0,146,147,1,0,0,0,146,
        144,1,0,0,0,147,21,1,0,0,0,148,146,1,0,0,0,149,152,5,40,0,0,150,
        152,3,50,25,0,151,149,1,0,0,0,151,150,1,0,0,0,152,153,1,0,0,0,153,
        155,5,12,0,0,154,151,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,
        159,3,48,24,0,157,159,3,18,9,0,158,154,1,0,0,0,158,157,1,0,0,0,159,
        23,1,0,0,0,160,163,5,40,0,0,161,163,3,50,25,0,162,160,1,0,0,0,162,
        161,1,0,0,0,163,164,1,0,0,0,164,166,5,12,0,0,165,162,1,0,0,0,165,
        166,1,0,0,0,166,167,1,0,0,0,167,168,3,48,24,0,168,169,5,12,0,0,169,
        170,3,48,24,0,170,25,1,0,0,0,171,172,3,28,14,0,172,173,3,30,15,0,
        173,174,5,13,0,0,174,27,1,0,0,0,175,176,5,14,0,0,176,177,3,34,17,
        0,177,178,5,15,0,0,178,179,3,32,16,0,179,180,5,16,0,0,180,29,1,0,
        0,0,181,182,5,17,0,0,182,183,5,15,0,0,183,184,3,32,16,0,184,185,
        5,16,0,0,185,31,1,0,0,0,186,187,3,6,3,0,187,188,5,1,0,0,188,190,
        1,0,0,0,189,186,1,0,0,0,190,191,1,0,0,0,191,189,1,0,0,0,191,192,
        1,0,0,0,192,33,1,0,0,0,193,194,3,36,18,0,194,197,7,1,0,0,195,198,
        5,40,0,0,196,198,3,50,25,0,197,195,1,0,0,0,197,196,1,0,0,0,198,206,
        1,0,0,0,199,200,3,52,26,0,200,203,7,2,0,0,201,204,5,40,0,0,202,204,
        3,50,25,0,203,201,1,0,0,0,203,202,1,0,0,0,204,206,1,0,0,0,205,193,
        1,0,0,0,205,199,1,0,0,0,206,35,1,0,0,0,207,212,3,38,19,0,208,209,
        7,0,0,0,209,211,3,38,19,0,210,208,1,0,0,0,211,214,1,0,0,0,212,213,
        1,0,0,0,212,210,1,0,0,0,213,37,1,0,0,0,214,212,1,0,0,0,215,218,5,
        40,0,0,216,218,3,50,25,0,217,215,1,0,0,0,217,216,1,0,0,0,218,219,
        1,0,0,0,219,221,5,12,0,0,220,217,1,0,0,0,220,221,1,0,0,0,221,222,
        1,0,0,0,222,223,3,48,24,0,223,39,1,0,0,0,224,225,5,24,0,0,225,226,
        5,40,0,0,226,227,5,7,0,0,227,41,1,0,0,0,228,229,5,25,0,0,229,230,
        3,34,17,0,230,231,5,7,0,0,231,43,1,0,0,0,232,233,5,26,0,0,233,234,
        5,39,0,0,234,237,5,27,0,0,235,238,5,40,0,0,236,238,3,50,25,0,237,
        235,1,0,0,0,237,236,1,0,0,0,238,239,1,0,0,0,239,240,5,7,0,0,240,
        241,5,15,0,0,241,242,3,32,16,0,242,243,5,16,0,0,243,244,5,28,0,0,
        244,45,1,0,0,0,245,258,3,36,18,0,246,247,5,40,0,0,247,249,5,12,0,
        0,248,246,1,0,0,0,248,249,1,0,0,0,249,250,1,0,0,0,250,251,3,48,24,
        0,251,252,5,12,0,0,252,253,3,48,24,0,253,258,1,0,0,0,254,255,3,48,
        24,0,255,256,5,29,0,0,256,258,1,0,0,0,257,245,1,0,0,0,257,248,1,
        0,0,0,257,254,1,0,0,0,258,47,1,0,0,0,259,264,3,52,26,0,260,264,3,
        54,27,0,261,264,3,56,28,0,262,264,3,58,29,0,263,259,1,0,0,0,263,
        260,1,0,0,0,263,261,1,0,0,0,263,262,1,0,0,0,264,49,1,0,0,0,265,266,
        5,39,0,0,266,267,5,30,0,0,267,268,7,3,0,0,268,269,5,5,0,0,269,51,
        1,0,0,0,270,273,5,39,0,0,271,273,3,50,25,0,272,270,1,0,0,0,272,271,
        1,0,0,0,273,53,1,0,0,0,274,275,5,31,0,0,275,276,3,60,30,0,276,277,
        5,32,0,0,277,278,3,60,30,0,278,279,5,32,0,0,279,280,3,60,30,0,280,
        281,5,7,0,0,281,55,1,0,0,0,282,283,5,33,0,0,283,284,3,60,30,0,284,
        285,5,32,0,0,285,286,5,40,0,0,286,287,5,7,0,0,287,57,1,0,0,0,288,
        291,5,34,0,0,289,292,5,40,0,0,290,292,3,52,26,0,291,289,1,0,0,0,
        291,290,1,0,0,0,292,293,1,0,0,0,293,294,5,32,0,0,294,295,5,40,0,
        0,295,296,5,32,0,0,296,297,7,4,0,0,297,298,5,7,0,0,298,59,1,0,0,
        0,299,300,5,30,0,0,300,305,5,40,0,0,301,302,5,32,0,0,302,304,5,40,
        0,0,303,301,1,0,0,0,304,307,1,0,0,0,305,306,1,0,0,0,305,303,1,0,
        0,0,306,308,1,0,0,0,307,305,1,0,0,0,308,309,5,5,0,0,309,61,1,0,0,
        0,31,67,76,78,98,107,117,120,127,132,137,139,146,151,154,158,162,
        165,191,197,203,205,212,217,220,237,248,257,263,272,291,305
    ]

class SOGAParser ( Parser ):

    grammarFileName = "SOGA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'data'", "'='", "'array['", "']'", 
                     "'compute_firings('", "')'", "'truncate_state'", "'skip'", 
                     "'+'", "'-'", "'*'", "'end if'", "'if'", "'{'", "'}'", 
                     "'else'", "'<'", "'<='", "'>='", "'>'", "'=='", "'!='", 
                     "'prune('", "'observe('", "'for'", "'in range('", "'end for'", 
                     "'^2'", "'['", "'gm('", "','", "'uniform('", "'poisson('", 
                     "'disc'", "'nbin'", "'mom1'", "'mom2'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDV", "NUM", 
                      "COMM", "WS", "DIGIT" ]

    RULE_progr = 0
    RULE_data = 1
    RULE_array = 2
    RULE_instr = 3
    RULE_compute_firings = 4
    RULE_args = 5
    RULE_truncate_state = 6
    RULE_assignment = 7
    RULE_const = 8
    RULE_const_term = 9
    RULE_add = 10
    RULE_add_term = 11
    RULE_mul = 12
    RULE_conditional = 13
    RULE_ifclause = 14
    RULE_elseclause = 15
    RULE_block = 16
    RULE_bexpr = 17
    RULE_lexpr = 18
    RULE_monom = 19
    RULE_prune = 20
    RULE_observe = 21
    RULE_loop = 22
    RULE_expr = 23
    RULE_vars = 24
    RULE_idd = 25
    RULE_symvars = 26
    RULE_gm = 27
    RULE_uniform = 28
    RULE_poisson = 29
    RULE_list = 30

    ruleNames =  [ "progr", "data", "array", "instr", "compute_firings", 
                   "args", "truncate_state", "assignment", "const", "const_term", 
                   "add", "add_term", "mul", "conditional", "ifclause", 
                   "elseclause", "block", "bexpr", "lexpr", "monom", "prune", 
                   "observe", "loop", "expr", "vars", "idd", "symvars", 
                   "gm", "uniform", "poisson", "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    IDV=39
    NUM=40
    COMM=41
    WS=42
    DIGIT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.DataContext)
            else:
                return self.getTypedRuleContext(SOGAParser.DataContext,i)


        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.InstrContext)
            else:
                return self.getTypedRuleContext(SOGAParser.InstrContext,i)


        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.ArrayContext)
            else:
                return self.getTypedRuleContext(SOGAParser.ArrayContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_progr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgr" ):
                listener.enterProgr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgr" ):
                listener.exitProgr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgr" ):
                return visitor.visitProgr(self)
            else:
                return visitor.visitChildren(self)




    def progr(self):

        localctx = SOGAParser.ProgrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_progr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 62
                    self.data()
                    self.state = 63
                    self.match(SOGAParser.T__0) 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__3) | (1 << SOGAParser.T__5) | (1 << SOGAParser.T__7) | (1 << SOGAParser.T__8) | (1 << SOGAParser.T__13) | (1 << SOGAParser.T__23) | (1 << SOGAParser.T__24) | (1 << SOGAParser.T__25) | (1 << SOGAParser.IDV))) != 0):
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.T__5, SOGAParser.T__7, SOGAParser.T__8, SOGAParser.T__13, SOGAParser.T__23, SOGAParser.T__24, SOGAParser.T__25, SOGAParser.IDV]:
                    self.state = 70
                    self.instr()
                    self.state = 71
                    self.match(SOGAParser.T__0)
                    pass
                elif token in [SOGAParser.T__3]:
                    self.state = 73
                    self.array()
                    self.state = 74
                    self.match(SOGAParser.T__0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symvars(self):
            return self.getTypedRuleContext(SOGAParser.SymvarsContext,0)


        def list_(self):
            return self.getTypedRuleContext(SOGAParser.ListContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = SOGAParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SOGAParser.T__1)
            self.state = 82
            self.symvars()
            self.state = 83
            self.match(SOGAParser.T__2)
            self.state = 84
            self.list_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def IDV(self):
            return self.getToken(SOGAParser.IDV, 0)

        def getRuleIndex(self):
            return SOGAParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = SOGAParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SOGAParser.T__3)
            self.state = 87
            self.match(SOGAParser.NUM)
            self.state = 88
            self.match(SOGAParser.T__4)
            self.state = 89
            self.match(SOGAParser.IDV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(SOGAParser.AssignmentContext,0)


        def conditional(self):
            return self.getTypedRuleContext(SOGAParser.ConditionalContext,0)


        def prune(self):
            return self.getTypedRuleContext(SOGAParser.PruneContext,0)


        def observe(self):
            return self.getTypedRuleContext(SOGAParser.ObserveContext,0)


        def loop(self):
            return self.getTypedRuleContext(SOGAParser.LoopContext,0)


        def compute_firings(self):
            return self.getTypedRuleContext(SOGAParser.Compute_firingsContext,0)


        def truncate_state(self):
            return self.getTypedRuleContext(SOGAParser.Truncate_stateContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = SOGAParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instr)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.T__8, SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.assignment()
                pass
            elif token in [SOGAParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.conditional()
                pass
            elif token in [SOGAParser.T__23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.prune()
                pass
            elif token in [SOGAParser.T__24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.observe()
                pass
            elif token in [SOGAParser.T__25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.loop()
                pass
            elif token in [SOGAParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.compute_firings()
                pass
            elif token in [SOGAParser.T__7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.truncate_state()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compute_firingsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(SOGAParser.ArgsContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_compute_firings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompute_firings" ):
                listener.enterCompute_firings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompute_firings" ):
                listener.exitCompute_firings(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompute_firings" ):
                return visitor.visitCompute_firings(self)
            else:
                return visitor.visitChildren(self)




    def compute_firings(self):

        localctx = SOGAParser.Compute_firingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compute_firings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SOGAParser.T__5)
            self.state = 101
            self.args()
            self.state = 102
            self.match(SOGAParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SOGAParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = SOGAParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 104
                    self.matchWildcard() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Truncate_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SOGAParser.RULE_truncate_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruncate_state" ):
                listener.enterTruncate_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruncate_state" ):
                listener.exitTruncate_state(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruncate_state" ):
                return visitor.visitTruncate_state(self)
            else:
                return visitor.visitChildren(self)




    def truncate_state(self):

        localctx = SOGAParser.Truncate_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_truncate_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(SOGAParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symvars(self):
            return self.getTypedRuleContext(SOGAParser.SymvarsContext,0)


        def const(self):
            return self.getTypedRuleContext(SOGAParser.ConstContext,0)


        def add(self):
            return self.getTypedRuleContext(SOGAParser.AddContext,0)


        def mul(self):
            return self.getTypedRuleContext(SOGAParser.MulContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SOGAParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.symvars()
                self.state = 113
                self.match(SOGAParser.T__2)
                self.state = 117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 114
                    self.const()
                    pass

                elif la_ == 2:
                    self.state = 115
                    self.add()
                    pass

                elif la_ == 3:
                    self.state = 116
                    self.mul()
                    pass


                pass
            elif token in [SOGAParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(SOGAParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.Const_termContext)
            else:
                return self.getTypedRuleContext(SOGAParser.Const_termContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = SOGAParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.const_term()
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 123
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__9 or _la==SOGAParser.T__10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 124
                    self.const_term() 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SOGAParser.NUM)
            else:
                return self.getToken(SOGAParser.NUM, i)

        def idd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.IddContext)
            else:
                return self.getTypedRuleContext(SOGAParser.IddContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_const_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_term" ):
                listener.enterConst_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_term" ):
                listener.exitConst_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_term" ):
                return visitor.visitConst_term(self)
            else:
                return visitor.visitChildren(self)




    def const_term(self):

        localctx = SOGAParser.Const_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_const_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 130
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 131
                self.idd()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SOGAParser.T__11:
                self.state = 134
                self.match(SOGAParser.T__11)
                self.state = 137
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 135
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 136
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.Add_termContext)
            else:
                return self.getTypedRuleContext(SOGAParser.Add_termContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = SOGAParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.add_term()
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 142
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__9 or _la==SOGAParser.T__10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 143
                    self.add_term() 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(SOGAParser.VarsContext,0)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def idd(self):
            return self.getTypedRuleContext(SOGAParser.IddContext,0)


        def const_term(self):
            return self.getTypedRuleContext(SOGAParser.Const_termContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_add_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_term" ):
                listener.enterAdd_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_term" ):
                listener.exitAdd_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_term" ):
                return visitor.visitAdd_term(self)
            else:
                return visitor.visitChildren(self)




    def add_term(self):

        localctx = SOGAParser.Add_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_add_term)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 151
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SOGAParser.NUM]:
                        self.state = 149
                        self.match(SOGAParser.NUM)
                        pass
                    elif token in [SOGAParser.IDV]:
                        self.state = 150
                        self.idd()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 153
                    self.match(SOGAParser.T__11)


                self.state = 156
                self.vars_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.const_term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.VarsContext)
            else:
                return self.getTypedRuleContext(SOGAParser.VarsContext,i)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def idd(self):
            return self.getTypedRuleContext(SOGAParser.IddContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)




    def mul(self):

        localctx = SOGAParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 162
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 160
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 161
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 164
                self.match(SOGAParser.T__11)


            self.state = 167
            self.vars_()
            self.state = 168
            self.match(SOGAParser.T__11)
            self.state = 169
            self.vars_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifclause(self):
            return self.getTypedRuleContext(SOGAParser.IfclauseContext,0)


        def elseclause(self):
            return self.getTypedRuleContext(SOGAParser.ElseclauseContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = SOGAParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.ifclause()
            self.state = 172
            self.elseclause()
            self.state = 173
            self.match(SOGAParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bexpr(self):
            return self.getTypedRuleContext(SOGAParser.BexprContext,0)


        def block(self):
            return self.getTypedRuleContext(SOGAParser.BlockContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_ifclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfclause" ):
                listener.enterIfclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfclause" ):
                listener.exitIfclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfclause" ):
                return visitor.visitIfclause(self)
            else:
                return visitor.visitChildren(self)




    def ifclause(self):

        localctx = SOGAParser.IfclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(SOGAParser.T__13)
            self.state = 176
            self.bexpr()
            self.state = 177
            self.match(SOGAParser.T__14)
            self.state = 178
            self.block()
            self.state = 179
            self.match(SOGAParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(SOGAParser.BlockContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_elseclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseclause" ):
                listener.enterElseclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseclause" ):
                listener.exitElseclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseclause" ):
                return visitor.visitElseclause(self)
            else:
                return visitor.visitChildren(self)




    def elseclause(self):

        localctx = SOGAParser.ElseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SOGAParser.T__16)
            self.state = 182
            self.match(SOGAParser.T__14)
            self.state = 183
            self.block()
            self.state = 184
            self.match(SOGAParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.InstrContext)
            else:
                return self.getTypedRuleContext(SOGAParser.InstrContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SOGAParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.instr()
                self.state = 187
                self.match(SOGAParser.T__0)
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__5) | (1 << SOGAParser.T__7) | (1 << SOGAParser.T__8) | (1 << SOGAParser.T__13) | (1 << SOGAParser.T__23) | (1 << SOGAParser.T__24) | (1 << SOGAParser.T__25) | (1 << SOGAParser.IDV))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(SOGAParser.LexprContext,0)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def idd(self):
            return self.getTypedRuleContext(SOGAParser.IddContext,0)


        def symvars(self):
            return self.getTypedRuleContext(SOGAParser.SymvarsContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_bexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBexpr" ):
                listener.enterBexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBexpr" ):
                listener.exitBexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBexpr" ):
                return visitor.visitBexpr(self)
            else:
                return visitor.visitChildren(self)




    def bexpr(self):

        localctx = SOGAParser.BexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_bexpr)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.lexpr()
                self.state = 194
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__17) | (1 << SOGAParser.T__18) | (1 << SOGAParser.T__19) | (1 << SOGAParser.T__20))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 195
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 196
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.symvars()
                self.state = 200
                _la = self._input.LA(1)
                if not(_la==SOGAParser.T__21 or _la==SOGAParser.T__22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 201
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 202
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.MonomContext)
            else:
                return self.getTypedRuleContext(SOGAParser.MonomContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_lexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexpr" ):
                listener.enterLexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexpr" ):
                listener.exitLexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexpr" ):
                return visitor.visitLexpr(self)
            else:
                return visitor.visitChildren(self)




    def lexpr(self):

        localctx = SOGAParser.LexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.monom()
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 208
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__9 or _la==SOGAParser.T__10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.monom() 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(SOGAParser.VarsContext,0)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def idd(self):
            return self.getTypedRuleContext(SOGAParser.IddContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_monom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonom" ):
                listener.enterMonom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonom" ):
                listener.exitMonom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonom" ):
                return visitor.visitMonom(self)
            else:
                return visitor.visitChildren(self)




    def monom(self):

        localctx = SOGAParser.MonomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_monom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 215
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 216
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 219
                self.match(SOGAParser.T__11)


            self.state = 222
            self.vars_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PruneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def getRuleIndex(self):
            return SOGAParser.RULE_prune

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrune" ):
                listener.enterPrune(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrune" ):
                listener.exitPrune(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrune" ):
                return visitor.visitPrune(self)
            else:
                return visitor.visitChildren(self)




    def prune(self):

        localctx = SOGAParser.PruneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_prune)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(SOGAParser.T__23)
            self.state = 225
            self.match(SOGAParser.NUM)
            self.state = 226
            self.match(SOGAParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObserveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bexpr(self):
            return self.getTypedRuleContext(SOGAParser.BexprContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_observe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObserve" ):
                listener.enterObserve(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObserve" ):
                listener.exitObserve(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObserve" ):
                return visitor.visitObserve(self)
            else:
                return visitor.visitChildren(self)




    def observe(self):

        localctx = SOGAParser.ObserveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_observe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(SOGAParser.T__24)
            self.state = 229
            self.bexpr()
            self.state = 230
            self.match(SOGAParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDV(self):
            return self.getToken(SOGAParser.IDV, 0)

        def block(self):
            return self.getTypedRuleContext(SOGAParser.BlockContext,0)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def idd(self):
            return self.getTypedRuleContext(SOGAParser.IddContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = SOGAParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(SOGAParser.T__25)
            self.state = 233
            self.match(SOGAParser.IDV)
            self.state = 234
            self.match(SOGAParser.T__26)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 235
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 236
                self.idd()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 239
            self.match(SOGAParser.T__6)
            self.state = 240
            self.match(SOGAParser.T__14)
            self.state = 241
            self.block()
            self.state = 242
            self.match(SOGAParser.T__15)
            self.state = 243
            self.match(SOGAParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(SOGAParser.LexprContext,0)


        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.VarsContext)
            else:
                return self.getTypedRuleContext(SOGAParser.VarsContext,i)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def getRuleIndex(self):
            return SOGAParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SOGAParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.lexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SOGAParser.NUM:
                    self.state = 246
                    self.match(SOGAParser.NUM)
                    self.state = 247
                    self.match(SOGAParser.T__11)


                self.state = 250
                self.vars_()
                self.state = 251
                self.match(SOGAParser.T__11)
                self.state = 252
                self.vars_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.vars_()
                self.state = 255
                self.match(SOGAParser.T__28)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symvars(self):
            return self.getTypedRuleContext(SOGAParser.SymvarsContext,0)


        def gm(self):
            return self.getTypedRuleContext(SOGAParser.GmContext,0)


        def uniform(self):
            return self.getTypedRuleContext(SOGAParser.UniformContext,0)


        def poisson(self):
            return self.getTypedRuleContext(SOGAParser.PoissonContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = SOGAParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_vars)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.symvars()
                pass
            elif token in [SOGAParser.T__30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.gm()
                pass
            elif token in [SOGAParser.T__32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.uniform()
                pass
            elif token in [SOGAParser.T__33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.poisson()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDV(self, i:int=None):
            if i is None:
                return self.getTokens(SOGAParser.IDV)
            else:
                return self.getToken(SOGAParser.IDV, i)

        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def getRuleIndex(self):
            return SOGAParser.RULE_idd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdd" ):
                listener.enterIdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdd" ):
                listener.exitIdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdd" ):
                return visitor.visitIdd(self)
            else:
                return visitor.visitChildren(self)




    def idd(self):

        localctx = SOGAParser.IddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_idd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(SOGAParser.IDV)
            self.state = 266
            self.match(SOGAParser.T__29)
            self.state = 267
            _la = self._input.LA(1)
            if not(_la==SOGAParser.IDV or _la==SOGAParser.NUM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 268
            self.match(SOGAParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDV(self):
            return self.getToken(SOGAParser.IDV, 0)

        def idd(self):
            return self.getTypedRuleContext(SOGAParser.IddContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_symvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymvars" ):
                listener.enterSymvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymvars" ):
                listener.exitSymvars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymvars" ):
                return visitor.visitSymvars(self)
            else:
                return visitor.visitChildren(self)




    def symvars(self):

        localctx = SOGAParser.SymvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_symvars)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(SOGAParser.IDV)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.idd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.ListContext)
            else:
                return self.getTypedRuleContext(SOGAParser.ListContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_gm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGm" ):
                listener.enterGm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGm" ):
                listener.exitGm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGm" ):
                return visitor.visitGm(self)
            else:
                return visitor.visitChildren(self)




    def gm(self):

        localctx = SOGAParser.GmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_gm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(SOGAParser.T__30)
            self.state = 275
            self.list_()
            self.state = 276
            self.match(SOGAParser.T__31)
            self.state = 277
            self.list_()
            self.state = 278
            self.match(SOGAParser.T__31)
            self.state = 279
            self.list_()
            self.state = 280
            self.match(SOGAParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UniformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(SOGAParser.ListContext,0)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def getRuleIndex(self):
            return SOGAParser.RULE_uniform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniform" ):
                listener.enterUniform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniform" ):
                listener.exitUniform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniform" ):
                return visitor.visitUniform(self)
            else:
                return visitor.visitChildren(self)

        def getText(self):
            """ converts string "uniform([a,b], K)" in "gm(pi, mu, sigma)" where gm is a Gaussian Mix with K component approximating the uniform"""
            a = float(self.list_().NUM()[0].getText())
            b = float(self.list_().NUM()[1].getText())
            N = int(self.NUM().getText())
            pi = [round(1.0/N,4)]*N
            mu = [round(a+i*(b-a)/N+((b-a)/(2*N)),4) for i in range(N)]
            sigma = list([round((b-a)/(np.sqrt(12)*N),4)]*N)
            return 'gm('+str(pi)+','+str(mu)+','+str(sigma)+')'


    def uniform(self):

        localctx = SOGAParser.UniformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_uniform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(SOGAParser.T__32)
            self.state = 283
            self.list_()
            self.state = 284
            self.match(SOGAParser.T__31)
            self.state = 285
            self.match(SOGAParser.NUM)
            self.state = 286
            self.match(SOGAParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PoissonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SOGAParser.NUM)
            else:
                return self.getToken(SOGAParser.NUM, i)

        def symvars(self):
            return self.getTypedRuleContext(SOGAParser.SymvarsContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_poisson

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoisson" ):
                listener.enterPoisson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoisson" ):
                listener.exitPoisson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoisson" ):
                return visitor.visitPoisson(self)
            else:
                return visitor.visitChildren(self)




    def poisson(self):

        localctx = SOGAParser.PoissonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_poisson)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(SOGAParser.T__33)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 289
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 290
                self.symvars()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 293
            self.match(SOGAParser.T__31)
            self.state = 294
            self.match(SOGAParser.NUM)
            self.state = 295
            self.match(SOGAParser.T__31)
            self.state = 296
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__34) | (1 << SOGAParser.T__35) | (1 << SOGAParser.T__36) | (1 << SOGAParser.T__37))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 297
            self.match(SOGAParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SOGAParser.NUM)
            else:
                return self.getToken(SOGAParser.NUM, i)

        def getRuleIndex(self):
            return SOGAParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = SOGAParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(SOGAParser.T__29)
            self.state = 300
            self.match(SOGAParser.NUM)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 301
                    self.match(SOGAParser.T__31)
                    self.state = 302
                    self.match(SOGAParser.NUM) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 308
            self.match(SOGAParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





