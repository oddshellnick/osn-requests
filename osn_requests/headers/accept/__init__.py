import random
from typing import Optional
from osn_requests.headers.accept.data import MimeTypes
from osn_var_tools.python_instances_tools import get_class_attributes


def get_string(mime_type: str, quality: Optional[float]) -> str:
	"""
	Formats a MIME type string with an optional quality value.

	This function takes a MIME type and an optional quality value and formats them into a string suitable for an Accept header.
	If a quality value is provided, it is appended to the MIME type string with the format "; q=quality".

	Args:
		mime_type (str): The MIME type string (e.g., "text/html").
		quality (Optional[float]): An optional quality value between 0.0 and 1.0. If None, no quality value is added.

	Returns:
		str: The formatted MIME type string.
	"""
	return f"{mime_type}; q={quality:.1f}" if quality is not None else mime_type


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
	mime_types_list = []
	for attribute in [
		"application_common",
		"audio_common",
		"image_common",
		"video_common",
		"text_common"
	]:
		mime_types_list += getattr(MimeTypes, attribute)
	
	if fixed_len is None:
		min_choices = min_len
		max_choices = len(mime_types_list) if max_len is None else min(max_len, len(mime_types_list))
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, len(mime_types_list))
	
	mime_types = {
		choice: (random.uniform(0.7, 1.0) if random.choice([True, False]) else None)
		for choice in random.choices(mime_types_list, k=num_choices)
	}
	random.shuffle(list(mime_types.items()))
	
	mime_types["*/*"] = 0.1
	
	return ", ".join(
			get_string(mime_type, quality)
			for mime_type, quality in mime_types.items()
	)


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
	
	mime_types = {
		choice: (random.uniform(0.0, 1.0) if random.choice([True, False]) else None)
		for choice in random.choices(mime_types_list, k=num_choices)
	}
	random.shuffle(list(mime_types.items()))
	
	mime_types["*/*"] = 0.1
	
	return ", ".join(
			get_string(mime_type, quality)
			for mime_type, quality in mime_types.items()
	)
