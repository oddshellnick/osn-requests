import random
from osn_requests.headers.accept_charset.data import Charsets


def generate_random_accept_charset_header() -> str:
	charsets = {"utf-8": None, "ascii": None}

	choice_set = list(set(Charsets.common) - set(charsets.keys()))
	chosen = {
		choice: (random.uniform(0.7, 1.0) if random.choice([True, False]) else None)
		for choice in random.choices(
				choice_set,
				k=random.randint(0, min(3, len(choice_set)))
		)
	}
	random.shuffle(list(chosen.items()))
	charsets.update(chosen)

	charsets["*"] = 0.1

	return ", ".join(
			(f"{charset}; q={quality:.1f}" if quality is not None else charset)
			for charset, quality in charsets.items()
	)
