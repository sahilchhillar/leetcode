def createProperEmail(email):
    local, domain = email.split('@')
    newLocal = ""
    for _, char in enumerate(local):
        if char.isalpha():
            newLocal += char
        elif char == '.':
            continue
        elif char == '+':
            break
    return newLocal + '@' + domain

def uniqueEmails(emails):
    count = set()
    for email in emails:
        # Solution 1
        # new_email = createProperEmail(email)
        # print(new_email)
        # count.add(new_email)

        # Solution 2
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        count.add(local+'@'+domain)
    return len(count)

print(uniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))