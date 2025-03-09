import random
from osn_requests.headers.accept.data import MimeTypes
from osn_var_tools.python_instances_tools import get_class_attributes


def generate_random_accept_header() -> str:
	mime_types = {
		choice: (random.uniform(0.0, 1.0) if random.choice([True, False]) else None)
		for attribute in get_class_attributes(MimeTypes, contains_exclude="__").keys()
		for choice in random.choices(
				getattr(MimeTypes, attribute),
				k=random.randint(0, len(getattr(MimeTypes, attribute)))
		)
	}
	
	if len(mime_types) == 0:
		mime_types = {"*/*": None}
	else:
		random.shuffle(list(mime_types.items()))
	
	return ", ".join(
			(f"{mime_type}; q={quality:.1f}" if quality is not None else mime_type)
			for mime_type, quality in mime_types.items()
	)
