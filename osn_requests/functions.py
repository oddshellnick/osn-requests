from typing import Optional
from osn_requests.types import RequestHeaders


def reformat_headers(headers: Optional[RequestHeaders]) -> Optional[dict[str, str]]:
	"""
	Reformats header keys by replacing underscores with hyphens.

	This function takes an optional dictionary of HTTP headers and reformats the keys to use hyphens instead of underscores.
	This is often necessary because HTTP headers traditionally use hyphens in their names (e.g., 'User-Agent'),
	while in Python, it's common to use underscores in variable names (e.g., 'user_agent').

	Args:
		headers (Optional[RequestHeaders]): An optional dictionary of HTTP headers.
			If None, the function returns None without modification.
			If a dictionary, it should have string keys and string values.

	Returns:
		Optional[dict[str, str]]: A dictionary with reformatted header keys (underscores replaced by hyphens), or None if the input `headers` was None.

	Raises:
		TypeError: If the input `headers` is not a dictionary or None, or if keys or values within the headers dictionary are not strings.
	"""
	if headers is None:
		return headers
	
	if isinstance(headers, dict):
		reformatted_headers = {}
	
		for key, value in headers.items():
			if not isinstance(key, str) and not isinstance(value, str):
				raise TypeError("Keys and values in headers dictionary must be strings.")
	
			reformatted_headers[key.replace("_", "-")] = value
	
		return reformatted_headers
	
	raise TypeError("Headers must be a dictionary or None.")
