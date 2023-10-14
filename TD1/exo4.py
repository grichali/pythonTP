total_seconds = int(input("Veuillez sasir le nombre de seconds "))

hours = total_seconds // 3600 
tmp = total_seconds % 3600 
minutes = tmp // 60
seconds = tmp % 60 
print(f"{hours} h {minutes} min {seconds} second")