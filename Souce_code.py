import re
import html

class data_extractor:
    def __init__(self):
            #regex for matching an email address
        self.email_pattern = re.compile r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,3}$
                                         
        self.phone_number = re.compile r'(^\d{10}$)
                                        
        self.credit_card_numbers = re.compile r'^(\d{16}|\d{4}-\d{4}-\d{4}-\d{4})$'

        self.hashtags = re.compile '^#[a-zA-Z0-9_]+$'

        