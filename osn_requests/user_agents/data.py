from dataclasses import dataclass


@dataclass(frozen=True)
class UserAgentSupportedParts:
	"""
	A class that holds the different parts of a user agent that are supported.

	Attributes:
		os (list[str]): A list of supported operating systems.
		engine (list[str]): A list of supported rendering engines.
		browser (list[str]): A list of supported browsers.
		apple_webkit_browsers (list[str]): A list of browsers that use the AppleWebKit engine.
		blink_browsers (list[str]): A list of browsers that use the Blink engine.
		gecko_browsers (list[str]): A list of browsers that use the Gecko engine.
	"""
	os = ["Windows", "Macintosh", "Linux", "Android", "IOS"]
	engine = ["AppleWebKit", "Gecko", "Blink"]
	browser = ["Chrome", "Firefox", "Safari", "Opera", "Edge", "Yandex"]
	apple_webkit_browsers = ["Safari"]
	blink_browsers = ["Chrome", "Opera", "Edge", "Yandex"]
	gecko_browsers = ["Firefox"]


@dataclass(frozen=True)
class UserAgentOS:
	"""
	A class that holds the different OS specific user agent parts.

	Attributes:
		windows_versions (list[str]): A list of supported Windows versions.
		windows_architectures (list[str]): A list of supported Windows architectures.
		mac_os_intel_versions (list[str]): A list of supported macOS versions for Intel CPUs.
		mac_os_apple_silicon_versions (list[str]): A list of supported macOS versions for Apple Silicon CPUs.
		linux_distributions (list[str]): A list of supported Linux distributions.
		linux_architectures (list[str]): A list of supported Linux architectures.
		android_versions (list[str]): A list of supported Android versions.
		android_devices (list[str]): A list of supported Android devices.
		ios_versions (list[str]): A list of supported iOS versions.
		ios_devices (list[tuple[str, str]]): A list of supported iOS devices and their prefixes.
	"""
	windows_versions = [
		"NT 10.0",
		"NT 6.3",
		"NT 6.2",
		"NT 6.1",
		"NT 6.0",
		"NT 5.2",
		"NT 5.1",
		"NT 5.0"
	]
	
	windows_architectures = ["Win64; x64", "Win32", "WOW64"]
	
	linux_distributions = [
		"Debian",
		"Ubuntu",
		"Kubuntu",
		"Xubuntu",
		"Lubuntu",
		"Ubuntu MATE",
		"Ubuntu Budgie",
		"Ubuntu Studio",
		"Red Hat Enterprise Linux",
		"CentOS Stream",
		"Rocky Linux",
		"AlmaLinux",
		"Fedora",
		"Arch",
		"Manjaro",
		"EndeavourOS",
		"Artix",
		None
	]
	
	linux_architectures = [
		"x86_64",
		"i686",
		"armv7l",
		"aarch64",
		"armv6l",
		"armv5tel",
		"ppc",
		"ppc64",
		"ppc64le",
		"mips",
		"mips64",
		"mipsel",
		"mips64el",
		"riscv64",
		"s390x",
		"sparc",
		"sparc64",
		"sh4",
		"ia64",
		"loongarch64"
	]
	
	mac_os_intel_versions = [
		"10_11_0",
		"10_11_1",
		"10_11_2",
		"10_11_3",
		"10_11_4",
		"10_11_5",
		"10_11_6",
		"10_12_0",
		"10_12_1",
		"10_12_2",
		"10_12_3",
		"10_12_4",
		"10_12_5",
		"10_12_6",
		"10_13_0",
		"10_13_1",
		"10_13_3",
		"10_13_4",
		"10_13_5",
		"10_13_6",
		"10_14_0",
		"10_14_1",
		"10_14_2",
		"10_14_3",
		"10_14_4",
		"10_14_5",
		"10_14_6",
		"10_15_0",
		"10_15_1",
		"10_15_2",
		"10_15_3",
		"10_15_4",
		"10_15_5",
		"10_15_6",
		"10_15_7",
		"11_0",
		"11_0_1",
		"11_1",
		"11_2",
		"11_2_1",
		"11_2_2",
		"11_2_3",
		"11_3",
		"11_3_1",
		"11_4",
		"11_5",
		"11_5_1",
		"11_5_2",
		"11_6",
		"11_6_1",
		"11_6_2",
		"11_6_3",
		"11_6_4",
		"11_6_5",
		"11_6_6",
		"11_6_7",
		"11_6_8",
		"11_7",
		"11_7_1",
		"11_7_2",
		"11_7_3",
		"11_7_4",
		"11_7_5",
		"11_7_6",
		"11_7_7",
		"11_7_8",
		"11_7_9",
		"11_7_10",
		"12_0",
		"12_0_1",
		"12_1",
		"12_2",
		"12_2_1",
		"12_3",
		"12_3_1",
		"12_4",
		"12_5",
		"12_5_1",
		"12_6",
		"12_6_1",
		"12_6_2",
		"12_6_3",
		"12_6_4",
		"12_6_5",
		"12_6_6",
		"12_6_7",
		"12_6_8",
		"12_6_9",
		"12_7",
		"12_7_1",
		"12_7_2",
		"12_7_3",
		"12_7_4",
		"12_7_5",
		"12_7_6",
		"13_0",
		"13_0_1",
		"13_1",
		"13_2",
		"13_2_1",
		"13_3",
		"13_3_1",
		"13_4",
		"13_4_1",
		"13_5",
		"13_5_1",
		"13_5_2",
		"13_6",
		"13_6_1",
		"13_6_2",
		"13_6_3",
		"13_6_4",
		"13_6_5",
		"13_6_6",
		"13_6_7",
		"13_6_8",
		"13_6_9",
		"13_7",
		"13_7_1",
		"13_7_2",
		"13_7_3",
		"14_0",
		"14_1",
		"14_1_1",
		"14_1_2",
		"14_2",
		"14_2_1",
		"14_3",
		"14_3_1",
		"14_4",
		"14_4_1",
		"14_5",
		"14_6",
		"14_6_1",
		"14_7",
		"14_7_1",
		"14_7_2"
	]
	
	mac_os_apple_silicon_versions = [
		"15_0",
		"15_1",
		"15_1_1",
		"15_1_2",
		"15_2",
		"15_2_1",
		"15_3",
		"15_3_1",
		"15_4",
		"15_4_1",
		"15_5",
		"15_6",
		"15_6_1",
		"15_7",
		"15_7_1",
		"15_7_2"
	]
	
	android_versions = [
		"6.0",
		"6.0.1",
		"7.0",
		"7.0.1",
		"7.1",
		"7.1.1",
		"7.1.2",
		"8.0",
		"8.1",
		"9",
		"10",
		"11",
		"12",
		"12L",
		"13",
		"14",
		"15"
	]
	
	android_devices = [
		"Samsung Galaxy S6",
		"Samsung Galaxy S7",
		"Samsung Galaxy S8",
		"Samsung Galaxy S9",
		"Samsung Galaxy S10",
		"Samsung Galaxy S20",
		"Samsung Galaxy S21",
		"Samsung Galaxy S22",
		"Samsung Galaxy S23",
		"Samsung Galaxy S6+",
		"Samsung Galaxy S7+",
		"Samsung Galaxy S8+",
		"Samsung Galaxy S9+",
		"Samsung Galaxy S10+",
		"Samsung Galaxy S20+",
		"Samsung Galaxy S21+",
		"Samsung Galaxy S22+",
		"Samsung Galaxy S23+",
		"Samsung Galaxy S6 Ultra",
		"Samsung Galaxy S7 Ultra",
		"Samsung Galaxy S8 Ultra",
		"Samsung Galaxy S9 Ultra",
		"Samsung Galaxy S10 Ultra",
		"Samsung Galaxy S20 Ultra",
		"Samsung Galaxy S21 Ultra",
		"Samsung Galaxy S22 Ultra",
		"Samsung Galaxy S23 Ultra",
		"Samsung Galaxy S6 e",
		"Samsung Galaxy S7 e",
		"Samsung Galaxy S8 e",
		"Samsung Galaxy S9 e",
		"Samsung Galaxy S10 e",
		"Samsung Galaxy S20 FE",
		"Samsung Galaxy S21 FE",
		"Samsung Galaxy Note 5",
		"Samsung Galaxy Note 7",
		"Samsung Galaxy Note 8",
		"Samsung Galaxy Note 9",
		"Samsung Galaxy Note 10",
		"Samsung Galaxy Note 20",
		"Samsung Galaxy Note 5+",
		"Samsung Galaxy Note 7+",
		"Samsung Galaxy Note 8+",
		"Samsung Galaxy Note 9+",
		"Samsung Galaxy Note 10+",
		"Samsung Galaxy Note 20+",
		"Samsung Galaxy Note 5 Ultra",
		"Samsung Galaxy Note 7 Ultra",
		"Samsung Galaxy Note 8 Ultra",
		"Samsung Galaxy Note 9 Ultra",
		"Samsung Galaxy Note 10 Ultra",
		"Samsung Galaxy Note 20 Ultra",
		"Samsung Galaxy A3",
		"Samsung Galaxy A5",
		"Samsung Galaxy A7",
		"Samsung Galaxy A8",
		"Samsung Galaxy A9",
		"Samsung Galaxy A10",
		"Samsung Galaxy A20",
		"Samsung Galaxy A30",
		"Samsung Galaxy A40",
		"Samsung Galaxy A50",
		"Samsung Galaxy A60",
		"Samsung Galaxy A70",
		"Samsung Galaxy A80",
		"Samsung Galaxy A90",
		"Samsung Galaxy A11",
		"Samsung Galaxy A21",
		"Samsung Galaxy A31",
		"Samsung Galaxy A41",
		"Samsung Galaxy A51",
		"Samsung Galaxy A71",
		"Samsung Galaxy A12",
		"Samsung Galaxy A22",
		"Samsung Galaxy A32",
		"Samsung Galaxy A42",
		"Samsung Galaxy A52",
		"Samsung Galaxy A72",
		"Samsung Galaxy A13",
		"Samsung Galaxy A23",
		"Samsung Galaxy A33",
		"Samsung Galaxy A53",
		"Samsung Galaxy A73",
		"Samsung Galaxy A14",
		"Samsung Galaxy A24",
		"Samsung Galaxy A34",
		"Samsung Galaxy A54",
		"Samsung Galaxy A3s",
		"Samsung Galaxy A5s",
		"Samsung Galaxy A7s",
		"Samsung Galaxy M10",
		"Samsung Galaxy M20",
		"Samsung Galaxy M30",
		"Samsung Galaxy M40",
		"Samsung Galaxy M11",
		"Samsung Galaxy M21",
		"Samsung Galaxy M31",
		"Samsung Galaxy M41",
		"Samsung Galaxy M51",
		"Samsung Galaxy M02",
		"Samsung Galaxy M12",
		"Samsung Galaxy M22",
		"Samsung Galaxy M32",
		"Samsung Galaxy M52",
		"Samsung Galaxy M23",
		"Samsung Galaxy M33",
		"Samsung Galaxy M53",
		"Samsung Galaxy Z Fold",
		"Samsung Galaxy Z Fold 2",
		"Samsung Galaxy Z Fold 3",
		"Samsung Galaxy Z Fold 4",
		"Samsung Galaxy Z Fold 5",
		"Samsung Galaxy Z Flip",
		"Samsung Galaxy Z Flip 2",
		"Samsung Galaxy Z Flip 3",
		"Samsung Galaxy Z Flip 4",
		"Samsung Galaxy Z Flip 5",
		"Samsung Galaxy XCover",
		"Samsung Galaxy F",
		"Google Pixel",
		"Google Pixel XL",
		"Google Pixel 2",
		"Google Pixel 2 XL",
		"Google Pixel 3",
		"Google Pixel 3 XL",
		"Google Pixel 3a",
		"Google Pixel 3a XL",
		"Google Pixel 4",
		"Google Pixel 4 XL",
		"Google Pixel 4a",
		"Google Pixel 4a 5G",
		"Google Pixel 5",
		"Google Pixel 5a",
		"Google Pixel 6",
		"Google Pixel 6 Pro",
		"Google Pixel 6a",
		"Google Pixel 7",
		"Google Pixel 7 Pro",
		"Google Pixel 7a",
		"Google Pixel 8",
		"Google Pixel 8 Pro",
		"Google Nexus 5X",
		"Google Nexus 6P",
		"Poco F1",
		"Poco F2 Pro",
		"Poco F3",
		"Poco F4",
		"Poco F5",
		"Poco F5 Pro",
		"Poco X2",
		"Poco X3",
		"Poco X3 NFC",
		"Poco X3 Pro",
		"Poco X4 Pro",
		"Poco X5",
		"Poco X5 Pro",
		"Poco M2",
		"Poco M2 Pro",
		"Poco M3",
		"Poco M3 Pro",
		"Poco M4 Pro",
		"Poco M5",
		"Poco M5s",
		"Poco M6 Pro",
		"Poco C3",
		"Poco C31",
		"Poco C40",
		"Poco C50",
		"Poco C51",
		"Poco C55",
		"Vivo X5",
		"Vivo X6",
		"Vivo X7",
		"Vivo X9",
		"Vivo X20",
		"Vivo X21",
		"Vivo X23",
		"Vivo X27",
		"Vivo X30",
		"Vivo X50",
		"Vivo X60",
		"Vivo X70",
		"Vivo X80",
		"Vivo X90",
		"Vivo X5 Pro",
		"Vivo X6 Pro",
		"Vivo X7 Pro",
		"Vivo X9 Pro",
		"Vivo X20 Pro",
		"Vivo X21 Pro",
		"Vivo X23 Pro",
		"Vivo X27 Pro",
		"Vivo X30 Pro",
		"Vivo X50 Pro",
		"Vivo X60 Pro",
		"Vivo X70 Pro",
		"Vivo X80 Pro",
		"Vivo X90 Pro",
		"Vivo X5 Plus",
		"Vivo X6 Plus",
		"Vivo X7 Plus",
		"Vivo X9 Plus",
		"Vivo X20 Plus",
		"Vivo X21 Plus",
		"Vivo X23 Plus",
		"Vivo X27 Plus",
		"Vivo X30 Plus",
		"Vivo X50 Plus",
		"Vivo X60 Plus",
		"Vivo X70 Plus",
		"Vivo X80 Plus",
		"Vivo X90 Plus",
		"Vivo V3",
		"Vivo V5",
		"Vivo V7",
		"Vivo V9",
		"Vivo V11",
		"Vivo V15",
		"Vivo V17",
		"Vivo V19",
		"Vivo V20",
		"Vivo V21",
		"Vivo V23",
		"Vivo V25",
		"Vivo V27",
		"Vivo Y11",
		"Vivo Y12",
		"Vivo Y15",
		"Vivo Y17",
		"Vivo Y19",
		"Vivo Y20",
		"Vivo Y30",
		"Vivo Y50",
		"Vivo Y51",
		"Vivo Y52",
		"Vivo Y70",
		"Vivo Y72",
		"Vivo Y73",
		"Vivo Y75",
		"Vivo Y76",
		"Vivo Y81",
		"Vivo Y91",
		"Vivo Y11s",
		"Vivo Y12s",
		"Vivo Y15s",
		"Vivo Y17s",
		"Vivo Y19s",
		"Vivo Y20i",
		"Vivo Y30i",
		"Vivo Y50i",
		"Vivo Y51i",
		"Vivo Y52i",
		"Vivo Y70i",
		"Vivo Y72t",
		"Vivo Y73t",
		"Vivo Y75s",
		"Vivo Y76s",
		"Vivo Y81i",
		"Vivo Y91i",
		"Huawei P9",
		"Huawei P10",
		"Huawei P20",
		"Huawei P30",
		"Huawei P40",
		"Huawei P50",
		"Huawei P60",
		"Huawei P9 Lite",
		"Huawei P10 Lite",
		"Huawei P20 Lite",
		"Huawei P30 Lite",
		"Huawei P40 Lite",
		"Huawei P50 Lite",
		"Huawei P60 Lite",
		"Huawei P9 Pro",
		"Huawei P10 Pro",
		"Huawei P20 Pro",
		"Huawei P30 Pro",
		"Huawei P40 Pro",
		"Huawei P50 Pro",
		"Huawei P60 Pro",
		"Huawei Mate 8",
		"Huawei Mate 9",
		"Huawei Mate 10",
		"Huawei Mate 20",
		"Huawei Mate 30",
		"Huawei Mate 40",
		"Huawei Mate 50",
		"Huawei Mate 8 Lite",
		"Huawei Mate 9 Lite",
		"Huawei Mate 10 Lite",
		"Huawei Mate 20 Lite",
		"Huawei Mate 30 Lite",
		"Huawei Mate 40 Lite",
		"Huawei Mate 50 Lite",
		"Huawei Mate 8 Pro",
		"Huawei Mate 9 Pro",
		"Huawei Mate 10 Pro",
		"Huawei Mate 20 Pro",
		"Huawei Mate 30 Pro",
		"Huawei Mate 40 Pro",
		"Huawei Mate 50 Pro",
		"Huawei Mate RS",
		"Huawei Nova",
		"Huawei Nova 2",
		"Huawei Nova 3",
		"Huawei Nova 4",
		"Huawei Nova 5",
		"Huawei Nova 6",
		"Huawei Nova 7",
		"Huawei Nova 8",
		"Huawei Nova 9",
		"Huawei Nova 10",
		"Huawei Nova 11",
		"Huawei Nova Lite",
		"Huawei Nova 2 Lite",
		"Huawei Nova 3 Lite",
		"Huawei Nova 4 Lite",
		"Huawei Nova 5 Lite",
		"Huawei Nova 6 Lite",
		"Huawei Nova 7 Lite",
		"Huawei Nova 8 Lite",
		"Huawei Nova 9 Lite",
		"Huawei Nova 10 Lite",
		"Huawei Nova 11 Lite",
		"Huawei Nova Pro",
		"Huawei Nova 2 Pro",
		"Huawei Nova 3 Pro",
		"Huawei Nova 4 Pro",
		"Huawei Nova 5 Pro",
		"Huawei Nova 6 Pro",
		"Huawei Nova 7 Pro",
		"Huawei Nova 8 Pro",
		"Huawei Nova 9 Pro",
		"Huawei Nova 10 Pro",
		"Huawei Nova 11 Pro",
		"Redmi Note 3",
		"Redmi Note 4",
		"Redmi Note 5",
		"Redmi Note 6",
		"Redmi Note 7",
		"Redmi Note 8",
		"Redmi Note 9",
		"Redmi Note 10",
		"Redmi Note 11",
		"Redmi Note 12",
		"Redmi Note 3 Pro",
		"Redmi Note 4 Pro",
		"Redmi Note 5 Pro",
		"Redmi Note 6 Pro",
		"Redmi Note 7 Pro",
		"Redmi Note 8 Pro",
		"Redmi Note 9 Pro",
		"Redmi Note 10 Pro",
		"Redmi Note 11 Pro",
		"Redmi Note 12 Pro",
		"Redmi Note 3 Max",
		"Redmi Note 4 Max",
		"Redmi Note 5 Max",
		"Redmi Note 6 Max",
		"Redmi Note 7 Max",
		"Redmi Note 8 Max",
		"Redmi Note 9 Max",
		"Redmi Note 10 Max",
		"Redmi Note 11 Max",
		"Redmi Note 12 Max",
		"Redmi Note 3 S",
		"Redmi Note 4 S",
		"Redmi Note 5 S",
		"Redmi Note 6 S",
		"Redmi Note 7 S",
		"Redmi Note 8 S",
		"Redmi Note 9 S",
		"Redmi Note 10 S",
		"Redmi Note 11 S",
		"Redmi Note 12 S",
		"Redmi Note 10T",
		"Redmi Note 11T",
		"Redmi Note 12T",
		"Redmi Note 10T Pro",
		"Redmi Note 11T Pro",
		"Redmi Note 12T Pro",
		"Redmi Note 10R",
		"Redmi Note 11R",
		"Redmi Note 12R",
		"Redmi Note 10R Pro",
		"Redmi Note 11R Pro",
		"Redmi Note 12R Pro",
		"Redmi 1",
		"Redmi 2",
		"Redmi 3",
		"Redmi 4",
		"Redmi 5",
		"Redmi 6",
		"Redmi 7",
		"Redmi 8",
		"Redmi 9",
		"Redmi 10",
		"Redmi 12",
		"Redmi K20",
		"Redmi K30",
		"Redmi K40",
		"Redmi K50",
		"Redmi K60",
		"Redmi K20 Pro",
		"Redmi K30 Pro",
		"Redmi K40 Pro",
		"Redmi K50 Pro",
		"Redmi K60 Pro",
		"Redmi K20 Ultra",
		"Redmi K30 Ultra",
		"Redmi K40 Ultra",
		"Redmi K50 Ultra",
		"Redmi K60 Ultra",
		"Redmi K20s",
		"Redmi K30s",
		"Redmi K40s",
		"Redmi K50s",
		"Redmi K60s",
		"Xiaomi Mi 5",
		"Xiaomi Mi 6",
		"Xiaomi Mi 8",
		"Xiaomi Mi 9",
		"Xiaomi Mi 10",
		"Xiaomi Mi 11",
		"Xiaomi Mi 12",
		"Xiaomi Mi 13",
		"Xiaomi Mi 5 Pro",
		"Xiaomi Mi 6 Pro",
		"Xiaomi Mi 8 Pro",
		"Xiaomi Mi 9 Pro",
		"Xiaomi Mi 10 Pro",
		"Xiaomi Mi 11 Pro",
		"Xiaomi Mi 12 Pro",
		"Xiaomi Mi 13 Pro",
		"Xiaomi Mi 5 Lite",
		"Xiaomi Mi 6 Lite",
		"Xiaomi Mi 8 Lite",
		"Xiaomi Mi 9 Lite",
		"Xiaomi Mi 10 Lite",
		"Xiaomi Mi 11 Lite",
		"Xiaomi Mi 12 Lite",
		"Xiaomi Mi 13 Lite",
		"Xiaomi Mi 5 Ultra",
		"Xiaomi Mi 6 Ultra",
		"Xiaomi Mi 8 Ultra",
		"Xiaomi Mi 9 Ultra",
		"Xiaomi Mi 10 Ultra",
		"Xiaomi Mi 11 Ultra",
		"Xiaomi Mi 12 Ultra",
		"Xiaomi Mi 13 Ultra",
		"Xiaomi Mix",
		"Xiaomi Mix 2",
		"Xiaomi Mix 3",
		"Xiaomi Mix Alpha",
		"Xiaomi Mix Fold",
		"Black Shark",
		"Black Shark 2",
		"Black Shark 3",
		"Black Shark 4",
		"Black Shark 5",
		"Asus ZenFone 2",
		"Asus ZenFone 3",
		"Asus ZenFone 4",
		"Asus ZenFone 5",
		"Asus ZenFone 6",
		"Asus ZenFone 7",
		"Asus ZenFone 8",
		"Asus ZenFone 9",
		"Asus ZenFone 10",
		"Asus ZenFone 2 Pro",
		"Asus ZenFone 3 Pro",
		"Asus ZenFone 4 Pro",
		"Asus ZenFone 5 Pro",
		"Asus ZenFone 6 Pro",
		"Asus ZenFone 7 Pro",
		"Asus ZenFone 8 Pro",
		"Asus ZenFone 9 Pro",
		"Asus ZenFone 10 Pro",
		"Asus ZenFone 2 Deluxe",
		"Asus ZenFone 3 Deluxe",
		"Asus ZenFone 4 Deluxe",
		"Asus ZenFone 5 Deluxe",
		"Asus ZenFone 6 Deluxe",
		"Asus ZenFone 7 Deluxe",
		"Asus ZenFone 8 Deluxe",
		"Asus ZenFone 9 Deluxe",
		"Asus ZenFone 10 Deluxe",
		"Asus ROG Phone",
		"Asus ROG Phone 2",
		"Asus ROG Phone 3",
		"Asus ROG Phone 5",
		"Asus ROG Phone 6",
		"Asus ROG Phone 7",
		"Asus ROG Phone Pro",
		"Asus ROG Phone 2 Pro",
		"Asus ROG Phone 3 Pro",
		"Asus ROG Phone 5 Pro",
		"Asus ROG Phone 6 Pro",
		"Asus ROG Phone 7 Pro",
		"Asus ROG Phone Ultimate",
		"Asus ROG Phone 2 Ultimate",
		"Asus ROG Phone 3 Ultimate",
		"Asus ROG Phone 5 Ultimate",
		"Asus ROG Phone 6 Ultimate",
		"Asus ROG Phone 7 Ultimate",
		"Realme 1",
		"Realme 2",
		"Realme 3",
		"Realme 5",
		"Realme 6",
		"Realme 7",
		"Realme 8",
		"Realme 9",
		"Realme 10",
		"Realme 11",
		"Realme 1 Pro",
		"Realme 2 Pro",
		"Realme 3 Pro",
		"Realme 5 Pro",
		"Realme 6 Pro",
		"Realme 7 Pro",
		"Realme 8 Pro",
		"Realme 9 Pro",
		"Realme 10 Pro",
		"Realme 11 Pro",
		"Realme 1i",
		"Realme 2i",
		"Realme 3i",
		"Realme 5i",
		"Realme 6i",
		"Realme 7i",
		"Realme 8i",
		"Realme 9i",
		"Realme 10i",
		"Realme 11i",
		"Realme 1s",
		"Realme 2s",
		"Realme 3s",
		"Realme 5s",
		"Realme 6s",
		"Realme 7s",
		"Realme 8s",
		"Realme 9s",
		"Realme 10s",
		"Realme 11s",
		"Realme GT",
		"Realme GT Master Edition",
		"Realme GT Neo",
		"Realme GT Neo 2",
		"Realme GT 3",
		"Realme X",
		"Realme X2",
		"Realme X3",
		"Realme X50",
		"Realme X50 Pro",
		"Realme Narzo",
		"Realme Narzo 20",
		"Realme Narzo 30",
		"Realme Narzo 50",
		"Realme Narzo 60",
		"Oppo Find X",
		"Oppo Find X2",
		"Oppo Find X3",
		"Oppo Find X5",
		"Oppo Find X6",
		"Oppo Find X Pro",
		"Oppo Find X2 Pro",
		"Oppo Find X3 Pro",
		"Oppo Find X5 Pro",
		"Oppo Find X6 Pro",
		"Oppo Reno",
		"Oppo Reno 2",
		"Oppo Reno 3",
		"Oppo Reno 4",
		"Oppo Reno 5",
		"Oppo Reno 6",
		"Oppo Reno 7",
		"Oppo Reno 8",
		"Oppo Reno 9",
		"Oppo Reno 10",
		"Oppo Reno Pro",
		"Oppo Reno 2 Pro",
		"Oppo Reno 3 Pro",
		"Oppo Reno 4 Pro",
		"Oppo Reno 5 Pro",
		"Oppo Reno 6 Pro",
		"Oppo Reno 7 Pro",
		"Oppo Reno 8 Pro",
		"Oppo Reno 9 Pro",
		"Oppo Reno 10 Pro",
		"Oppo Reno Lite",
		"Oppo Reno 2 Lite",
		"Oppo Reno 3 Lite",
		"Oppo Reno 4 Lite",
		"Oppo Reno 5 Lite",
		"Oppo Reno 6 Lite",
		"Oppo Reno 7 Lite",
		"Oppo Reno 8 Lite",
		"Oppo Reno 9 Lite",
		"Oppo Reno 10 Lite",
		"Oppo A3",
		"Oppo A5",
		"Oppo A7",
		"Oppo A9",
		"Oppo A11",
		"Oppo A12",
		"Oppo A15",
		"Oppo A16",
		"Oppo A31",
		"Oppo A32",
		"Oppo A33",
		"Oppo A52",
		"Oppo A53",
		"Oppo A72",
		"Oppo A73",
		"Oppo A74",
		"Oppo A76",
		"Oppo A77",
		"Oppo A78",
		"Oppo K3",
		"Oppo K5",
		"Oppo K7",
		"Oppo K9",
		"Oppo K10",
		"OnePlus One",
		"OnePlus 2",
		"OnePlus 3",
		"OnePlus 3T",
		"OnePlus 5",
		"OnePlus 5T",
		"OnePlus 6",
		"OnePlus 6T",
		"OnePlus 7",
		"OnePlus 7 Pro",
		"OnePlus 7T",
		"OnePlus 7T Pro",
		"OnePlus 8",
		"OnePlus 8 Pro",
		"OnePlus 8T",
		"OnePlus 9",
		"OnePlus 9 Pro",
		"OnePlus 10 Pro",
		"OnePlus 11",
		"OnePlus Nord",
		"OnePlus Nord CE",
		"OnePlus Nord N10",
		"OnePlus Nord N100",
		"OnePlus Nord 2",
		"OnePlus Nord CE 2",
		"OnePlus Nord CE 3",
		"OnePlus Nord 3",
		"Honor 6",
		"Honor 7",
		"Honor 8",
		"Honor 9",
		"Honor 10",
		"Honor 20",
		"Honor 30",
		"Honor 50",
		"Honor 60",
		"Honor 70",
		"Honor 80",
		"Honor 90",
		"Honor 6 Pro",
		"Honor 7 Pro",
		"Honor 8 Pro",
		"Honor 9 Pro",
		"Honor 10 Pro",
		"Honor 20 Pro",
		"Honor 30 Pro",
		"Honor 50 Pro",
		"Honor 60 Pro",
		"Honor 70 Pro",
		"Honor 80 Pro",
		"Honor 90 Pro",
		"Honor 6 Lite",
		"Honor 7 Lite",
		"Honor 8 Lite",
		"Honor 9 Lite",
		"Honor 10 Lite",
		"Honor 20 Lite",
		"Honor 30 Lite",
		"Honor 50 Lite",
		"Honor 60 Lite",
		"Honor 70 Lite",
		"Honor 80 Lite",
		"Honor 90 Lite",
		"Honor X7",
		"Honor X8",
		"Honor X9",
		"Honor X10",
		"Honor X20",
		"Honor X30",
		"Honor X40",
		"Honor Magic",
		"Honor Magic 2",
		"Honor Magic 3",
		"Honor Magic 4",
		"Honor Magic 5",
		"Honor Magic Pro",
		"Honor Magic 2 Pro",
		"Honor Magic 3 Pro",
		"Honor Magic 4 Pro",
		"Honor Magic 5 Pro",
		"Honor Magic Ultimate",
		"Honor Magic 2 Ultimate",
		"Honor Magic 3 Ultimate",
		"Honor Magic 4 Ultimate",
		"Honor Magic 5 Ultimate",
		"ZTE Axon",
		"ZTE Axon 7",
		"ZTE Axon M",
		"ZTE Axon 9",
		"ZTE Axon 10",
		"ZTE Axon 20",
		"ZTE Axon 30",
		"ZTE Axon 40",
		"ZTE Axon 50",
		"ZTE Axon Pro",
		"ZTE Axon 7 Pro",
		"ZTE Axon M Pro",
		"ZTE Axon 9 Pro",
		"ZTE Axon 10 Pro",
		"ZTE Axon 20 Pro",
		"ZTE Axon 30 Pro",
		"ZTE Axon 40 Pro",
		"ZTE Axon 50 Pro",
		"ZTE Axon Ultra",
		"ZTE Axon 7 Ultra",
		"ZTE Axon M Ultra",
		"ZTE Axon 9 Ultra",
		"ZTE Axon 10 Ultra",
		"ZTE Axon 20 Ultra",
		"ZTE Axon 30 Ultra",
		"ZTE Axon 40 Ultra",
		"ZTE Axon 50 Ultra",
		"ZTE Blade V7",
		"ZTE Blade V8",
		"ZTE Blade V9",
		"ZTE Blade V10",
		"ZTE Blade 11",
		"ZTE Blade A3",
		"ZTE Blade A5",
		"ZTE Blade A7"
	]
	
	ios_versions = [
		"8_0",
		"8_0_2",
		"8_1",
		"8_1_1",
		"8_1_2",
		"8_1_3",
		"8_2",
		"8_3",
		"8_4",
		"8_4_1",
		"9_0",
		"9_0_1",
		"9_0_2",
		"9_1",
		"9_2",
		"9_2_1",
		"9_3",
		"9_3_1",
		"9_3_2",
		"9_3_3",
		"9_3_4",
		"9_3_5",
		"9_3_6",
		"10_0",
		"10_0_1",
		"10_0_2",
		"10_0_3",
		"10_1",
		"10_1_1",
		"10_2",
		"10_2_1",
		"10_3",
		"10_3_1",
		"10_3_2",
		"10_3_3",
		"10_3_4",
		"11_0",
		"11_0_1",
		"11_0_2",
		"11_0_3",
		"11_1",
		"11_1_1",
		"11_1_2",
		"11_2",
		"11_2_1",
		"11_2_2",
		"11_2_5",
		"11_2_6",
		"11_3",
		"11_3_1",
		"11_4",
		"11_4_1",
		"12_0",
		"12_0_1",
		"12_1",
		"12_1_1",
		"12_1_2",
		"12_1_3",
		"12_1_4",
		"12_2",
		"12_3",
		"12_3_1",
		"12_3_2",
		"12_4",
		"12_4_1",
		"12_4_2",
		"12_4_3",
		"12_4_4",
		"12_4_5",
		"12_4_6",
		"12_4_7",
		"12_4_8",
		"12_4_9",
		"12_5",
		"12_5_1",
		"12_5_2",
		"12_5_3",
		"12_5_4",
		"12_5_5",
		"12_5_6",
		"12_5_7",
		"13_0",
		"13_1",
		"13_1_1",
		"13_1_2",
		"13_1_3",
		"13_2",
		"13_2_2",
		"13_2_3",
		"13_3",
		"13_3_1",
		"13_4",
		"13_4_1",
		"13_5",
		"13_5_1",
		"13_6",
		"13_6_1",
		"13_7",
		"14_0",
		"14_0_1",
		"14_1",
		"14_2",
		"14_2_1",
		"14_3",
		"14_4",
		"14_4_1",
		"14_5",
		"14_5_1",
		"14_6",
		"14_7",
		"14_7_1",
		"14_8",
		"14_8_1",
		"15_0",
		"15_0_1",
		"15_0_2",
		"15_1",
		"15_1_1",
		"15_2",
		"15_2_1",
		"15_3",
		"15_3_1",
		"15_4",
		"15_4_1",
		"15_5",
		"15_6",
		"15_6_1",
		"15_7",
		"15_7_1",
		"15_7_2",
		"15_7_3",
		"15_7_4",
		"15_7_5",
		"15_7_6",
		"15_7_7",
		"15_7_8",
		"15_7_9",
		"15_8",
		"15_8_1",
		"15_8_2",
		"15_8_3",
		"16_0",
		"16_0_1",
		"16_1",
		"16_1_1",
		"16_1_2",
		"16_2",
		"16_3",
		"16_3_1",
		"16_4",
		"16_4_1",
		"16_5",
		"16_5_1",
		"16_6",
		"16_6_1",
		"16_7",
		"16_7_1",
		"16_7_2",
		"16_7_4",
		"16_7_5",
		"16_7_6",
		"16_7_7",
		"16_7_8",
		"16_7_9",
		"17_0",
		"17_0_1",
		"17_0_2",
		"17_0_3",
		"17_1",
		"17_1_1",
		"17_1_2",
		"17_2",
		"17_2_1",
		"17_3",
		"17_3_1",
		"17_4",
		"17_4_1",
		"17_5",
		"17_5_1",
		"17_6",
		"17_6_1",
		"18_0",
		"18_0_1",
		"18_1"
	]
	
	ios_devices = [
		("iPhone", "CPU iPhone OS"),
		("iPad", "CPU OS"),
		("iPod touch", "CPU iPhone")
	]


@dataclass(frozen=True)
class UserAgentEngine:
	"""
	A class that holds the different engine specific user agent parts.

<<<<<<<< HEAD:PyWebRequests/user_agents/data.py
    Attributes:
        apple_webkit_versions (list[range]): A list of ranges of numbers for AppleWebKit versions.
        gecko_versions (list[typing.Union[range, list[range]]]): A list of ranges of numbers for Gecko versions.
    """
========
	Attributes:
		apple_webkit_versions (list[range]): A list of ranges of numbers for AppleWebKit versions.
		gecko_versions (list[Union[range, list[range]]]): A list of ranges of numbers for Gecko versions.
	"""
>>>>>>>> dev:osn_requests/user_agents/data.py
	apple_webkit_versions = [range(500, 615), range(0, 50), range(1, 50)]
	gecko_versions = [
		range(2015, 2024),
		range(1, 12),
		[range(1, 31), range(1, 30), range(1, 29), range(1, 28)]
	]


@dataclass(frozen=True)
class UserAgentBrowser:
	"""
	A class that holds the different browser specific user agent parts.

<<<<<<<< HEAD:PyWebRequests/user_agents/data.py
    Attributes:
        chrome_versions (list[list[typing.Union[int, range]]]): A list of supported Chrome versions.
        firefox_versions (list[list[typing.Union[int, range]]]): A list of supported Firefox versions.
        safari_versions (list[typing.Union[int, range]]): A list of supported Safari versions.
        opera_versions (list[list[typing.Union[int, range]]]): A list of supported Opera versions.
        edge_versions (list[list[typing.Union[int, range]]]): A list of supported Edge versions.
        yandex_versions (list[list[typing.Union[int, range]]]): A list of supported Yandex versions.
    """
	chrome_versions = [
		[i, 0, range(2200 + 50 * (i - 40), 2250 + 50 * (i - 40)), range(0, 225)]
		for i in range(40, 133)
========
	Attributes:
		chrome_versions (list[list[Union[int, range]]]): A list of supported Chrome versions.
		firefox_versions (list[list[Union[int, range]]]): A list of supported Firefox versions.
		safari_versions (list[Union[int, range]]): A list of supported Safari versions.
		opera_versions (list[list[Union[int, range]]]): A list of supported Opera versions.
		edge_versions (list[list[Union[int, range]]]): A list of supported Edge versions.
		yandex_versions (list[list[Union[int, range]]]): A list of supported Yandex versions.
	"""
	chrome_versions = [
		[i, 0, range(2200 + 50 * (i - 40), 2250 + 50 * (i - 40)), range(0, 225)] for i in range(40, 133)
>>>>>>>> dev:osn_requests/user_agents/data.py
	]
	
	firefox_versions = [[i, 0, range(0, 3)] for i in range(35, 135)]
	
	safari_versions = [range(500, 715), range(0, 50), range(1, 50)]
	
	opera_versions = [
<<<<<<<< HEAD:PyWebRequests/user_agents/data.py
		[i, 0, range(1200 + 50 * (i - 14), 1250 + 50 * (i - 14)), range(15000, 16000)]
		for i in range(14, 96)
	]
	
	edge_versions = [
		[i, 0, range(300 + 50 * (i - 79), 350 + 50 * (i - 79)), range(19, 183)]
		for i in range(79, 133)
========
		[i, 0, range(1200 + 50 * (i - 14), 1250 + 50 * (i - 14)), range(15000, 16000)] for i in range(14, 96)
	]
	
	edge_versions = [
		[i, 0, range(300 + 50 * (i - 79), 350 + 50 * (i - 79)), range(19, 183)] for i in range(79, 133)
>>>>>>>> dev:osn_requests/user_agents/data.py
	]
	
	yandex_versions = [[i, range(1, 12), range(0, 15)] for i in range(15, 25)]
