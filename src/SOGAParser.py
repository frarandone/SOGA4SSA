# Generated from SOGA.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import numpy as np
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,306,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,
        9,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,75,8,0,10,0,12,0,78,9,0,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,96,8,
        3,1,4,1,4,1,4,1,4,1,5,5,5,103,8,5,10,5,12,5,106,9,5,1,6,1,6,1,6,
        1,6,1,6,3,6,113,8,6,1,6,3,6,116,8,6,1,7,1,7,1,7,5,7,121,8,7,10,7,
        12,7,124,9,7,1,8,1,8,3,8,128,8,8,1,8,1,8,1,8,3,8,133,8,8,3,8,135,
        8,8,1,9,1,9,1,9,5,9,140,8,9,10,9,12,9,143,9,9,1,10,1,10,3,10,147,
        8,10,1,10,3,10,150,8,10,1,10,1,10,3,10,154,8,10,1,11,1,11,3,11,158,
        8,11,1,11,3,11,161,8,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,4,15,185,8,15,11,15,12,15,186,1,16,1,16,1,16,1,16,3,16,193,
        8,16,1,16,1,16,1,16,1,16,3,16,199,8,16,3,16,201,8,16,1,17,1,17,1,
        17,5,17,206,8,17,10,17,12,17,209,9,17,1,18,1,18,3,18,213,8,18,1,
        18,3,18,216,8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,
        20,1,21,1,21,1,21,1,21,1,21,3,21,233,8,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,3,22,244,8,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,3,22,253,8,22,1,23,1,23,1,23,1,23,3,23,259,8,23,1,24,1,24,
        1,24,1,24,1,24,1,25,1,25,3,25,268,8,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,3,28,
        287,8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,5,29,
        299,8,29,10,29,12,29,302,9,29,1,29,1,29,1,29,6,65,104,122,141,207,
        300,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,0,5,1,0,9,10,1,0,17,20,1,0,21,22,1,
        0,38,39,1,0,34,37,314,0,65,1,0,0,0,2,79,1,0,0,0,4,84,1,0,0,0,6,95,
        1,0,0,0,8,97,1,0,0,0,10,104,1,0,0,0,12,115,1,0,0,0,14,117,1,0,0,
        0,16,127,1,0,0,0,18,136,1,0,0,0,20,153,1,0,0,0,22,160,1,0,0,0,24,
        166,1,0,0,0,26,170,1,0,0,0,28,176,1,0,0,0,30,184,1,0,0,0,32,200,
        1,0,0,0,34,202,1,0,0,0,36,215,1,0,0,0,38,219,1,0,0,0,40,223,1,0,
        0,0,42,227,1,0,0,0,44,252,1,0,0,0,46,258,1,0,0,0,48,260,1,0,0,0,
        50,267,1,0,0,0,52,269,1,0,0,0,54,277,1,0,0,0,56,283,1,0,0,0,58,294,
        1,0,0,0,60,61,3,2,1,0,61,62,5,1,0,0,62,64,1,0,0,0,63,60,1,0,0,0,
        64,67,1,0,0,0,65,66,1,0,0,0,65,63,1,0,0,0,66,76,1,0,0,0,67,65,1,
        0,0,0,68,69,3,6,3,0,69,70,5,1,0,0,70,75,1,0,0,0,71,72,3,4,2,0,72,
        73,5,1,0,0,73,75,1,0,0,0,74,68,1,0,0,0,74,71,1,0,0,0,75,78,1,0,0,
        0,76,74,1,0,0,0,76,77,1,0,0,0,77,1,1,0,0,0,78,76,1,0,0,0,79,80,5,
        2,0,0,80,81,3,50,25,0,81,82,5,3,0,0,82,83,3,58,29,0,83,3,1,0,0,0,
        84,85,5,4,0,0,85,86,5,39,0,0,86,87,5,5,0,0,87,88,5,38,0,0,88,5,1,
        0,0,0,89,96,3,12,6,0,90,96,3,24,12,0,91,96,3,38,19,0,92,96,3,40,
        20,0,93,96,3,42,21,0,94,96,3,8,4,0,95,89,1,0,0,0,95,90,1,0,0,0,95,
        91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,7,1,0,0,
        0,97,98,5,6,0,0,98,99,3,10,5,0,99,100,5,7,0,0,100,9,1,0,0,0,101,
        103,9,0,0,0,102,101,1,0,0,0,103,106,1,0,0,0,104,105,1,0,0,0,104,
        102,1,0,0,0,105,11,1,0,0,0,106,104,1,0,0,0,107,108,3,50,25,0,108,
        112,5,3,0,0,109,113,3,14,7,0,110,113,3,18,9,0,111,113,3,22,11,0,
        112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,116,1,0,0,0,
        114,116,5,8,0,0,115,107,1,0,0,0,115,114,1,0,0,0,116,13,1,0,0,0,117,
        122,3,16,8,0,118,119,7,0,0,0,119,121,3,16,8,0,120,118,1,0,0,0,121,
        124,1,0,0,0,122,123,1,0,0,0,122,120,1,0,0,0,123,15,1,0,0,0,124,122,
        1,0,0,0,125,128,5,39,0,0,126,128,3,48,24,0,127,125,1,0,0,0,127,126,
        1,0,0,0,128,134,1,0,0,0,129,132,5,11,0,0,130,133,5,39,0,0,131,133,
        3,48,24,0,132,130,1,0,0,0,132,131,1,0,0,0,133,135,1,0,0,0,134,129,
        1,0,0,0,134,135,1,0,0,0,135,17,1,0,0,0,136,141,3,20,10,0,137,138,
        7,0,0,0,138,140,3,20,10,0,139,137,1,0,0,0,140,143,1,0,0,0,141,142,
        1,0,0,0,141,139,1,0,0,0,142,19,1,0,0,0,143,141,1,0,0,0,144,147,5,
        39,0,0,145,147,3,48,24,0,146,144,1,0,0,0,146,145,1,0,0,0,147,148,
        1,0,0,0,148,150,5,11,0,0,149,146,1,0,0,0,149,150,1,0,0,0,150,151,
        1,0,0,0,151,154,3,46,23,0,152,154,3,16,8,0,153,149,1,0,0,0,153,152,
        1,0,0,0,154,21,1,0,0,0,155,158,5,39,0,0,156,158,3,48,24,0,157,155,
        1,0,0,0,157,156,1,0,0,0,158,159,1,0,0,0,159,161,5,11,0,0,160,157,
        1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,163,3,46,23,0,163,164,
        5,11,0,0,164,165,3,46,23,0,165,23,1,0,0,0,166,167,3,26,13,0,167,
        168,3,28,14,0,168,169,5,12,0,0,169,25,1,0,0,0,170,171,5,13,0,0,171,
        172,3,32,16,0,172,173,5,14,0,0,173,174,3,30,15,0,174,175,5,15,0,
        0,175,27,1,0,0,0,176,177,5,16,0,0,177,178,5,14,0,0,178,179,3,30,
        15,0,179,180,5,15,0,0,180,29,1,0,0,0,181,182,3,6,3,0,182,183,5,1,
        0,0,183,185,1,0,0,0,184,181,1,0,0,0,185,186,1,0,0,0,186,184,1,0,
        0,0,186,187,1,0,0,0,187,31,1,0,0,0,188,189,3,34,17,0,189,192,7,1,
        0,0,190,193,5,39,0,0,191,193,3,48,24,0,192,190,1,0,0,0,192,191,1,
        0,0,0,193,201,1,0,0,0,194,195,3,50,25,0,195,198,7,2,0,0,196,199,
        5,39,0,0,197,199,3,48,24,0,198,196,1,0,0,0,198,197,1,0,0,0,199,201,
        1,0,0,0,200,188,1,0,0,0,200,194,1,0,0,0,201,33,1,0,0,0,202,207,3,
        36,18,0,203,204,7,0,0,0,204,206,3,36,18,0,205,203,1,0,0,0,206,209,
        1,0,0,0,207,208,1,0,0,0,207,205,1,0,0,0,208,35,1,0,0,0,209,207,1,
        0,0,0,210,213,5,39,0,0,211,213,3,48,24,0,212,210,1,0,0,0,212,211,
        1,0,0,0,213,214,1,0,0,0,214,216,5,11,0,0,215,212,1,0,0,0,215,216,
        1,0,0,0,216,217,1,0,0,0,217,218,3,46,23,0,218,37,1,0,0,0,219,220,
        5,23,0,0,220,221,5,39,0,0,221,222,5,7,0,0,222,39,1,0,0,0,223,224,
        5,24,0,0,224,225,3,32,16,0,225,226,5,7,0,0,226,41,1,0,0,0,227,228,
        5,25,0,0,228,229,5,38,0,0,229,232,5,26,0,0,230,233,5,39,0,0,231,
        233,3,48,24,0,232,230,1,0,0,0,232,231,1,0,0,0,233,234,1,0,0,0,234,
        235,5,7,0,0,235,236,5,14,0,0,236,237,3,30,15,0,237,238,5,15,0,0,
        238,239,5,27,0,0,239,43,1,0,0,0,240,253,3,34,17,0,241,242,5,39,0,
        0,242,244,5,11,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,
        0,245,246,3,46,23,0,246,247,5,11,0,0,247,248,3,46,23,0,248,253,1,
        0,0,0,249,250,3,46,23,0,250,251,5,28,0,0,251,253,1,0,0,0,252,240,
        1,0,0,0,252,243,1,0,0,0,252,249,1,0,0,0,253,45,1,0,0,0,254,259,3,
        50,25,0,255,259,3,52,26,0,256,259,3,54,27,0,257,259,3,56,28,0,258,
        254,1,0,0,0,258,255,1,0,0,0,258,256,1,0,0,0,258,257,1,0,0,0,259,
        47,1,0,0,0,260,261,5,38,0,0,261,262,5,29,0,0,262,263,7,3,0,0,263,
        264,5,5,0,0,264,49,1,0,0,0,265,268,5,38,0,0,266,268,3,48,24,0,267,
        265,1,0,0,0,267,266,1,0,0,0,268,51,1,0,0,0,269,270,5,30,0,0,270,
        271,3,58,29,0,271,272,5,31,0,0,272,273,3,58,29,0,273,274,5,31,0,
        0,274,275,3,58,29,0,275,276,5,7,0,0,276,53,1,0,0,0,277,278,5,32,
        0,0,278,279,3,58,29,0,279,280,5,31,0,0,280,281,5,39,0,0,281,282,
        5,7,0,0,282,55,1,0,0,0,283,286,5,33,0,0,284,287,5,39,0,0,285,287,
        3,50,25,0,286,284,1,0,0,0,286,285,1,0,0,0,287,288,1,0,0,0,288,289,
        5,31,0,0,289,290,5,39,0,0,290,291,5,31,0,0,291,292,7,4,0,0,292,293,
        5,7,0,0,293,57,1,0,0,0,294,295,5,29,0,0,295,300,5,39,0,0,296,297,
        5,31,0,0,297,299,5,39,0,0,298,296,1,0,0,0,299,302,1,0,0,0,300,301,
        1,0,0,0,300,298,1,0,0,0,301,303,1,0,0,0,302,300,1,0,0,0,303,304,
        5,5,0,0,304,59,1,0,0,0,31,65,74,76,95,104,112,115,122,127,132,134,
        141,146,149,153,157,160,186,192,198,200,207,212,215,232,243,252,
        258,267,286,300
    ]

class SOGAParser ( Parser ):

    grammarFileName = "SOGA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'data'", "'='", "'array['", "']'", 
                     "'compute_firings('", "')'", "'skip'", "'+'", "'-'", 
                     "'*'", "'end if'", "'if'", "'{'", "'}'", "'else'", 
                     "'<'", "'<='", "'>='", "'>'", "'=='", "'!='", "'prune('", 
                     "'observe('", "'for'", "'in range('", "'end for'", 
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
                      "<INVALID>", "<INVALID>", "IDV", "NUM", "COMM", "WS", 
                      "DIGIT" ]

    RULE_progr = 0
    RULE_data = 1
    RULE_array = 2
    RULE_instr = 3
    RULE_compute_firings = 4
    RULE_args = 5
    RULE_assignment = 6
    RULE_const = 7
    RULE_const_term = 8
    RULE_add = 9
    RULE_add_term = 10
    RULE_mul = 11
    RULE_conditional = 12
    RULE_ifclause = 13
    RULE_elseclause = 14
    RULE_block = 15
    RULE_bexpr = 16
    RULE_lexpr = 17
    RULE_monom = 18
    RULE_prune = 19
    RULE_observe = 20
    RULE_loop = 21
    RULE_expr = 22
    RULE_vars = 23
    RULE_idd = 24
    RULE_symvars = 25
    RULE_gm = 26
    RULE_uniform = 27
    RULE_poisson = 28
    RULE_list = 29

    ruleNames =  [ "progr", "data", "array", "instr", "compute_firings", 
                   "args", "assignment", "const", "const_term", "add", "add_term", 
                   "mul", "conditional", "ifclause", "elseclause", "block", 
                   "bexpr", "lexpr", "monom", "prune", "observe", "loop", 
                   "expr", "vars", "idd", "symvars", "gm", "uniform", "poisson", 
                   "list" ]

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
    IDV=38
    NUM=39
    COMM=40
    WS=41
    DIGIT=42

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
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 60
                    self.data()
                    self.state = 61
                    self.match(SOGAParser.T__0) 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__3) | (1 << SOGAParser.T__5) | (1 << SOGAParser.T__7) | (1 << SOGAParser.T__12) | (1 << SOGAParser.T__22) | (1 << SOGAParser.T__23) | (1 << SOGAParser.T__24) | (1 << SOGAParser.IDV))) != 0):
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.T__5, SOGAParser.T__7, SOGAParser.T__12, SOGAParser.T__22, SOGAParser.T__23, SOGAParser.T__24, SOGAParser.IDV]:
                    self.state = 68
                    self.instr()
                    self.state = 69
                    self.match(SOGAParser.T__0)
                    pass
                elif token in [SOGAParser.T__3]:
                    self.state = 71
                    self.array()
                    self.state = 72
                    self.match(SOGAParser.T__0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 78
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
            self.state = 79
            self.match(SOGAParser.T__1)
            self.state = 80
            self.symvars()
            self.state = 81
            self.match(SOGAParser.T__2)
            self.state = 82
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
            self.state = 84
            self.match(SOGAParser.T__3)
            self.state = 85
            self.match(SOGAParser.NUM)
            self.state = 86
            self.match(SOGAParser.T__4)
            self.state = 87
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
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.T__7, SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.assignment()
                pass
            elif token in [SOGAParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.conditional()
                pass
            elif token in [SOGAParser.T__22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.prune()
                pass
            elif token in [SOGAParser.T__23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.observe()
                pass
            elif token in [SOGAParser.T__24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.loop()
                pass
            elif token in [SOGAParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.compute_firings()
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
            self.state = 97
            self.match(SOGAParser.T__5)
            self.state = 98
            self.args()
            self.state = 99
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
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 101
                    self.matchWildcard() 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.symvars()
                self.state = 108
                self.match(SOGAParser.T__2)
                self.state = 112
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 109
                    self.const()
                    pass

                elif la_ == 2:
                    self.state = 110
                    self.add()
                    pass

                elif la_ == 3:
                    self.state = 111
                    self.mul()
                    pass


                pass
            elif token in [SOGAParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(SOGAParser.T__7)
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
        self.enterRule(localctx, 14, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.const_term()
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 118
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__8 or _la==SOGAParser.T__9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 119
                    self.const_term() 
                self.state = 124
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
        self.enterRule(localctx, 16, self.RULE_const_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 125
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 126
                self.idd()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SOGAParser.T__10:
                self.state = 129
                self.match(SOGAParser.T__10)
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
        self.enterRule(localctx, 18, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.add_term()
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 137
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__8 or _la==SOGAParser.T__9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 138
                    self.add_term() 
                self.state = 143
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
        self.enterRule(localctx, 20, self.RULE_add_term)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 146
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SOGAParser.NUM]:
                        self.state = 144
                        self.match(SOGAParser.NUM)
                        pass
                    elif token in [SOGAParser.IDV]:
                        self.state = 145
                        self.idd()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 148
                    self.match(SOGAParser.T__10)


                self.state = 151
                self.vars_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
        self.enterRule(localctx, 22, self.RULE_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 157
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 155
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 156
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 159
                self.match(SOGAParser.T__10)


            self.state = 162
            self.vars_()
            self.state = 163
            self.match(SOGAParser.T__10)
            self.state = 164
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
        self.enterRule(localctx, 24, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.ifclause()
            self.state = 167
            self.elseclause()
            self.state = 168
            self.match(SOGAParser.T__11)
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
        self.enterRule(localctx, 26, self.RULE_ifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SOGAParser.T__12)
            self.state = 171
            self.bexpr()
            self.state = 172
            self.match(SOGAParser.T__13)
            self.state = 173
            self.block()
            self.state = 174
            self.match(SOGAParser.T__14)
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
        self.enterRule(localctx, 28, self.RULE_elseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(SOGAParser.T__15)
            self.state = 177
            self.match(SOGAParser.T__13)
            self.state = 178
            self.block()
            self.state = 179
            self.match(SOGAParser.T__14)
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
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 181
                self.instr()
                self.state = 182
                self.match(SOGAParser.T__0)
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__5) | (1 << SOGAParser.T__7) | (1 << SOGAParser.T__12) | (1 << SOGAParser.T__22) | (1 << SOGAParser.T__23) | (1 << SOGAParser.T__24) | (1 << SOGAParser.IDV))) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_bexpr)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.lexpr()
                self.state = 189
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__16) | (1 << SOGAParser.T__17) | (1 << SOGAParser.T__18) | (1 << SOGAParser.T__19))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 190
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 191
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.symvars()
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==SOGAParser.T__20 or _la==SOGAParser.T__21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 196
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 197
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
        self.enterRule(localctx, 34, self.RULE_lexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.monom()
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 203
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__8 or _la==SOGAParser.T__9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.monom() 
                self.state = 209
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
        self.enterRule(localctx, 36, self.RULE_monom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 212
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 210
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 211
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 214
                self.match(SOGAParser.T__10)


            self.state = 217
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
        self.enterRule(localctx, 38, self.RULE_prune)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(SOGAParser.T__22)
            self.state = 220
            self.match(SOGAParser.NUM)
            self.state = 221
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
        self.enterRule(localctx, 40, self.RULE_observe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(SOGAParser.T__23)
            self.state = 224
            self.bexpr()
            self.state = 225
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
        self.enterRule(localctx, 42, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(SOGAParser.T__24)
            self.state = 228
            self.match(SOGAParser.IDV)
            self.state = 229
            self.match(SOGAParser.T__25)
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 230
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 231
                self.idd()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 234
            self.match(SOGAParser.T__6)
            self.state = 235
            self.match(SOGAParser.T__13)
            self.state = 236
            self.block()
            self.state = 237
            self.match(SOGAParser.T__14)
            self.state = 238
            self.match(SOGAParser.T__26)
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
        self.enterRule(localctx, 44, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.lexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SOGAParser.NUM:
                    self.state = 241
                    self.match(SOGAParser.NUM)
                    self.state = 242
                    self.match(SOGAParser.T__10)


                self.state = 245
                self.vars_()
                self.state = 246
                self.match(SOGAParser.T__10)
                self.state = 247
                self.vars_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.vars_()
                self.state = 250
                self.match(SOGAParser.T__27)
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
        self.enterRule(localctx, 46, self.RULE_vars)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.symvars()
                pass
            elif token in [SOGAParser.T__29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.gm()
                pass
            elif token in [SOGAParser.T__31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.uniform()
                pass
            elif token in [SOGAParser.T__32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
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
        self.enterRule(localctx, 48, self.RULE_idd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(SOGAParser.IDV)
            self.state = 261
            self.match(SOGAParser.T__28)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==SOGAParser.IDV or _la==SOGAParser.NUM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 263
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
        self.enterRule(localctx, 50, self.RULE_symvars)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(SOGAParser.IDV)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
        self.enterRule(localctx, 52, self.RULE_gm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(SOGAParser.T__29)
            self.state = 270
            self.list_()
            self.state = 271
            self.match(SOGAParser.T__30)
            self.state = 272
            self.list_()
            self.state = 273
            self.match(SOGAParser.T__30)
            self.state = 274
            self.list_()
            self.state = 275
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
        self.enterRule(localctx, 54, self.RULE_uniform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(SOGAParser.T__31)
            self.state = 278
            self.list_()
            self.state = 279
            self.match(SOGAParser.T__30)
            self.state = 280
            self.match(SOGAParser.NUM)
            self.state = 281
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
        self.enterRule(localctx, 56, self.RULE_poisson)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(SOGAParser.T__32)
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 284
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 285
                self.symvars()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 288
            self.match(SOGAParser.T__30)
            self.state = 289
            self.match(SOGAParser.NUM)
            self.state = 290
            self.match(SOGAParser.T__30)
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__33) | (1 << SOGAParser.T__34) | (1 << SOGAParser.T__35) | (1 << SOGAParser.T__36))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 292
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
        self.enterRule(localctx, 58, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(SOGAParser.T__28)
            self.state = 295
            self.match(SOGAParser.NUM)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 296
                    self.match(SOGAParser.T__30)
                    self.state = 297
                    self.match(SOGAParser.NUM) 
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 303
            self.match(SOGAParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





