# osn-requests: Simplified Web Scraping and Requests

A Python library that simplifies making HTTP requests, especially for web scraping, with enhanced features for header management, HTML parsing, and proxy handling.


## Key Features

`osn-requests` is designed to be a user-friendly wrapper around the popular `requests` library, providing a set of functions to streamline common web scraping tasks. It includes features for:

*   **Simplified GET Requests:**  A straightforward function (`get_req`) for making GET requests with automatic header reformatting.
*   **Easy HTML Parsing:**  Fetching and parsing HTML content into an `lxml` ElementTree with a single function (`get_html`), making it easy to navigate and extract data using XPath.
*   **XPath Element Finding:** Convenient functions (`find_web_elements`, `find_web_element`) to locate elements within parsed HTML using XPath expressions.
*   **Header Management:** Automatic reformatting of headers to replace underscores with hyphens, and tools to generate realistic, randomized HTTP headers such as `User-Agent`, `Accept`, `Accept-Language`, `Accept-Encoding`, and `Accept-Charset`.
*   **Proxy Handling:**  Fetching lists of free proxies with filtering options for protocol and country (`get_free_proxies`).


## Installation

* **With pip:**
    ```bash
    pip install osn-requests
    ```

* **With git:**
    ```bash
    pip install git+https://github.com/oddshellnick/osn-requests.git
    ```


## Usage

Here are some examples of how to use `osn-requests`:

### Making a simple GET request

```python
from osn_requests import get_req

response = get_req("https://httpbin.org/get")
print(response.status_code)
print(response.json())
```

### Making a GET request with custom headers

```python
from osn_requests import get_req
from osn_requests.types import RequestHeaders

headers = RequestHeaders(
    User_Agent="My Custom Agent",
    Accept_Language="en-US,en;q=0.9"
)

response = get_req("https://httpbin.org/get", headers=headers)
print(response.request.headers)
```

### Fetching and parsing HTML content

```python
from osn_requests import get_html, find_web_elements

html_tree = get_html("https://example.com")
title_elements = find_web_elements(html_tree, "//title/text()")

if title_elements:
    print("Title:", title_elements[0])
```

### Finding a single web element

```python
from osn_requests import get_html, find_web_element

html_tree = get_html("https://example.com")
link_element = find_web_element(html_tree, "//a/@href")

if link_element:
    print("First Link URL:", link_element)
```

### Getting a list of free proxies

```python
from osn_requests.proxies import get_free_proxies

proxies = get_free_proxies(protocol_filter="https", country_filter="US")

if proxies:
    print("Found free HTTPS proxies in US:")
    for proxy in proxies[:3]: # Print first 3 proxies
        print(f"  {proxy['protocol']}://{proxy['ip']}:{proxy['port']} ({proxy['country']})")
else:
    print("No free proxies found matching the criteria.")
```

### Generating random realistic headers

```python
from osn_requests.headers.user_agent import generate_random_user_agent_header
from osn_requests.headers.accept import generate_random_realistic_accept_header
from osn_requests.headers.accept_language import generate_random_realistic_accept_language_header
from osn_requests.headers.accept_encoding import generate_random_realistic_accept_encoding_header
from osn_requests.headers.accept_charset import generate_random_realistic_accept_charset_header

print("Random User-Agent:", generate_random_user_agent_header())
print("Random Accept:", generate_random_realistic_accept_header())
print("Random Accept-Language:", generate_random_realistic_accept_language_header())
print("Random Accept-Encoding:", generate_random_realistic_accept_encoding_header())
print("Random Accept-Charset:", generate_random_realistic_accept_charset_header())
```


## Functions

### `get_req(...)`

Sends a GET request to the specified URL. This function is a wrapper around `requests.get` with automatic header reformatting (underscores in header keys are replaced with hyphens).

### `get_html(...)`

Fetches HTML content from a URL and parses it into an `lxml` ElementTree for easy XPath querying. It uses `get_req` to fetch the content and `BeautifulSoup` and `lxml` to parse it.

### `find_web_elements(...)`

Finds all web elements within an `lxml` ElementTree that match the given XPath expression. Returns a list of `lxml` ElementTree objects.

### `find_web_element(...)`

Finds the first web element within an `lxml` ElementTree that matches the given XPath expression. Returns the first matching `lxml` ElementTree object or `None` if no match is found.

### `get_free_proxies(...)`

Fetches a list of free proxies from a public API, optionally filtered by protocol (`http`, `https`, etc.) and country (ISO country code). Returns a list of `Proxy` dictionaries.

### Header Generation Functions (`osn_requests.headers`)

*   `generate_random_user_agent_header()`: Generates a complete random User-Agent header string.
*   `generate_random_realistic_accept_header(...)`: Generates a realistic random Accept header string.
*   `generate_random_accept_header(...)`: Generates a random Accept header string from all available MIME types.
*   `generate_random_realistic_accept_language_header(...)`: Generates a realistic random Accept-Language header string.
*   `generate_random_accept_language_header(...)`: Generates a random Accept-Language header string from all available languages.
*   `generate_random_realistic_accept_encoding_header(...)`: Generates a realistic random Accept-Encoding header string.
*   `generate_random_accept_encoding_header(...)`: Generates a random Accept-Encoding header string from all available encodings.
*   `generate_random_realistic_accept_charset_header(...)`: Generates a realistic random Accept-Charset header string.
*   `generate_random_accept_charset_header(...)`: Generates a random Accept-Charset header string from all available charsets.

### `reformat_headers(...)`

Reformats header keys in a dictionary by replacing underscores with hyphens.

### `get_proxy_link(...)`

Constructs a proxy link string from a `Proxy` dictionary, in the format `protocol://ip:port`.


## Types

The library defines several types using `TypedDict` for better type hinting and clarity:

*   `RequestHeaders`:  A dictionary type for HTTP request headers.
*   `RequestProxy`: A dictionary type for proxy configurations for different protocols.
*   `Proxy`: A dictionary type representing a proxy server with `protocol`, `ip`, `port`, and `country`.
*   `QualityValue`: A dictionary type for representing items with associated quality values, used in headers like `Accept` and `Accept-Language`.


## Future Notes

osn-requests is continually being developed and improved. Future plans include adding support for more advanced scraping techniques and incorporating additional utilities for handling various web data formats. Contributions and feature requests are welcome!
