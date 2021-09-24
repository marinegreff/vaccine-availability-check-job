#!/usr/bin/env python
import preprocessing

from_email = "@gmail.com"
to_email = ""

# This will need to allow less secure apps to access the gmail account (see Google's instructions to change this in the account settings)
# This will also need an app-specific password to be created (because 2-step verification)
smtp_token = "" # Token to authorize the sending of emails from the From email.

clinique_id = "" # Id of the vaccine clinique, to be found when browsing mittvaccin.se
appointment_id = "" # Appointment Id, to be found when browsing mittvaccin.se
