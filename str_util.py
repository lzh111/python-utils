def remove_the_last_punctuate_in_the_string(string):
    """
    去掉字符串中最后一个标点符号，例如
    输入："1、2、3、4、"
    返回："1、2、3、4"
    """
    return string[::-1].replace('、', '', 1)[::-1]
    
    
def _replace_brackets(text):
    """
    将中文括号改为英文括号
    @param text:
    @return:
    """
    return text.replace("（", "(").replace("）", ")")
