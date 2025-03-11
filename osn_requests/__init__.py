import requests
from lxml import etree
from typing import Optional
from bs4 import BeautifulSoup
from osn_requests.functions import reformat_headers
from osn_requests.types import (
	auth_parameter_type,
	cert_parameter_type,
	cookies_parameter_type,
	data_parameter_type,
	files_parameter_type,
	headers_parameter_type,
	hooks_parameter_type,
	json_parameter_type,
	params_parameter_type,
	proxies_parameter_type,
	timeout_parameter_type,
	url_parameter_type,
	verify_parameter_type
)


def get_req(
		url: url_parameter_type,
		params: params_parameter_type = None,
		data: data_parameter_type = None,
		headers: headers_parameter_type = None,
		cookies: cookies_parameter_type = None,
		files: files_parameter_type = None,
		auth: auth_parameter_type = None,
		timeout: timeout_parameter_type = None,
		allow_redirects: bool = False,
		proxies: proxies_parameter_type = None,
		hooks: hooks_parameter_type = None,
		stream: Optional[bool] = None,
		verify: verify_parameter_type = None,
		cert: cert_parameter_type = None,
		json: json_parameter_type = None
) -> requests.Response:
	"""
	Sends a GET request to the specified URL using the requests library.

	This function is a wrapper around `requests.get` that simplifies making HTTP GET requests.
	It accepts various parameters to customize the request, such as headers, parameters, and proxies.
	Headers are automatically reformatted to replace underscores with hyphens.

	Args:
		url (url_parameter_type): The URL to request.
		params (params_parameter_type): Query parameters to append to the URL. Defaults to None.
		data (data_parameter_type): Data to send in the request body. Defaults to None.
		headers (headers_parameter_type): Request headers. Underscores in keys are replaced with hyphens. Defaults to None.
		cookies (cookies_parameter_type): Request cookies. Defaults to None.
		files (files_parameter_type): Files to upload. Defaults to None.
		auth (auth_parameter_type): Authentication tuple or object. Defaults to None.
		timeout (timeout_parameter_type): Request timeout in seconds. Defaults to None.
		allow_redirects (bool): Whether to allow redirects. Defaults to False.
		proxies (proxies_parameter_type): Dictionary of proxies to use. Defaults to None.
		hooks (hooks_parameter_type): Request hooks. Defaults to None.
		stream (Optional[bool]): Whether to stream the response body. Defaults to None.
		verify (verify_parameter_type): SSL verification. Defaults to None.
		cert (cert_parameter_type): SSL client certificate. Defaults to None.
		json (json_parameter_type): JSON data to send in the request body. Defaults to None.

	Returns:
		requests.Response: The response object from the requests library.
	"""
	return requests.get(
			url=url,
			params=params,
			data=data,
			headers=reformat_headers(headers),
			cookies=cookies,
			files=files,
			auth=auth,
			timeout=timeout,
			allow_redirects=allow_redirects,
			proxies=proxies,
			hooks=hooks,
			stream=stream,
			verify=verify,
			cert=cert,
			json=json
	)


def get_html(
		url: url_parameter_type,
		params: params_parameter_type = None,
		data: data_parameter_type = None,
		headers: headers_parameter_type = None,
		cookies: cookies_parameter_type = None,
		files: files_parameter_type = None,
		auth: auth_parameter_type = None,
		timeout: timeout_parameter_type = None,
		allow_redirects: bool = False,
		proxies: proxies_parameter_type = None,
		hooks: hooks_parameter_type = None,
		stream: Optional[bool] = None,
		verify: verify_parameter_type = None,
		cert: cert_parameter_type = None,
		json: json_parameter_type = None
) -> etree._Element:
	"""
	Fetches HTML content from a URL and parses it into an lxml ElementTree.

	This function sends a GET request to the specified URL using `get_req` and then parses the HTML content
	of the response using BeautifulSoup and lxml for easy element selection and manipulation.

	Args:
		url (url_parameter_type): The URL to fetch HTML from.
		params (params_parameter_type): Query parameters to append to the URL. Defaults to None.
		data (data_parameter_type): Data to send in the request body. Defaults to None.
		headers (headers_parameter_type): Request headers. Underscores in keys are replaced with hyphens. Defaults to None.
		cookies (cookies_parameter_type): Request cookies. Defaults to None.
		files (files_parameter_type): Files to upload. Defaults to None.
		auth (auth_parameter_type): Authentication tuple or object. Defaults to None.
		timeout (timeout_parameter_type): Request timeout in seconds. Defaults to None.
		allow_redirects (bool): Whether to allow redirects. Defaults to False.
		proxies (proxies_parameter_type): Dictionary of proxies to use. Defaults to None.
		hooks (hooks_parameter_type): Request hooks. Defaults to None.
		stream (Optional[bool]): Whether to stream the response body. Defaults to None.
		verify (verify_parameter_type): SSL verification. Defaults to None.
		cert (cert_parameter_type): SSL client certificate. Defaults to None.
		json (json_parameter_type): JSON data to send in the request body. Defaults to None.

	Returns:
		etree._Element: The root element of the parsed HTML as an lxml ElementTree object.
	"""
	return etree.HTML(
			str(
					BeautifulSoup(
							get_req(
									url=url,
									params=params,
									data=data,
									headers=headers,
									cookies=cookies,
									files=files,
									auth=auth,
									timeout=timeout,
									allow_redirects=allow_redirects,
									proxies=proxies,
									hooks=hooks,
									stream=stream,
									verify=verify,
									cert=cert,
									json=json
							).content,
							"html.parser"
					)
			)
	)


def find_web_elements(etree_: etree._Element, xpath: str) -> list[etree._Element]:
	"""
	Finds all web elements matching a given XPath expression.

	Args:
		etree_ (etree._Element): The lxml ElementTree object to search within.
		xpath (str): The XPath expression to use.

	Returns:
		list[etree._Element]: A list of lxml ElementTree objects matching the XPath.
	"""
	return etree_.xpath(xpath)


def find_web_element(etree_: etree._Element, xpath: str) -> Optional[etree._Element]:
	"""
	Finds the first web element matching a given XPath expression.

	Args:
		etree_ (etree._Element): The lxml ElementTree object to search within.
		xpath (str): The XPath expression to use.

	Returns:
		Optional[etree._Element]: The first matching lxml ElementTree object, or None if no match is found.
	"""
	try:
		return find_web_elements(etree_, xpath)[0]
	except IndexError:
		return None
