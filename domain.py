import dns.resolver 

if __name__ == '__main__':
	loookup_continue = True
	while loookup_continue:
		name = input('Enter the DNS name to resolve: ')
		record_type = input('Enter the query type\
		[A/MS/CNAME]: ')
		answers = dns.resolver.query(name, record_type)
		if record_type == 'A':
			print('Got answer IP address: %s' %[x.to_text() for x\
			in answers])
		elif record_type == 'CNAME':
			print('Got answer Aliases: %s' %[x.to_text() for x in\
			answers])
		elif record_type == 'MX':
			for rdata in answers:
				print('Got answers for mail server records:')
				print('Mailserver', rdata.exchange.to_text(), 'has preference', rdata.preference)
			print('Record type: %s is not implemented'
			%record_type)
		lookup_more = input("Do you want to lookup more records? [y/n]: ")
		if lookup_more.lower() == 'n':
			loookup_continue = False

