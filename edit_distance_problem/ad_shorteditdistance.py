# shortest edit distance algorithm
# an example of dynamical programing

from ex_class_tree import tree


strr = raw_input('Input the original and the target string\n').split()
origin = strr[0]
target = strr[1]
o = len(origin)
t = len(target)

def f(i,j):
    if origin[i] == target[j]:
        return 0
    else:
        return 1


edit = [[i+j for j in range(t+1)] for i in range(o+1)]

for i in range(o):
    j = 0
    while i > -1 and j < t:
        edit[i+1][j+1] = min(edit[i][j+1]+1 , edit[i+1][j]+1, edit[i][j] + f(i,j))
        i += -1
        j += 1
for j in range(t-1):
    i = o-1
    while i > -1 and j < t-1:
        edit[i+1][j+2] = min(edit[i][j+2]+1 , edit[i+1][j+1]+1, edit[i][j+1] + f(i,j+1))
        i += -1
        j += 1

'''
for i in range(o+1):
    print ' '.join([str(edit[i][j]) for j in range(t+1)])
'''
    
print 'The edit distance is %d' % edit[o][t]

dict_prcs = {origin:[]}

def prcs(i,j,temp):    
    if edit[i][j] != 0:
        dict_prcs[temp] = []
        if origin[i-1] == target[j-1]:
            prcs(i-1,j-1,temp)
        else:
            if edit[i-1][j] <= edit[i][j-1] and edit[i-1][j] <= edit[i-1][j-1]:
                lv = temp[:i-1]+temp[i:]
                dict_prcs[temp].append(lv)
                prcs(i-1,j,lv)
            if edit[i][j-1] <= edit[i-1][j] and edit[i][j-1] <= edit[i-1][j-1]:
                lv = temp[:i] + target[j-1] + temp[i:]
                dict_prcs[temp].append(lv)
                prcs(i,j-1,lv)
            if edit[i-1][j-1] <= edit[i][j-1] and edit[i-1][j-1]<= edit[i-1][j]:
                lv = temp[:i-1] + target[j-1] + temp[i:]
                dict_prcs[temp].append(lv)
                prcs(i-1,j-1,lv)

prcs(o,t,origin)

ptree = tree([])
ptree.d = dict_prcs
ptree.dict_reset()
pss = ptree.paths()
method_number = len(pss) 
           
print 'The following are all the methods:'            
for i in range(method_number):
    print '%d. '%(i+1) + '-->'.join(pss[i])
            
                
