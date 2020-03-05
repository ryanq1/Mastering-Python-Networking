import ntplib
from time import ctime

HOST_NAME = 'pool.ntp.org'

if __name__ == '__main__':
	params = {}
	client = ntplib.NTPClient()
	response = client.request(HOST_NAME)
	print('Receieved time: %s' %ctime(response.tx_time))
	print('ref_clock: ',ntplib.ref_id_to_text(response.ref_id,response.stratum))
	print('stratum: ',response.stratum)
	print('last_update: ', response.ref_time)
	print('offset: %f', response.offset)
	print('precision: ', response.precision)
	print('root_delay: %.6f' %response.root_delay)
	print('root_dispersion: %.6f' %response.root_dispersion)
