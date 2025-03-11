import random
from typing import Any, Optional
from osn_requests.headers.types import (
	QualityValue,
	necessary_quality_values
)


def sort_qualities(values: list[QualityValue]) -> list[QualityValue]:
	"""
	Sorts and shuffles a list of QualityValue items based on their quality values.

	This function takes a list of QualityValue dictionaries, groups them by quality,
	sorts these groups in descending order of quality, shuffles items within each quality group,
	and returns a new list with the QualityValue items ordered by quality groups and shuffled within each group.

	Args:
		values (list[QualityValue]): A list of QualityValue dictionaries.

	Returns:
		list[QualityValue]: A new list of QualityValue dictionaries, sorted by quality groups in descending order and shuffled within each group.
	"""
	groups = {}
	
	for value in values:
		quality_str = f"{value['quality']:.1f}" if isinstance(value["quality"], float) else ""
	
		if quality_str not in groups:
			groups[quality_str] = [value]
		else:
			groups[quality_str].append(value)
	
	groups: dict[str, list[QualityValue]] = dict(
			sorted(
					groups.items(),
					key=lambda item_: float(item_[0])
					if item_[0]
					else 2.0,
					reverse=True
			)
	)
	
	for quality_str, items_list in groups.items():
		random.shuffle(items_list)
	
	return [
		QualityValue(name=item["name"], quality=item["quality"])
		for quality_str, items_list in groups.items()
		for item in items_list
	]


def get_quality_string(value: QualityValue) -> str:
	"""
	Formats a QualityValue item into a string representation with an optional quality value.

	This function takes a QualityValue dictionary and formats it into a string suitable for headers like Accept-Language or Accept-Encoding.
	If a quality value is provided, it is appended to the item name with the format "; q=quality".

	Args:
		value (QualityValue): A QualityValue dictionary.

	Returns:
		str: The formatted string representation of the QualityValue item.
	"""
	return f"{value['name']}; q={value['quality']:.1f}" if value["quality"] is not None else value["name"]


def calculate_num_choices(
		list_len: int,
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> int:
	"""
	Calculates the number of choices to be made, considering fixed, maximum, and minimum lengths.

	This function determines the number of items to be chosen from a list, based on the provided length constraints.
	It allows specifying a fixed number of choices, or a range with minimum and maximum limits.
	If `fixed_len` is provided, the function returns the minimum of `fixed_len` and `list_len`.
	If `fixed_len` is None, it generates a random number of choices between `min_len` and `max_len` (or `list_len` if `max_len` is None), ensuring the result is within the bounds of `list_len`.

	Args:
		list_len (int): The total length of the list from which choices are to be made.
		fixed_len (Optional[int]): If provided, the function will attempt to return exactly this number of choices. If `fixed_len` is greater than `list_len`, it will return `list_len`.
		max_len (Optional[int]): The maximum number of choices to be made. Used only when `fixed_len` is None. If None, the maximum number of choices defaults to `list_len`.
		min_len (int): The minimum number of choices to be made. Used only when `fixed_len` is None. Defaults to 0.

	Returns:
		int: The calculated number of choices.
	"""
	if fixed_len is None:
		min_choices = min_len
		max_choices = list_len if max_len is None else min(max_len, list_len)
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, list_len)
	
	return num_choices


def is_quality_value(value: Any) -> bool:
	"""
	Checks if a given value is a valid QualityValue dictionary.

	This function validates whether the input `value` conforms to the structure of a QualityValue TypedDict.
	It checks if the value is a dictionary, if it contains all the required keys ('name', 'quality') as defined in QualityValue,
	and if the types of the values associated with these keys match the expected types (str for 'name', Optional[float] for 'quality').

	Args:
		value (Any): The value to be checked.

	Returns:
		bool: True if the value is a valid QualityValue dictionary, False otherwise.
	"""
	if not isinstance(value, dict):
		return False
	
	quality_value_keys = QualityValue.__annotations__
	
	if not (
			all(
					key in value.keys()
					and isinstance(value[key], type_)
					for key, type_ in quality_value_keys.items()
			)
			and len(value) == len(quality_value_keys)
	):
		return False
	
	return True


def build_start_quality_values(values: necessary_quality_values) -> list[QualityValue]:
	"""
	Builds a list of QualityValue items from various input types.

	This function takes an optional input `values` and converts it into a list of `QualityValue` items.
	It supports handling `None`, a single string, a single `QualityValue` dictionary, or a list of strings or `QualityValue` dictionaries as input.
	This ensures a consistent output format for further processing of quality values.

	Args:
		values (necessary_quality_values): The input value to be converted into a list of `QualityValue` items.
			It can be one of the following:
				- `None`: Returns an empty list.
				- `str`: A single string representing the 'name' of a `QualityValue` with no specified quality. Returns a list containing a single `QualityValue` with the given name and `quality=None`.
				- `QualityValue`: A single `QualityValue` dictionary. Returns a list containing this single `QualityValue`.
				- `list[Union[str, QualityValue]]`: A list where each element can be either a string (name of `QualityValue`) or a `QualityValue` dictionary. Returns a list of `QualityValue` dictionaries. Strings in the list are converted to `QualityValue` with `quality=None`.

	Returns:
		list[QualityValue]: A list of `QualityValue` dictionaries.

	Raises:
		ValueError: If the provided type of `values` argument is not supported.
	"""
	if values is None:
		return []
	elif isinstance(values, str):
		return [QualityValue(name=values, quality=None)]
	elif is_quality_value(values):
		return [values]
	elif isinstance(values, list) and all(isinstance(value, str) or is_quality_value(value) for value in values):
		return [
			QualityValue(name=value, quality=None)
			if isinstance(value, str)
			else value
			for value in values
		]
	else:
		raise ValueError(
				"Invalid value for 'values'. Must be a QualityValue or a list of QualityValue dictionaries."
		)
