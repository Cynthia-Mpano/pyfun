texts=[]
num = 1
print("enter five texts:")
while num <= 5:
 text= input(f"enter string {num}: ")
 count= len(text.replace(" " , ""))
 texts.append(f"{text} : {count}")
 num = num + 1

print(texts)