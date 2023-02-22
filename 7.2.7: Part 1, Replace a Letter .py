# update the function body to return the input `string` 
# with the character at `index` replaced with a dash (-)
string = "Elephant"
index = 3
letter = "-"

def replace_at_index(string, index):
    return string[:index] + letter + string[index+1:]

print (replace_at_index(string,index))
