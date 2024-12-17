from pytube import YouTube

link = input("Enter video link here -> ")

Y_tube = YouTube(link)
print('------')
print(f' Video Title ==> {Y_tube.title}')


#stream = Y_tube.streams.filter(progressive="True", res="720p")
stream = Y_tube.streams.all()


video = list(enumerate(stream))

for i in video:
    print(i)

index = int(input("Enter the index of the desired stream -> "))

stream[index].download()
print('Success')


'''

stream = Y_tube.streams.filter(progressive="True" and )
video = stream.get_highest_resolution
video.download()
https://www.instagram.com/ansh_tyagi746?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=='''


