import subprocess

# Get all Wi-Fi profiles
data = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    stderr=subprocess.DEVNULL
).decode("utf-8", errors="ignore").split("\n")

profiles = []
for line in data:
    if "All User Profile" in line:
        profiles.append(line.split(":")[1].strip())

print(f'{"WiFi Name":<30} | Password')
print("-" * 50)

for profile in profiles:
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore").split("\n")

        password = ""
        for line in result:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        print(f"{profile:<30} | {password}")

    except Exception:
        print(f"{profile:<30} | Error")
