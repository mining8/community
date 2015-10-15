# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class DNS_TLD_PW(Signature):
    name = "dns_tld_pw"
    description = "Resolves .PW TLD, Possibly Malicious"
    severity = 2
    categories = ["tldwatch"]
    authors = ["RedSocks"]
    minimum = "2.0"

    domains_re = [
        ".*\\.pw",
    ]

    def on_complete(self):
        for indicator in self.domains_re:
            match = self.check_domain(pattern=indicator, regex=True)
            if match:
                self.mark_ioc("domain", match)

        return self.has_marks()
