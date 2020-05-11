##Week 5 Assignment 9.4 ##
## Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a
# Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#fl=input("Enter the file name:")
fh=open("/Users/welcome/Cookbook/mbox-short.txt",'r')
counts=dict()
for line in fh:
    words=line.split()
    #print(words)
    if line.startswith('From '):
        #print (words[1])
        email_address=words[1]
        counts[email_address]=counts.get(email_address,0)+1

largeval=0
largekey=0
leastval=1000000000000000000000000000000000000000000000000000000000000000000000000
leastkey=None
for key, value in counts.items():
    if value>largeval:
        largeval=value
        largekey=key
    if value<leastval:
        leastval=value
        leastkey=key
print(largekey,largeval)

