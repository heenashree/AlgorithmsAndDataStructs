def validPhoneNumber(phoneNumber):
    import re
    regex = r"(\({1}\d{3}\){1}\s{1}\d{3}\-{1}\d{4})"
    if re.search(regex, phoneNumber):
        match = re.search(regex, phoneNumber)

        # The groups contain the matched values.  In particular:
        #    match.group(0) always returns the fully matched string
        #    match.group(1) match.group(2), ... will return the capture
        #            groups in order from left to right in the input string
        #    match.group() is equivalent to match.group(0)

        # So this will print "June 24"
        print ("Full match: %s" % (match.group(0)))
    else:
        print ("The regex pattern does not match. :(")



validPhoneNumber("(123) 456-7890")
def create_phone_number(n):
  print  (''.join(str_list[3:6]))

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])