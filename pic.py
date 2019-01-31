WIDTH=500
HEIGHT=500
MAXVAL=255

retstr=""

def header():
    top="P3 \n"
    size=str(HEIGHT) + " "+str(WIDTH)+"\n"
    max=str(MAXVAL)+"/n"
    retstr=top+size+max
    write(retstr)
    
def main():
    file=open("image.ppm","w")
    header()
    file.close()

main()
