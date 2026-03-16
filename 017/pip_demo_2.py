# Установи: pip install humanize
import humanize
from datetime import datetime, timedelta

now = datetime.now()
hour_ago = now + timedelta(hours=10)

print(humanize.naturaltime(hour_ago))  # "an hour ago"
print(humanize.naturalday(now))        # "today"

