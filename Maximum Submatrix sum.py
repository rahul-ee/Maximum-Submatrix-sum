#r,c = [int(x) for x in input().split(' ')]
#matrix = [[int(x) for x in input().split(' ')] for _ in range(r)]
#left,right = 0,0
r,c = 4,5
matrix = [[1, 2, -1, -4, -20], 
     [-8, -3, 4, 2, 1],  
     [3, 8, 10, 1, 3],  
     [-4, -1, 1, 7, -6]] 
current_sum = 0
max_sum = -9999999
max_left,max_right,max_up,max_down = 0,0,0,0
temp_up,temp_down = 0,0

for i in range(c):
    temp = [0 for _ in range(r)]
    for j in range(i,c):
        for k in range(r):
            temp[k] = temp[k] + matrix[k][j]
        
        max_ending_here = 0
        max_so_far = -9999999
        for l in range(r):
            max_ending_here = max_ending_here + temp[l]
            if max_ending_here>max_so_far:
                max_so_far = max_ending_here
                temp_down = l
            if max_ending_here<0:
                max_ending_here = 0
                temp_up = l+1
        #print(temp,max_so_far)
        current_sum = max_so_far
        
        if max_sum<current_sum:
            max_sum = current_sum
            max_up = temp_up
            max_down = temp_down
            max_left = i
            max_right = j
        #print(temp,i,j,current_sum,max_sum,max_left,max_right,max_up,max_down)
print(max_sum , [max_up,max_left],[max_down,max_right])
            
        


        
        
