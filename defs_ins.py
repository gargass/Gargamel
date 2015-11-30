
# coding: utf-8

# In[ ]:

def zagraj_ins(katalog, dzwiek, time):
    """
    Granie nuty na instrumencie
    
    Wywołanie: zagraj_ins(katalog, dzwiek, fs, time)
    katalog - nazwa katalogu z utworem
    dzwiek - napis z nazwą instrumentu i nuty
    time - czas trwania dźwięku
    """
    import numpy as np
    S=pow(2, 1/6)
    f=440
    fs=44100
    defs_notes=eval(open('defs_notes.txt').read())
    p=1
    a=0
    l=1
    t_echo=1
    ob_echo=1
    czy_up=0
    up=1
    up_1=0
    up_2=0
    czy_down=0
    down=1
    down_1=0
    down_2=0
    funkcja='sin(x)'
    if len(dzwiek)!=3:
        defs_ins=eval(open(katalog+'/sample'+dzwiek[0:2]+'.txt').read())

    
        p=defs_ins["power"]
        a=defs_ins["a"]
        l=defs_ins["long"]
        t_echo=defs_ins["times"]
        ob_echo=defs_ins["obniz"]
    
        czy_up=defs_ins["czy_up"]
        up=defs_ins["up"]
        up_1=defs_ins["up_1"]
        up_2=defs_ins["up_2"]
    
        czy_down=defs_ins["czy_down"]
        down=defs_ins["down"]
        down_1=defs_ins["down_1"]
        down_2=defs_ins["down_2"]   
    
        funkcja=defs_ins["funkcja"]
        nuta=dzwiek[3:6]
    else:
        nuta=dzwiek
        
    time=time*l
    t = np.linspace(0, time, time*fs)
    k=6*(np.fromstring(nuta[2], dtype=int, sep=',')-4)+defs_notes[nuta[0]]-4.5+defs_notes[nuta[1]]
    x=2*np.pi*440*(t+a)*(S**k)
    
    if funkcja=="sin(x)":
        y_tmp=np.sign(np.sin(x))*np.abs(np.sin(x))**p
    if funkcja=="arcsin(sin(x))":
        y_tmp=np.sign(np.arcsin(np.sin(x)))*np.abs(np.arcsin(np.sin(x)))**p
        
    y=np.zeros(t_echo*len(y_tmp))
    
    for i in range(t_echo):
        y[i*len(y_tmp):(i+1)*len(y_tmp)]=y_tmp*ob_echo**i
   
    if czy_up:
        i1=int(len(y)*up_1)
        i2=int(len(y)*up_2)
        y[i1:i2] *= np.linspace(up,1,i2-i1)
    if czy_down:
        i1=int(len(y)*down_1)
        i2=int(len(y)*down_2)
        y[i1:i2] *= np.linspace(1,down,i2-i1)

    return y



