import re

s = "location.href = '/Facility/Details/cb6afcfa-c528-43ff-b42d-a14ea85f7377'"
m = re.search(r"'([^']*)'", s)

print(m.group(1))

add = "236 22 St E Prince Albert SK S6V 1N1"

community = "Prince Albert"

new = add.split(community)

print(new[0][:-1], community + new[1])