from datetime import datetime
import pytz


def get_now_time():
    now = datetime.now(pytz.timezone('Europe/Kiev'))
    # Convert to naive datetime
    return now.replace(tzinfo=None)
