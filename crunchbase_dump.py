from crunchbase import Crunchbase
import tokens

cb = Crunchbase(tokens.CRUNCHBASE_TOKEN)
query = cb.companies

for c in query:
	print(companies)
