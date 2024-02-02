with open('artifacts.txt','r') as f:
    txt=f.read()

with open('artifacts.txt','w') as f:
    txt=f.write(txt+'added one more line')

print(txt)
print('end of stage 03')