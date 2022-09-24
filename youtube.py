from pytube import YouTube
url=["https://www.youtube.com/shorts/612kODvCklM", "https://www.youtube.com/shorts/dFcf85CwPd8"]
i = 0
url_size=len(url)
while i < url_size:
    print(i)
    youtube=YouTube(url[i])
    print("Iniciando   ")
    print("Titulo: " + youtube.title)
    video=youtube.streams.get_highest_resolution()
    video.download("/videos")
    i += 1