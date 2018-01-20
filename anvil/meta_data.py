from six import string_types, iteritems
from functools import wraps
import config as cfg
import log


class MetaData(log.LogMixin):
    LOG = log.obtainLogger(__name__)
    PROTECTED = 'protected_fields'
    IGNORED = 'ignore_keys'
    NEW = 'new'

    def __init__(self, *args, **kwargs):
        self.protected_fields = self._cast_input_to_list(kwargs.pop(self.PROTECTED, None))
        self.data = self.merge_dicts(*[d.data if isinstance(d, self.__class__) else d for d in args], **kwargs)

    @classmethod
    def merge_dicts(cls, *args, **kwargs):
        """ Merges metadata for every dict that has been input.  Starts with dict args then input kwargs
            Overwrites data if there are conflicts from left to right.

        :param protected_fields: list, fields that the metadata should keep and ignore on merge.
        :param args: (dict), tuple of input dictionaries
        :param kwargs: dict, input kwargs to merge
        :return: dict, combined data.
        """
        ignore_keys = kwargs.pop(cls.IGNORED, None) or []
        data = {}

        for input_dict in [dict(d) for d in args if d] + [kwargs]:
            for key in ignore_keys:
                try:
                    input_dict.pop(key)
                except KeyError:
                    pass
            data.update(input_dict)
        return data

    def merge(self, *args, **kwargs):
        new = kwargs.pop(self.NEW, False)
        ignore_keys = self._cast_input_to_list(kwargs.pop('ignore_keys', None)) + self.protected_fields
        keep_originals = self._cast_input_to_list(kwargs.pop('keep_originals', False))
        if keep_originals:
            ignore_keys = ignore_keys + list(self.data)

        input_dict = self.merge_dicts(ignore_keys=ignore_keys, *args, **kwargs)
        if new:
            return self.__class__(self.data, input_dict, ignore_keys=ignore_keys)
        else:
            self.data.update(input_dict)
            return self.data

    def serialize(self, ignore_keys=None):
        ignore_fields = self._cast_input_to_list(ignore_keys)
        try:
            return '{%s}' % (', '.join(['%s: %s' % (str(key), str(value)) for key, value in iteritems(self.data) if
                                        key not in ignore_fields]))
        except:
            raise UnicodeError('Could not cast metadata to string for metadata %s' % self.data)

    def to_str_dict(self):
        data = {}
        for k, v in iteritems(self.data):
            try:
                data.update({str(k): str(v)})
            except:
                pass
        return data

    def update(self, other):
        self.merge(other)
        return self

    @staticmethod
    def _cast_input_to_list(string_or_none_or_list):
        if not isinstance(string_or_none_or_list, list):
            string_or_none_or_list = []

        elif isinstance(string_or_none_or_list, string_types):
            string_or_none_or_list = [string_or_none_or_list]

        return string_or_none_or_list

    def get(self, item, *args, **kwargs):
        return self.data.get(item, *args, **kwargs)

    def keys(self):
        return list(self.data)

    def iteritems(self):
        return iteritems(self.data)

    def __radd__(self, other):
        return self.__add__(other)

    def __getattr__(self, item):
        """ Delegate to the data field so we can access all metadata with dot notation.
        """
        try:
            super(MetaData, self).__getattribute__('data')[item]
        except (AttributeError, KeyError):
            super(MetaData, self).__getattribute__(item)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.merge_dicts(self.data, other.data, ignore_keys=None)
        if isinstance(other, dict):
            return self.merge_dicts(self.data, other, ignore_keys=None)
        if other is None:
            return self.data
        else:
            raise ValueError('Addition for %s and %s types unsupported.' % (self.__class__, type(other)))

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(list(self.data))

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other = other.data
        if isinstance(other, dict):
            return self.dict_compare(self.data, other)
        return False

    def __iter__(self):
        return iter(self.data)

    @staticmethod
    def dict_compare(d1, d2):
        """ Taken from: https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python
        """
        d1_keys = set(list(d1))
        d2_keys = set(list(d2))
        intersect_keys = d1_keys.intersection(d2_keys)
        added = d1_keys - d2_keys
        removed = d2_keys - d1_keys
        modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
        same = set(o for o in intersect_keys if d1[o] == d2[o])
        return added, removed, modified, same


def cls_merge_name_tokens_and_meta_data(pre=True):
    def outer(function):
        @wraps(function)
        def inner(cls_or_self, *args, **kwargs):
            for meta_attr in [cfg.META_DATA, cfg.NAME_TOKENS]:
                if not hasattr(cls_or_self, meta_attr):
                    setattr(cls_or_self, meta_attr, MetaData())

            name_tokens = MetaData(kwargs.pop(cfg.NAME_TOKENS, {}))
            meta_data = MetaData(kwargs.pop(cfg.META_DATA, {}))

            if pre:
                kwargs[cfg.NAME_TOKENS] = name_tokens + getattr(cls_or_self, cfg.NAME_TOKENS)
                kwargs[cfg.META_DATA] = meta_data + getattr(cls_or_self, cfg.META_DATA)

            function_result = function(cls_or_self, *args, **kwargs)

            if not pre:
                cls_or_self.name_tokens.merge(name_tokens)
                cls_or_self.meta_data.merge(meta_data)

            if not 'Attribute' in repr(cls_or_self):
                MetaData.info('Adding to node %r, name_tokens: %s, meta_data: %s, pre: %s',
                              cls_or_self, name_tokens, meta_data, pre)
            return function_result

        return inner

    return outer
