if __name__=='__main__':
    
    print(' Rozpakowanie bibliotek: ', end="")
    import sys
    import numpy as np
    import scipy.signal
    import scipy.io.wavfile
    import defs_ins as di
    print('OK')
    
    argv=list(sys.argv)
    katalog=argv[len(argv)-1]
    utwor=katalog
    czy_zip=False
    if katalog[len(katalog)-4:len(katalog)]=='.zip':
        print(' Rozpakowanie '+katalog+' do tmp')
        czy_zip=True
        utwor=katalog[0:len(katalog)-4]
        import zipfile as zf
        katalog_zip=zf.ZipFile(katalog)
        katalog_zip.extractall('tmp')
        #katalog='tmp/'+katalog[0:len(katalog)-4]
        katalog='tmp'
    print(' Wczytanie plików z '+katalog+' \n')
    
    defs= eval(open(katalog+"/defs.txt").read())
    bpm=defs["bpm"]
    length_sample=defs["length_sample"]
    
    fs0=44100
    
    #Zorientować się, jak długi ma byc plik
    song=np.genfromtxt(katalog+'/song.txt', dtype='str')
    song_n=np.size(song)
    song_len=np.zeros(song_n)
    for s in range(song_n):
        if song_n==1:
            song_s=np.str(song)
        else:
            song_s=song[s]            
        track=np.genfromtxt(katalog+'/track'+song_s+'.txt', dtype='str', comments='!')
        if length_sample:
            track_n=np.zeros(len(track))
            for t in range(len(track)):
                track_n[t]=float(track[t, -1][1:len(track[t, -1])])
            track_n=sum(track_n)
        else:
            sam_len=1
            track_n=len(track)       
        song_len[s]=60/bpm*fs0*track_n
    
    song_len=sum(song_len)
    song_final=np.zeros(song_len)                   
    
    t1=0
    t2=0
    for s in range(song_n):
        if song_n==1:
            song_s=np.str(song)
        else:
            song_s=song[s]
        print(' track'+song_s+": ", end="")
        
            
        track=np.genfromtxt(katalog+'/track'+song_s+'.txt', dtype='str', comments='!')        
        track_n=np.shape(track)        
        if len(track_n)==1:
            track_len=len(track)
            sample_n=1
        else:
            (track_len, sample_n)=track_n       
        
        if length_sample:
            sample_len=track[:, sample_n-1]
            sample_n=sample_n-1

        for t in range(track_len):
            print('.', end="")

            for sample in range(sample_n):
                if len(track_n)==1:
                    track_t=track[t]
                else:
                    track_t=track[t, sample]
                if length_sample:
                    sam_len=float(sample_len[t][1:len(sample_len[t])])
                else:
                    sam_len=1
                #print(track_t, sam_len)
                dzwiek=track_t
                if dzwiek!='--' and dzwiek!='---':
                    if len(dzwiek)==2:
                        fs,y = scipy.io.wavfile.read(katalog+'/sample'+dzwiek+'.wav')
                        y = np.mean(y,axis=1)
                        y /= 32767
                    else:
                        y=di.zagraj_ins(katalog, dzwiek, 60/bpm*sam_len)


                else:
                    y=np.zeros(60/bpm*fs0*sam_len)
                        
                
                #print(t1, t2)
                t2=min(t1+len(y), len(song_final))
                song_final[t1:t2]+=y[0:(t2-t1)]
            t1=min(60/bpm*fs0*sam_len+t1, len(song_final))
        print(" |")

    song_final /= 32767
    scipy.io.wavfile.write(utwor+'.wav', fs0, np.int16(song_final/max(np.abs(song_final))*32767))
    print('\n Zapisano '+utwor+'.wav')
    
