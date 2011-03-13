import os, time, datetime;

file_path = '/Users/Jams/Documents/workspace/OpenFile/testTxt/'
file_name = '1.txt'


print "file at: %s" % file_path + file_name
actual_file = open(file_path + file_name, 'r')
for eachline in actual_file:
	eachline.strip()
	print eachline
#file_stats = os.stat(file_path+file_name)
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file_path + file_name)

print mode
print ino
print dev
print nlink
print uid
print gid
print size
print datetime.datetime.fromtimestamp(atime)
print "created: %s" % datetime.datetime.fromtimestamp(ctime)
print "last modified: %s" % datetime.datetime.fromtimestamp(mtime)


[ 
{	"modifydate":"12312341234.13241",
	"tags":['todo','today'],
	"deleted":0,
	"createdata":"12312341234.13241",
	"systemtags":[],

}
]