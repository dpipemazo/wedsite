from wedsite.settings import (DEFAULT_JSON, DEFAULT_ACCESS)

CUSTOMIZED_JSON = DEFAULT_JSON

# Example of how to override/set fields of data. Uncomment to
#	see the Broom's last name changed to "Pandas"
#CUSTOMIZED_JSON['broom']['last_name'] = "Pandas"

# Override the favicon
CUSTOMIZED_JSON['favicon'] = "best-favicon-ever.ico"

CUSTOMIZED_ACCESS = DEFAULT_ACCESS

# Example of how to set access restrictions on certain pages
#	of the site.. Uncomment to be barred from viewing the team
#	page unless logged in.
#CUSTOMIZED_ACCESS['team'] = False