#__author__ = 'water'
d={'wml':39,'huaishuo':100,'gid':20}
print d['wml']
print d['huaishuo']
print d['gid']

print 'gid' in d
print d.get('wml')
print d.get('www')
print d.get('www',-1)

print d.pop('wml')
print d
d['key'] = 2000
print d