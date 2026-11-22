"""Run mitmdump with a mobile-compatible leaf certificate lifetime."""

import datetime

from mitmproxy import certs
from mitmproxy.tools.main import mitmdump

# Chromium/Cronet rejects certificates whose validity period exceeds its
# current public-CA limit.  mitmproxy's default is 365 days; keeping the
# generated leaf certificate below 200 days avoids that rejection while the
# project CA remains unchanged.
certs.CERT_EXPIRY = datetime.timedelta(days=180)


def main() -> None:
    mitmdump()


if __name__ == "__main__":
    main()
