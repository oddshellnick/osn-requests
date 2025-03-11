import requests
from lxml import etree
from typing import Optional
from bs4 import BeautifulSoup


def get_req(url: str, headers: Optional[dict] = None, proxies: Optional[dict] = None) -> requests.Response:
	"""
	Retrieves content from a given URL.

	Args:
		url (str): The URL to fetch.
		headers (Optional[dict]): HTTP headers to include in the request. Defaults to None.
		proxies (Optional[dict]): Proxies to use for the request. Defaults to None.

	Returns:
		requests.Response: The response object from the request.
	"""
	return requests.get(url=url, headers=headers, proxies=proxies)


def get_html(url: str, headers: Optional[dict] = None, proxies: Optional[dict] = None) -> etree._Element:
	"""
	Fetches a URL and parses the content into an lxml ElementTree object.

	Args:
		url (str): The URL to fetch.
		headers (Optional[dict]): HTTP headers to include in the request. Defaults to None.
		proxies (Optional[dict]): Proxies to use for the request. Defaults to None.

	Returns:
		 etree._Element: An lxml ElementTree object representing the parsed HTML.
	"""
	return etree.HTML(
			str(
					BeautifulSoup(
							requests.get(url=url, headers=headers, proxies=proxies).content,
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
