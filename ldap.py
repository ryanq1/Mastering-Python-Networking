import ldap

ldap_client = ldap.initialize("ldap://10.0.2.15:389/")

ldap_client.simple_bind("dc=localdomain,dc=loc")

base_dn = 'ou=users,dc=localdomain,dc=loc'
filter = '(objectclass=person)'
attrs = ['sn']

result = ldap_client.search_s(base_dn, ldap.SCOPE_SUBTREE,
      filter, attrs)
print(result)

