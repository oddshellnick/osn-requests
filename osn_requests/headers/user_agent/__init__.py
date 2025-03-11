from osn_requests.headers.user_agent.os_ua_generation import generate_random_os_ua
from osn_requests.headers.user_agent.engine_ua_generation import generate_random_engine_ua
from osn_requests.headers.user_agent.browser_ua_generation import generate_random_browser_ua
from osn_requests.headers.user_agent.mozilla_ua_generation import generate_random_mozilla_ua


def generate_random_user_agent_header() -> str:
	"""
	Generates a complete random user agent header string.

	This function combines the Mozilla, OS, Engine, and Browser user agent parts
	to generate a complete user agent string.

	Returns:
		str: Complete user agent string.
	"""
	mozilla_ua = generate_random_mozilla_ua()
	os_ua, used_os = generate_random_os_ua()
	engine_ua, used_engine = generate_random_engine_ua(platform=used_os)
	browser_ua, used_browser = generate_random_browser_ua(engine=used_engine, engine_ua=engine_ua)
	
	return f"{mozilla_ua} ({os_ua}) {engine_ua} {browser_ua}"
