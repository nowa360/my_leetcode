"""
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/
"""


def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    res = set()
    for email in emails:
        local, domain = [x for x in email.split('@')]
        plus_idx = local.find('+')
        if plus_idx == -1:
            plus_idx = len(local)

        local = local[:plus_idx].replace('.', '')
        res.add(local + '@' + domain)
    return len(res)
