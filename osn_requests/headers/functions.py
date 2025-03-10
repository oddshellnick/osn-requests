import random
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
