import subprocess
Wifi_name = input("The name of the Wifi:")
ssids = []
go = "False"
pwd = ""
try:
    results = subprocess.check_output(["netsh","wlan","show","profile","name=",Wifi_name,"key=clear"])
    results = results.decode("ascii")
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]

    x = 0
    while x < len(ls):
        if x % 25 == 0:
            ssids.append(ls[x])
        x += 1


    for each in ssids[1]:
        if ":" in each:
            go = "True"
        if go == "True":
            pwd += (each)
    if len(pwd) >= 8:
        print("Your password of",pwd)
    else:
        print("You have not connected to this network before.")
except:
    print("The wifi name is wrong please retry with the correct wifi name.")

    

        

