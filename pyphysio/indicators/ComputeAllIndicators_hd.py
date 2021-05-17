# coding=utf-8
import pyphysio.indicators.TimeDomain as td_ind
import pyphysio.indicators.FrequencyDomain as fd_ind
import pyphysio.indicators.NonLinearDomain as nld_ind

from ..BaseIndicator import Indicator as _Indicator

__author__ = 'DHuzard - hd'


class TimeDomain(_Indicator):
    """
    Return an dictionnary containing all the HRV parameters from the Time Domain (defined in the TimeDomain.py).

    Returns
    -------
    TimeDomain_dict : Dictionnary
#TODO: Finish presentation
    
    """

    def __init__(self, **kwargs):
        _Indicator.__init__(self, **kwargs)
        
#    def do_nothing(self):
#       pass

    @classmethod
    def algorithm(cls, data, params):
        """
        Calculates all the TimeDomain parameters
        @return: a dictionary with all the parameters
        @rtype: dict
        """
        # Creates the Time Domain Indicators
        rmssd = td_ind.RMSSD()
        mean = td_ind.Mean()
        min = td_ind.Min()
        max = td_ind.Max()
        range = td_ind.Range()
        median = td_ind.Median()
        stdev = td_ind.StDev()
        sum = td_ind.Sum()
        auc = td_ind.AUC()
        auc_detrended = td_ind.DetrendedAUC()
        sdsd = td_ind.SDSD()
        triang = td_ind.Triang()
        tinn = td_ind.TINN()
        
        ## applies the TimeDomain Indicators
        timedomain_dict =	{
            "rmssd" : rmssd(data),
            "mean" : mean(data),
            "min" : min(data),
            "max" : max(data),
            "range" : range(data),
            "median" : median(data),
            "stdev" : stdev(data),
            "sum" : sum(data),
            "auc" : auc(data),
            "auc_detrended" : auc_detrended(data),
            "sdsd" : sdsd(data),
            "triang" : triang(data),
            "tinn" : tinn(data)
        }

        return timedomain_dict


class FrequencyDomain(_Indicator):
    """
    Return an dictionnary containing all the HRV parameters from the Frequency Domain (defined in the FrequencyDomain.py).

    Returns
    -------
    FrequencyDomain_dict : Dictionnary
#TODO: Finish presentation
    
    """

    def __init__(self, **kwargs):
        _Indicator.__init__(self, **kwargs)
        
#    def do_nothing(self):
#       pass

    @classmethod
    def algorithm(cls, data, params):
        """
        Calculates all the FrequencyDomain parameters
        @return: a dictionary with all the parameters
        @rtype: dict
        """
        # Creates the Time Domain Indicators
        VLF = fd_ind.PowerInBand(interp_freq=4, freq_max=0.04, freq_min=0, method = 'ar')
        print(f"VLF created with {freq_min} and {freq_max} as boundaries.")
        LF = fd_ind.PowerInBand(interp_freq=4, freq_max=0.15, freq_min=0.04, method = 'ar')
        print(f"LF created with {freq_min} and {freq_max} as boundaries.")
        HF = fd_ind.PowerInBand(interp_freq=4, freq_max=0.4, freq_min=0.15, method = 'ar')
        print(f"HF created with {freq_min} and {freq_max} as boundaries.")

        ## applies the TimeDomain Indicators
        freqdomain_dict =	{
            "VLF" : VLF(ibi.resample(4)), #resampling is needed to compute the Power Spectrum Density
            "LF" : LF(ibi.resample(4)), #resampling is needed to compute the Power Spectrum Density
            "HF" : HF(ibi.resample(4)) #resampling is needed to compute the Power Spectrum Density
        }

        return freqdomain_dict


class NonLinearDomain(_Indicator):
    """
    Return an dictionnary containing all the HRV parameters from the Non-Linear Domain (defined in the NonLinearDomain.py).

    Returns
    -------
    NonLinearDomain_dict : Dictionary
#TODO: Finish presentation
    
    """

    def __init__(self, **kwargs):
        _Indicator.__init__(self, **kwargs)
        
#    def do_nothing(self):
#       pass

    @classmethod
    def algorithm(cls, data, params):
        """
        Calculates all the NonLinearDomain parameters
        @return: a dictionary with all the parameters
        @rtype: dict
        """
        # Creates the NonLinear Domain Indicators
        sd1 = nld_ind.PoincareSD1()
        sd2 = nld_ind.PoincareSD2()
        sd1sd2 = nld_ind.PoincareSD1SD2() # SD1/SD2
        poinell = nld_ind.PoinEll()
        pnnx = nld_ind.PNNx(threshold=0.1) # Relative frequency of pairs of consecutive samples s1, s2 
        nnx = nld_ind.NNx(threshold=0.1) # Counts the pairs of consecutive samples s1, s2
        entropy_approx = nld_ind.ApproxEntropy()
        entropy_sample = nld_ind.SampleEntropy()
        dfa_short = nld_ind.DFAShortTerm()
        dfa_long = nld_ind.DFALongTerm()

        ## applies the NonLinear Domain Indicators
        nonlineardomain_dict =	{
            "sd1" : sd1(ibi),
            "sd2" : sd2(ibi),
            "sd1sd2" : sd1sd2(ibi),
            "poinell" : poinell(ibi),
            "pnnx" : pnnx(ibi),
            "nnx" : nnx(ibi),
            "entropy_approx" : entropy_approx(ibi),
            "entropy_sample" : entropy_sample(ibi),
            "dfa_short" : dfa_short(ibi),
            "dfa_long" : dfa_long(ibi)
        }

        return nonlineardomain_dict
    
