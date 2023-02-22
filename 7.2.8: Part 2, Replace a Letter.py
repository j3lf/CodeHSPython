# update the function body to return `string`, but with the character at
# `index` replaced by `letter`
string = "Pepper"
index = 3
string2 = "e"

def replace_at_index(string, index, string2):
    return string[:index] + string2 + string[index+1:]

print (replace_at_index(string,index, string2))
