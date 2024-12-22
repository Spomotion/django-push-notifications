try:
	# Python 3.8+
	import importlib.metadata as importlib_metadata

	try:
		# Ugly hack for APNS sub-deps Python 3.10+
		import collections
		from collections.abc import Iterable, Mapping, MutableMapping, MutableSet

		collections.Iterable = Iterable
		collections.Mapping = Mapping
		collections.MutableSet = MutableSet
		collections.MutableMapping = MutableMapping
	except ImportError:
		pass

except ImportError:
	# <Python 3.7 and lower
	import importlib_metadata

__version__ = importlib_metadata.version("django-push-notifications")
