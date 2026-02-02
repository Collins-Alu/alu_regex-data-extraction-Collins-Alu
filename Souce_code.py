import re

class data_extractor:
    def __init__(self):
        self.email_pattern = re.compile (r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,3}$')
                                         
        self.phone_number = re.compile (r'\^(^\d{10}$')
                                        
        self.credit_card_numbers = re.compile (r'\^(\d{16}|\d{4}-\d{4}-\d{4}-\d{4})$')

        self.hashtags = re.compile (r'\^#[a-zA-Z0-9_]+$')

        self.malicious.intent = re.compile (r' <script.*?>.*?<script>|javascript:wait|WaitFor\s+delay|union|s+select', re.IGNORECASE | re.DOTALL)

    def redact_credit_card_number(self, match):

        raw_cc = match.group()

        digits = re.sub(r'\D', '', raw_cc)

        if len(digits) == 16:
            return f"XXXX-XXXX-XXXX-{digits[-4:]}"
        return raw_cc
    
    def process_text(self, raw_text):
        print(f"--- Proccessing Input Stream ({len(raw_text)}) chars) ---\n")
        if self.malicious.intent(raw_text):
            print("ALERT! Malicious intent detected")
            print("Proceed with caution.")

    results = {
            "email":[],
            "phone number":[],
            "Credit card redacted": [],
            "hashtag": []
            }
