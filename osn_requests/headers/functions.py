import random
from typing import Optional


def sort_qualities(items: dict[str, Optional[float]]) -> dict[str, Optional[float]]:
	"""
	Sorts and shuffles a dictionary of items based on their quality values.

	This function takes a dictionary of items and their associated quality values, groups the items by quality,
	sorts these groups in descending order of quality, shuffles items within each quality group, and returns a new dictionary
	with the items ordered by quality groups and shuffled within each group.

	Args:
		items (dict[str, Optional[float]]): A dictionary where keys are item strings and values are their quality scores (floats between 0.0 and 1.0, or None).

	Returns:
		dict[str, Optional[float]]: A new dictionary with the same items, sorted by quality groups in descending order and shuffled within each group.
	"""
	groups = {}
	
	for item, quality in items.items():
		quality_str = f"{quality:.2f}" if isinstance(quality, float) else ""
	
		if quality_str not in groups:
			groups[quality_str] = [item]
		else:
			groups[quality_str].append(item)
	
	groups = dict(
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
	
	return {
		item: float(quality_str)
		if quality_str
		else None
		for quality_str, items_list in groups.items()
		for item in items_list
	}


def get_quality_string(item: str, quality: Optional[float]) -> str:
	"""
	Formats an item string with an optional quality value.

	This function takes an item string and an optional quality value and formats them into a string suitable for headers like Accept-Language or Accept-Encoding.
	If a quality value is provided, it is appended to the item string with the format "; q=quality".

	Args:
		item (str): The item string (e.g., "gzip").
		quality (Optional[float]): An optional quality value between 0.0 and 1.0. If None, no quality value is added.

	Returns:
		str: The formatted item string.
	"""
	return f"{item}; q={quality:.1f}" if quality is not None else item
