class UnsupportedOSError(Exception):
	"""
	Exception raised when the operating system is not supported.

	This exception is raised when the provided operating system name is not among the supported OS types.
	"""
	
	def __init__(self, os_name: str):
		"""
		Initializes a new instance of `UnsupportedBrowserError`.

		Args:
		   os_name (str): The name of the unsupported operating system.
		"""
		super().__init__(f"Unsupported OS: {os_name}")


class UnsupportedEngineError(Exception):
	"""
	Exception raised when the browser engine is not supported.

	This exception is raised when the provided browser engine name is not among the supported engine types.
	"""
	
	def __init__(self, engine_name: str):
		"""
		Initializes a new instance of `UnsupportedBrowserError`.

		Args:
		   engine_name (str): The name of the unsupported browser engine.
		"""
		super().__init__(f"Unsupported engine: {engine_name}")


class UnsupportedBrowserError(Exception):
	"""
	Exception raised when the browser is not supported.

	This exception is raised when the provided browser name is not among the supported browser types.
	"""
	
	def __init__(self, browser_name: str):
		"""
		Initializes a new instance of `UnsupportedBrowserError`.

		Args:
		   browser_name (str): The name of the unsupported browser.
		"""
		super().__init__(f"Unsupported browser: {browser_name}")
