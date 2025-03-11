from typing import (
	Any,
	Optional,
	TypedDict,
	Union
)


class RequestProxy(TypedDict, total=False):
	"""
	Type definition for a dictionary of proxies for different protocols.

	This TypedDict defines the structure for a dictionary that can hold proxy configurations for various network protocols.
	It is designed to be used with request libraries that accept a dictionary of proxies, where keys are protocol names and values are proxy URLs.
	The `total=False` indicates that not all protocol keys are required in a `RequestProxy` instance.

	Attributes:
	   http (str): Proxy URL for HTTP requests.
	   https (str): Proxy URL for HTTPS requests.
	   socks4 (str): Proxy URL for SOCKS4 protocol requests.
	   socks5 (str): Proxy URL for SOCKS5 protocol requests.
	   ftp (str): Proxy URL for FTP protocol requests.
	"""
	http: str
	https: str
	socks4: str
	socks5: str
	ftp: str


class RequestHeaders(TypedDict, total=False):
	"""
	Type definition for a dictionary of HTTP request headers.

	This TypedDict defines the structure for a dictionary that can hold various standard HTTP request headers.
	It is designed to be used with request libraries for setting custom HTTP headers in requests.
	The `total=False` indicates that not all header keys are required in a `RequestHeaders` instance.

	Attributes:
	   Accept (str): The Accept header, indicating the MIME types the client can handle.
	   Accept_Charset (str): The Accept-Charset header, indicating the character sets the client can handle.
	   Accept_Encoding (str): The Accept-Encoding header, indicating the content encodings the client can handle.
	   Accept_Language (str): The Accept-Language header, indicating the preferred languages for the response.
	   Authorization (str): The Authorization header, used for authentication.
	   Cache_Control (str): The Cache-Control header, used to specify caching directives.
	   Connection (str): The Connection header, controlling network connection options.
	   Date (str): The Date header, representing the date and time at which the message was originated.
	   Expect (str): The Expect header, indicating specific server behavior expectations.
	   From (str): The From header, providing an email address for the human user who controls the requesting user agent.
	   Host (str): The Host header, specifying the domain name of the server and optionally the port number.
	   If_Match (str): The If-Match header, used with conditional requests to match entity tags.
	   If_Modified_Since (str): The If-Modified-Since header, used with conditional GET requests to check if the resource has been modified since a specific date.
	   If_None_Match (str): The If-None-Match header, used with conditional requests to check if entity tags do not match.
	   If_Range (str): The If-Range header, used to specify a range of bytes to be retrieved only if the entity tag or date matches.
	   If_Unmodified_Since (str): The If-Unmodified-Since header, used with conditional requests to check if the resource has not been modified since a specific date.
	   Max_Forwards (str): The Max-Forwards header, limiting the number of proxies or gateways that can forward the request.
	   MIME_Version (str): The MIME-Version header, indicating the MIME version used.
	   Pragma (str): The Pragma header, used for implementation-specific directives.
	   Proxy_Authorization (str): The Proxy-Authorization header, used for authenticating with a proxy.
	   Range (str): The Range header, requesting only part of a resource.
	   Referer (str): The Referer header, indicating the URL of the page that linked to the requested URL.
	   TE (str): The TE header, specifying the transfer encodings the client is willing to accept.
	   Trailer (str): The Trailer header, allowing the sender to include additional headers at the end of a chunked message.
	   Transfer_Encoding (str): The Transfer-Encoding header, indicating that the message body is encoded.
	   Upgrade (str): The Upgrade header, requesting the server to switch to a different protocol.
	   User_Agent (str): The User-Agent header, identifying the client software making the request.
	   Via (str): The Via header, indicating intermediate protocols and hosts between the user agent and the server.
	   Warning (str): The Warning header, carrying information about possible problems.
	"""
	Accept: str
	Accept_Charset: str
	Accept_Encoding: str
	Accept_Language: str
	Authorization: str
	Cache_Control: str
	Connection: str
	Date: str
	Expect: str
	From: str
	Host: str
	If_Match: str
	If_Modified_Since: str
	If_None_Match: str
	If_Range: str
	If_Unmodified_Since: str
	Max_Forwards: str
	MIME_Version: str
	Pragma: str
	Proxy_Authorization: str
	Range: str
	Referer: str
	TE: str
	Trailer: str
	Transfer_Encoding: str
	Upgrade: str
	User_Agent: str
	Via: str
	Warning: str


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


url_parameter_type = Union[str, bytes]
params_parameter_type = Optional[Any]
data_parameter_type = Optional[Any]
headers_parameter_type = Optional[Union[RequestHeaders, dict[str, Optional[Union[str, bytes]]]]]
cookies_parameter_type = Optional[Any]
files_parameter_type = Optional[Any]
auth_parameter_type = Optional[Any]
timeout_parameter_type = Optional[Any]
proxies_parameter_type = Optional[Union[RequestProxy, dict[str, str]]]
hooks_parameter_type = Optional[Any]
verify_parameter_type = Optional[Any]
cert_parameter_type = Optional[Any]
json_parameter_type = Optional[Any]
