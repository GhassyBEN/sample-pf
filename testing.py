"""Module providing a function printing python version."""

import sys
from datetime import datetime

from timeline import ProjectTimelines

# from dateutil.relativedelta import relativedelta

print(sys.version)
print(sys.executable)

DSD = datetime(2018, 1, 1)
DP = 20
CP = 30
OP = 30
MPCOD = 1
MTCOD = 3

pr_timelines = ProjectTimelines(DSD, DP, CP, OP, MPCOD, MTCOD)
pr_df = pr_timelines.df
print(pr_df)
# fc = dsd + relativedelta(months=dp)
# print(fc)

name = input('Your Name?')
print(name)