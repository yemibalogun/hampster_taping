import uiautomator as u
import time
from datetime import datetime


# Connect to the device
d = u.Device()

# Get the screen width and height
width = d.info['displayWidth']
height = d.info['displayHeight']

# Calculate the center coordinates
center_x = int(width / 2)
center_y = int(height / 2)

while True:
	# Tap the center of the screen
	taps = 0
	start_time = time.time() # Record the star time

	# Perform 3,500 taps
	while taps < 1150:
		print(f"starting taps at: {start_time}")
		d.click(center_x, center_y)
		taps += 1
		time.sleep(0.01)  # Add a delay to avoid overwhelming the device
	
	end_time = time.time() # Recore the end time
	elapsed_time = end_time - start_time # Calculate the elapsed time 

	print(f"Completed {taps} taps in {elapsed_time:.2f} seconds!")
	print("...waiting for 30min")
	now = datetime.now()
	formatted_now = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
	print(formatted_now)

	# Delay for 1,833 seconds
	time.sleep(1833)
	
	time_after_delay = datetime.now()
	formatted_time_after_delay = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
	print(f"Time after delay: {formatted_time_after_delay}")
	print('Delay time completed')
