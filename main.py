import os, sys,dns.resolver
from dns.exception import DNSException
print("DomainTaker \nAuthor: MarkusHaas2002(Github) | Markusbug(Twitter)")
def check(domain):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    try:
        answer = resolver.query(domain,"CNAME")
        for data in answer:
            print(data+";"+domain)
    except DNSException:
        """Nothing"""
try:
    domain = sys.argv[1]
except:
    print("No Parameter Provided.\nUse: python main.py [Domain]")
    exit()
if domain is None:
    print("No Parameter Provided.")
    exit()
os.system("sublist3r -d "+domain+" -o "+domain+".txt")
with open(domain+".txt") as f:
    content = f.read().splitlines()
i = 0
while i < len(content):
        check(content[i])
        i += 1
exit()
