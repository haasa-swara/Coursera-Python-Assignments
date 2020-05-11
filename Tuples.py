##10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.



fh=open("/Users/welcome/Cookbook/mbox-short.txt")
count=dict()
for line in fh:
    words=line.split()
    #print(words)
    if line.startswith('From '):
        #print(words[5])
        time=words[5]
        #print(time)
        new_time=time.split(':')
        #print(new_time[0])
        count[new_time[0]]=count.get(new_time[0],0)+1
print(sorted(count)) ### sorted(count) returns sorted keys of dictionaries
for key in sorted(count):
    print(key,count.get(key)) ###count.get(key) gives the value for the sorted key