'''
#Aufgabe 1a)

def blocksatz(totalWords):

    totalLen = 0
    for x in range(len(totalWords)):
        totalLen += len(totalWords[x])
    totalLen += len(totalWords)

    tempWords = totalWords #temporaere Liste aus der Element geloescht werden

    def blockzeile(globalWords): # Erfüllt Aufgabe für eine Zeile mit weniger als 80 Zeichen

        lenWords = 0
        for x in range(len(globalWords)):
            lenWords += len(globalWords[x]) # Ermittelt die Gesamtlänge der Wörter in der Liste
        #print(lenWords)
        delimiter = '' # delimiter für .join Methode

        globalWordsGaps = [] 
        for x in range(len(globalWords)):
            globalWordsGaps.append(globalWords[x]) 
            if x == len(globalWords)-1: 
                break # bricht die Schleife ab, sodass kein '' nach dem letzten Wort hinzugefügt wird
            globalWordsGaps.append(' ') # Fügt ein leeres Element zwischen jedem Wort in der Liste ein. Später benutzen wir die .join Methode, um die Liste in einen String umzuwandeln. Die leeren Elemente zeigen an, wo standardmäßig Leerzeichen sein sollen.

        minSpaces = len(globalWords) - 1 # So viele Leerzeichen sind standardmäßig zwischen den Wörtern in der Liste
        target = 80 #Länge der Zeile. Wird in (c) mit Parameter ersetzt.
        n = target - lenWords - minSpaces # So viele Leerzeichen müssen hinzugefügt werden, um auf 80 Zeichen zu kommen.
        #print(n)
        #print(minSpaces)
        addSpaces = n // minSpaces # Anzahl der Leerzeichen, die hinter jedem "standardmäßigen" Leerzeichen hinzugefügt werden müssen
        restSpaces = n - addSpaces*minSpaces #rest
        #print(addSpaces)
        #print(restSpaces)

        i = 1
        #print(addSpaces)
        while i < len(globalWordsGaps): #fuegt Leerzeichen hinzu
            #if n <= 0:
                #break
            globalWordsGaps[i] += addSpaces * ' '
            #n = n - addSpaces
            i += 2 #erhoeht um 2, weil nur in Elementen mit Leerzeichen mehr Leerzeichen hinzugefügt werden sollen
        i = 1
        k = 1 #zweite Laufvariable, die sich nicht um 2 erhoeht
        while k <= restSpaces: #fuegt Rest hinzu
            globalWordsGaps[i] += ' '
            i += 2
            k += 1
        
        
        joinGlobalWords = delimiter.join(globalWordsGaps)
        return joinGlobalWords


    def cutWords(allWords): # cutWords soll das Wort, das eine Teilwörterliste über 80 Zeichen bringt abschneiden und die Teilwörterliste unter 80 Zeichen ausgeben.
        #print(len(allWords))
        lenWords = 0
        cutList = []
        spaces  = 0
        i = 0
        
        while lenWords + spaces < 80:
            lenWords += len(allWords[spaces])
            spaces += 1
            if lenWords + spaces > 80:
                break
            cutList.append(allWords[i])
            i += 1

        return cutList # Woerter werden in Blocktext gesetzt
    #print(blockzeile(cutWords(totalWords)))

    #print(totalLen)
    while totalLen > 80:
        cutList2 = cutWords(tempWords)
        #print(len(cutList2[1]))
        #print(cutList2[0])
        if len(cutList2[0]) > 80:
            over = 80 - cutList2
            cutList2[0] = cutList2[0[:over]] #schneidet Woerter mit mehr als 80 Zeichen ab.
            print(cutList2)
        else:
            #print(cutList2)
            for x in range(len(cutList2)):
                totalLen -= len(cutList2[x])
            totalLen -= len(cutList2)
            print(blockzeile(cutList2))
            del tempWords[:len(cutList2)]
            #print(totalLen)
    delimiter = ' '
    joinTempWords = delimiter.join(tempWords)
    return joinTempWords

woerter = ['Hallo', 'das', 'Langeswort', 'hier','long', 'ist', 'ein', 'Test', 'der', 'zum',' zum', 'Testen', 'gedacht', 'ist', 'blah', 'blah', 'mehr', 'lange', 'woerter', 'test', 'test', 'lalalalalala', 'Hallo', 'das', 'Langeswort', 'hier', 'ist', 'ein', 'Test', 'der', 'zum',' zum', 'Testen', 'gedacht', 'ist', 'blah','lalalalalala', 'Hallo', 'das', 'Langeswort', 'hier', 'ist', 'ein', 'Test', 'der', 'zum',' zum', 'Testen', 'gedacht', 'ist', 'blah']


print(blocksatz(woerter))
'''

#Aufgabe 1b)

def blocksatz(totalWords,characters):

    totalLen = 0
    for x in range(len(totalWords)):
        totalLen += len(totalWords[x])
    totalLen += len(totalWords)

    tempWords = totalWords #temporaere Liste aus der Element geloescht werden

    def blockzeile(globalWords): # Erfüllt Aufgabe für eine Zeile mit weniger als 80 Zeichen

        lenWords = 0
        for x in range(len(globalWords)):
            lenWords += len(globalWords[x]) # Ermittelt die Gesamtlänge der Wörter in der Liste
        #print(lenWords)
        delimiter = '' # delimiter für .join Methode

        globalWordsGaps = [] 
        for x in range(len(globalWords)):
            globalWordsGaps.append(globalWords[x]) 
            if x == len(globalWords)-1: 
                break # bricht die Schleife ab, sodass kein '' nach dem letzten Wort hinzugefügt wird
            globalWordsGaps.append(' ') # Fügt ein leeres Element zwischen jedem Wort in der Liste ein. Später benutzen wir die .join Methode, um die Liste in einen String umzuwandeln. Die leeren Elemente zeigen an, wo standardmäßig Leerzeichen sein sollen.

        minSpaces = len(globalWords) - 1 # So viele Leerzeichen sind standardmäßig zwischen den Wörtern in der Liste
        target = characters #Länge der Zeile. Wird in (c) mit Parameter ersetzt.
        n = target - lenWords - minSpaces # So viele Leerzeichen müssen hinzugefügt werden, um auf 80 Zeichen zu kommen.
        #print(n)
        #print(minSpaces)
        addSpaces = n // minSpaces # Anzahl der Leerzeichen, die hinter jedem "standardmäßigen" Leerzeichen hinzugefügt werden müssen
        restSpaces = n - addSpaces*minSpaces #rest
        #print(addSpaces)
        #print(restSpaces)

        i = 1
        #print(addSpaces)
        while i < len(globalWordsGaps): #fuegt Leerzeichen hinzu
            #if n <= 0:
                #break
            globalWordsGaps[i] += addSpaces * ' '
            #n = n - addSpaces
            i += 2 #erhoeht um 2, weil nur in Elementen mit Leerzeichen mehr Leerzeichen hinzugefügt werden sollen
        i = 1
        k = 1 #zweite Laufvariable, die sich nicht um 2 erhoeht
        while k <= restSpaces: #fuegt Rest hinzu
            globalWordsGaps[i] += ' '
            i += 2
            k += 1
        
        
        joinGlobalWords = delimiter.join(globalWordsGaps)
        return joinGlobalWords


    def cutWords(allWords): # cutWords soll das Wort, das eine Teilwörterliste über 80 Zeichen bringt abschneiden und die Teilwörterliste unter 80 Zeichen ausgeben.
        #print(len(allWords))
        lenWords = 0
        cutList = []
        spaces  = 0
        i = 0
        
        while lenWords + spaces < characters:
            lenWords += len(allWords[spaces])
            spaces += 1
            if lenWords + spaces > characters:
                break
            cutList.append(allWords[i])
            i += 1

        return cutList # Woerter werden in Blocktext gesetzt
    #print(blockzeile(cutWords(totalWords)))

    #print(totalLen)
    while totalLen > characters:
        cutList2 = cutWords(tempWords)
        #print(len(cutList2[1]))
        #print(cutList2[0])
        if len(cutList2[0]) > characters:
            over = characters - cutList2
            cutList2[0] = cutList2[0[:over]] #schneidet Woerter mit mehr als 80 Zeichen ab.
            print(cutList2)
        else:
            #print(cutList2)
            for x in range(len(cutList2)):
                totalLen -= len(cutList2[x])
            totalLen -= len(cutList2)
            print(blockzeile(cutList2))
            del tempWords[:len(cutList2)]
            #print(totalLen)
    delimiter = ' '
    joinTempWords = delimiter.join(tempWords)
    return joinTempWords

woerter = ['Hallo', 'das', 'Langeswort', 'hier','long', 'ist', 'ein', 'Test', 'der', 'zum',' zum', 'Testen', 'gedacht', 'ist', 'blah', 'blah', 'mehr', 'lange', 'woerter', 'test', 'test', 'lalalalalala', 'Hallo', 'das', 'Langeswort', 'hier', 'ist', 'ein', 'Test', 'der', 'zum',' zum', 'Testen', 'gedacht', 'ist', 'blah','lalalalalala', 'Hallo', 'das', 'Langeswort', 'hier', 'ist', 'ein', 'Test', 'der', 'zum',' zum', 'Testen', 'gedacht', 'ist', 'blah']


print(blocksatz(woerter,80))

#1c)
'''
def block(words):
    text = []  # Hier sammle ich alle Zeilen
    line = []  # Hier sammle ich alle Wörter und Leerzeichen bis es 80 Zeichen gibt

    def lenList(a):  # Diese Funktion brauche ich, um die Anzahl von allen Elementen zu bestimmen
        counter = 0
        for item in a:
            counter += len(item)
        return counter
    
    for i in range(len(words)):
        
        if len(words[i]) > 80:  # Dieser Teil betrachtet den Fall, wenn Wörter über 80 Zeichen lang sind
            repeats = len(words[i]) // 80  # Hier bestimme ich, wie viele solche Schnitte ich habe
            for k in range(repeats):
                part = words[i][k * 80: k * 80 + 80]
                text.append(part)  # Directly append since each part is exactly 80 characters
            if repeats * 80 < len(words[i]):  # Restabschnitt, der kleiner als 80 ist, wird in der neuen Zeile direkt gespeichert
                lastPartOfABIgWord = words[i][repeats * 80: repeats * 80 + 80]
                line = [lastPartOfABIgWord]
        elif lenList(line) + len(words[i]) + 1 <= 80:  # Sonst, wenn das Wort kürzer als 80 Zeichen ist und die Zeile die Länge 80 nicht überschreitet
            line.append(words[i])
        else:
            spaces = 80 - lenList(line)  # Anzahl der Leerzeichen
            for j in range(spaces):
                indexOfSpace = j % (len(line) - 1) if len(line) > 1 else 0
                line[indexOfSpace] += " "
            text.append("".join(line))  # Zeile abschließen und speichern
            line = [words[i]]
    
    if line:  # Überprüfen, ob "line" nicht leer ist, und wenn nicht, sie am Ende anhängen
        spaces = 80 - lenList(line)
        for j in range(spaces):
            indexOfSpace = j % (len(line) - 1) if len(line) > 1 else 0
            line[indexOfSpace] += " "
        text.append("".join(line))  # Sicherstellen, dass die Elemente in "line" mit einem Leerzeichen getrennt werden
    
    return text

filename = 'words.txt' #datei lesen und Wöter manipulieren
words = read_words_from_file(filename)

for line in block(words):
    print(line)
'''