import xml.etree.ElementTree as ET
def speakkommand():
    tree = ET.parse('commands\\speak\\speak.xml')
    root = tree.getroot()
    frases = {}
    answers = []
    for child in root:
        phrase = str(*child.attrib.values())
        for answer in child:
            answers.append(answer.text)
    frases[phrase] = answers
    return frases


def timedecoder(type:str): #time или date
    phrases = []
    tree = ET.parse('commands\\timedate\\timeanswers.xml')
    root = tree.getroot()
    for child in root:
        f = str(*child.attrib.values())
        if f == type:
            for phrse in range(0,len(child)):
                phrases.append(child[phrse].text)
            return phrases
def jokedecoder():
    phrases = []
    tree = ET.parse('commands\\jokes\\j_phrases.xml')
    root = tree.getroot()
    for child in root:
        for ans in child:
            phrases.append(ans.text)
    return(phrases)