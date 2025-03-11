class Encodings:
	"""
	Provides a collection of supported content encodings.

	This class is a container for lists of content encodings that can be used in HTTP Accept-Encoding headers.
	It includes a comprehensive list of all commonly supported encodings.

	Attributes:
	   all (list[str]): A list of strings representing all supported content encodings.
	"""
	all = ["gzip", "compress", "deflate", "br", "zstd", "identity"]
