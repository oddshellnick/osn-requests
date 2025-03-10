from typing import (
	Optional,
	TypedDict,
	Union
)


class QualityValue(TypedDict):
	"""
	Represents an item with an associated quality value.

	This TypedDict is used to define the structure for items that have a name and an optional quality value, often used in HTTP headers like Accept, Accept-Language, etc.

	Attributes:
	   name (str): The name of the item, such as a mime type, charset, or language code.
	   quality (Optional[float]): An optional quality value associated with the item, ranging from 0.0 to 1.0. A higher value indicates a higher preference. If None, it implies the highest preference.
	"""
	name: str
	quality: Optional[float]

necessary_quality_value = Union[str, QualityValue]
necessary_quality_values = Optional[Union[necessary_quality_value, list[necessary_quality_value]]]
