#Full Application
from cmu_graphics import *
from PIL import Image
import math, copy
import pandas as pd
import random as rand
from random import *

def onAppStart(app):
    app.directionScreen = False
    app.matrixScreen = False
    app.monteSongScreen = False
    app.matrixSuggestionsScreen = False
    app.preferences = []
    app.songsSample = []
    app.plus = 0
    app.startGraph = [300 for i in range(10)]
    app.homeScreen = True
    app.uploadScreen = False
    app.startGraph = [300 for i in range(10)]
    app.one = None
    app.fileName = False #sets the global app variable to nothing, will later be assigned to the file path uploaded by user
    app.summaryScreen = False
    app.topSongsScreen = False
    app.topArtistsScreen = False
    app.longestSongsScreen = False
    app.graphScreen = False
    app.leastSongsScreen = False
    app.songRecScreen = False
    app.clicked = False
    app.topSong1 = None
    app.topSong2 = None
    app.topSong3 = None 
    app.topSong4 = None
    app.topSong5 = None
    app.topSong = None
    app.Image = "hiphop.jpg"
    app.longestSong1 = None
    app.longestSong2 = None
    app.longestSong3 = None
    app.longestSong4 = None
    app.suggested = []
    app.longestSong5 = None
    app.longestMins = None
    app.leastSong1 = None
    app.leastSong2 = None
    app.leastSong3 = None
    app.leastSong4 = None
    app.leastSong5 = None
    app.uploadFile = False
    app.maximize = False
    app.file = '' 
    app.topArtistsPrint = None
    app.longestSongsPrint = None
    app.genreData = 'dataset.csv' #Cite: Referenced Song Database of 125k+ songs used for genre feature tracking: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset 
    app.referenceData = 'tracks.csv' #Cite: Referenced Song Database of 600k+ songs for song reccomendation algorithm: https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks?select=tracks.csv
    #Cite: SAMPLE1.csv file - Referenced sample listening history used for app operation: Found on https://www.kaggle.com/code/saraclay/mini-project-1/input 



def onMousePress(app, mouseX, mouseY): # All organized up by screens/sub screens
    if app.homeScreen == True:
        if distance(mouseX, mouseY, 380, 20) <= 12:
            app.homeScreen = False
            app.directionScreen = True
        elif distance(mouseX, mouseY, 95, 300) <= 45:
            app.homeScreen = False
            app.uploadScreen = True
        elif distance(mouseX, mouseY, 205, 300) <= 45:
            app.homeScreen = False
            app.summaryScreen = True
        elif distance(mouseX, mouseY, 315, 300) <= 45:
            app.homeScreen = False
            app.songRecScreen = True
    elif app.directionScreen == True:
        if 325 <= mouseX <= 385 and 15 <= mouseY <= 35:
            app.directionScreen = False
            app.homeScreen = True
    elif app.matrixSuggestionsScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.homeScreen = True
            app.matrixSuggestionsScreen = False
    elif app.uploadScreen == True:
        if 150 <= mouseX <= 250 and 175 <= mouseY <= 225:
            app.uploadFile = True
        elif 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.uploadFile = False
            app.uploadScreen = False
            app.homeScreen = True
    elif app.matrixScreen == True:
        if 0 <= mouseX <= 200 and 18 < mouseY < 22:
            app.preferences = app.new.preferencesUpdate(0)
        if 0 <= mouseX <= 220 and 38 < mouseY < 42:
            app.preferences = app.new.preferencesUpdate(1)
        if 0 <= mouseX <= 220 and 58 < mouseY < 62:
            app.preferences = app.new.preferencesUpdate(2)
        if 0 <= mouseX <= 220 and 78 < mouseY < 82:
            app.preferences = app.new.preferencesUpdate(3)
        if 0 <= mouseX <= 220 and 98 < mouseY < 102:
            app.preferences = app.new.preferencesUpdate(4)
        if 0 <= mouseX <= 220 and 118 < mouseY < 122:
            app.preferences = app.new.preferencesUpdate(5)
        if 0 <= mouseX <= 220 and 138 < mouseY < 142:
            app.preferences = app.new.preferencesUpdate(6)
        if 0 <= mouseX <= 220 and 158 < mouseY < 162:
            app.preferences = app.new.preferencesUpdate(7)
        if 0 <= mouseX <= 220 and 178 < mouseY < 182:
            app.preferences = app.new.preferencesUpdate(8)
        if 0 <= mouseX <= 220 and 198 < mouseY < 202:
            app.preferences = app.new.preferencesUpdate(9)
        if 170 <= mouseX <= 230 and 350 <= mouseY <= 380:
            app.matrixScreen = False
            app.matrixRecs = app.new.calculation()
            app.matrixSuggestionsScreen = True    
    elif app.summaryScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.summaryScreen = False
            app.homeScreen = True
        elif 150 <= mouseX <= 250 and 100 <= mouseY <= 130:
            app.summaryScreen = False
            new2 = topSongs(app.file, app.genreData)
            app.topSong = new2.topSong()
            app.topSong1 = new2.topSong1()
            app.topSong2 = new2.topSong2()
            app.topSong3 = new2.topSong3()
            app.topSong4 = new2.topSong4()
            app.topSong5 = new2.topSong5()
            app.topAccSong = new2.topAccSong()
            app.songsList = new2.topSongsList()
            app.one = new2.topGenre()
            app.topGenre = getPicture(app, app.one[-1])
            app.Image = Image.open(app.topGenre)
            app.Image = CMUImage(app.Image)
            app.topSongsScreen = True
        elif 150 <= mouseX <= 250 and 150 <= mouseY <= 180:
            app.summaryScreen = False
            new = topArtist(app.file)
            app.topArtist = new.runFunction()
            app.topArtistsScreen = True
        elif 150 <= mouseX <= 250 and 200 <= mouseY <= 230:
            app.summaryScreen = False
            new2 = longestSongs(app.file)
            app.longestMins = new2.longestMins()
            app.longestSong1 = new2.longestSong1()
            app.longestSong2 = new2.longestSong2()
            app.longestSong3 = new2.longestSong3()
            app.longestSong4 = new2.longestSong4()
            app.longestSong5 = new2.longestSong5()
            app.longestSongsScreen = True
        elif 150 <= mouseX <= 250 and 250 <= mouseY <= 280:
            app.summaryScreen = False
            new2 = leastSongs(app.file)
            app.leastSong1 = new2.leastSong1()
            app.leastSong2 = new2.leastSong2()
            app.leastSong3 = new2.leastSong3()
            app.leastSong4 = new2.leastSong4()
            app.leastSong5 = new2.leastSong5()
            app.leastTime = new2.leastTotalTime()
            app.leastSongsScreen = True
        elif 30 <= mouseX <= 90 and 350 <= mouseY <= 380:
            app.summaryScreen = False
            new = Graph(app.file)
            app.message = new.runDimensions()
            app.axis = new.runAxis()
            app.graphScreen = True
    elif app.monteSongScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.homeScreen = True
            app.monteSongScreen = False
        elif 35 <= mouseX <= 95 and 350 <= mouseY <= 380:
            new = Reccomendation(app.songsList, app.referenceData)
            app.reccomendation = new.reccomend()
            app.reference = new.reference()
    elif app.songRecScreen == True:
        if 170 <= mouseX <= 230 and 300 <= mouseY <= 330:
            app.monteSongScreen = True
            new = Reccomendation(app.songsList, app.referenceData)
            app.reccomendation = new.reccomend()
            app.reference = new.reference()
            app.songRecScreen = False   
        elif 170 <= mouseX <= 230 and 200 <= mouseY <= 230:
            app.songRecScreen = False
            app.matrixScreen = True
            app.new = matrixReccomender(app.songsList, app.genreData)
            app.songsSample = app.new.pullSongs()
            app.suggested = app.new.suggestedSongs()
            app.features = app.new.findFeatureMatrix()
        elif 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.songsRecScreen = False
            app.summaryScreen = True
    elif app.topArtistsScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.topArtistsScreen = False
            app.summaryScreen = True
    elif app.topSongsScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.topSongsScreen = False
            app.summaryScreen = True
    elif app.longestSongsScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.longestSongsScreen = False
            app.summaryScreen = True   
    elif app.leastSongsScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.leastSongsScreen = False
            app.summaryScreen = True
    elif app.graphScreen == True:
        if 325 <= mouseX <= 385 and 350 <= mouseY <= 380:
            app.graphScreen = False
            app.summaryScreen = True




def onKeyPress(app, key): #Used for file uploading (handles all key possibilities when user is typing)
    if app.uploadFile == True:
        if (key.isalpha() or key.isdigit() or key == '.') and key != 'enter' and key != 'backspace':
            app.file += key
        elif key == 'backspace':
            app.file = app.file[0:-1]
        elif key == 'enter':
            app.uploadFile = False

def onMouseMove(app, mouseX, mouseY):
    if app.graphScreen == True:
        if 30 <= mouseX <= 370 and 120 <= mouseY <= 300 and app.maximize == False:
            app.maximize = True
        elif (mouseX <= 30 or mouseX >= 370) and (mouseY <= 120 or mouseY >= 300) and app.maximize == True:
            app.maximize = False
        if app.maximize == True:
            app.plus = 100
            app.startGraph = [200 for i in range(10)]
        else:
            app.plus = 0
            app.startGraph = [300 for i in range(10)]

    
    



 # All buttons for analysis use classs
 # Graphing uses classes as well


class Graph: # Class for Graphing
    def __init__(self, data):
        self.data = data
        songs = pd.read_csv(self.data) #Cite: currently using example listening history dataset found online to test code (https://www.kaggle.com/datasets/saraclay/my-spotify-streaming-history?resource=download)
        columnsListed = list(songs.columns) #List of all the columns


        onlyMinutes = songs.iloc[:, 3:]
        onlyMinutesList = []

        sortedMinutes = onlyMinutes.sort_values('msPlayed')
        topMinutes = sortedMinutes.tail()
        topMinutesList = []


        onlyTracks = songs.iloc[:, 2:3]
        tracksList = []
        longestSongs = []
        longestSongsListened = []

        onlyArtists = songs.iloc[:, 1:2]
        artistsList = []


        for m, row in onlyArtists.iterrows():
            artistsList.append(row["artistName"])

        for i, row in onlyTracks.iterrows():
            tracksList.append(row["trackName"])

        for j, row in onlyMinutes.iterrows():
            onlyMinutesList.append(row["msPlayed"])

        for k,row in topMinutes.iterrows():
            topMinutesList.append(row["msPlayed"])
        secondsListenedTo = 0

        currentNum = None
        bestNum = 1
        bestArtist = None

        self.artistsCountDict = dict()
        self.reversedDict = dict()


        for artist in range(len(artistsList)):
            currentArtist = artistsList[artist]
            currentNum = artistsList.count(currentArtist)
            if currentArtist in self.artistsCountDict:
                pass
            else:
                self.artistsCountDict[currentArtist] = currentNum
        self.sortedDict = dict()
        
        for artist in self.artistsCountDict:
            self.reversedDict[self.artistsCountDict[artist]] = artist

        self.sortedDict = sorted(self.reversedDict, reverse = True)




    def runDimensions(self):
        self.resultDict = dict()
        i = 0
        for item in self.sortedDict:
            if i <= 10:
                artist = self.reversedDict.get(item)
                self.resultDict[item] = artist
                i += 1
            else:
                break
        yVals = Bars(self.resultDict)
        return yVals.dimensions()
    def runAxis(self):
        listAxis = []
        i = 0
        for item in self.sortedDict:
            if i <= 10:
                listAxis.append(item)
                i += 1
            else:
                break
        result = (pushTo10(listAxis[0]))//5
        return result
       
   


class Bars: #Creates the dimensions for each bar on graph depending on metrics of artist
    def __init__(self, countToArtist):
        self.countArtist = countToArtist
    def dimensions(self):
        listCounts = list(self.countArtist.keys())
        maxCount = listCounts[0]
        resultVals = []
        for count in listCounts:
            value = (count/maxCount)
            resultVals.append((value, self.countArtist.get(count)))
        return resultVals


#All Data Analysis Classes are below

class longestSongs: # Class for Longest Songs

    def __init__(self, data):
        self.data = data
        songs = pd.read_csv(self.data) #Cite: currently using example listening history dataset found online to test code (https://www.kaggle.com/datasets/saraclay/my-spotify-streaming-history?resource=download)
        columnsListed = list(songs.columns) #List of all the columns


        onlyMinutes = songs.iloc[:, 3:]
        onlyMinutesList = []

        sortedMinutes = onlyMinutes.sort_values('msPlayed')
        topMinutes = sortedMinutes.tail()
        topMinutesList = []


        onlyTracks = songs.iloc[:, 2:3]
        tracksList = []
        longestSongs = []
        longestSongsListened = []

        onlyArtists = songs.iloc[:, 1:2]
        artistsList = []

        secondsListenedTo = 0

        for m, row in onlyArtists.iterrows():
            artistsList.append(row["artistName"])

        for i, row in onlyTracks.iterrows():
            tracksList.append(row["trackName"])

        for j, row in onlyMinutes.iterrows():
            onlyMinutesList.append(row["msPlayed"])

        for k,row in topMinutes.iterrows():
            topMinutesList.append(row["msPlayed"])

        for value in topMinutesList:
            corresponding = onlyMinutesList.index(value)
            longestSongs.append(tracksList[corresponding])
            longestSongsListened.append(value/1000)
        self.longestSongs = []
        self.longestSongsListened = []
        for i in range(len(longestSongs)):
            self.longestSongs.append(longestSongs[-i+1])
        for j in range(len(longestSongsListened)):
            self.longestSongsListened.append(longestSongsListened[-i+1])
    def longestMins(self):
        return f'{int(self.longestSongsListened[0] // 60)} minutes and {rounded(self.longestSongsListened[0] % 60)} seconds'
    
    def longestSong1(self):
        return f'1: {self.longestSongs[0]}: {int(self.longestSongsListened[0] // 60)} minutes and {rounded(self.longestSongsListened[0] % 60)} seconds'
    def longestSong2(self):
        return f'2: {self.longestSongs[1]}: {int(self.longestSongsListened[1] // 60)} minutes and {rounded(self.longestSongsListened[1] % 60)} seconds'
    def longestSong3(self):
        return f'3: {self.longestSongs[2]}: {int(self.longestSongsListened[2] // 60)} minutes and {rounded(self.longestSongsListened[2] % 60)} seconds'
    def longestSong4(self):
        return f'4: {self.longestSongs[3]}: {int(self.longestSongsListened[3] // 60)} minutes and {rounded(self.longestSongsListened[3] % 60)} seconds'
    def longestSong5(self):
        return f'5: {self.longestSongs[4]}: {int(self.longestSongsListened[4] // 60)} minutes and {rounded(self.longestSongsListened[4] % 60)} seconds'

class topArtist: # Class for Top Artist
    def __init__(self, data):
        self.data = data
    
    def runFunction(self):
        songs = pd.read_csv(self.data) #Cite: currently using example listening history dataset found online to test code (https://www.kaggle.com/datasets/saraclay/my-spotify-streaming-history?resource=download)
        columnsListed = list(songs.columns) #List of all the columns


        onlyMinutes = songs.iloc[:, 3:]
        onlyMinutesList = []

        sortedMinutes = onlyMinutes.sort_values('msPlayed')
        topMinutes = sortedMinutes.tail()
        topMinutesList = []


        onlyTracks = songs.iloc[:, 2:3]
        tracksList = []
        longestSongs = []
        longestSongsListened = []

        onlyArtists = songs.iloc[:, 1:2]
        artistsList = []


        for m, row in onlyArtists.iterrows():
            artistsList.append(row["artistName"])

        for i, row in onlyTracks.iterrows():
            tracksList.append(row["trackName"])

        for j, row in onlyMinutes.iterrows():
            onlyMinutesList.append(row["msPlayed"])

        for k,row in topMinutes.iterrows():
            topMinutesList.append(row["msPlayed"])
        secondsListenedTo = 0

        currentNum = None
        bestNum = 1
        bestArtist = None


        for artist in range(len(artistsList)):
            currentArtist = artistsList[artist]
            currentNum = artistsList.count(currentArtist)
            if currentNum > bestNum:
                bestArtist = currentArtist
                bestNum = currentNum
        numOccurencesBestArtist = 0


        for artist in range(len(artistsList)):
            if artistsList[artist] == bestArtist:
                numOccurencesBestArtist += 1
                secondsListenedTo += onlyMinutesList[artist] / 1000


        minutesListenedTo = (secondsListenedTo // 60)
        remained = secondsListenedTo % 60
        return (f'{bestArtist}, with a total listening time of {int(minutesListenedTo)} minutes and {rounded(remained)} seconds')

class topSongs: # Class for Top Songs

    def __init__(self, data, genre):
        self.data = data
        self.genreData = genre
        print(pd.read_csv(self.data, nrows=1))
        print(pd.read_csv(self.genreData, nrows =1))
        songs = pd.read_csv(data) #Cite: currently using example listening history dataset found online to test code (https://www.kaggle.com/datasets/saraclay/my-spotify-streaming-history?resource=download)
        columnsListed = list(songs.columns) #List of all the columns


        onlyMinutes = songs.iloc[:, 3:]
        onlyMinutesList = []

        sortedMinutes = onlyMinutes.sort_values('msPlayed')
        topMinutes = sortedMinutes.tail()
        topMinutesList = []


        onlyTracks = songs.iloc[:, 2:3]
        self.tracksList = []
        longestSongs = []
        longestSongsListened = []

        onlyArtists = songs.iloc[:, 1:2]
        self.artistsList = []

        secondsListenedTo = 0

        for m, row in onlyArtists.iterrows():
            self.artistsList.append(row["artistName"])

        for i, row in onlyTracks.iterrows():
            self.tracksList.append(row["trackName"])

        for j, row in onlyMinutes.iterrows():
            onlyMinutesList.append(row["msPlayed"])

        for k,row in topMinutes.iterrows():
            topMinutesList.append(row["msPlayed"])

        for value in topMinutesList:
            corresponding = onlyMinutesList.index(value)
            longestSongs.append(self.tracksList[corresponding])
            longestSongsListened.append(value/1000)

        secondsListenedTo = 0

        currentNum = None
        bestNum = 1
        bestArtist = None


        for artist in range(len(self.artistsList)):
            currentArtist = self.artistsList[artist]
            currentNum = self.artistsList.count(currentArtist)
            if currentNum > bestNum:
                bestArtist = currentArtist
                bestNum = currentNum
        numOccurencesBestArtist = 0


        for artist in range(len(self.artistsList)):
            if self.artistsList[artist] == bestArtist:
                numOccurencesBestArtist += 1
                secondsListenedTo += onlyMinutesList[artist] / 1000


        songsList = []
        for song, row in onlyTracks.iterrows():
            songsList.append(row["trackName"])

        dictionarySongs = dict()
        dictionarySongsReversed = dict()

        #creates a dictionary mapping each song to amount listened to
        for song in songsList:
            indexes = checkOccurences(songsList, song)
            newVal = 0
            for index in indexes:
                newVal += onlyMinutesList[index]
            dictionarySongs[song] = newVal #creates dictionary mapping each song to how much it was listened to (important, used later)
            dictionarySongsReversed[newVal] = song # creates same dictionary but keys/values switched, used for top songs function

        bestNum = 1
        bestSong = []

        for song in dictionarySongs:
            currMinutes = dictionarySongs[song]
            if currMinutes > bestNum:
                bestNum = currMinutes
                bestSong = [song, bestNum]

        newDictionary = sorted(dictionarySongsReversed, reverse = True)
        self.topSongs = []
        i = 0
        for time in newDictionary:
            if i <= 20:
                self.topSongs.append([dictionarySongsReversed.get(time), time])
                i += 1
            else:
                break
    
    def topSong1(self):
        return f'{1}. {self.topSongs[0][0]} by {self.artistsList[self.tracksList.index(self.topSongs[0][0])]}: {int(self.topSongs[0][1]/60000)} minutes and {rounded((self.topSongs[0][1] // 1000) % 60)} seconds'
    def topSong2(self):
        return  f'{2}. {self.topSongs[1][0]} by {self.artistsList[self.tracksList.index(self.topSongs[1][0])]}: {int(self.topSongs[1][1]/60000)} minutes and {rounded((self.topSongs[1][1] // 1000) % 60)} seconds'
    def topSong3(self):
        return f'{3}. {self.topSongs[2][0]} by {self.artistsList[self.tracksList.index(self.topSongs[2][0])]}: {int(self.topSongs[2][1]/60000)} minutes and {rounded((self.topSongs[2][1] // 1000) % 60)} seconds'
    def topSong4(self):
        return f'{4}. {self.topSongs[3][0]} by {self.artistsList[self.tracksList.index(self.topSongs[3][0])]}: {int(self.topSongs[3][1]/60000)} minutes and {rounded((self.topSongs[3][1] // 1000) % 60)} seconds'
    def topSong5(self):
        return  f'{5}. {self.topSongs[4][0]} by {self.artistsList[self.tracksList.index(self.topSongs[4][0])]}: {int(self.topSongs[4][1]/60000)} minutes and {rounded((self.topSongs[4][1] // 1000) % 60)} seconds'
    def topSong(self):
        return f'Your Favorite Song is {self.topSongs[0][0]}, by {self.artistsList[self.tracksList.index(self.topSongs[0][0])]}'
    def topAccSong(self):
        return f'{self.topSongs[0][0]}'
    def topGenre(self):
        self.topArtistsList = []
        result = []
        index = 10
        while not result:
            for i in range(index):
                self.topArtistsList.append(self.artistsList[self.tracksList.index(self.topSongs[i][0])])
            result = genreFinder(self.genreData, self.topArtistsList)
            index += 10
        return genreFinder(self.genreData, self.topArtistsList)
    
    def topSongsList(self):
        self.topSongsList = []
        for i in range(20):
            self.topSongsList.append(self.topSongs[i][0])
        return self.topSongsList


class leastSongs: # Class for Least Songs

    def __init__(self, data):
        self.data = data
        songs = pd.read_csv(self.data) #Cite: currently using example listening history dataset found online to test code (https://www.kaggle.com/datasets/saraclay/my-spotify-streaming-history?resource=download)
        columnsListed = list(songs.columns) #List of all the columns


        onlyMinutes = songs.iloc[:, 3:]
        onlyMinutesList = []

        sortedMinutes = onlyMinutes.sort_values('msPlayed')
        topMinutes = sortedMinutes.tail()
        topMinutesList = []


        onlyTracks = songs.iloc[:, 2:3]
        self.tracksList = []
        longestSongs = []
        longestSongsListened = []

        onlyArtists = songs.iloc[:, 1:2]
        self.artistsList = []

        secondsListenedTo = 0

        for m, row in onlyArtists.iterrows():
            self.artistsList.append(row["artistName"])

        for i, row in onlyTracks.iterrows():
            self.tracksList.append(row["trackName"])

        for j, row in onlyMinutes.iterrows():
            onlyMinutesList.append(row["msPlayed"])

        for k,row in topMinutes.iterrows():
            topMinutesList.append(row["msPlayed"])

        for value in topMinutesList:
            corresponding = onlyMinutesList.index(value)
            longestSongs.append(self.tracksList[corresponding])
            longestSongsListened.append(value/1000)

        secondsListenedTo = 0

        currentNum = None
        bestNum = 1
        bestArtist = None


        for artist in range(len(self.artistsList)):
            currentArtist = self.artistsList[artist]
            currentNum = self.artistsList.count(currentArtist)
            if currentNum > bestNum:
                bestArtist = currentArtist
                bestNum = currentNum
        numOccurencesBestArtist = 0


        for artist in range(len(self.artistsList)):
            if self.artistsList[artist] == bestArtist:
                numOccurencesBestArtist += 1
                secondsListenedTo += onlyMinutesList[artist] / 1000


        songsList = []
        for song, row in onlyTracks.iterrows():
            songsList.append(row["trackName"])

        dictionarySongs = dict()
        dictionarySongsReversed = dict()

        #creates a dictionary mapping each song to amount listened to
        for song in songsList:
            indexes = checkOccurences(songsList, song)
            newVal = 0
            for index in indexes:
                newVal += onlyMinutesList[index]
            dictionarySongs[song] = newVal #creates dictionary mapping each song to how much it was listened to (important, used later)
            dictionarySongsReversed[newVal] = song # creates same dictionary but keys/values switched, used for top songs function

        bestNum = 1
        bestSong = []

        for song in dictionarySongs:
            currMinutes = dictionarySongs[song]
            if currMinutes > bestNum:
                bestNum = currMinutes
                bestSong = [song, bestNum]

        origDictionary = sorted(dictionarySongsReversed)
        self.leastSongs = []
        j = 0
        for time in origDictionary:
            if j < 5:
                self.leastSongs.append([dictionarySongsReversed.get(time), time])
                j += 1
            else:
                break
    def leastSong1(self):
        return f'{self.leastSongs[0][0]} by {self.artistsList[self.tracksList.index(self.leastSongs[0][0])]}'
    def leastSong2(self):
        return f'{self.leastSongs[1][0]} by {self.artistsList[self.tracksList.index(self.leastSongs[1][0])]}'
    def leastSong3(self):
        return f'{self.leastSongs[2][0]} by {self.artistsList[self.tracksList.index(self.leastSongs[2][0])]}'
    def leastSong4(self):
        return f'{self.leastSongs[3][0]} by {self.artistsList[self.tracksList.index(self.leastSongs[3][0])]}'
    def leastSong5(self):
        return f'{self.leastSongs[4][0]} by {self.artistsList[self.tracksList.index(self.leastSongs[4][0])]}'
    def leastTotalTime(self):
        self.sum = 0
        for i in range(5):
            self.sum += self.leastSongs[i][1]
        return f'You listened to these songs for a total of {self.sum // 1000} seconds!'


class matrixReccomender: #1st Recccomendation Algorithm: Uses Matrix Factorization - Content Based Filtering
    def __init__(self, topSongs, genreData):
        self.topSongs = topSongs
        self.songs = pd.read_csv(genreData)
        print(list(self.songs.columns))
    
        onlyArtists = self.songs.iloc[:, 2:3]
        onlyGenres = self.songs.iloc[:, 20:]
        onlyTracks = self.songs.iloc[:, 4:5]
        onlyEnergy = self.songs.iloc[:, 9:10]
        onlyValence = self.songs.iloc[:, 17:18]
        onlyAcoust = self.songs.iloc[:, 14:15]
        onlySpeech = self.songs.iloc[:, 13:14]
        

        self.artistsList = []
        for a, row in onlyArtists.iterrows():
            self.artistsList.append(row["artists"])

        self.tracksList = []
        for c, row in onlyTracks.iterrows():
            self.tracksList.append(row["track_name"])
    
        self.genresList = []
        for b, row in onlyGenres.iterrows():
            self.genresList.append(row["track_genre"])
            
        self.energyList = []
        for h, row in onlyEnergy.iterrows():
            self.energyList.append(row["energy"])
        
        self.acoustList = []
        for z, row in onlyAcoust.iterrows():
            self.acoustList.append(row["acousticness"])
            
        self.valenceList = []
        for i, row in onlyValence.iterrows():
            self.valenceList.append(row["valence"])
        self.preferences = [0 for i in range(10)]


    def pullSongs(self):  #Suggest sample songs for training
        self.sample = []
        for song in self.topSongs:
            if song in self.tracksList:
                self.sample.append(song)
        if len(self.sample) == 0:
            self.randomNum = rand.sample(range(1, 120000), 3)
            for num in self.randomNum:
                self.sample.append(self.tracksList[num])
            return self.sample
        else:
            return self.sample[0:3]
    def suggestedSongs(self): #Suggested Song Set
        firstSong = self.sample[1]
        index = self.tracksList.index(firstSong)
        self.newData = self.songs.loc[self.songs['track_genre'] == self.genresList[index]]
        self.intlData = self.songs.loc[self.songs['track_genre'] == 'pop-film']
        self.intlDataI = self.songs.loc[self.songs['track_genre'] == 'indian']

        randomList = rand.sample(range(1, 1000), 10)
        self.suggested = []
        onlyTracks = self.newData.iloc[:, 4:5]
        onlyArtists = self.newData.iloc[:, 2:3]

        tracksIntl = self.intlData.iloc[:, 4:5]
        tracksIntlI = self.intlDataI.iloc[:, 4:5]

        self.tracksIntl = []
        for b, row in tracksIntl.iterrows():
            self.tracksIntl.append(row['track_name'])

        self.tracksIntlI = []
        for c, row in tracksIntlI.iterrows():
            self.tracksIntlI.append(row['track_name'])

        self.newtracksList = []
        for c, row in onlyTracks.iterrows():
            self.newtracksList.append(row["track_name"])


        self.newArtistsList = []
        for a, row in onlyArtists.iterrows():
            self.newArtistsList.append(row["artists"])

        for i in randomList:
            if self.newtracksList[i] not in self.tracksIntl and self.newtracksList[i] not in self.tracksIntlI:
                self.suggested.append((self.newtracksList[i], self.newArtistsList[i]))
        val = len(self.suggested)
        return self.suggested[:val//2]

    def findFeatureMatrix(self): #Returns Features
        self.matrix = []
        for val in self.suggested:
            index = self.tracksList.index(val[0])
            self.matrix.append([binary(self.energyList[index]), binary(self.valenceList[index]), binary(self.acoustList[index])])
        print(self.matrix)
        return self.matrix
    def preferencesUpdate(self, index): #Training Part by User
        if self.preferences[index] == 1:
            self.preferences[index] = 0
        else:
            self.preferences[index] = 1
        print(f'Original Preferences: {self.preferences}')
        return self.preferences
    def calculation(self): #Finds Calculations
        diff = 10 - len(self.matrix)
        for i in range(diff):
            self.preferences.pop()
        print(f'Updated Preferences: {self.preferences}')
        for i in range(len(self.matrix)):
            subList = self.matrix[i]
            sum1 = sum(subList)
            for j in range(len(subList)):
                val = self.matrix[i][j]
                sum12 = sum1**0.5
                if sum12 == 0:
                    self.matrix[i][j] = 0
                else:
                    self.matrix[i][j] = val / ((sum1)**0.5)
        print(f'Matrix: {self.matrix}')

        energyColumn = getColumns(self.matrix, 0)
        valenceColumn = getColumns(self.matrix, 1)
        acoustColumn = getColumns(self.matrix, 2)

        self.userProfile = [0 for i in range(3)]

        self.userProfile[0] = dotProduct(energyColumn, self.preferences)
        self.userProfile[1] = dotProduct(valenceColumn, self.preferences)
        self.userProfile[2] = dotProduct(acoustColumn, self.preferences)
        print(f'UserProfile: {self.userProfile}') #Creates User Profile
        
        df = [0, 0, 0]

        df[0] = sumList(energyColumn)
        df[1] = sumList(valenceColumn)
        df[2] = sumList(acoustColumn)
        idf1 = list(range(1,4))
        for i in range(len(df)):
            val1 = df[i]
            length = len(self.matrix)
            if val1 == 0:
                val1 = 0.1
            idf1[i] = idf(length, val1)
        idf2 = list(idf1) #Finds IDF

        weightedScores = list(range(1, len(self.matrix)))

        for i in range(len(weightedScores)):
            weightedScores[i] = dotProduct(self.matrix[i], idf2)
        probabilities = list(range(1, len(self.matrix)))

        print(f'Self.userprofile : {self.userProfile}, WeightedScores: {weightedScores}')

        for j in range(len(probabilities)):
            list3 = [weightedScores[j], weightedScores[j], weightedScores[j]]
            probabilities[j] = dotProduct(self.userProfile, list3)
        maximum = max(probabilities[val//2:])
        index = probabilities.index(maximum)
        print(self.suggested[index])
        return self.suggested[index]

#Citation: Specific Matrix Factorization Algorithm inspiration/concept used from https://www.analyticsvidhya.com/blog/2015/08/beginners-guide-learn-content-based-recommender-systems/ 

class Reccomendation: #2nd reccomendation Algorithm (Monte Carlo Methods) 
    def __init__(self, songsList, referenceData):  
        songs = pd.read_csv(referenceData)
        self.songsList = songsList
        columnsListed = list(songs.columns)

        onlyTracks = songs.iloc[:, 1:2]
        onlyEnergy = songs.iloc[:, 9:10]
        onlyArtists = songs.iloc[:, 5:6]
        onlySpeechiness = songs.iloc[:, 13:14]
        onlyValence = songs.iloc[:, 17:18]
        onlyLive = songs.iloc[:, 16:17]
        onlyExplicit = songs.iloc[:, 4:5]
        onlyDance = songs.iloc[:, 8:9]


        self.tracksList = []
        for j, row in onlyTracks.iterrows():
            self.tracksList.append(row["name"])
        
        self.artistsList = []
        for b, row in onlyArtists.iterrows():
            self.artistsList.append(row["artists"])


        self.energyList = []
        for k, row in onlyEnergy.iterrows():
            self.energyList.append(row["energy"])


        self.speechList = []
        for l, row in onlySpeechiness.iterrows():
            self.speechList.append(row["speechiness"])


        self.liveList = []
        for m, row in onlyLive.iterrows():
            self.liveList.append(row["liveness"])

        self.valenceList = []
        for n, row in onlyValence.iterrows():
            self.valenceList.append(row["valence"])
        
        self.danceList = []

        for o, row in onlyDance.iterrows():
            self.danceList.append(row["danceability"])

        self.explicitList = []
        for p, row in onlyExplicit.iterrows():
            self.explicitList.append(row["explicit"])
        

        self.songsListAcc= []
        for song in self.songsList:
            if song in self.tracksList:
                self.songsListAcc.append(song)


        if len(self.songsListAcc) == 0:
            return None

        self.desired = []
        index = self.tracksList.index(self.songsListAcc[0])
        self.desired.append(self.energyList[index])
        self.desired.append(self.speechList[index])
        self.desired.append(self.valenceList[index])
        self.desired.append(self.danceList[index])
        self.desired.append(self.explicitList[index])


        if len(self.desired) == 0:
            return None
    def reccomend(self):
        reccomendations = []
        results = []

        numSimulations = 200

        for i in range(numSimulations):
            index = randint(1, 586672)
            results = []
            results.append(self.energyList[index])
            results.append(self.speechList[index])
            results.append(self.valenceList[index])
            results.append(self.danceList[index])
            results.append(self.explicitList[index])
            if checkSimilar(self.desired, results) == True:
                reccomendations.append((self.tracksList[index], self.artistsList[index]))
            else:
                pass
        return reccomendations
    def reference(self):
        return self.songsListAcc[1]
      






    


    

    
    
#All Helper Functions used in Functions are below:

def sumList(list1): #Finds the sum of all values in a list
    sum = 0
    for i in list1:
        sum += i
    return sum


def distance(x1, y1, x2, y2): # Distance Helper Function
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def pushTo10(num): #Helper Function, rounds number up to nearest 10
    while num % 10 != 0:
        num += 1
    return num     


def getPicture(app, genre): #Returns picture file for each genre
    if genre == 'r-n-b':
        return "rnb.jpg"
    elif genre == 'techno':
        return "techno.jpg"
    elif genre == 'tango':
        return "tango.jpg"
    elif genre == 'spanish':
        return "spanish.jpg"
    elif genre == 'reggae' or genre == 'reggaetron':
        return "reggae.jpg"
    elif genre == 'rock-n-roll':
        return "rocknroll.jpg"
    elif genre == 'punk':
        return "punk.jpg"
    elif genre == 'pop':
        return "pop.jpg"
    elif genre == 'latino' or genre == 'salsa':
        return "latino.jpg"
    elif genre == 'k-pop' or genre == 'world':
        return "kpop.jpg"
    elif genre == 'indie':
        return "indie.jpg"
    elif genre == 'house':
        return "house.jpg"
    elif genre == 'hip-hop':
        return "hiphop.jpg"
    elif genre == 'edm':
        return "edm.jpg"
    else:
        return "edm.jpg"

        

def checkSimilar(desired, results): #Returns if features are similar enough to delta values set
    deltaList = [0.1, 0.1, 0.1, 0.1]
    for item in range(len(desired)):
        if item < 4:
            delta = deltaList[item]
            if (results[item] - delta) <= desired[item] <= (results[item] + delta):
                pass
            else:
                return False
        elif item == 4:
            if results[item] == desired[item]:
                pass
            else:
                return False
    return True


def color(val): #Returns green for 0, white for 1
    if val == 0:
        return 'darkSlateGray'
    else:
        return 'white'  


def genreFinder(data, artistList): #Returns the genre for respective artist
    songs = pd.read_csv(data)
    
    onlyArtists = songs.iloc[:, 2:3]
    onlyGenres = songs.iloc[:, 20:]

    artistsList = []
    for a, row in onlyArtists.iterrows():
        artistsList.append(row["artists"])
    
    genresList = []
    for b, row in onlyGenres.iterrows():
        genresList.append(row["track_genre"])
    result = []
    resultList = []
    for i in artistList:
        if i in artistsList:
            resultList.append(genresList[artistsList.index(i)])
    print(resultList)
    return resultList
                        
def checkOccurences(list, val): #Checks the occurences of a value in a list
    indexes = []
    for i in range(len(list)):
        if list[i] == val:
            indexes.append(i)
    return indexes

def getColumns(list1, colNum): #Returns the column in a list for a column number
    column = []
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if j == colNum:
                column.append(list1[i][j])
    return column


def dotProduct(list1, list2): #Returns the dot product of 2 lists
    result = 0
    length = len(list1)
    for val in range(length):
        result += list1[val]*list2[val]
    return result

def idf(total, val): #Returns the inverse document frequency (IDF) value
    return math.log((total/val), 10)     
    

def binary(value): #Returns 0 or 1 depending on if a value is above/below 0.5
    if value < 0.5:
        return 0 
    else:        
        return 1

        
def redrawAll(app):
    if app.homeScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        
        drawCircle(380, 20, 12, fill = 'white')
        drawCircle(95, 300, 45, fill = 'white')
        drawCircle(205, 300, 45, fill = 'white')
        drawCircle(315, 300, 45, fill = 'white')
        drawLabel('?', 380, 20, bold = True, size = 20, font = 'montserrat', fill = 'black')
        drawLabel('Upload', 95, 300, bold = True, size = 16, font = 'montserrat', fill = 'black')
        drawLabel('Spotify Assistant', 185, 50, size = 28, 
                fill = 'white', font = 'montserrat', bold = True)
        drawLabel('Summary', 205, 300, bold = True, size = 15, font = 'montserrat', fill = 'black')
        drawLabel('Reccomend', 315, 300, bold = True, size = 13, font = 'montserrat', fill = 'black')
        drawCircle(325, 50, 18, fill = 'white')
        drawRect(325, 50, 22, 24, fill = 'darkSlateGray', align = 'center')
        drawCircle(320, 46, 3, fill = 'white', align = 'center')
        drawCircle(330, 46, 3, fill = 'white', align = 'center')

        drawCircle(325, 52, 2, fill = 'white', align = 'center')
        drawOval(325, 57, 12, 3, fill = 'white', align = 'center')
    elif app.matrixScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        for i in range(len(app.suggested)):
            drawLabel(f'{app.suggested[i][0]} by {app.suggested[i][1]}', 10, 20 + (20*i), size = 10, fill = 'white', align = 'left')
        for j in range(len(app.preferences)):
            drawCircle(380, 20 + (20*j), 3, fill = color(app.preferences[j]))
        drawRect(170, 350, 60, 30, fill = 'white')
        drawLabel('Done', 200, 365)
        drawLabel('Click on each song you would listen to. When finished, press done', 200, 390, fill = 'white', size = 11)
    elif app.matrixSuggestionsScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Here are the songs we reccomend based on your choices!', 200, 15, size = 15, font = 'montserrat', fill = 'white')
        for i in range(len(app.matrixRecs)):
            drawLabel(app.matrixRecs[i], 200, 100 + (20*i), fill = 'white', size = 14)
        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Home', 355, 365, size = 12, font = 'montserrat')
    elif app.directionScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Directions', 200, 50, size = 28, fill = 'white',
                  font = 'montserrat', bold = True)


        

        drawRect(325, 15, 60, 20, fill = 'white')
        drawLabel('Home', 355, 25, size = 12, font = 'montserrat')

        drawLabel('1. Upload your listening data in a CSV file format via the upload button', 10, 100, fill = 'white', align = 'left')
        drawLabel('2. Confirm that your file is readable and uploaded', 10, 120, fill = 'white', align = 'left')
        drawLabel('3. Click the Summary button for an analysis of your data', 10, 140, fill = 'white', align = 'left')
        drawLabel('4. Use the toggles on the Summary page for a deeper dive', 10, 160, fill = 'white', align = 'left')
        drawLabel('5. Click the Graph button to see your top artists graphed', 10, 180, fill = 'white', align = 'left')
        drawLabel('6. Click the Reccomendations button to receive song reccomendations', 10, 200, fill = 'white', align = 'left')
        drawLabel('*Note: To receive reccomendations, make sure you click on top songs on the summary', 10, 220, fill = 'white', align = 'left', size = 10)
    elif app.uploadScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')

        drawLabel('Input your listening data in a CSV file format', 200, 50, size = 14, fill = 'white',
                  font = 'montserrat', bold = True)
        drawRect(200, 200, 100, 50, fill = 'white', align = 'center')
        drawLabel('Upload', 200, 200, font = 'montserrat', size = 20, bold = True)
        if app.uploadFile == True:
            drawRect(0, 0, app.width, app.height, fill = 'black')
            drawLabel('Type in your csv file path below, press enter when done', 200, 100, size = 14, fill = 'white')
            drawLabel('ie. StreamingHistory.csv', 200, 120, size = 14, fill = 'white')
            drawLabel(app.file, app.width/2, app.height/2, fill = 'white', size = 18)

        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Home', 355, 365, size = 12, font = 'montserrat')
    elif app.summaryScreen == True:
        drawRect(0, 0 , app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Results', 200, 50, size = 28, fill = 'white',
                  font = 'montserrat', bold = True)
        
        drawRect(150, 100, 100, 30, fill = 'white' )
        drawRect(150, 150, 100, 30, fill = 'white' )

        drawRect(150, 200, 100, 30, fill = 'white' )
        drawRect(150, 250, 100, 30, fill = 'white' )
        drawRect(325, 350, 60, 30, fill = 'white')

        drawRect(30, 350, 60, 30, fill = 'white')

        drawLabel('Top Songs', 200, 115, fill = 'black' )
        drawLabel('Top Artists', 200, 165, fill = 'black' )
        drawLabel('Longest Songs', 200, 215, fill = 'black' )
        drawLabel('Least Listened to Songs', 200, 265, size = 9, fill = 'black' )
        drawLabel('Graph', 60, 365, size = 12, font = 'montserrat')
        drawLabel('Home', 355, 365, size = 12, font = 'montserrat')
    elif app.topSongsScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Here are your top songs!', 200, 50, size = 16, fill = 'white',
                  font = 'montserrat', bold = True)
        drawLabel(app.topSong1, 200, 100, fill = 'white', font = 'montserrat', size = 11, bold = False)
        drawLabel(app.topSong2, 200, 120, fill = 'white', font = 'montserrat', size = 11, bold = False)
        drawLabel(app.topSong3, 200, 140, fill = 'white', font = 'montserrat', size = 11, bold = False)
        drawLabel(app.topSong4, 200, 160, fill = 'white', font = 'montserrat', size = 11, bold = False)
        drawLabel(app.topSong5, 200, 180, fill = 'white', font = 'montserrat', size = 11, bold = False)
        
        drawImage(app.Image, 125, 240, width = 150, height = 150)

        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Summary', 355, 365, size = 12, font = 'montserrat')
    elif app.topArtistsScreen == True:
        
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Here is your favorite artist!', 200, 50, size = 16, fill = 'white',
                  font = 'montserrat', bold = True)
        drawLabel(app.topArtist, 200, 100, fill = 'white', font = 'montserrat', size = 11, bold = False)

        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Summary', 355, 365, size = 12, font = 'montserrat')


    elif app.longestSongsScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Here are your longest songs!', 200, 50, size = 16, fill = 'white',
                  font = 'montserrat', bold = True)
        drawLabel(app.longestSong1, 200, 100, fill = 'white', font = 'montserrat', size = 10, bold = False)
        drawLabel(app.longestSong2, 200, 120, fill = 'white', font = 'montserrat', size = 10, bold = False)
        drawLabel(app.longestSong3, 200, 140, fill = 'white', font = 'montserrat', size = 10, bold = False)
        drawLabel(app.longestSong4, 200, 160, fill = 'white', font = 'montserrat', size = 10, bold = False)
        drawLabel(app.longestSong5, 200, 180, fill = 'white', font = 'montserrat', size = 10, bold = False)

        drawLabel(f'''That's crazy, you listened to a song {app.longestMins} long!''', 200, 260, size = 12, fill = 'white', font = 'montserrat', bold = True)
        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Summary', 355, 365, size = 12, font = 'montserrat')
    elif app.leastSongsScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Here are the songs you listened to the least!', 200, 50, size = 16, fill = 'white',
                  font = 'montserrat', bold = True)
        drawLabel(f'1: {app.leastSong1}', 200, 100, fill = 'white', font = 'montserrat', size = 12, bold = False)
        drawLabel(f'2: {app.leastSong2}', 200, 120, fill = 'white', font = 'montserrat', size = 12, bold = False)
        drawLabel(f'3: {app.leastSong3}', 200, 140, fill = 'white', font = 'montserrat', size = 12, bold = False)
        drawLabel(f'4: {app.leastSong4}', 200, 160, fill = 'white', font = 'montserrat', size = 12, bold = False)
        drawLabel(f'5: {app.leastSong5}', 200, 180, fill = 'white', font = 'montserrat', size = 12, bold = False)
        drawLabel(app.leastTime, 200, 220, fill = 'white', font = 'montserrat', size = 14, bold = False)
        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Summary', 355, 365, size = 12, font = 'montserrat')
    elif app.graphScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'white')
        drawLabel('Graphed!', 200, 50, font = 'montserrat', size = 18, bold = False)
        drawRect(325, 350, 60, 30, fill = 'black')
        drawLabel('*Press on Graph to Toggle On/Off Zoom', 100, 10, size = 9)
        drawLine(30, 300, 30, 120 - app.plus, fill = 'black')
        drawLine(30, 300, 370, 300, fill = 'black')
        for i in range(10):
            drawRect(336 - (34*i), 300-(app.message[i][0]*(180+app.plus)), 34, app.message[i][0]*(180+app.plus), fill = 'purple', border = 'black', borderWidth = 1)
            msg = app.message[i][1]
            j = 0
            
            for item in msg.split(' '):
                if len(item) > 6:
                    drawLabel(item, 336-(36*i), 312 + (14*j), size = 8, font = 'arial', fill = 'black', align = 'left')
                else:
                    drawLabel(item, 336-(34*i), 312 + (14*j), size = 8, font = 'arial', fill = 'black', align = 'left')
                j += 1
        for j in range(6):
            drawLabel(app.axis*j, 20, 300-((36+(app.plus//5))*j), size = 8)


        drawLine(30, 300, 30, 120, fill = 'black')
        drawLine(30, 300, 370, 300, fill = 'black')
        drawLabel('Top Artists', 200, 385, size = 10)
        drawLabel('Amount Listened To', 8, 220, rotateAngle = 270, size = 8)
        drawRect(325, 350, 60, 30, fill = 'black')
        drawLabel('Home', 355, 365, size = 12, font = 'montserrat', fill = 'white')
    elif app.songRecScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawRect(170, 200, 60, 30, fill = 'white')
        drawRect(170, 300, 60, 30, fill = 'white')
        drawLabel('Interactive', 200, 215, size = 11)
        drawLabel('Non-Interactive', 200, 315, size = 9)
        drawLabel('Click on the reccomendation type you want', 200, 100, size = 11, fill = 'white')
    elif app.monteSongScreen == True:
        drawRect(0, 0, app.width, app.height, fill = 'darkSlateGray')
        drawLabel('Here are the songs we reccomend!', 200, 50, size = 16, fill = 'white',
                  font = 'montserrat', bold = True)
        if len(app.reccomendation) >= 5:
            for i in range(5):
                drawLabel(f'{i+1}: {app.reccomendation[i][0]} by {app.reccomendation[i][1]}', 200, 80 + (20*i), fill = 'white', size = 12, bold = False)
        else:
            for i in range(len(app.reccomendation)):
                drawLabel(f'{i+1}: {app.reccomendation[i][0]} by {app.reccomendation[i][1]}', 200, 80 + (20*i), fill = 'white', size = 12, bold = False)
        drawLabel(f'Reference: {app.reference}', 200, 200, size = 12, font = 'montserrat', fill = 'white')
        drawRect(325, 350, 60, 30, fill = 'white')
        drawLabel('Home', 355, 365, size = 12, font = 'montserrat')
        drawRect(35, 350, 60, 30, fill = 'white')
        drawLabel('Regenerate', 65, 365, font = 'montserrat', size = 11)







        
def main():
    runApp()


main()