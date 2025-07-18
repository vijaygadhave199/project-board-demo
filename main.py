# main.py
# In progress: Replacing print with logging
import logging
logging.basicConfig(level=logging.INFO)
def greet():
    logging.info("Hello, GitHub!")  # ✅ Refactored
    print("Legacy greeting")        # ❌ Still needs conversion
greet()
