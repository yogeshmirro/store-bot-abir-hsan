import re
from configs import Config
async def rmw(cap):
    caps = re.sub(Config.REMOVE_WORD,"",cap)
    return caps
#     for i in Config.REMOVE_WORD:
#         if i in cap:
#             try:
#                 cap1 = cap.replace(f"{i}","")
#                 cap = cap1
#             except:
#                 pass
#         else:
#             continue
#     return cap
