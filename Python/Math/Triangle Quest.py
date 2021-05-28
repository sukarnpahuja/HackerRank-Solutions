for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10 ** i - 1) // 9) * i)
    
    #we need to get a number that when multiples by i yielded 1,22,333,444. Thus, we needed to have values 1,11,111,1111. (rep-unit)
    # refer document --> http://www.fact-index.com/r/re/repunit.html
