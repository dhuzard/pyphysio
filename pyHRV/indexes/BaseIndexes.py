__author__ = 'AleB'


class Index(object):
    """This is an index extractor class.
    To calculate an index the relative class (subclass of this) must be instantiated,
    the resulting value will be available through the 'value' property. This class is abstract.
    """

    def __init__(self, data=None, value=None):
        """
        Initializes the index. This class is abstract.
        @param data: DataSeries from where extract the index.
        @param value: Already present result.
        """
        assert self.__class__ != Index
        self._value = value
        self._data = data

    @property
    def value(self):
        """
        Returns the value of the index, calculated during the instantiation.

        @return: Number
        """
        return self._value

    @classmethod
    def calculate_on(cls, state):
        raise NotImplementedError(cls.__name__ + " is not available as an on-line index.")


class TDIndex(Index):
    """This is the base class for the Time Domain Indexes.
    """

    def __init__(self, data=None):
        super(TDIndex, self).__init__(data)


class FDIndex(Index):
    """This is the base class for the Frequency Domain Indexes.
    It uses the settings' default interpolation frequency parameter.
    """

    def __init__(self, interp_freq, data=None):
        super(FDIndex, self).__init__(data)
        self._interp_freq = interp_freq


class NonLinearIndex(Index):
    """This is the base class for the Non Linear Indexes."""

    def __init__(self, data=None):
        super(NonLinearIndex, self).__init__(data)


class SupportValue(object):
    """Abstract class that defines the SupportValues' interface."""

    def __init__(self):
        self._state = 0

    def enqueuing(self, new_value):
        """Updates the support-value with the new enqueued value."""
        self._state += 1

    def dequeuing(self, old_value):
        """Updates the support-value with the just dequeued value."""
        pass

