import subprocess

def offline_process():
    p = subprocess.Popen('satdump meteor_hrpt cadu "C:/Users/Justin Isa/Downloads/crosswalkersam_meteor_hrpt_2022_04_08_14_14_42.cadu" "C:/Users/Justin Isa/Desktop/SatDumpTest" --samplerate 3000000',
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        shell = True)
    
    output, error = p.communicate()
    if p.returncode == 0:
        print("Success")
    else:
        print("Error: ", error)
        print("Output: ", output)

def live_process():
    p = subprocess.Popen('satdump live ')

def record_process():
    p = subprocess.Popen('satdump record cadu "C:/Users/Justin Isa/Desktop/SatDumpTest" --source rtlsdr --frequency 1700e6 --samplerate 3e6 --gain 40',
            stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        shell = True)

            output, error = p.communicate()
    if p.returncode == 0:
        print("Success")
    else:
        print("Error: ", error)
        print("Output: ", output)
