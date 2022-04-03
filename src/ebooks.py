import pdftotext

def encrypt(filePath, inputStr):
    with open(filePath, "rb") as f:
        pdf = pdftotext.PDF(f)
    
    inputStrArr = inputStr.split()
    final = dict.fromkeys(inputStrArr, "")
    for pageNum in range(0, len(pdf)):
        wordList = pdf[pageNum].split()
        for wordInd in range(0, len(wordList)):
            if wordList[wordInd] in inputStrArr:
                final[wordList[wordInd]] = (str(pageNum) + " " + str(wordInd))
                inputStrArr.remove(wordList[wordInd])

    result = ""
    for strInd in final.values():
        result += strInd + " "
    return [result, inputStrArr]

def decrypt(filePath, ciphertext):
    res = ""
    with open(filePath, "rb") as f:
        pdf = pdftotext.PDF(f)
    indices = ciphertext.split()
    for index in range(0, len(indices), 2):
        wordList = pdf[int(indices[index])]
        wordList = wordList.split()
        res += (wordList[int(indices[index + 1])]) + " "
    return res