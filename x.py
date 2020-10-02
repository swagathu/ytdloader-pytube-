try:
    from pytube import YouTube
    import os
    import sys
    import subprocess
    import shutil
except:
    print('The modulenot installed check imported library list..')
    quit()
def progress_Check(chunk: bytes, file_handler: None, bytes_remaining: int):
    #Gets the percentage of the file that has been downloaded.
    percent = round(((file_size-bytes_remaining)/file_size)*100)
    x='Downloaded.....'+str(percent)+'%'
    sys.stdout.write('\r'+str(x))
    sys.stdout.flush()
def speed():
    c=[0,'ultrafast','superfast','veryfast','faster','fast','medium','slow','slower','veryslow']
    n=int(input('''Enter the encode quality:(bydefault libx264 used)
                    Saved in Downloads_YTpyDl
                (1)ultrafast,
                (2)superfast,
                (3)veryfast,
                (4)faster,
                (5)fast,
                (6)medium,
                (7)slow,
                (8)slower,
                (9)veryslow\n:-->'''))
    return c[n]
def downlvid(link):
    if os.path.exists('aud.mp4'):
        os.remove('aud.mp4')
    if os.path.exists('vid.mp4'):
        os.remove('vid.mp4')
    yt = YouTube(link, on_progress_callback=progress_Check)
    global file_size
    print('Select itag needed')
    print('Title: ',yt.title)
    print('Number of views: ',yt.views)
    print('Length of video: ',yt.length,'seconds')
    print('Ratings: ',yt.rating)
    print('Select Video Qual.\n\n')
    for i in yt.streams.filter(only_video=True):
        print(i)
        print('\n')
    x=input('Enter itag:-->')
    print('\n\n')
    print('Select Audio Qual.\n\n')
    for i in yt.streams.filter(only_audio=True):
        print(i)
        print('\n')
    y=input('Enter itag:-->')
    print('\n\n')
    ys = yt.streams.get_by_itag(x)
    ysa = yt.streams.get_by_itag(y)#vid=ys

    print("Now downloading,  ")
    video = yt.streams.filter(only_video=True).get_by_itag(x)
    audio = yt.streams.filter(only_audio=True).get_by_itag(y)

    print('FileSize : ' + str(round((video.filesize+audio.filesize)/(1024*1024))) + 'MB')
    print('Getting Video...')
    nam=yt.title#+'.mp4'
    namxfv=nam
    bad_chars = [';', ':', '!', '*','|']
    for i in bad_chars :
        nam = nam.replace(i, '')

    nam=nam.replace(' ','_')
    nam=nam.replace('&','and')
    nam=nam.replace(')','r1br@1')
    nam=nam.replace('(','l123a9')
    nam=nam.replace('-','@min92@$')

    string_with_nonASCII = nam

    encoded_string = string_with_nonASCII.encode("ascii", "ignore")
    nam = encoded_string.decode()
    namv=nam+'v'+'.mp4'
    nama=nam+'a'+'.mp4'

    if os.path.exists(nama):
        os.remove(nama)
    if os.path.exists(namv):
        os.remove(namv)
    dp=os.path.join(os.path.expanduser('~'),'Downloads')
    dlpath=dp+'\YtpyDL\\'
    dlpath.replace(' ','')
    ds=nam+'.mp4'
    downf=dlpath+ds
    nn=ds.replace('_',' ')
    nn=nn.replace('l123a9','(')
    nn =nn.replace('r1br@1',')')
    nn=nn.replace('@min92@$','-')
    namxdv=nn
    nn=dp+'\YtpyDL\\'+nn
    print(namxfv)
    if os.path.exists(nn):
        ask=input('File with same name alredy exists do you want to continue?\n(if you continue file will be replaced)\n[y/n]-->')
        if ask=='y':
            os.remove(nn)
        else:
            print('\n\nExit...\n\n')
            quit()
    file_size = video.filesize
    out_file1 = ys.download()
    os.rename(out_file1, namv)
    print('\nGetting Audio..')
    sys.stdout.flush()
    file_size = audio.filesize
    out_file = ysa.download()
    os.rename(out_file, nama)
    print('\n\n\n')
    print(yt.title+'.mp4\n\n')
    print('Merging....')
    namb=nam+'.bat'
    s=open(namb,'w')
    xbat='@echo off\nffmpeg -i '+'"'+nama+'"'+' -i '+'"'+namv+'"'+' -preset '+speed()+' '+'"'+nam+'.mp4"'
    s.write(xbat)
    s.close()
    filepath=namb
    subprocess.call([namb])
    if os.path.exists(namb):
        os.remove(namb)
    return nama,namv,nam+'.mp4',namxfv+'.mp4'
def q():
    aww=input('Do you need to continue?[y/n]\n-->')
    #if not count==1:
    if aww=='n':
     quit()

aws=True
count=0
while aws:
    try:
        ds=downlvid(input('Enter or copy paste the video Link(remove the playlist part in link if present..)\n(Sometimes this may not work):>'))
    except Exception as e:
        print(e)
        q()
        count=1
        continue
    if os.path.exists(ds[0]):
        os.remove(ds[0])
    if os.path.exists(ds[1]):
        os.remove(ds[1])
    dp=os.path.join(os.path.expanduser('~'),'Downloads')
    dlpath=dp+'\YtpyDL\\'
    dlpath.replace(' ','')
    if not os.path.isdir(dlpath):
        os.makedirs(dlpath)
    downf=dlpath+ds[2]
    nn=ds[3]
    nn=dp+'\YtpyDL\\'+nn
    shutil.move(ds[2],downf)
    if os.path.exists(downf):
        os.rename(downf,nn)
    if not count==1:
        q()
