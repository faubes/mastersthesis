for a in range(0,6):
    for b in range(2,6):
        for c in range(1,6):
            for d in range(2,6):
                file = open("Graphs/2Chord" + str(a) + "-" + str(b) + "-" + str(c) + "-" + str(d) + ".txt", "w")
                file.write(str(a+b+c+d) + "\n")
                for k in range(0,a+b+c+d):
                    if(k == 0 and a == 0):
                        line = str(k+1) + "," + str(a+b) + "," + str(a+b+c) + "," + str(a+b+c+d-1)
                    elif(k == 0 and a != 0):
                        line = str(k+1) + "," + str(a+b+c) + "," + str(a+b+c+d-1)
                    elif(k == a):
                        line = str(k+1) + "," + str(a+b) + "," + str(k-1)    
                    elif(k == a+b):
                        line = str(a) + "," + str(k-1) + "," + str(k+1)
                    elif(k == a+b+c):
                        line = "0," + str(k-1) + "," + str(k+1)
                    elif(k == a+b+c+d-1):
                        line = str(k-1) + ",0"  
                    else:
                        line = str(k-1) + "," + str(k+1)
                    file.write(line + "\n")
                file.close()
                
