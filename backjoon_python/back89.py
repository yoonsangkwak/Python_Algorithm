# 4673번

def self_number():
    self_list = []
    num_list = []
    for i in range(1, 10001):
        self_list.append(i)
        for j in range(len(str(i))):
            if len(str(i)) == 4:
                num = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
            elif len(str(i)) == 3:
                num = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
            elif len(str(i)) == 2:
                num = i + int(str(i)[0]) + int(str(i)[1])
            elif len(str(i)) == 1:
                num = i + i

            if num <= 10000:
                num_list.append(num)
        
    for k in range(len(num_list)):
        if num_list[k] in self_list:
            self_list.remove(num_list[k])
    
    for x in self_list:
        print(x)
        
self_number()