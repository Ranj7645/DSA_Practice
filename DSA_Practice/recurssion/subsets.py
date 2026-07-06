from attr.filters import exclude
from jsonschema.validators import extend

ans = []
def subset1(original_str, index,temp_str):
    if index>=len(original_str):
        ans.append(temp_str)
        return
    temp_str = temp_str+original_str[index]
    subset1(original_str,index+1,temp_str)
    temp_str = temp_str[:len(temp_str)-1]
    subset1(original_str, index + 1, temp_str)

# subset1("abc",0,"")
print("ans", ans)

def subset2(original_str,index,temp_str):
    if index>=len(original_str):
        return [temp_str]
    include = subset2(original_str,index +1,temp_str+original_str[index])
    exclude = subset2(original_str,index +1,temp_str)
    # include.extend(exclude)
    # return include
    # or
    return include+exclude


print(subset2("abc",0,""))