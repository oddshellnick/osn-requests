import random
from typing import Optional
from osn_requests.headers.user_agent.errors import UnsupportedOSError
from osn_requests.headers.user_agent.data_types import supported_ua_platforms
from osn_requests.headers.user_agent.data import (
	UserAgentOS,
	UserAgentSupportedParts
)


def generate_ios_ua() -> str:
	"""
	Generates a random iOS platform user agent string.

	Returns:
		str: iOS platform user agent string.
	"""
	ios_version = random.choice(UserAgentOS.ios_versions)
	device, os_prefix = random.choice(UserAgentOS.ios_devices)
	
	return f"{device}; {os_prefix} {ios_version} like Mac OS X"


def generate_android_ua() -> str:
	"""
	Generates a random Android platform user agent string.

	Returns:
		str: Android platform user agent string.
	"""
	android_type = random.choice(["Linux", "Mobile", None])
	android_version = random.choice(UserAgentOS.android_versions)
	device = random.choice(UserAgentOS.android_devices)
	
	return f"{'Linux; ' if android_type == 'Linux' else ''}Android {android_version}{'; Mobile' if android_type == 'Mobile' else ''}; {device}"


def generate_linux_ua() -> str:
	"""
	Generates a random Linux platform user agent string.

	Returns:
		str: Linux platform user agent string.
	"""
	prefix = random.choice(["X11", None])
	linux_distribution = random.choice(UserAgentOS.linux_distributions)
	linux_architecture = random.choice(UserAgentOS.linux_architectures)
	
	return "; ".join(
			list(filter(None, [prefix, linux_distribution, f"Linux {linux_architecture}"]))
	)


def generate_mac_ua() -> str:
	"""
	Generates a random Macintosh platform user agent string.

	Returns:
		str: Macintosh platform user agent string.
	"""
	cpu = random.choice(["Intel", "Apple Silicon"])
	macos_version = random.choice(
			UserAgentOS.mac_os_intel_versions
			if cpu == "Intel"
			else UserAgentOS.mac_os_apple_silicon_versions
	)
	
	return f"Macintosh; {cpu} Mac OS X {macos_version}"


def generate_windows_ua() -> str:
	"""
	Generates a random Windows platform user agent string.

	Returns:
		str: Windows platform user agent string.
	"""
	windows_version = random.choice(UserAgentOS.windows_versions)
	windows_architecture = random.choice(UserAgentOS.windows_architectures)
	
	return f"Windows {windows_version}; {windows_architecture}"


def generate_random_os_ua(os_to_generate: Optional[supported_ua_platforms] = None) -> tuple[str, str]:
	"""
	Generates a random OS user agent string based on the given OS.

	This function generates a user agent string for a specified OS, or a random OS if none is specified.

	Args:
		os_to_generate (typing.Optional[supported_ua_platforms]): The OS for which to generate the user agent.

	Returns:
		tuple[str, str]: A tuple containing the generated user agent string and the OS used.

	Raises:
		UnsupportedOSError: If the provided os_to_generate is not supported.
	"""
	if os_to_generate is None:
		os_to_generate = random.choice(UserAgentSupportedParts.os)
	
	if os_to_generate == "Windows":
		return generate_windows_ua(), os_to_generate
	elif os_to_generate == "Macintosh":
		return generate_mac_ua(), os_to_generate
	elif os_to_generate == "Linux":
		return generate_linux_ua(), os_to_generate
	elif os_to_generate == "Android":
		return generate_android_ua(), os_to_generate
	elif os_to_generate == "IOS":
		return generate_ios_ua(), os_to_generate
	else:
		raise UnsupportedOSError(os_to_generate)
