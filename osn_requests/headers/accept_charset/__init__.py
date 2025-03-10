import random
from typing import Optional
from osn_requests.headers.accept_charset.data import Charsets


def get_string(charset: str, quality: Optional[float]) -> str:
	"""
	Formats a charset string with an optional quality value.

	This function takes a charset and an optional quality value and formats them into a string suitable for an Accept-Charset header.
	If a quality value is provided, it is appended to the charset string with the format "; q=quality".

	Args:
		charset (str): The charset string (e.g., "utf-8").
		quality (Optional[float]): An optional quality value between 0.0 and 1.0. If None, no quality value is added.

	Returns:
		str: The formatted charset string.
	"""
	return f"{charset}; q={quality:.1f}" if quality is not None else charset


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
	charsets = {"utf-8": None, "ascii": None}
	
	charsets_list = list(set(Charsets.common) - set(charsets.keys()))
	
	if fixed_len is None:
		min_choices = min_len
		max_choices = len(charsets_list) if max_len is None else min(max_len, len(charsets_list))
	
		num_choices = random.randint(min_choices, max_choices)
	else:
		num_choices = min(fixed_len, len(charsets_list))
	
	chosen = {
		choice: (random.uniform(0.7, 1.0) if random.choice([True, False]) else None)
		for choice in random.choices(charsets_list, k=num_choices)
	}
	random.shuffle(list(chosen.items()))
	charsets.update(chosen)
	
	charsets["*"] = 0.1
	
	return ", ".join(get_string(charset, quality) for charset, quality in charsets.items())


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
	
	charsets = {
		choice: (random.uniform(0.0, 1.0) if random.choice([True, False]) else None)
		for choice in random.choices(charsets_list, k=num_choices)
	}
	random.shuffle(list(charsets.items()))
	
	charsets["*"] = 0.1
	
	return ", ".join(get_string(charset, quality) for charset, quality in charsets.items())
