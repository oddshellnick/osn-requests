import random
from typing import Optional
from osn_requests.headers.user_agent.data import (
	UserAgentEngine,
	UserAgentSupportedParts
)
from osn_requests.headers.user_agent.errors import (
	UnsupportedEngineError,
	UnsupportedOSError
)
from osn_requests.headers.user_agent.data_types import (
	supported_ua_engines,
	supported_ua_platforms
)


def generate_random_gecko_ua() -> str:
	"""
	Generates a random Gecko engine user agent string.

	Returns:
		str: Gecko engine user agent string.
	"""
	year = random.choice(UserAgentEngine.gecko_versions[0])
	month = random.choice(UserAgentEngine.gecko_versions[1])
	
	if month in [1, 3, 5, 7, 8, 10, 12]:
		day = random.choice(UserAgentEngine.gecko_versions[2][0])
	elif month in [4, 6, 9, 11]:
		day = random.choice(UserAgentEngine.gecko_versions[2][1])
	elif year % 4 == 0:
		day = random.choice(UserAgentEngine.gecko_versions[2][2])
	else:
		day = random.choice(UserAgentEngine.gecko_versions[2][3])
	
	gecko_version = f"{year}{month:02d}{day:02d}"
	return f"Gecko/{gecko_version}"


def generate_random_apple_webkit_ua() -> str:
	"""
	Generates a random AppleWebKit engine user agent string.

	Returns:
		str: AppleWebKit engine user agent string.
	"""
	version_parts = [str(random.choice(part)) for part in UserAgentEngine.apple_webkit_versions]
	
	return f"AppleWebKit/{'.'.join(version_parts)} (KHTML, like Gecko)"


def generate_random_engine_ua(
		engine_to_generate: Optional[supported_ua_engines] = None,
		platform: Optional[supported_ua_platforms] = None
) -> tuple[str, str]:
	"""
	Generates a random engine user agent string based on the given engine and platform.

	This function generates a user agent string for a specified engine, or a random engine if none is specified.
	It can also generate a user agent string based on the specified platform.

	Args:
		engine_to_generate (typing.Optional[supported_ua_engines]): The engine for which to generate the user agent.
		platform (typing.Optional[supported_ua_platforms]): The platform on which to base the engine choice.

	Returns:
		tuple[str, str]: A tuple containing the generated user agent string and the engine used.

	Raises:
		UnsupportedEngineError: If the provided engine_to_generate is not supported.
		UnsupportedOSError: If the provided platform is not supported.
	"""
	if platform is not None and platform not in UserAgentSupportedParts.os:
		raise UnsupportedOSError(platform)
	
	if engine_to_generate is None:
		engine_to_generate = "AppleWebKit" if platform == "IOS" else random.choice(UserAgentSupportedParts.engine)
	
	if engine_to_generate == "AppleWebKit":
		return generate_random_apple_webkit_ua(), engine_to_generate
	elif engine_to_generate == "Gecko":
		return generate_random_gecko_ua(), engine_to_generate
	elif engine_to_generate == "Blink":
		return generate_random_apple_webkit_ua(), engine_to_generate
	else:
		raise UnsupportedEngineError(engine_to_generate)
