from typing import Literal, Union


supported_ua_platforms = Union[Literal["Windows", "Macintosh", "Linux", "Android", "IOS"], str]
supported_ua_engines = Union[Literal["AppleWebKit", "Gecko", "Blink"], str]
supported_ua_browsers = Union[
	Literal["Chrome", "Firefox", "Safari", "Opera", "Edge", "YandexBrowser"],
	str
]
