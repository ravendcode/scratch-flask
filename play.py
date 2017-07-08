# from functools import wraps

from datetime import datetime

d = datetime.now()

print(d.replace(year=d.year + 1))

