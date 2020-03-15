import requests
import json

class Domains:
    base_url='https://api.transip.nl/v6'
    base_url_domains=base_url + '/domains'
    def __init__(self, headers):
        self.headers = headers

    def list_domains(self):
        url = self.base_url_domains
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting domains failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def retrieve_domain(self, domain):
        url = self.base_url_domains + '/' + domain
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Retrieve domain "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def register_domain(self, data):
        url = self.base_url_domains
        res = requests.post(url, headers=self.headers, data=data)
        if res.status_code != 201:
            print('Creating/Transfering domain failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return

    def tranfer_domain(self, data):
        return Domains.register_domain(self, data)

    def update_domain(self, data):
        url = self.base_url_domains
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Creating/Transfering domain failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return

    def cancel_domain(self, domain, immediately=False):
        if immediately:
            data = '{"endTime": "immediately"}'
        else:
            data = '{"endTime": "end"}'
        url = self.base_url_domains + '/' + domain
        res = requests.delete(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Canceling domain failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return

    def get_domain_branding(self, domain):
        url = self.base_url_domains + '/' + domain + '/branding'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Get domain branding for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def update_domain_branding(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/branding'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Update domain branding for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return

    def list_contacts(self, domain):
        url = self.base_url_domains + '/' + domain + '/contacts'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('List domain contacts for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def update_contacts(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/contacts'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Update contacts for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return

    def list_dns_entries(self, domain):
        url=self.base_url_domains + '/' + domain + '/dns'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting dns entries for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def add_dns_entry(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/dns'
        res = requests.post(url, headers=self.headers, data=data)
        if res.status_code != 201:
            print('Creating dns entry for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data was: {0}'.format(data))
            exit(1)
        return

    def update_dns_entry(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/dns'
        res = requests.patch(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Updating dns entry for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def update_all_dns_entries(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/dns'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Updating all dns entries for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def delete_dns_entry(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/dns'
        res = requests.delete(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Deleting dns entry for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def list_dnssec_entries(self, domain):
        url=self.base_url_domains + '/' + domain + '/dnssec'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting dnssec entries for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def update_all_dnssec_entries(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/dnssec'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Updating all dnssec entries for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def list_nameservers(self, domain):
        url=self.base_url_domains + '/' + domain + '/nameservers'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting nameservers for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def update_nameservers(self, domain, data):
        url = self.base_url_domains + '/' + domain + '/nameservers'
        res = requests.put(url, headers=self.headers, data=data)
        if res.status_code != 204:
            print('Updating nameservers for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return

    def list_ssl(self, domain):
        url=self.base_url_domains + '/' + domain + '/ssl'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Listing ssl for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def whois(self, domain):
        url=self.base_url_domains + '/' + domain + '/whois'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Whois for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def whitelabel(self):
        url=self.base_url + '/whitelabel'
        res = requests.post(url, headers=self.headers)
        if res.status_code != 201:
            print('Whitelabel request failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def domain_availability(self, domain):
        url=self.base_url + '/domain-availability/' + domain
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Checking availability for "{0}" failed with status code: {1}'.format(domain, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def domains_availability(self, data):
        url=self.base_url + '/domain-availability'
        res = requests.get(url, headers=self.headers, data=data)
        if res.status_code != 200:
            print('Checking availability for multiple domains failed with status code: {0}'.format(res.status_code))
            print(res.text)
            print('Data: ' + data)
            exit(1)
        return json.loads(res.text)

    def list_tlds(self):
        url=self.base_url + '/tlds'
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Listing tlds failed with status code: {0}'.format(res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)

    def info_tld(self, tld):
        url=self.base_url + '/tlds/.' + tld
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            print('Getting info about tld "{0}" failed with status code: {1}'.format(tld, res.status_code))
            print(res.text)
            exit(1)
        return json.loads(res.text)
