import hashlib 
import string 

#opens csv and hashes each row to md5

with open("original.csv", 'rb') as file:
    with open("target.csv", 'w') as output:
        for line in file:
            line=line.strip()
            print hashlib.md5(line).hexdigest()
            output.write(hashlib.md5(line).hexdigest() +'\n')
            