import re
import html

class data_extractor:
    def __init__(self):
            #regex for matching an email address
        self.email_pattern = re.compile (r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,3}$')
                                         
        self.phone_number = re.compile (r'\^(^\d{10}$')
                                        
        self.credit_card_numbers = re.compile (r'\^(\d{16}|\d{4}-\d{4}-\d{4}-\d{4})$')

        self.hashtags = re.compile (r'\^#[a-zA-Z0-9_]+$')

    def redact_credit_card_number(self, match):

        raw_cc = match.group()

        digits = re.sub(r'\D', '', raw_cc)

        if len(digits) == 16:
            return f"XXXX-XXXX-XXXX-{digits[-4:]}"
        return raw_cc
    

