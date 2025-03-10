import random
from typing import Optional
from osn_requests.headers.types import QualityValue
from osn_requests.headers.accept_encoding.data import Encodings
from osn_requests.headers.functions import (
	calculate_num_choices,
	get_quality_string,
	sort_qualities
)


def generate_random_realistic_accept_encoding_header(
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a realistic random Accept-Encoding header string.

	This function creates an Accept-Encoding header string that is representative of common browser accept headers.
	It selects encoding types from a predefined list and assigns them realistic quality values, prioritizing more common encodings.

	Args:
		fixed_len (Optional[int]): If provided, the header will contain exactly this many encoding types.
		max_len (Optional[int]): The maximum number of encoding types to include in the header. Used if `fixed_len` is None. Defaults to the length of the encoding list.
		min_len (int): The minimum number of encoding types to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a realistic random Accept-Encoding header.
	"""
	encodings_list = Encodings.all
	num_choices = calculate_num_choices(
			list_len=len(encodings_list),
			fixed_len=fixed_len,
			min_len=min_len,
			max_len=max_len
	)
	
	encodings = [
		QualityValue(
				name=choice,
				quality=random.uniform(0.7, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.sample(encodings_list, k=num_choices)
	]
	
	encodings = sort_qualities(encodings)
	
	encodings.append(QualityValue(name="*", quality=0.1))
	
	return ", ".join(get_quality_string(encoding) for encoding in encodings)


def generate_random_accept_encoding_header(
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a random Accept-Encoding header string.

	This function creates a random Accept-Encoding header string by selecting encoding types from a predefined list and assigning them random quality values.

	Args:
		fixed_len (Optional[int]): If provided, the header will contain exactly this many encoding types.
		max_len (Optional[int]): The maximum number of encoding types to include in the header. Used if `fixed_len` is None. Defaults to the length of the encoding list.
		min_len (int): The minimum number of encoding types to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a random Accept-Encoding header.
	"""
	encodings_list = Encodings.all
	num_choices = calculate_num_choices(
			list_len=len(encodings_list),
			fixed_len=fixed_len,
			min_len=min_len,
			max_len=max_len
	)
	
	encodings = [
		QualityValue(
				name=choice,
				quality=random.uniform(0.0, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.sample(encodings_list, k=num_choices)
	]
	random.shuffle(encodings)
	
	encodings.append(QualityValue(name="*", quality=0.1))
	
	return ", ".join(get_quality_string(encoding) for encoding in encodings)
