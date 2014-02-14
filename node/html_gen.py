from cold_fuzzer import PageHolder

page = PageHolder()
with open('last_page.html', 'w') as f:
	f.write(page)
print page.dump()