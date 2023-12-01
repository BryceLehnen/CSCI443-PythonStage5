import statistics

# Define seperate arrays for the raw
homeToBrowse = []
homeToSearch = []
homeToAccount = []
movieToMovie = []
homeToBrowseOptions = []
timeToScrollup = []
timeToSettings = []

# Open the file and read it line by line
data = open("Stage5Data.csv", "r")
data.readline() # Reads the header for each column
for line in data:
    user = line.split(",")
    # Now we have all of the user data, we can store the data for each seperate test
    homeToBrowse.append([user[0], user[7]])
    homeToSearch.append([user[1], user[8]])
    homeToAccount.append([user[2], user[9]])
    movieToMovie.append([user[3], user[10]])
    homeToBrowseOptions.append([user[4], user[11]])
    timeToScrollup.append([user[5], user[12]])
    timeToSettings.append([user[6], user[13]])

# Compiles data and prints out the mean and standard deviation
def dataCompiler(dataArray):
    mean = 0
    sd = []
    # Compile mean and standard deviation for times
    for x in range(len(dataArray)):
        mean = mean + float(dataArray[x][0])
        sd.append(float(dataArray[x][0]))
    mean = mean / len(dataArray)
    print("Average of ", round(mean, 2), " seconds with a standard deviation of ", round(statistics.stdev(sd, mean), 4))

    mean = 0
    sd = []
    # Compile mean and standard deviation for errors
    for x in range(len(dataArray)):
        mean = mean + float(dataArray[x][1])
        sd.append(float(dataArray[x][1]))
    mean = mean / len(dataArray)
    print("Average of ", round(mean, 2), " errors with a standard deviation of ", round(statistics.stdev(sd, mean), 4))
    return

# Sends each array of data
print("\nHome to Browse")
dataCompiler(homeToBrowse)
print("\nHome to Search")
dataCompiler(homeToSearch)
print("\nHome to Account")
dataCompiler(homeToAccount)
print("\nMovie to movie")
dataCompiler(movieToMovie)
print("\nHome to Browse with Options")
dataCompiler(homeToBrowseOptions)
print("\nTime to Find Scrollup Button")
dataCompiler(timeToScrollup)
print("\nTime to Find Settings")
dataCompiler(timeToSettings)
