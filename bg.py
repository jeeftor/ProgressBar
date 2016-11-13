import time
from workflow import Workflow3

wf = Workflow3()
time.sleep(5)

# Store results in The cache so we can pick them up from elsewhere

wf.store_data('bg_result', "HELLO")
