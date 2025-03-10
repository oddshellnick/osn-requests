import random
from typing import Optional
from osn_requests.headers.types import QualityValue
from osn_requests.headers.accept.data import MimeTypes
from osn_var_tools.python_instances_tools import get_class_attributes
from osn_requests.headers.functions import (
	get_quality_string,
	sort_qualities
)


def generate_random_realistic_accept_header(
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a realistic random Accept header string.

	This function creates an Accept header string that is representative of common browser accept headers.
	It selects MIME types from a curated list of common types across different categories (application, audio, image, video, text) and assigns them realistic quality values.

	Args:
		fixed_len (Optional[int]): If provided, the header will contain exactly this many MIME types (including "*/*").
		max_len (Optional[int]): The maximum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to the length of the common MIME types list.
		min_len (int): The minimum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a realistic random Accept header.
	"""
	mime_types = [QualityValue(name="text/html", quality=None)]
	
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
	
	if fixed_len is None:
		min_choices = min_len
		max_choices = len(mime_types_list) if max_len is None else min(max_len, len(mime_types_list))
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, len(mime_types_list))
	
	mime_types += [
		QualityValue(
				name=choice,
				quality=random.uniform(0.7, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.choices(mime_types_list, k=num_choices)
	]
	
	mime_types = sort_qualities(mime_types)
	
	mime_types.append(QualityValue(name="*/*", quality=0.1))
	
	return ", ".join(get_quality_string(mime_type) for mime_type in mime_types)


def generate_random_accept_header(
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a random Accept header string.

	This function creates a random Accept header string by selecting MIME types from a comprehensive list of all available types, and assigning them random quality values.

	Args:
		fixed_len (Optional[int]): If provided, the header will contain exactly this many MIME types (including "*/*").
		max_len (Optional[int]): The maximum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to the length of the all MIME types list.
		min_len (int): The minimum number of MIME types to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a random Accept header.
	"""
	mime_types_list = []
	for attribute in get_class_attributes(MimeTypes, contains_exclude=["__", "common"]).keys():
		mime_types_list += getattr(MimeTypes, attribute)
	
	if fixed_len is None:
		min_choices = min_len
		max_choices = len(mime_types_list) if max_len is None else min(max_len, len(mime_types_list))
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, len(mime_types_list))
	
	mime_types = [
		QualityValue(
				name=choice,
				quality=random.uniform(0.0, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.choices(mime_types_list, k=num_choices)
	]
	random.shuffle(mime_types)
	
	mime_types.append(QualityValue(name="*/*", quality=0.1))
	
	return ", ".join(get_quality_string(mime_type) for mime_type in mime_types)
