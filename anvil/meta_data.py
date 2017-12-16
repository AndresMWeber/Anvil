from six import string_types, iteritems


class MetaData(object):
    def __init__(self, *input_dicts, **meta_data_kwargs):
        self.protected_fields = self._cast_input_to_list(meta_data_kwargs.pop('protected_fields', None))
        self.data = self.merge_dicts(*input_dicts, **meta_data_kwargs)

    @staticmethod
    def merge_dicts(*input_dicts, **input_kwargs):
        """ Merges metadata for every dict that has been input.  Starts with dict args then input kwargs
            Overwrites data if there are conflicts from left to right.

        :param protected_fields: list, fields that the metadata should keep and ignore on merge.
        :param input_dicts: (dict), tuple of input dictionaries
        :param input_kwargs: dict, input kwargs to merge
        :return: dict, combined data.
        """
        ignore_keys = input_kwargs.pop('ignore_keys', None) or []
        data = {}

        for input_dict in [d for d in input_dicts if isinstance(d, dict)] + [input_kwargs]:
            for key in ignore_keys:
                try:
                    input_dict.pop(key)
                except KeyError:
                    pass
            data.update(input_dict)
        return data

    def merge(self, *input_dicts, **input_kwargs):
        ignore_keys = self._cast_input_to_list(input_kwargs.pop('ignore_keys', None)) + self.protected_fields
        keep_originals = self._cast_input_to_list(input_kwargs.pop('keep_originals', False))
        if keep_originals:
            ignore_keys = ignore_keys + list(self.data)
        self.data.update(self.merge_dicts(ignore_keys=ignore_keys,
                                          *input_dicts,
                                          **input_kwargs))

    def serialize(self, ignore_keys=None):
        ignore_fields = self._cast_input_to_list(ignore_keys)
        try:
            return '{%s}' % (', '.join(['%s: %s' % (str(key), str(value)) for key, value in iteritems(self.data) if
                                        key not in ignore_fields]))
        except:
            raise UnicodeError('Could not cast metadata to string for metadata %s' % self.data)

    def copy_dict_as_strings(self):
        data = {}
        for k, v in iteritems(self.data):
            try:
                data.update({str(k): str(v)})
            except:
                pass
        return data

    @staticmethod
    def _cast_input_to_list(string_or_none_or_list):
        if not isinstance(string_or_none_or_list, list):
            string_or_none_or_list = []

        elif isinstance(string_or_none_or_list, string_types):
            string_or_none_or_list = [string_or_none_or_list]

        return string_or_none_or_list

    def keys(self):
        return list(self.data)

    @staticmethod
    def dict_compare(d1, d2):
        """ Taken from: https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python
        """
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        intersect_keys = d1_keys.intersection(d2_keys)
        added = d1_keys - d2_keys
        removed = d2_keys - d1_keys
        modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
        same = set(o for o in intersect_keys if d1[o] == d2[o])
        return added, removed, modified, same

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.merge_dicts(self.data, other.data, ignore_keys=None)
        if isinstance(other, dict):
            return self.merge_dicts(self.data, other, ignore_keys=None)
        else:
            raise ValueError('Addition for %s and %s types unsupported.' % (self.__class__, type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __getattr__(self, item):
        """ Delegate to the data field so we can access all metadata with dot notation.
        """
        try:
            super(MetaData, self).__getattribute__('data')[item]
        except (AttributeError, KeyError):
            super(MetaData, self).__getattribute__(item)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(list(self.data))

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other = other.data
        if isinstance(other, dict):
            return self.dict_compare(self.data, other)
        return False
