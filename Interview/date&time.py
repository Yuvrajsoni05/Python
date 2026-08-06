from datetime import datetime, timedelta

now = datetime.now()

# tomorrow = now + timedelta(days=1)
# yesterday = now - timedelta(days=1)

# tomorrow = tomorrow.strftime("%Y-%m-%d")
# yesterday = yesterday.strftime("%Y-%m-%d")

# print(tomorrow, yesterday)


next_cam_datetime = now + timedelta(days=3)

current_date = now.strftime("%Y-%m-%d")

next_cam_date = next_cam_datetime.strftime("%Y-%m-%d")
if next_cam_datetime.strftime("%A") == "Saturday":
    next_cam_datetime = next_cam_datetime + timedelta(days=2)
    next_cam_date = next_cam_datetime.strftime("%Y-%m-%d")
elif next_cam_datetime.strftime("%A") == "Sunday":
    next_cam_datetime = next_cam_datetime + timedelta(days=1)
    next_cam_date = next_cam_datetime.strftime("%Y-%m-%d")


print(current_date)
print(next_cam_date)
