Email Address:
([\w.-])it matches one or more word characters,letters,digits,underscore,dots or hyphens at the start
([\w.-])matches one or more word charachters dots or hyphens(domain name) 
([a-zA-Z]{2,3}$)matches a domain extension of 2 to 3 letters at the end

Phone numbers:
(\d{10}$)it matches preceding token exactly 10 times

Credit card:
(\d{16})Exactly 16 digits in a row |/or
(\d{4})blocks of 4 digits separated by dashes

Hashtags:
([a-zA-Z0=9_])Charachter class matching any letter A-Z number 0-9 or underscore

redacted credit cards:
strips non digit  characters to check length
return masked version keeping formatting similar to input

proccess.text:
checks hostile input before processing

