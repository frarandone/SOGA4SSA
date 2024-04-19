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
        4,1,41,291,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,71,8,0,10,0,12,0,74,9,0,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,91,8,3,1,4,1,4,1,4,1,4,1,4,
        3,4,98,8,4,1,4,3,4,101,8,4,1,5,1,5,1,5,5,5,106,8,5,10,5,12,5,109,
        9,5,1,6,1,6,3,6,113,8,6,1,6,1,6,1,6,3,6,118,8,6,3,6,120,8,6,1,7,
        1,7,1,7,5,7,125,8,7,10,7,12,7,128,9,7,1,8,1,8,3,8,132,8,8,1,8,3,
        8,135,8,8,1,8,1,8,3,8,139,8,8,1,9,1,9,3,9,143,8,9,1,9,3,9,146,8,
        9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,4,13,170,8,13,11,13,12,
        13,171,1,14,1,14,1,14,1,14,3,14,178,8,14,1,14,1,14,1,14,1,14,3,14,
        184,8,14,3,14,186,8,14,1,15,1,15,1,15,5,15,191,8,15,10,15,12,15,
        194,9,15,1,16,1,16,3,16,198,8,16,1,16,3,16,201,8,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,
        19,218,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,3,20,229,
        8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,238,8,20,1,21,1,21,
        1,21,1,21,3,21,244,8,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,3,23,
        253,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,3,26,272,8,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,27,1,27,1,27,1,27,5,27,284,8,27,10,27,12,27,287,9,27,
        1,27,1,27,1,27,5,61,107,126,192,285,0,28,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,5,1,0,7,
        8,1,0,15,18,1,0,19,20,1,0,37,38,1,0,33,36,299,0,61,1,0,0,0,2,75,
        1,0,0,0,4,80,1,0,0,0,6,90,1,0,0,0,8,100,1,0,0,0,10,102,1,0,0,0,12,
        112,1,0,0,0,14,121,1,0,0,0,16,138,1,0,0,0,18,145,1,0,0,0,20,151,
        1,0,0,0,22,155,1,0,0,0,24,161,1,0,0,0,26,169,1,0,0,0,28,185,1,0,
        0,0,30,187,1,0,0,0,32,200,1,0,0,0,34,204,1,0,0,0,36,208,1,0,0,0,
        38,212,1,0,0,0,40,237,1,0,0,0,42,243,1,0,0,0,44,245,1,0,0,0,46,252,
        1,0,0,0,48,254,1,0,0,0,50,262,1,0,0,0,52,268,1,0,0,0,54,279,1,0,
        0,0,56,57,3,2,1,0,57,58,5,1,0,0,58,60,1,0,0,0,59,56,1,0,0,0,60,63,
        1,0,0,0,61,62,1,0,0,0,61,59,1,0,0,0,62,72,1,0,0,0,63,61,1,0,0,0,
        64,65,3,6,3,0,65,66,5,1,0,0,66,71,1,0,0,0,67,68,3,4,2,0,68,69,5,
        1,0,0,69,71,1,0,0,0,70,64,1,0,0,0,70,67,1,0,0,0,71,74,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,1,1,0,0,0,74,72,1,0,0,0,75,76,5,2,0,
        0,76,77,3,46,23,0,77,78,5,3,0,0,78,79,3,54,27,0,79,3,1,0,0,0,80,
        81,5,4,0,0,81,82,5,38,0,0,82,83,5,5,0,0,83,84,5,37,0,0,84,5,1,0,
        0,0,85,91,3,8,4,0,86,91,3,20,10,0,87,91,3,34,17,0,88,91,3,36,18,
        0,89,91,3,38,19,0,90,85,1,0,0,0,90,86,1,0,0,0,90,87,1,0,0,0,90,88,
        1,0,0,0,90,89,1,0,0,0,91,7,1,0,0,0,92,93,3,46,23,0,93,97,5,3,0,0,
        94,98,3,10,5,0,95,98,3,14,7,0,96,98,3,18,9,0,97,94,1,0,0,0,97,95,
        1,0,0,0,97,96,1,0,0,0,98,101,1,0,0,0,99,101,5,6,0,0,100,92,1,0,0,
        0,100,99,1,0,0,0,101,9,1,0,0,0,102,107,3,12,6,0,103,104,7,0,0,0,
        104,106,3,12,6,0,105,103,1,0,0,0,106,109,1,0,0,0,107,108,1,0,0,0,
        107,105,1,0,0,0,108,11,1,0,0,0,109,107,1,0,0,0,110,113,5,38,0,0,
        111,113,3,44,22,0,112,110,1,0,0,0,112,111,1,0,0,0,113,119,1,0,0,
        0,114,117,5,9,0,0,115,118,5,38,0,0,116,118,3,44,22,0,117,115,1,0,
        0,0,117,116,1,0,0,0,118,120,1,0,0,0,119,114,1,0,0,0,119,120,1,0,
        0,0,120,13,1,0,0,0,121,126,3,16,8,0,122,123,7,0,0,0,123,125,3,16,
        8,0,124,122,1,0,0,0,125,128,1,0,0,0,126,127,1,0,0,0,126,124,1,0,
        0,0,127,15,1,0,0,0,128,126,1,0,0,0,129,132,5,38,0,0,130,132,3,44,
        22,0,131,129,1,0,0,0,131,130,1,0,0,0,132,133,1,0,0,0,133,135,5,9,
        0,0,134,131,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,139,3,42,
        21,0,137,139,3,12,6,0,138,134,1,0,0,0,138,137,1,0,0,0,139,17,1,0,
        0,0,140,143,5,38,0,0,141,143,3,44,22,0,142,140,1,0,0,0,142,141,1,
        0,0,0,143,144,1,0,0,0,144,146,5,9,0,0,145,142,1,0,0,0,145,146,1,
        0,0,0,146,147,1,0,0,0,147,148,3,42,21,0,148,149,5,9,0,0,149,150,
        3,42,21,0,150,19,1,0,0,0,151,152,3,22,11,0,152,153,3,24,12,0,153,
        154,5,10,0,0,154,21,1,0,0,0,155,156,5,11,0,0,156,157,3,28,14,0,157,
        158,5,12,0,0,158,159,3,26,13,0,159,160,5,13,0,0,160,23,1,0,0,0,161,
        162,5,14,0,0,162,163,5,12,0,0,163,164,3,26,13,0,164,165,5,13,0,0,
        165,25,1,0,0,0,166,167,3,6,3,0,167,168,5,1,0,0,168,170,1,0,0,0,169,
        166,1,0,0,0,170,171,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,
        27,1,0,0,0,173,174,3,30,15,0,174,177,7,1,0,0,175,178,5,38,0,0,176,
        178,3,44,22,0,177,175,1,0,0,0,177,176,1,0,0,0,178,186,1,0,0,0,179,
        180,3,46,23,0,180,183,7,2,0,0,181,184,5,38,0,0,182,184,3,44,22,0,
        183,181,1,0,0,0,183,182,1,0,0,0,184,186,1,0,0,0,185,173,1,0,0,0,
        185,179,1,0,0,0,186,29,1,0,0,0,187,192,3,32,16,0,188,189,7,0,0,0,
        189,191,3,32,16,0,190,188,1,0,0,0,191,194,1,0,0,0,192,193,1,0,0,
        0,192,190,1,0,0,0,193,31,1,0,0,0,194,192,1,0,0,0,195,198,5,38,0,
        0,196,198,3,44,22,0,197,195,1,0,0,0,197,196,1,0,0,0,198,199,1,0,
        0,0,199,201,5,9,0,0,200,197,1,0,0,0,200,201,1,0,0,0,201,202,1,0,
        0,0,202,203,3,42,21,0,203,33,1,0,0,0,204,205,5,21,0,0,205,206,5,
        38,0,0,206,207,5,22,0,0,207,35,1,0,0,0,208,209,5,23,0,0,209,210,
        3,28,14,0,210,211,5,22,0,0,211,37,1,0,0,0,212,213,5,24,0,0,213,214,
        5,37,0,0,214,217,5,25,0,0,215,218,5,38,0,0,216,218,3,44,22,0,217,
        215,1,0,0,0,217,216,1,0,0,0,218,219,1,0,0,0,219,220,5,22,0,0,220,
        221,5,12,0,0,221,222,3,26,13,0,222,223,5,13,0,0,223,224,5,26,0,0,
        224,39,1,0,0,0,225,238,3,30,15,0,226,227,5,38,0,0,227,229,5,9,0,
        0,228,226,1,0,0,0,228,229,1,0,0,0,229,230,1,0,0,0,230,231,3,42,21,
        0,231,232,5,9,0,0,232,233,3,42,21,0,233,238,1,0,0,0,234,235,3,42,
        21,0,235,236,5,27,0,0,236,238,1,0,0,0,237,225,1,0,0,0,237,228,1,
        0,0,0,237,234,1,0,0,0,238,41,1,0,0,0,239,244,3,46,23,0,240,244,3,
        48,24,0,241,244,3,50,25,0,242,244,3,52,26,0,243,239,1,0,0,0,243,
        240,1,0,0,0,243,241,1,0,0,0,243,242,1,0,0,0,244,43,1,0,0,0,245,246,
        5,37,0,0,246,247,5,28,0,0,247,248,7,3,0,0,248,249,5,5,0,0,249,45,
        1,0,0,0,250,253,5,37,0,0,251,253,3,44,22,0,252,250,1,0,0,0,252,251,
        1,0,0,0,253,47,1,0,0,0,254,255,5,29,0,0,255,256,3,54,27,0,256,257,
        5,30,0,0,257,258,3,54,27,0,258,259,5,30,0,0,259,260,3,54,27,0,260,
        261,5,22,0,0,261,49,1,0,0,0,262,263,5,31,0,0,263,264,3,54,27,0,264,
        265,5,30,0,0,265,266,5,38,0,0,266,267,5,22,0,0,267,51,1,0,0,0,268,
        271,5,32,0,0,269,272,5,38,0,0,270,272,3,46,23,0,271,269,1,0,0,0,
        271,270,1,0,0,0,272,273,1,0,0,0,273,274,5,30,0,0,274,275,5,38,0,
        0,275,276,5,30,0,0,276,277,7,4,0,0,277,278,5,22,0,0,278,53,1,0,0,
        0,279,280,5,28,0,0,280,285,5,38,0,0,281,282,5,30,0,0,282,284,5,38,
        0,0,283,281,1,0,0,0,284,287,1,0,0,0,285,286,1,0,0,0,285,283,1,0,
        0,0,286,288,1,0,0,0,287,285,1,0,0,0,288,289,5,5,0,0,289,55,1,0,0,
        0,30,61,70,72,90,97,100,107,112,117,119,126,131,134,138,142,145,
        171,177,183,185,192,197,200,217,228,237,243,252,271,285
    ]

class SOGAParser ( Parser ):

    grammarFileName = "SOGA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'data'", "'='", "'array['", "']'", 
                     "'skip'", "'+'", "'-'", "'*'", "'end if'", "'if'", 
                     "'{'", "'}'", "'else'", "'<'", "'<='", "'>='", "'>'", 
                     "'=='", "'!='", "'prune('", "')'", "'observe('", "'for'", 
                     "'in range('", "'end for'", "'^2'", "'['", "'gm('", 
                     "','", "'uniform('", "'poisson('", "'disc'", "'nbin'", 
                     "'mom1'", "'mom2'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDV", "NUM", "COMM", "WS", "DIGIT" ]

    RULE_progr = 0
    RULE_data = 1
    RULE_array = 2
    RULE_instr = 3
    RULE_assignment = 4
    RULE_const = 5
    RULE_const_term = 6
    RULE_add = 7
    RULE_add_term = 8
    RULE_mul = 9
    RULE_conditional = 10
    RULE_ifclause = 11
    RULE_elseclause = 12
    RULE_block = 13
    RULE_bexpr = 14
    RULE_lexpr = 15
    RULE_monom = 16
    RULE_prune = 17
    RULE_observe = 18
    RULE_loop = 19
    RULE_expr = 20
    RULE_vars = 21
    RULE_idd = 22
    RULE_symvars = 23
    RULE_gm = 24
    RULE_uniform = 25
    RULE_poisson = 26
    RULE_list = 27

    ruleNames =  [ "progr", "data", "array", "instr", "assignment", "const", 
                   "const_term", "add", "add_term", "mul", "conditional", 
                   "ifclause", "elseclause", "block", "bexpr", "lexpr", 
                   "monom", "prune", "observe", "loop", "expr", "vars", 
                   "idd", "symvars", "gm", "uniform", "poisson", "list" ]

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
    IDV=37
    NUM=38
    COMM=39
    WS=40
    DIGIT=41

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
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 56
                    self.data()
                    self.state = 57
                    self.match(SOGAParser.T__0) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__3) | (1 << SOGAParser.T__5) | (1 << SOGAParser.T__10) | (1 << SOGAParser.T__20) | (1 << SOGAParser.T__22) | (1 << SOGAParser.T__23) | (1 << SOGAParser.IDV))) != 0):
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.T__5, SOGAParser.T__10, SOGAParser.T__20, SOGAParser.T__22, SOGAParser.T__23, SOGAParser.IDV]:
                    self.state = 64
                    self.instr()
                    self.state = 65
                    self.match(SOGAParser.T__0)
                    pass
                elif token in [SOGAParser.T__3]:
                    self.state = 67
                    self.array()
                    self.state = 68
                    self.match(SOGAParser.T__0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 74
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
            self.state = 75
            self.match(SOGAParser.T__1)
            self.state = 76
            self.symvars()
            self.state = 77
            self.match(SOGAParser.T__2)
            self.state = 78
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
            self.state = 80
            self.match(SOGAParser.T__3)
            self.state = 81
            self.match(SOGAParser.NUM)
            self.state = 82
            self.match(SOGAParser.T__4)
            self.state = 83
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.T__5, SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.assignment()
                pass
            elif token in [SOGAParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.conditional()
                pass
            elif token in [SOGAParser.T__20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.prune()
                pass
            elif token in [SOGAParser.T__22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.observe()
                pass
            elif token in [SOGAParser.T__23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.loop()
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
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.symvars()
                self.state = 93
                self.match(SOGAParser.T__2)
                self.state = 97
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 94
                    self.const()
                    pass

                elif la_ == 2:
                    self.state = 95
                    self.add()
                    pass

                elif la_ == 3:
                    self.state = 96
                    self.mul()
                    pass


                pass
            elif token in [SOGAParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(SOGAParser.T__5)
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
        self.enterRule(localctx, 10, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.const_term()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 103
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__6 or _la==SOGAParser.T__7):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 104
                    self.const_term() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_const_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 110
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 111
                self.idd()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SOGAParser.T__8:
                self.state = 114
                self.match(SOGAParser.T__8)
                self.state = 117
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 115
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 116
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
        self.enterRule(localctx, 14, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.add_term()
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 122
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__6 or _la==SOGAParser.T__7):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 123
                    self.add_term() 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_add_term)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 131
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SOGAParser.NUM]:
                        self.state = 129
                        self.match(SOGAParser.NUM)
                        pass
                    elif token in [SOGAParser.IDV]:
                        self.state = 130
                        self.idd()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 133
                    self.match(SOGAParser.T__8)


                self.state = 136
                self.vars_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
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
        self.enterRule(localctx, 18, self.RULE_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 142
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 140
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 141
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 144
                self.match(SOGAParser.T__8)


            self.state = 147
            self.vars_()
            self.state = 148
            self.match(SOGAParser.T__8)
            self.state = 149
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
        self.enterRule(localctx, 20, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.ifclause()
            self.state = 152
            self.elseclause()
            self.state = 153
            self.match(SOGAParser.T__9)
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
        self.enterRule(localctx, 22, self.RULE_ifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(SOGAParser.T__10)
            self.state = 156
            self.bexpr()
            self.state = 157
            self.match(SOGAParser.T__11)
            self.state = 158
            self.block()
            self.state = 159
            self.match(SOGAParser.T__12)
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
        self.enterRule(localctx, 24, self.RULE_elseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(SOGAParser.T__13)
            self.state = 162
            self.match(SOGAParser.T__11)
            self.state = 163
            self.block()
            self.state = 164
            self.match(SOGAParser.T__12)
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
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 166
                self.instr()
                self.state = 167
                self.match(SOGAParser.T__0)
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__5) | (1 << SOGAParser.T__10) | (1 << SOGAParser.T__20) | (1 << SOGAParser.T__22) | (1 << SOGAParser.T__23) | (1 << SOGAParser.IDV))) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_bexpr)
        self._la = 0 # Token type
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.lexpr()
                self.state = 174
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__14) | (1 << SOGAParser.T__15) | (1 << SOGAParser.T__16) | (1 << SOGAParser.T__17))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 175
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 176
                    self.idd()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.symvars()
                self.state = 180
                _la = self._input.LA(1)
                if not(_la==SOGAParser.T__18 or _la==SOGAParser.T__19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SOGAParser.NUM]:
                    self.state = 181
                    self.match(SOGAParser.NUM)
                    pass
                elif token in [SOGAParser.IDV]:
                    self.state = 182
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
        self.enterRule(localctx, 30, self.RULE_lexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.monom()
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 188
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__6 or _la==SOGAParser.T__7):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 189
                    self.monom() 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_monom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
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

                self.state = 199
                self.match(SOGAParser.T__8)


            self.state = 202
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
        self.enterRule(localctx, 34, self.RULE_prune)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(SOGAParser.T__20)
            self.state = 205
            self.match(SOGAParser.NUM)
            self.state = 206
            self.match(SOGAParser.T__21)
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
        self.enterRule(localctx, 36, self.RULE_observe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(SOGAParser.T__22)
            self.state = 209
            self.bexpr()
            self.state = 210
            self.match(SOGAParser.T__21)
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
        self.enterRule(localctx, 38, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(SOGAParser.T__23)
            self.state = 213
            self.match(SOGAParser.IDV)
            self.state = 214
            self.match(SOGAParser.T__24)
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
            self.match(SOGAParser.T__21)
            self.state = 220
            self.match(SOGAParser.T__11)
            self.state = 221
            self.block()
            self.state = 222
            self.match(SOGAParser.T__12)
            self.state = 223
            self.match(SOGAParser.T__25)
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
        self.enterRule(localctx, 40, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.lexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SOGAParser.NUM:
                    self.state = 226
                    self.match(SOGAParser.NUM)
                    self.state = 227
                    self.match(SOGAParser.T__8)


                self.state = 230
                self.vars_()
                self.state = 231
                self.match(SOGAParser.T__8)
                self.state = 232
                self.vars_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.vars_()
                self.state = 235
                self.match(SOGAParser.T__26)
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
        self.enterRule(localctx, 42, self.RULE_vars)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.IDV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.symvars()
                pass
            elif token in [SOGAParser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.gm()
                pass
            elif token in [SOGAParser.T__30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.uniform()
                pass
            elif token in [SOGAParser.T__31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
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
        self.enterRule(localctx, 44, self.RULE_idd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(SOGAParser.IDV)
            self.state = 246
            self.match(SOGAParser.T__27)
            self.state = 247
            _la = self._input.LA(1)
            if not(_la==SOGAParser.IDV or _la==SOGAParser.NUM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 248
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
        self.enterRule(localctx, 46, self.RULE_symvars)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(SOGAParser.IDV)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
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
        self.enterRule(localctx, 48, self.RULE_gm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(SOGAParser.T__28)
            self.state = 255
            self.list_()
            self.state = 256
            self.match(SOGAParser.T__29)
            self.state = 257
            self.list_()
            self.state = 258
            self.match(SOGAParser.T__29)
            self.state = 259
            self.list_()
            self.state = 260
            self.match(SOGAParser.T__21)
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
        self.enterRule(localctx, 50, self.RULE_uniform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(SOGAParser.T__30)
            self.state = 263
            self.list_()
            self.state = 264
            self.match(SOGAParser.T__29)
            self.state = 265
            self.match(SOGAParser.NUM)
            self.state = 266
            self.match(SOGAParser.T__21)
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
        self.enterRule(localctx, 52, self.RULE_poisson)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(SOGAParser.T__31)
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.NUM]:
                self.state = 269
                self.match(SOGAParser.NUM)
                pass
            elif token in [SOGAParser.IDV]:
                self.state = 270
                self.symvars()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 273
            self.match(SOGAParser.T__29)
            self.state = 274
            self.match(SOGAParser.NUM)
            self.state = 275
            self.match(SOGAParser.T__29)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__32) | (1 << SOGAParser.T__33) | (1 << SOGAParser.T__34) | (1 << SOGAParser.T__35))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 277
            self.match(SOGAParser.T__21)
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
        self.enterRule(localctx, 54, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(SOGAParser.T__27)
            self.state = 280
            self.match(SOGAParser.NUM)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 281
                    self.match(SOGAParser.T__29)
                    self.state = 282
                    self.match(SOGAParser.NUM) 
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 288
            self.match(SOGAParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





