import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

profiles = [] 
for i in data:
    if "All User Profile" in i:        
        profiles.append(i.split(":")[1][1:-1])

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')

result = []
for j in results:
    if "Key Content" in j:
        result.append(j.split(":")[1][1:-1])

    try:
        print("{:<30}|  {:<}".format(i, result[0]))
    except Exception as e:
        print("{:<30}|  {:<}".format(i, ""))

    except Exception as e:
        print("{:<30}|  {:<}".format(i, "Error Occurred"))    


