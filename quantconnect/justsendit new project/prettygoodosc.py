#region imports
from AlgorithmImports import *
#endregion
import config
import statistics as stats
from collections import deque



class PGO_LB():
    
    def __init__(self, algorithm, length):

        self.Length = length

        self.pgo_osc = deque(maxlen=self.Length)
        self.is_ready = False
        # self.short = deque(maxlen=self.Length_short)
        # self.short = deque(maxlen=self.Length_short)
        self.sma = SimpleMovingAverage(self.Length)
        self.ema = ExponentialMovingAverage(self.Length)
        self.tr = TrueRange()
        self.pgo_osc_value = None

      

        self.Bullish = False
        self.Bearish = False


        

    def Bull_Or_Bear(self, color, bar):
        self.tr.Update(IndicatorDataPoint(bar.EndTime))
        if self.tr.IsReady:
            self.sma.Update(IndicatorDataPoint(bar.EndTime, bar.Close))
            self.ema.Update(IndicatorDataPoint(bar.EndTime, self.tr.Current.Value))
        if self.ema.IsReady:
            self.pgo_osc_value = (bar.Close - self.sma.Current.Value) / self.ema.Current.Value
            self.is_ready = True
        
        
            if self.pgo_osc_value > 0:
                self.Bearish = False
                self.Bullish = True
            elif self.pgo_osc_value < 0:
                self.Bullish = False
                self.Bearish = True
            else:
                self.Bullish = False
                self.Bearish = False

                