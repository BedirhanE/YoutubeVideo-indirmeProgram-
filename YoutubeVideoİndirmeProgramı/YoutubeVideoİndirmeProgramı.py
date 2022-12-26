
from pytube import YouTube

#Ýndirilecek vidonun link baðlama kýsmý
link = input("Enter the Youtube video link: ")

#Ýndirilecek videonun dosya adý
file_name = input("Enter the file name: ")

# yt adýnda bir youtube nesnesi oluþturdum
yt = YouTube(link)

# Ýndirme formatý
video = yt.streams.first()

# Dosya yolunu belirledim
download_path = 'C:\Users\elcin\OneDrive'

# Videoyu indirme iþlemini yaptýðým yer 
video.download(download_path, file_name)

 print("Video downloaded successfully!")
