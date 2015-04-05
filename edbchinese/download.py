import urllib

N = 4762
for i in range(1, N+1):
    _id = '%04d' % i
    url = "http://www.edbchinese.hk/lexlist_en/result.jsp?id=%s" % _id
    print url
    f = urllib.urlopen(url)
    html = f.read()
    h = open('data/'+_id+'.html', 'w')
    h.write(html)
    h.close()
