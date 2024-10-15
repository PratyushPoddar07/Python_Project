import pyscreenshot as ImageGrab
from datetime import datetime
import time
import os
import schedule as sb

def take_screenshot():
    print("Taking screenshot....")

    image_name =f"scrrenshot-{str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}"
    
    # create the screenshots directory if it doesn't exist

    screenshot_dir ="./screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    filepath = f"./screenshots/{image_name}.png"
    
    # taking ss 
    screenshot = ImageGrab.grab()


    screenshot.save(filepath)

    print(f"Screenshot svaed at {filepath}")
    return filepath

def main():
    sb.every(5).seconds.do(take_screenshot)

    start_time = time.time()

    while True:
        # sb.run_pending()
        # time.sleep(1)

        sb.run_pending()
        # check if 5 seconds have passed
        elapsed_time =time.time() - start_time
        if elapsed_time > 5:
            print("Stopping screenshot process after 5 seconds.")
            break

        time.sleep(1)
        
if __name__== '__main__':
    main()