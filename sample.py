from pygame import mixer as mix
mix.init()
def play_song(path):
    mix.music.load(path)
    mix.music.play()
    mix.music.set_volume(0.7)
    
def control(inp):   
    if(inp=="stop"):
        mix.music.stop()
    elif(inp=="pause"):
        mix.music.pause()
    elif(inp=="play"):
        mix.music.play()
    elif(inp=="unpause"):
        mix.music.unpause()
if __name__=="__main__":
    print("I'm inside sample.py") 
 
#play_song(r"C:\Users\admin\Desktop\New folder\Nattu Nattu.mp3")

#while True:
    #inp=input("Enter control:")
    #control(inp)