from notifypy import Notify
import time


notification = Notify(
  default_notification_title="Protect Eyes",
  default_application_name="Eye Protect",
  default_notification_icon="./EyeProtect.png",
  default_notification_audio="./sound.wav"
)

def your_function():
  time.sleep(1200)
  notification.message = "Rest for 20 Seconds to one Minute"
  notification.send()



while(True):
    your_function()
    time.sleep(20)
    notification.message = "You can WorK Again"
    notification.send()


