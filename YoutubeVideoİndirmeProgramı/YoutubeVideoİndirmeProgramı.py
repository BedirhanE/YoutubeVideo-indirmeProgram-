
from pytube import YouTube

#�ndirilecek vidonun link ba�lama k�sm�
link = input("Enter the Youtube video link: ")

#�ndirilecek videonun dosya ad�
file_name = input("Enter the file name: ")

# yt ad�nda bir youtube nesnesi olu�turdum
yt = YouTube(link)

# �ndirme format�
video = yt.streams.first()

# Dosya yolunu belirledim
download_path = 'C:\Users\elcin\OneDrive'

# Videoyu indirme i�lemini yapt���m yer 
video.download(download_path, file_name)

 print("Video downloaded successfully!")
