from IPython.display import clear_output

import os
import urllib

def deal_with_duplicates(infile):
    
    lines = []
    frequencies = {}
    with open(infile, "r") as f:
        lines = [line[:-1] for line in f.readlines()]

    N = len(lines)

    with open(infile, "w") as f:
        for i in range(0, N):
#             print("i = {}".format(i+1))
            if i%4 == 0:
                key = lines[i]
                if key in frequencies:
                    frequencies[key] += 1;
                    count = frequencies[key]
                    key = key + str(count)
                else:
                    frequencies[key] = 1
                f.write(key)
                f.write("\n")
            else:
                f.write(lines[i])
                f.write("\n")
                
def get_images(infile, N, out_dir="/home/ankit/Desktop/IIT-G/Code/images"):
    
    deal_with_duplicates(infile)
    lines = []
    with open(infile) as f:
        lines = [line[:-1] for line in f.readlines()]
        lines = lines[:(N*4)]

    for i in range(0, (N*4), 4):
        clear_output(wait=True)
        print(i)
        sample = lines[i : i+4]
        print(sample)
        label = sample[0]
        query = sample[1]
        pos = sample[2]
        neg = sample[3]
        
        try:
            os.mkdir(os.path.join(out_dir, label))
            urllib.request.urlretrieve(query, os.path.join(out_dir, label, "q.png"))
            urllib.request.urlretrieve(pos, os.path.join(out_dir, label, "p.png"))
            urllib.request.urlretrieve(neg, os.path.join(out_dir, label, "n.png"))
        except FileExistsError:
            continue
            
        
    
