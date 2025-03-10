import random
from typing import Optional
from osn_requests.headers.accept.data import MimeTypes
from osn_var_tools.python_instances_tools import get_class_attributes
from osn_requests.headers.types import (
	QualityValue,
	necessary_quality_values
)
from osn_requests.headers.functions import (
	build_start_quality_values,
	calculate_num_choices,
	get_quality_string,
	sort_qualities
)


def generate_random_realistic_accept_header(
		necessary_mime_types: necessary_quality_values = None,
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a realistic random Accept header string.

	This function creates an Accept header string that is representative of common browser accept headers.
	It selects MIME types from a curated list of common types across different categories (application, audio, image, video, text) and assigns them realistic quality values.

	Args:
		necessary_mime_types (necessary_quality_values):  MIME types that must be included in the header.
		fixed_len (Optional[int]): If provided, the header will contain exactly this many MIME types (including "*/*").
		max_len (Optional[int]): The maximum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to the length of the common MIME types list.
		min_len (int): The minimum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a realistic random Accept header.
	"""
	mime_types = build_start_quality_values(necessary_mime_types)
	
	for mime_type in ["text/html"]:
		if mime_type not in [a["name"] for a in mime_types]:
			mime_types.append(QualityValue(name=mime_type, quality=None))
	
	mime_types_list = []
	for attribute in [
		"application_common",
		"audio_common",
		"image_common",
		"video_common",
		"text_common"
	]:
		mime_types_list += getattr(MimeTypes, attribute)
	
	mime_types_list = list(set(mime_types_list) - set(map(lambda a: a["name"], mime_types)))
	num_choices = calculate_num_choices(
			list_len=len(mime_types_list),
			fixed_len=fixed_len,
			min_len=min_len,
			max_len=max_len
	)
	
	mime_types += [
		QualityValue(
				name=choice,
				quality=random.uniform(0.7, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.sample(mime_types_list, k=num_choices)
	]
	
	mime_types = sort_qualities(mime_types)
	
	mime_types.append(QualityValue(name="*/*", quality=0.1))
	
	return ", ".join(get_quality_string(mime_type) for mime_type in mime_types)


def generate_random_accept_header(
		necessary_mime_types: necessary_quality_values = None,
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a random Accept header string.

	This function creates a random Accept header string by selecting MIME types from a comprehensive list of all available types, and assigning them random quality values.

	Args:
		necessary_mime_types (necessary_quality_values): MIME types that must be included in the header.
		fixed_len (Optional[int]): If provided, the header will contain exactly this many MIME types (including "*/*").
		max_len (Optional[int]): The maximum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to the length of the all MIME types list.
		min_len (int): The minimum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a random Accept header.
	"""
	mime_types = build_start_quality_values(necessary_mime_types)
	
	mime_types_list = []
	for attribute in get_class_attributes(MimeTypes, contains_exclude=["__", "common"]).keys():
		mime_types_list += getattr(MimeTypes, attribute)
	
	mime_types_list = list(set(mime_types_list) - set(map(lambda a: a["name"], mime_types)))
	num_choices = calculate_num_choices(
			list_len=len(mime_types_list),
			fixed_len=fixed_len,
			min_len=min_len,
			max_len=max_len
	)
	
	mime_types += [
		QualityValue(
				name=choice,
				quality=random.uniform(0.0, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.sample(mime_types_list, k=num_choices)
	]
	random.shuffle(mime_types)
	
	mime_types.append(QualityValue(name="*/*", quality=0.1))
	
	return ", ".join(get_quality_string(mime_type) for mime_type in mime_types)
