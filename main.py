# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        file_content = f.read()
        # print(file_content)
    
    return file_content


def count_words():
    text = read_file_content("./story.txt")
    
    # [assignment] Add your code here
    results = {}
    counter = 0

    # convert to list 
    text = text.split()
  
    # count unique words 
    for word in text:
        # check if current word is already in the results dictionary 
        if word not in results:
            counter = text.count(word)
            results[word]=counter
        
        
    print(results)
   



    return {"as": 10, "would": 20}

count_words()