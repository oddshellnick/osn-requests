from osn_requests import get_req
from typing import (
	Callable,
	Optional,
	TypedDict,
	Union
)
from osn_requests.headers.user_agent import generate_random_user_agent_header
from osn_requests.headers.accept import generate_random_realistic_accept_header
from osn_requests.headers.accept_charset import generate_random_realistic_accept_charset_header
from osn_requests.headers.accept_encoding import generate_random_realistic_accept_encoding_header
from osn_requests.headers.accept_language import generate_random_realistic_accept_language_header


class Proxy(TypedDict):
	"""
	Type definition for a proxy dictionary.

	This TypedDict defines the structure of a proxy object, which includes the protocol, IP address, port, and country of the proxy server.

	Attributes:
	   protocol (str): The protocol used by the proxy (e.g., 'http', 'https', 'socks4', 'socks5').
	   ip (str): The IP address of the proxy server.
	   port (str): The port number the proxy server is listening on.
	   country (str): The country where the proxy server is located, represented by its ISO country code.
	"""
	protocol: str
	ip: str
	port: str
	country: str


def get_proxy_link(proxy: Proxy) -> str:
	"""
	Constructs a proxy link string from a Proxy dictionary.

	This function takes a Proxy dictionary and formats it into a string that can be used as a proxy URL in requests libraries.

	Args:
		proxy (Proxy): A dictionary containing proxy details.

	Returns:
		str: A string representing the proxy link in the format 'protocol://ip:port'.
	"""
	return f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"


def create_filter_function(parameters: Optional[Union[list[str], str]]) -> Callable[[str], bool]:
	"""
	Creates a filter function based on provided parameters.

	This function generates a callable filter that checks if a given string matches any of the provided parameters.
	It supports filtering against a single string, a list of strings, or no filter at all (None).

	Args:
		parameters (Optional[Union[list[str], str]]):  The parameters to filter against. Can be:
			- None: Returns a function that always returns True (no filtering).
			- str: Returns a function that checks if the input string is equal to this parameter.
			- list[str]: Returns a function that checks if the input string is present in this list.

	Returns:
		Callable[[str], bool]: A function that takes a string as input and returns True if it matches the filter criteria, False otherwise.

	Raises:
		TypeError: If the `parameters` argument is not None, str, or list[str].
	"""
	if isinstance(parameters, list):
		return lambda x: any(parameter == x for parameter in parameters)
	elif isinstance(parameters, str):
		return lambda x: parameters == x
	elif parameters is None:
		return lambda x: True
	else:
		raise TypeError(f"Expected None, str or list[str], got {type(parameters)}")


def get_free_proxies(
		protocol_filter: Optional[Union[str, list[str]]] = None,
		country_filter: Optional[Union[str, list[str]]] = None
) -> list[Proxy]:
	"""
	Fetches a list of free proxies, optionally filtered by protocol and country.

	This function retrieves a list of free proxies from a public API. It allows filtering the proxies based on the protocol they support (e.g., 'http', 'https') and the country of origin.

	Args:
		protocol_filter (Optional[Union[str, list[str]]]):  Filters proxies by protocol. Can be a single protocol string or a list of protocol strings. If None, no protocol filtering is applied.
		country_filter (Optional[Union[str, list[str]]]): Filters proxies by country. Can be a single country code (ISO) or a list of country codes. If None, no country filtering is applied.

	Returns:
		list[Proxy]: A list of Proxy dictionaries that match the specified filters. Each dictionary contains proxy details (protocol, ip, port, country).
	"""
	protocol_filter_function = create_filter_function(protocol_filter)
	country_filter_function = create_filter_function(country_filter)
	
	proxies = get_req(
			url="https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.json",
			headers={
				"Accept": generate_random_realistic_accept_header(),
				"Accept-Encoding": generate_random_realistic_accept_encoding_header(),
				"Accept-Charset": generate_random_realistic_accept_charset_header(),
				"Accept-Language": generate_random_realistic_accept_language_header(),
				"User-Agent": generate_random_user_agent_header()
			},
	).json()
	
	return [
		Proxy(
				protocol=proxy["protocol"],
				ip=proxy["ip"],
				port=proxy["port"],
				country=proxy["geolocation"]["country"]
		)
		for proxy in proxies
		if protocol_filter_function(proxy["protocol"])
		and country_filter_function(proxy["geolocation"]["country"])
	]
