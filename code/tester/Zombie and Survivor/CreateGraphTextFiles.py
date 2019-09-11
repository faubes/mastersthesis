for m in range(2,11):
    for n in range(m,11):
        file = open("Graphs/Q" + str(m) + "-" + str(n) + ".txt", "w")
        file.write(str(m+n) + "\n")
        for k in range(0,m+n):
            
            if(k == 0):
                line = str(k+1) + "," + str(m) + "," + str(m+n-1)
            elif(k == m):
                line = "0," + str(k-1) + "," + str(k+1)
            elif(k == n+m-1):
                line = str(k-1) + ",0"  
            else:
                line = str(k-1) + "," + str(k+1)
            file.write(line + "\n")
        file.close()
