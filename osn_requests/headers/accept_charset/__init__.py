import random
from typing import Optional
from osn_requests.headers.types import QualityValue
from osn_requests.headers.accept_charset.data import Charsets
from osn_requests.headers.functions import (
	get_quality_string,
	sort_qualities
)


def generate_random_realistic_accept_charset_header(
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a realistic random Accept-Charset header string.

	This function creates an Accept-Charset header string that resembles realistic browser headers.
	It includes "utf-8" and "ascii" by default and randomly selects additional charsets from a common list, assigning them optional quality values.

	Args:
		fixed_len (Optional[int]): If provided, the header will contain exactly this many charsets (including "utf-8" and "ascii").
		max_len (Optional[int]): The maximum number of charsets to include in the header. Used if `fixed_len` is None. Defaults to the length of the common charset list.
		min_len (int): The minimum number of charsets to include in the header.  Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a random Accept-Charset header.
	"""
	charsets = [
		QualityValue(name="utf-8", quality=None),
		QualityValue(name="ascii", quality=None)
	]
	
	charsets_list = list(set(Charsets.common) - set(map(lambda a: a["name"], charsets)))
	
	if fixed_len is None:
		min_choices = min_len
		max_choices = len(charsets_list) if max_len is None else min(max_len, len(charsets_list))
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, len(charsets_list))
	
	charsets += [
		QualityValue(
				name=choice,
				quality=random.uniform(0.7, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.choices(charsets_list, k=num_choices)
	]
	
	charsets = sort_qualities(charsets)
	
	charsets.append(QualityValue(name="*", quality=0.1))
	
	return ", ".join(get_quality_string(charset) for charset in charsets)


def generate_random_accept_charset_header(
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a random Accept-Charset header string.

	This function creates a random Accept-Charset header string by selecting charsets from a comprehensive list and assigning them random quality values.

	Args:
		fixed_len (Optional[int]): If provided, the header will contain exactly this many charsets.
		max_len (Optional[int]): The maximum number of charsets to include in the header. Used if `fixed_len` is None. Defaults to the length of the all charset list.
		min_len (int): The minimum number of charsets to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a random Accept-Charset header.
	"""
	charsets_list = Charsets.all
	
	if fixed_len is None:
		min_choices = min_len
		max_choices = len(charsets_list) if max_len is None else min(max_len, len(charsets_list))
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, len(charsets_list))
	
	charsets = [
		QualityValue(
				name=choice,
				quality=random.uniform(0.0, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.choices(charsets_list, k=num_choices)
	]
	random.shuffle(charsets)
	
	charsets.append(QualityValue(name="*", quality=0.1))
	
	return ", ".join(get_quality_string(charset) for charset in charsets)
