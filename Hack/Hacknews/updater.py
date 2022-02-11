from .views import sync_items
from apscheduler.schedulers.background import BackgroundScheduler


#this function defines the scheduler by invoking the constructor BackgroundScheduler.
#the variable scheduler is then used to kickstart the scheduler using the .add_job method to determine the function to schedule
#and the .start() to start the task based on the interval specified.
#this whole operation works in the background because the class used BackgroundScheduler()
def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(sync_items, "interval", minutes=5)
    scheduler.start()