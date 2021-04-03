from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bacon(request):
    return HttpResponse("<h1>Le epic bacon</h1>")


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    # create a dict of all words with values being times used
    worddict = {}
    for word in wordlist:
        if not (word in worddict):
            worddict[word] = 1
        else:
            worddict[word] += 1
    
    # find most used word
    best = wordlist[0]
    for key in worddict.keys():
        if worddict[key] > worddict[best]:
            best = key
    
    # sort words
    sortedlist = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'topword': best, 'topfreq': worddict[best], 'sortedlist': sortedlist})
