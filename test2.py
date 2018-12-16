from datetime import date

from businessdate import BusinessDate, BusinessPeriod

BusinessDate(20140101).add_days(10)
#20140111

import nsequoter
nsequoter.get_equity_quote('3MINDIA')
