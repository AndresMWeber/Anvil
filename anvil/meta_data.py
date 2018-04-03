from six import iteritems
import config as cfg
import log
from utils.generic import to_list, to_str_dict, pop_dict_keys, merge_dicts, dict_compare


class MetaData(log.LogMixin):
    PROTECTED_KWARG = 'protected'
    PROTECT_ALL_KWARG = 'protect_all'
    IGNORED_KWARG = 'ignored'
    FORCE_KWARG = 'force'
    NEW_KWARG = 'new'

    def __init__(self, *args, **kwargs):
        """By default 'type' is always a protected field.

        :param protected: (list or str), a string list of fields that are protected.
                            If you want to set them after protecting you need use the keyword "force".
        :param args: (dict), tuple of input dictionaries
        :param kwargs: dict, input kwargs to merge
        """
        protect_all = kwargs.pop(self.PROTECT_ALL_KWARG, False)
        self.protected = set(to_list(kwargs.pop(self.PROTECTED_KWARG, None)) + [cfg.TYPE])
        self.data = {}
        self.merge(force=True, *args, **kwargs)

        if protect_all:
            self.protected = set(self.data)

    def copy(self):
        return self.data.copy()

    def merge(self, *args, **kwargs):
        """Merge the incoming dictionaries into the current MetaData instance.

        If the user passes a list of ignore_keys then these keys will be ignored...however the user can permanently set
        them as protected.

        :param force: (bool), whether or not to use both ignore_keys and the protected keys.
        :param new: (bool), merge will return a new MetaData from the merge and leave the current one unchanged.
        :param args: (dict), tuple of input dictionaries
        :param kwargs: dict, input kwargs to merge
        :return: (MetaData or dict), depending on the new kwarg will return the updated dictionary or a new MetaData.
        """
        new, force = kwargs.pop(self.NEW_KWARG, False), kwargs.pop(self.FORCE_KWARG, False)
        ignore_keys = set(to_list(kwargs.pop(self.IGNORED_KWARG, None))).union(getattr(self, self.PROTECTED_KWARG))
        processed_data = merge_dicts(*self._process_args(args), **kwargs)

        if not force:
            pop_dict_keys(processed_data, ignore_keys)

        if new:
            return self.__class__(self.data, processed_data, protected=ignore_keys or None)
        else:
            self.data.update(processed_data)
            return self.data

    def set_protected(self, key_or_keys):
        """Update the internal protected keys list permanently and protect those keys!

        :param args: (dict), tuple of input dictionaries
        :param kwargs: dict, input kwargs to merge
        :param key_or_keys: (str or list(str)): list of strings or string representing keys we want to write-protect.
        """
        self.protected = self.protected.union(set(to_list(key_or_keys)))

    def update(self, *args, **kwargs):
        """For ease of use to act like a dictionary.

        Instead of the frustrating NON return of dicts, returns self while merge returns the self.data dictionary

        :param args: (dict), tuple of input dictionaries
        :param kwargs: dict, input kwargs to merge
        :return: (MetaData), updated instance
        """
        self.merge(*args, **kwargs)
        return self

    def get(self, item, *args, **kwargs):
        return self.data.get(item, *args, **kwargs)

    def keys(self):
        return list(self.data)

    def iteritems(self):
        return iteritems(self.data)

    def to_dict(self):
        return self.data

    def _process_args(self, args):
        return tuple(arg.data if isinstance(arg, self.__class__) else arg for arg in args)

    def __serialize__(self):
        """Not finished."""
        try:
            return str(to_str_dict(self.data))
        except:
            raise UnicodeError('Could not cast meta_data to string for meta_data %s' % self.data)

    def __radd__(self, other):
        """Adds other to self."""
        return self.__add__(other)

    def __getattr__(self, item):
        """Delegate to the data field so we can access all meta_data with dot notation."""
        try:
            super(MetaData, self).__getattribute__('data')[item]
        except (AttributeError, KeyError):
            super(MetaData, self).__getattribute__(item)

    def __add__(self, other):
        """Merges internal dictionary with other."""
        if isinstance(other, self.__class__):
            return self.merge(other.data, new=True)
        if isinstance(other, dict):
            return self.merge(other, new=True)
        if other is None:
            return self
        else:
            raise ValueError('Addition for %s and %s types unsupported.' % (self.__class__, type(other)))

    def __getitem__(self, key):
        """"Gets item at key."""
        return self.data[key]

    def __len__(self):
        """Returns the number of keys in self.data"""
        return len(self.keys())

    def __setitem__(self, key, value):
        """Sets the item in the self.data dictionary."""
        self.data[key] = value

    def __eq__(self, other):
        """Compares the other dictionary/MetaData object to its own data."""
        other = other.data if isinstance(other, self.__class__) else other
        if isinstance(other, dict):
            return dict_compare(self.data, other)
        return False

    def __iter__(self):
        """Returns an iterator of the internal data dict."""
        return iter(self.data)

    def __repr__(self):
        """Shows the current values of the data and what fields are protected."""
        return '<{MODULE}.{CLASS}(data={DATA}, protected={PROTECTED}) at {ID}>'.format(MODULE=self.__class__.__module__,
                                                                                       CLASS=self.__class__.__name__,
                                                                                       DATA=self.data,
                                                                                       PROTECTED=self.protected,
                                                                                       ID=hex(id(self)))

    def __str__(self):
        """Shows the current values of the data and what fields are protected."""
        return '{CLASS}({DATA}, protected={PROTECTED})'.format(CLASS=self.__class__.__name__,
                                                               DATA=self.data,
                                                               PROTECTED=self.protected)
