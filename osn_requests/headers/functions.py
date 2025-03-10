import random
from typing import Optional
from osn_requests.headers.types import QualityValue


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
