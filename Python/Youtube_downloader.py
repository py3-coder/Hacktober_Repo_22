from __future__ import unicode_literals
import youtube_dl

print('This Script is developed by ASSASSIN\n')
listMy = []
url = input('Enter URL of YouTube video : ')

ydl_opts = {
    #'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]'
    #'format': 'bestvideo[height<=144]/best[height<=144]'
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(url, download=False) 
    formats = meta.get('formats', [meta])
for f in formats:
    if not f['format_note'] in listMy:
        listMy.append(f['format_note'])

print('\nSelect the video quality -->')
for i in range(len(listMy)-1):
    print('[',(i+1),']'," ",listMy[i+1])

choice = int(input("\nEnter your choice "))


if choice<len(listMy) and choice>0:
    videoQuality = 'bestvideo[height<='+(listMy[choice])[:-1]+']/best[height<='+(listMy[choice])[:-1]+']'
    destPath = 'C:/YouTube_Downloads/%(title)s-'+listMy[choice]+'%(id)s.%(ext)s'
    ydl_opts['format'] = videoQuality
    ydl_opts['outtmpl'] = destPath
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=True)

    print('\nDownloading Completed !!!')

else:
    print('WRONG CHOICE...')


input("\n\nPress any key to EXIT---")
