""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time

# Instagram credentials
username = "old_question2025"  # Your Instagram username
password = "Samrat@1265"  # Your Instagram password

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username=username, 
                 password=password,
                 want_check_browser=True,
                 headless_browser=False,  # Run in visible mode
                 page_delay=30)  # Increase delay between actions

with smart_run(session):
    """ Activity flow """
    # Add initial delay to ensure proper loading
    time.sleep(15)
    
    # Start with a very simple action - just liking a few photos
    session.set_do_like(enabled=True, percentage=50)
    session.like_by_tags(['nature'], amount=3)  # Start with just one tag and fewer likes
