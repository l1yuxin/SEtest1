path = "C:\\Users\\user\\Desktop\\yq_in.txt"
with open(path,'r',encoding = 'GBK') as f:
    a = [line.split() for line in f]

a_All = []
a_Part = []
for msd_id,a_type,a_data in a:
    a_Part.append([a_type, '\t', a_data, '\n'])
    a_All.append([msd_id,a_type,a_data])


l = len(a_All)
t = open("输出.txt",'w',encoding = 'GBK')
province = a_All[0][0]
flag = 0
for i in range(0,l):
    if flag == 0:
        t.write(a[i][0]+'\n')
        flag = 1
    if a_All[i][0] == province:
        t.writelines(a_Part[i])
    else:
        province = a_All[i][0]
        flag = 0
        t.write('\n')
