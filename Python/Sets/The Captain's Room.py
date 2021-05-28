# Enter your code here. Read input from STDIN. Print output to STDOUT

#Input the group size
K = int(input())
if K>1 and K<1000:
    room_list = list(map(int,input().split()))
    room_set = set(room_list)
    
    output_room = (sum(room_set)*K - sum(room_list))//(K-1)
    print(output_room)
    
    '''
    # METHOD-2 : Takes more time
    #input the room nos assigned to each member
    members_room = list(map(int,input().split()))
    
    #distinctive room no. assigned to each group
    room_list = list(set(members_room))
    
    #determining captain's room
    for i in range(len(room_list)):
        if members_room.count(room_list[i]) == 1:
            print(room_list[i])
    '''
    
