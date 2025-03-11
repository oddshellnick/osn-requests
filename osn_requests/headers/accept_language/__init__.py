import random
from typing import Optional
from osn_requests.headers.accept_language.data import Languages
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


def generate_random_realistic_accept_language_header(
		necessary_languages: necessary_quality_values = None,
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a realistic random Accept-Language header string.

	This function creates an Accept-Language header string that is representative of common browser accept headers.
	It selects language codes from a curated list of common languages and assigns them realistic quality values.

	Args:
		necessary_languages (Optional[Union[str, QualityValue, list[Union[str, QualityValue]]]]): Languages that must be included in the header.
		fixed_len (Optional[int]): If provided, the header will contain exactly this many language codes (including "*").
		max_len (Optional[int]): The maximum number of language codes to include in the header. Used if `fixed_len` is None. Defaults to the length of the common languages list.
		min_len (int): The minimum number of language codes to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a realistic random Accept-Language header.
	"""
	languages = build_start_quality_values(necessary_languages)
	
	languages_list = list(set(Languages.common) - set(map(lambda a: a["name"], languages)))
	num_choices = calculate_num_choices(
			list_len=len(languages_list),
			fixed_len=fixed_len,
			min_len=min_len,
			max_len=max_len
	)
	
	languages += [
		QualityValue(
				name=choice,
				quality=random.uniform(0.3, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.sample(languages_list, k=num_choices)
	]
	
	languages = sort_qualities(languages)
	
	languages.append(QualityValue(name="*", quality=0.1))
	
	return ", ".join(get_quality_string(language) for language in languages)


def generate_random_accept_language_header(
		necessary_languages: necessary_quality_values = None,
		fixed_len: Optional[int] = None,
		max_len: Optional[int] = None,
		min_len: int = 0
) -> str:
	"""
	Generates a random Accept-Language header string.

	This function creates a random Accept-Language header string by selecting language codes from a comprehensive list and assigning them random quality values.

	Args:
		necessary_languages (Optional[Union[str, QualityValue, list[Union[str, QualityValue]]]]): Languages that must be included in the header.
		fixed_len (Optional[int]): If provided, the header will contain exactly this many language codes (including "*").
		max_len (Optional[int]): The maximum number of language codes to include in the header. Used if `fixed_len` is None. Defaults to the length of the all languages list.
		min_len (int): The minimum number of language codes to include in the header. Used if `fixed_len` is None. Defaults to 0.

	Returns:
		str: A string representing a random Accept-Language header.
	"""
	languages = build_start_quality_values(necessary_languages)
	
	languages_list = list(set(Languages.all) - set(map(lambda a: a["name"], languages)))
	num_choices = calculate_num_choices(
			list_len=len(languages_list),
			fixed_len=fixed_len,
			min_len=min_len,
			max_len=max_len
	)
	
	languages = [
		QualityValue(
				name=choice,
				quality=random.uniform(0.0, 1.0)
				if random.choice([True, False])
				else None
		)
		for choice in random.sample(languages_list, k=num_choices)
	]
	random.shuffle(languages)
	
	languages.append(QualityValue(name="*", quality=0.1))
	
	return ", ".join(get_quality_string(language) for language in languages)
