# Generated from ASGMT.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,1,1,1,3,1,33,8,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,2,1,
        2,1,2,3,2,44,8,2,1,2,1,2,1,3,1,3,3,3,50,8,3,1,3,1,3,3,3,54,8,3,1,
        3,1,3,3,3,58,8,3,1,3,3,3,61,8,3,1,4,1,4,3,4,65,8,4,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,3,8,90,8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,5,
        11,100,8,11,10,11,12,11,103,9,11,1,11,1,11,1,12,1,12,1,12,2,37,101,
        0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,1,0,15,16,1,0,10,13,107,
        0,26,1,0,0,0,2,30,1,0,0,0,4,43,1,0,0,0,6,60,1,0,0,0,8,64,1,0,0,0,
        10,66,1,0,0,0,12,71,1,0,0,0,14,79,1,0,0,0,16,89,1,0,0,0,18,91,1,
        0,0,0,20,93,1,0,0,0,22,95,1,0,0,0,24,106,1,0,0,0,26,27,3,8,4,0,27,
        28,5,1,0,0,28,29,3,2,1,0,29,1,1,0,0,0,30,37,3,4,2,0,31,33,5,2,0,
        0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,36,3,4,2,0,35,32,
        1,0,0,0,36,39,1,0,0,0,37,38,1,0,0,0,37,35,1,0,0,0,38,3,1,0,0,0,39,
        37,1,0,0,0,40,41,3,6,3,0,41,42,5,3,0,0,42,44,1,0,0,0,43,40,1,0,0,
        0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,3,6,3,0,46,5,1,0,0,0,47,61,5,
        16,0,0,48,50,3,24,12,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,
        51,61,3,8,4,0,52,54,3,24,12,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,
        1,0,0,0,55,61,3,12,6,0,56,58,3,24,12,0,57,56,1,0,0,0,57,58,1,0,0,
        0,58,59,1,0,0,0,59,61,3,14,7,0,60,47,1,0,0,0,60,49,1,0,0,0,60,53,
        1,0,0,0,60,57,1,0,0,0,61,7,1,0,0,0,62,65,5,15,0,0,63,65,3,10,5,0,
        64,62,1,0,0,0,64,63,1,0,0,0,65,9,1,0,0,0,66,67,5,15,0,0,67,68,5,
        4,0,0,68,69,7,0,0,0,69,70,5,5,0,0,70,11,1,0,0,0,71,72,5,6,0,0,72,
        73,3,22,11,0,73,74,5,7,0,0,74,75,3,22,11,0,75,76,5,7,0,0,76,77,3,
        22,11,0,77,78,5,8,0,0,78,13,1,0,0,0,79,80,5,9,0,0,80,81,3,16,8,0,
        81,82,5,7,0,0,82,83,3,18,9,0,83,84,5,7,0,0,84,85,3,20,10,0,85,86,
        5,8,0,0,86,15,1,0,0,0,87,90,5,16,0,0,88,90,3,8,4,0,89,87,1,0,0,0,
        89,88,1,0,0,0,90,17,1,0,0,0,91,92,5,16,0,0,92,19,1,0,0,0,93,94,7,
        1,0,0,94,21,1,0,0,0,95,96,5,4,0,0,96,101,5,16,0,0,97,98,5,7,0,0,
        98,100,5,16,0,0,99,97,1,0,0,0,100,103,1,0,0,0,101,102,1,0,0,0,101,
        99,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,5,0,0,105,23,
        1,0,0,0,106,107,5,14,0,0,107,25,1,0,0,0,10,32,37,43,49,53,57,60,
        64,89,101
    ]

class ASGMTParser ( Parser ):

    grammarFileName = "ASGMT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'*'", "'['", "']'", "'gm('", 
                     "','", "')'", "'poisson('", "'disc'", "'nbin'", "'mom1'", 
                     "'mom2'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDV", "NUM", 
                      "COMM", "WS", "DIGIT" ]

    RULE_assignment = 0
    RULE_add = 1
    RULE_add_term = 2
    RULE_term = 3
    RULE_symvars = 4
    RULE_idd = 5
    RULE_gm = 6
    RULE_poisson = 7
    RULE_prate = 8
    RULE_psupp = 9
    RULE_ppar = 10
    RULE_list = 11
    RULE_sub = 12

    ruleNames =  [ "assignment", "add", "add_term", "term", "symvars", "idd", 
                   "gm", "poisson", "prate", "psupp", "ppar", "list", "sub" ]

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
    IDV=15
    NUM=16
    COMM=17
    WS=18
    DIGIT=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symvars(self):
            return self.getTypedRuleContext(ASGMTParser.SymvarsContext,0)


        def add(self):
            return self.getTypedRuleContext(ASGMTParser.AddContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_assignment

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

        localctx = ASGMTParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.symvars()
            self.state = 27
            self.match(ASGMTParser.T__0)
            self.state = 28
            self.add()
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
                return self.getTypedRuleContexts(ASGMTParser.Add_termContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.Add_termContext,i)


        def getRuleIndex(self):
            return ASGMTParser.RULE_add

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

        localctx = ASGMTParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.add_term()
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ASGMTParser.T__1:
                        self.state = 31
                        self.match(ASGMTParser.T__1)


                    self.state = 34
                    self.add_term() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.TermContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.TermContext,i)


        def getRuleIndex(self):
            return ASGMTParser.RULE_add_term

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

        localctx = ASGMTParser.Add_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_add_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 40
                self.term()
                self.state = 41
                self.match(ASGMTParser.T__2)


            self.state = 45
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ASGMTParser.NUM, 0)

        def symvars(self):
            return self.getTypedRuleContext(ASGMTParser.SymvarsContext,0)


        def sub(self):
            return self.getTypedRuleContext(ASGMTParser.SubContext,0)


        def gm(self):
            return self.getTypedRuleContext(ASGMTParser.GmContext,0)


        def poisson(self):
            return self.getTypedRuleContext(ASGMTParser.PoissonContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)
            
        def is_var(self, data):
            """ Returns 1 if term is a variable, 0 if it's a constant """
            if not self.NUM() is None:
                return False
            elif not self.symvars() is None:
                if not self.symvars().IDV() is None:
                    return True
                elif not self.symvars().idd() is None:
                    if self.symvars().idd().is_data(data):
                        return False
                    else:
                        return True
            elif not self.gm() is None:
                return True
            elif not self.poisson() is None:
                return True
    
        def is_const(self, data):
            return not self.is_var(data)

        def getValue(self, data):
            if self.is_const(data):
                if not self.NUM() is None:
                    return float(self.NUM().getText())
                elif not self.symvars() is None:
                    return self.symvars().idd().getValue(data)
            else:
                raise("Calling getValue for a variable")

                
    def term(self):

        localctx = ASGMTParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(ASGMTParser.NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ASGMTParser.T__13:
                    self.state = 48
                    self.sub()


                self.state = 51
                self.symvars()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ASGMTParser.T__13:
                    self.state = 52
                    self.sub()


                self.state = 55
                self.gm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ASGMTParser.T__13:
                    self.state = 56
                    self.sub()


                self.state = 59
                self.poisson()
                pass


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
            return self.getToken(ASGMTParser.IDV, 0)

        def idd(self):
            return self.getTypedRuleContext(ASGMTParser.IddContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_symvars

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
            
        def getVar(self, data):
            if self.idd() is None:
                return self.getText()
            else:
                if self.idd().IDV(1) is None:
                    return self.getText()
                else:
                    data_idx = data[self.idd().IDV(1).getText()][0]
                return self.idd().IDV(0).getText()+'['+str(data_idx)+']'




    def symvars(self):

        localctx = ASGMTParser.SymvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_symvars)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(ASGMTParser.IDV)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.idd()
                pass


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
                return self.getTokens(ASGMTParser.IDV)
            else:
                return self.getToken(ASGMTParser.IDV, i)

        def NUM(self):
            return self.getToken(ASGMTParser.NUM, 0)

        def getRuleIndex(self):
            return ASGMTParser.RULE_idd

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
            
        def is_data(self, data):
            if self.IDV(0).getText() in data.keys():
                return True
            else:
                return False
   
        def getValue(self, data):
            data_name = self.IDV(0).getText()
            if not self.NUM() is None:
                data_idx = int(self.NUM().getText())
            elif not self.IDV(1) is None:
                data_idx = data[self.IDV(1).getText()][0]
            return data[data_name][data_idx]


    def idd(self):

        localctx = ASGMTParser.IddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ASGMTParser.IDV)
            self.state = 67
            self.match(ASGMTParser.T__3)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==ASGMTParser.IDV or _la==ASGMTParser.NUM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.match(ASGMTParser.T__4)
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
                return self.getTypedRuleContexts(ASGMTParser.ListContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.ListContext,i)


        def getRuleIndex(self):
            return ASGMTParser.RULE_gm

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

        localctx = ASGMTParser.GmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_gm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ASGMTParser.T__5)
            self.state = 72
            self.list_()
            self.state = 73
            self.match(ASGMTParser.T__6)
            self.state = 74
            self.list_()
            self.state = 75
            self.match(ASGMTParser.T__6)
            self.state = 76
            self.list_()
            self.state = 77
            self.match(ASGMTParser.T__7)
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

        def prate(self):
            return self.getTypedRuleContext(ASGMTParser.PrateContext,0)


        def psupp(self):
            return self.getTypedRuleContext(ASGMTParser.PsuppContext,0)


        def ppar(self):
            return self.getTypedRuleContext(ASGMTParser.PparContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_poisson

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

        localctx = ASGMTParser.PoissonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_poisson)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ASGMTParser.T__8)
            self.state = 80
            self.prate()
            self.state = 81
            self.match(ASGMTParser.T__6)
            self.state = 82
            self.psupp()
            self.state = 83
            self.match(ASGMTParser.T__6)
            self.state = 84
            self.ppar()
            self.state = 85
            self.match(ASGMTParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ASGMTParser.NUM, 0)

        def symvars(self):
            return self.getTypedRuleContext(ASGMTParser.SymvarsContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_prate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrate" ):
                listener.enterPrate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrate" ):
                listener.exitPrate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrate" ):
                return visitor.visitPrate(self)
            else:
                return visitor.visitChildren(self)




    def prate(self):

        localctx = ASGMTParser.PrateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_prate)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASGMTParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(ASGMTParser.NUM)
                pass
            elif token in [ASGMTParser.IDV]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.symvars()
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


    class PsuppContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ASGMTParser.NUM, 0)

        def getRuleIndex(self):
            return ASGMTParser.RULE_psupp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPsupp" ):
                listener.enterPsupp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPsupp" ):
                listener.exitPsupp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPsupp" ):
                return visitor.visitPsupp(self)
            else:
                return visitor.visitChildren(self)




    def psupp(self):

        localctx = ASGMTParser.PsuppContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_psupp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ASGMTParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ASGMTParser.RULE_ppar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPpar" ):
                listener.enterPpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPpar" ):
                listener.exitPpar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPpar" ):
                return visitor.visitPpar(self)
            else:
                return visitor.visitChildren(self)




    def ppar(self):

        localctx = ASGMTParser.PparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ppar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ASGMTParser.T__9) | (1 << ASGMTParser.T__10) | (1 << ASGMTParser.T__11) | (1 << ASGMTParser.T__12))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
                return self.getTokens(ASGMTParser.NUM)
            else:
                return self.getToken(ASGMTParser.NUM, i)

        def getRuleIndex(self):
            return ASGMTParser.RULE_list

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

        localctx = ASGMTParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ASGMTParser.T__3)
            self.state = 96
            self.match(ASGMTParser.NUM)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 97
                    self.match(ASGMTParser.T__6)
                    self.state = 98
                    self.match(ASGMTParser.NUM) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 104
            self.match(ASGMTParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ASGMTParser.RULE_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)




    def sub(self):

        localctx = ASGMTParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ASGMTParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





