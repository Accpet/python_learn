#__author__ = 'water'
d={'try':39,'huaishuo':100,'gid':20}
print d['try']
print d['huaishuo']
print d['gid']

print 'gid' in d
print d.get('try')
print d.get('www')
print d.get('www',-1)

print d.pop('try')
print d
d['key'] = 2000
print d