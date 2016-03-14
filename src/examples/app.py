#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Nexmo API
# Copyright (c) 2008-2016 Hive Solutions Lda.
#
# This file is part of Hive Nexmo API.
#
# Hive Nexmo API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Nexmo API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Nexmo API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

class NexmoApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "nexmo",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.balance()

    @appier.route("/balance", "GET")
    def balance(self):
        api = self.get_api()
        balance = api.balance_account()
        return balance

    @appier.route("/sms", "GET")
    def sms(self):
        sender = self.field("sender")
        receiver = self.field("receiver")
        text = self.field("text")
        api = self.get_api()
        result = api.send_sms(sender, receiver, text)
        return result

    def get_api(self):
        return base.get_api()

if __name__ == "__main__":
    app = NexmoApp()
    app.serve()
