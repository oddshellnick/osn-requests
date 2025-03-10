import re
import random
from typing import (
	Optional,
	Sequence,
	Union
)
from osn_requests.headers.user_agent.data_types import (
	supported_ua_browsers,
	supported_ua_engines
)
from osn_requests.headers.user_agent.errors import (
	UnsupportedBrowserError,
	UnsupportedEngineError
)
from osn_requests.headers.user_agent.data import (
	UserAgentBrowser,
	UserAgentEngine,
	UserAgentSupportedParts
)


def create_browser_version_from_parts(parts: list[Union[int, list[int]]], drop_last_zero: bool = False) -> str:
	"""
	Creates a browser version string from a list of parts.

	This function generates a browser version string by combining a list of integer or range parts.
	If a part is a range, it selects a random value within that range.
	It can optionally drop the last part if it is 0 with a certain probability.

	Args:
		parts (list[Union[int, list[int]]]): List of parts for the version string.
		drop_last_zero (bool): If True, last part can be dropped if it's 0.

	Returns:
		str: The generated browser version string.
	"""
	browser_version = [
		str(part)
		if isinstance(part, int)
		else str(random.choice(part))
		for part in parts
	]
	
	if drop_last_zero and browser_version[-1] == 0 and random.choice([True, False]):
		browser_version.pop(-1)
	
	return ".".join(browser_version)


def generate_yandex_ua() -> str:
	"""
	Generates a Yandex browser user agent string.

	Returns:
		str: Yandex browser user agent string.
	"""
	yandex_version = create_browser_version_from_parts(UserAgentBrowser.yandex_versions)
	return f"YaBrowser/{yandex_version}"


def generate_edge_ua() -> str:
	"""
	Generates an Edge browser user agent string.

	Returns:
		str: Edge browser user agent string.
	"""
	edge_version = create_browser_version_from_parts(UserAgentBrowser.edge_versions)
	return f"Edg/{edge_version}"


def generate_opera_ua() -> str:
	"""
	Generates an Opera browser user agent string.

	Returns:
		str: Opera browser user agent string.
	"""
	opera_version = create_browser_version_from_parts(UserAgentBrowser.opera_versions)
	return f"Opera/{opera_version}"


def generate_firefox_ua() -> str:
	"""
	Generates a Firefox browser user agent string.

	Returns:
		str: Firefox browser user agent string.
	"""
	firefox_version = create_browser_version_from_parts(UserAgentBrowser.firefox_versions, True)
	return f"Firefox/{firefox_version}"


def add_safari_version(current_versions: list[str], possible_versions: list[Sequence]) -> list[str]:
	"""
	Recursively adds or modifies Safari version parts.

	This function takes a list of existing Safari version parts, a list of possible version parts at each level,
	a current level, and a boolean indicating whether the previous level was changed.
	It recursively modifies or adds version parts based on the possible versions.

	Args:
		current_versions (list[str]): A list of current version parts.
		possible_versions (list[Sequence]): A list of possible version parts at each level.

	Returns:
		list[str]: Modified list of version parts.
	"""
	previous_level_changed = False
	
	for i in range(len(possible_versions)):
		if previous_level_changed:
			current_versions[i] = str(random.choice(possible_versions[i]))
	
			if random.choice([True, False]):
				break
		else:
			previous_version = current_versions[i]
	
			current_versions[i] = str(random.randint(int(current_versions[i]), max(possible_versions[i])))
	
			previous_level_changed = previous_version != current_versions[i]
	
	return current_versions


def generate_safari_ua(engine_ua: Optional[str] = None) -> str:
	"""
	Generates a Safari browser user agent string.

	This function generates a Safari user agent string, optionally using an existing AppleWebKit version
	from a given engine user agent string.

	Args:
		engine_ua (typing.Optional[str]): An optional engine user agent string, from which to extract AppleWebKit version.

	Returns:
		str: Safari browser user agent string.
	"""
	if engine_ua is None or re.search(r"AppleWebKit/(\d+(?:\.\d+)*)", engine_ua) is None:
		version_parts = []
	
		for i in range(len(UserAgentEngine.apple_webkit_versions)):
			version_parts.append(str(random.choice(UserAgentEngine.apple_webkit_versions[i])))
	
			if random.choice([True, False]):
				break
	
		safari_version = ".".join(version_parts)
	else:
		webkit_version: list[str] = re.search(r"AppleWebKit/(\d+(?:\.\d+)*)", engine_ua).group(1).split(".")
		webkit_version = add_safari_version(webkit_version, UserAgentBrowser.safari_versions)
	
		safari_version = ".".join(webkit_version)
	
	return f"Safari/{safari_version}"


def generate_chrome_ua() -> str:
	"""
	Generates a Chrome browser user agent string.

	Returns:
		str: Chrome browser user agent string.
	"""
	chrome_version = create_browser_version_from_parts(UserAgentBrowser.chrome_versions)
	return f"Chrome/{chrome_version}"


def generate_random_browser_ua(
		browser_to_generate: Optional[supported_ua_browsers] = None,
		engine: Optional[supported_ua_engines] = None,
		engine_ua: Optional[str] = None
) -> tuple[str, str]:
	"""
	Generates a random browser user agent string.

	This function creates a user agent string for a specific browser, or a randomly chosen browser if none is provided.
	It also supports generating user agent strings based on a given engine.

	Args:
		browser_to_generate (Optional[supported_ua_browsers]): The browser for which to generate the user agent. If None, a random browser will be selected.
		engine (Optional[supported_ua_engines]): The engine to base the browser choice on.  This can influence the selection of the browser if `browser_to_generate` is None.
		engine_ua (Optional[str]): An optional engine user agent string, specifically used for Safari version generation.

	Returns:
		tuple[str, str]: A tuple containing: the generated user agent string (str), the name of the browser used to generate the user agent (str).

	Raises:
		UnsupportedBrowserError: If the provided browser_to_generate is not supported.
		UnsupportedEngineError: If the provided engine is not supported.
	"""
	if engine is not None and engine not in UserAgentSupportedParts.engine:
		raise UnsupportedEngineError(engine)
	
	if browser_to_generate is None:
		if engine is None:
			browser_to_generate = random.choice(UserAgentSupportedParts.browser)
		elif engine == "AppleWebKit":
			browser_to_generate = random.choice(UserAgentSupportedParts.apple_webkit_browsers)
		elif engine == "Blink":
			browser_to_generate = random.choice(UserAgentSupportedParts.blink_browsers)
		elif engine == "Gecko":
			browser_to_generate = random.choice(UserAgentSupportedParts.gecko_browsers)
	
	if browser_to_generate == "Chrome":
		chrome_ua = generate_chrome_ua()
		safari_ua = generate_safari_ua(engine_ua)
	
		return " ".join(list(filter(None, [chrome_ua, safari_ua]))), browser_to_generate
	elif browser_to_generate == "Firefox":
		return generate_firefox_ua(), browser_to_generate
	elif browser_to_generate == "Safari":
		return generate_safari_ua(engine_ua), browser_to_generate
	elif browser_to_generate == "Opera":
		chrome_ua = generate_chrome_ua()
		opera_ua = generate_opera_ua()
		safari_ua = generate_safari_ua(engine_ua)
	
		return " ".join(list(filter(None, [chrome_ua, opera_ua, safari_ua]))), browser_to_generate
	elif browser_to_generate == "Edge":
		chrome_ua = generate_chrome_ua()
		edge_ua = generate_edge_ua()
		safari_ua = generate_safari_ua(engine_ua)
	
		return " ".join(list(filter(None, [chrome_ua, edge_ua, safari_ua]))), browser_to_generate
	elif browser_to_generate == "Yandex":
		chrome_ua = generate_chrome_ua()
		yandex_ua = generate_yandex_ua()
		safari_ua = generate_safari_ua(engine_ua)
	
		return " ".join(list(filter(None, [chrome_ua, yandex_ua, safari_ua]))), browser_to_generate
	else:
		raise UnsupportedBrowserError(browser_to_generate)
