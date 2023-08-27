"""
The Sims 4 Community Library is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Set, Dict

from sims4communitylib.enums.enumtypes.common_int import CommonInt
from sims4communitylib.enums.enumtypes.common_versioned_values_mixin import CommonVersionedValuesMixin


class CommonVersionedInt(CommonInt, CommonVersionedValuesMixin):
    """Integer, but with a version."""

    @classmethod
    def get_version(cls) -> str:
        """The version of the enum. If this changes, it means values have changed and should be updated."""
        raise NotImplementedError()

    @classmethod
    def is_obsolete_value(cls, value: 'CommonVersionedInt') -> bool:
        """Determine if a value is considered to be obsolete."""
        return value in cls.get_obsolete_values()

    @classmethod
    def get_obsolete_values(cls) -> Set['CommonVersionedInt']:
        """Retrieve a set of values considered as obsolete."""
        raise NotImplementedError()

    @classmethod
    def _get_obsolete_conversion_mapping(cls) -> Dict['CommonVersionedInt', 'CommonVersionedInt']:
        """_get_obsolete_conversion_mapping()

        Retrieve a mapping of obsolete values into non-obsolete values.

        :return: A mapping of obsolete values into non-obsolete values.
        :type: Dict[CommonVersionedInt, CommonVersionedInt]
        """
        raise NotImplementedError()

    @classmethod
    def convert_obsolete_value(cls, value: 'CommonVersionedInt') -> 'CommonVersionedInt':
        """convert_obsolete_value(value)

        Convert an obsolete value to its new equivalent, if there is one.


        """
        mapping: Dict[CommonVersionedInt, CommonVersionedInt] = cls._get_obsolete_conversion_mapping()
        convert_value = mapping.get(value, value)
        if convert_value == value:
            return convert_value
        return cls.convert_obsolete_value(convert_value)
