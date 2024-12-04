import os
import shutil

def count_elements(v):
    
    elements=0

    for i in v:
        elements=elements+1
    
    return elements

def create(file):
    if not os.path.isdir(file):
        os.mkdir(file)

def move(i,path):
    shutil.move( i , directory_path+"/"+ path)

extensions=["Text Files","Photo Files","Pdf Files","Word Files","Excel Files","Video Files","Jar Files","STL Files","Audio Files",
            "Rar Files","Zip Files","PowerPoint Files","Exe Files","Fzpz Files","Drawio Files","Fantome Files","Apk Files","DLL Files",
            "C Files","Html_Javascript_Css","Log Files"]
    
strangedir="Strange Files"

elements=count_elements(extensions)

directory_path=os.getcwd()
files=os.listdir(directory_path)

for i in files:

    verified=False

    #Text
    if i.endswith(".txt"):
        create(extensions[0])
        move(i,extensions[0])
    
    #Foto
    elif i.endswith(".jpg") or i.endswith(".jfif") or i.endswith(".dng") or i.endswith(".JPG") or i.endswith(".png") or i.endswith(".gif") or i.endswith(".webp") or i.endswith(".tiff") or i.endswith(".psd") or i.endswith(".raw") or i.endswith(".bmp") or i.endswith(".heif") or i.endswith(".indd") or i.endswith(".svg") or i.endswith(".jpeg"):
        create(extensions[1])
        move(i,extensions[1])
    
    #PDF
    elif i.endswith(".pdf"):
        create(extensions[2])
        move(i,extensions[2])
    
    #Word
    elif i.endswith(".docx"):
        create(extensions[3])
        move(i,extensions[3])
    
    #Excel
    elif i.endswith(".xls"):
        create(extensions[4])
        move(i,extensions[4])
        
    #Video
    elif i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi") or i.endswith(".mov") or i.endswith(".wmv") or i.endswith(".flv") or i.endswith(".webm") or i.endswith(".3gp") or i.endswith(".ogv") or i.endswith(".m4a"):
        create(extensions[5])
        move(i,extensions[5])
     
    #Jar    
    elif i.endswith(".jar"):
        create(extensions[6])
        move(i,extensions[6])
    
    #STL
    elif i.endswith(".stl"):
        create(extensions[7])
        move(i,extensions[7])
    
    #MP3    
    elif i.endswith(".mp3") or i.endswith(".aac") or i.endswith(".ogg") or i.endswith(".wma") or i.endswith(".flac") or i.endswith(".alac") or i.endswith(".ape") or i.endswith(".wav") or i.endswith(".aiff") or i.endswith(".opus") or i.endswith(".midi") or i.endswith(".mid"):
        create(extensions[8])
        move(i,extensions[8])
    
    #RAR
    elif i.endswith(".rar") or i.endswith(".7z"):
        create(extensions[9])
        move(i,extensions[9])
    
    #ZIP    
    elif i.endswith(".zip"):
        create(extensions[10])
        move(i,extensions[10])
    
    #PowerPoint
    elif i.endswith(".pptx"):
        create(extensions[11])
        move(i,extensions[11])
    
    #Exe    
    elif i.endswith(".exe"):
        create(extensions[12])
        move(i,extensions[12])
    
    #Fzpz    
    elif i.endswith(".fzpz") or i.endswith(".fzz"):
        create(extensions[13])
        move(i,extensions[13])

    #Drawio
    elif i.endswith(".drawio"):
        create(extensions[14])
        move(i,extensions[14])
    
    #Fantome    
    elif i.endswith(".fantome"):
        create(extensions[15])
        move(i,extensions[15])
    
    #Apk    
    elif i.endswith(".apk"):
        create(extensions[16])
        move(i,extensions[16])
    
    #Dll    
    elif i.endswith(".dll"):
        create(extensions[17])
        move(i,extensions[17])
    
    #C    
    elif i.endswith(".c") or i.endswith(".h"):
        create(extensions[18])
        move(i,extensions[18])
    
    #Website    
    elif i.endswith(".index") or i.endswith(".css") or i.endswith("js") or i.endswith(".html"):
        create(extensions[19])
        move(i,extensions[19])
    
    #Log    
    elif i.endswith(".log"):
        create(extensions[20])
        move(i,extensions[20])
    
    else:
        
        for file in range(elements-1):
            
            if i == extensions[file] or i == "FileOrganizer.py":
        
                verified=True
        
        if not verified:
            create(strangedir)
            move(i,strangedir)