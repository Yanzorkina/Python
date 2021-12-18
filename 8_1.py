import re


def email_parse(email):

        mail_valid = re.compile(r'(?P<name>\w+)@(?P<domain>\w+\.\w+)', re.IGNORECASE)
        try:
            if not mail_valid.match(email):
                raise ValueError(f'wrong email: {email}')
            print(mail_valid.match(email).groupdict())
        except ValueError as e:
            print(e)



email_parse("dfdfdf@sdsd.er")
email_parse("dfdfdf@sdsder")

