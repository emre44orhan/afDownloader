import os 
import sys
import pytube
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

font = QFont("Century Gothic", 20)
label = QFont("Century Gothic", 13)

class Main(QWidget):

     def __init__(self):
        super().__init__()

        self.setWindowTitle("afDownloader")
        self.setGeometry(200, 200, 700, 350)
        self.setFixedSize(700,350)
        self.setWindowIcon(QIcon('./assets/youtube-dl-gui.png'))

        self.content()
        self.center()
        self.show()
        
     def content(self):
        # Single Video
        videoText = QLabel("Video Link", self)
        videoText.move(20,45)
        videoText.setFont(font)
        
        self.videoLink = QLineEdit(self)
        self.videoLink.setGeometry(150,40,400,50)
        self.videoLink.setFont(font)

        downloadButton = QPushButton("", self)
        downloadButton.setGeometry(630,45,50,30)
        downloadButton.clicked.connect(self.videoDownload)
        downloadButton.setIcon(QIcon('./assets/cloud_download_32px.png'))

        chooseDirectory = QPushButton("", self)
        chooseDirectory.setGeometry(575,45,50,30)
        chooseDirectory.setIcon(QIcon('./assets/folder_32px.png'))
        chooseDirectory.clicked.connect(self.chooseDirVideo)

        self.videoDownloadAlert = QLabel("", self)
        self.videoDownloadAlert.move(600,20)
        self.videoDownloadAlert.resize(50,20)
        self.videoDownloadAlert.setFont(label)

        self.chooseDirLabel = QLabel("", self)
        self.chooseDirLabel.move(20,90)
        self.chooseDirLabel.resize(500,40)
        self.chooseDirLabel.setFont(label)

        # Playlist 
        playlistText = QLabel("Playlist Link", self)
        playlistText.move(20,200)
        playlistText.setFont(font)
        
        self.playListLink = QLineEdit(self)
        self.playListLink.setGeometry(170,190,400,50)
        self.playListLink.setFont(font)

        downloadButton1 = QPushButton("", self)
        downloadButton1.setGeometry(640,200,50,30)
        downloadButton1.setIcon(QIcon('./assets/cloud_download_32px.png'))
        downloadButton1.clicked.connect(self.playListDownload)

        chooseDirectory1 = QPushButton("", self)
        chooseDirectory1.setGeometry(585,200,50,30)
        chooseDirectory1.setIcon(QIcon('./assets/folder_32px.png'))
        chooseDirectory1.clicked.connect(self.chooseDirPlaylist)

        self.playListDownloadAlert = QLabel("", self)
        self.playListDownloadAlert.move(600, 175)
        self.playListDownloadAlert.resize(50,20)
        self.playListDownloadAlert.setFont(label)
       
        self.chooseDirLabel1 = QLabel("", self)
        self.chooseDirLabel1.move(20,250)
        self.chooseDirLabel1.resize(500,40)
        self.chooseDirLabel1.setFont(label)

     def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
     
     def chooseDirVideo(self):
        self.videoDir = QFileDialog.getExistingDirectory(os.getenv("Desktop"))
        if self.videoDir:
            self.chooseDirLabel.setText(f"Dizin seçildi: {self.videoDir}")
        """else:
            self.chooseDirLabel.setText("Dizin seçilmedi.")"""       
     
     def chooseDirPlaylist(self):
        self.playListDir = QFileDialog.getExistingDirectory(os.getenv("Desktop"))
        if self.playListDir:
            self.chooseDirLabel1.setText(f"Dizin seçildi: {self.playListDir}")
        else:
            self.chooseDirLabel1.setText("Dizin seçilmedi.")
       
     def videoDownload(self):
         self.link = self.videoLink.text()

         youtube = pytube.YouTube(self.link)
         video = youtube.streams.get_highest_resolution()
         video.download(self.videoDir + "/")
         self.videoLink.clear()
         self.videoDownloadAlert.setText("Done!") 
      
     def playListDownload(self):
        self.playList = self.playListLink.text()
        youtube_playlist = pytube.Playlist(self.playlist)

        for playlist in youtube_playlist:
                video = pytube.YouTube(playlist)
                stream = video.streams.get_highest_resolution()
                stream.download(self.playListDir + "/")
                self.playListDownloadAlert.setText("Done!")
             
if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    app = Main()
    sys.exit(uygulama.exec_())