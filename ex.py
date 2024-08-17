from datetime import datetime 
  
start = datetime.strptime("1:40", "%H:%M") 
end = datetime.strptime("11:40", "%H:%M") 
print(str(start))

difference = end - start 
print(str(difference)[:2])


a = ":abcdef"
print(a.split(":"))