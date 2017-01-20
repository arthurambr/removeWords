import urllib

def read_text1():
    quotes = open("/Users/arthur/Python/removeShitWords/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    checkShit(contents_of_file)
    piratize(contents_of_file)

def read_text2():
    quotes = open("/Users/arthur/Python/removeShitWords/movie_quotes copy.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    checkShit(contents_of_file)
    piratize(contents_of_file)

def piratize(words):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+words)
    result = connection.read()
    print(result)
    connection.close()

def checkShit (shit):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+shit)
    result = connection.read()
    if (result=="true"):
        print("You dirty, naughty boy!")
    elif "false" in result:
        print("You are Mama's little angel")
    else:
        print("Could not scan the document")
    connection.close()

read_text1()
read_text2()

