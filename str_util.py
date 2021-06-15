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

def set_table_or_chart_name(document, text, bold=False, style=None, size=12):
    """ 编写表名或图名
    
    一号：27.5 小一号：24
    二号：21 小二号：18
    三号：15.75
    四号：13.75
    小四：12
    五号：10.5
    @param document:
    @param text:
    @param bold:
    @param style:
    @param size:
    @return:
    """
    paragraph = document.add_paragraph('', style)
    # 居中
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    if style:
        paragraph.style = style
    else:
        paragraph.style = document.styles['Normal']
        paragraph_run = paragraph.add_run(text)
        paragraph_run.font.color.rgb = COLOR_BLACK
        # 字体大小
        paragraph_run.font.size = Pt(size)
        #
        paragraph_run.font.name = FONT_NAME_BLACK
        paragraph_run._element.rPr.rFonts.set(qn('w:eastAsia'), "黑体")
        if bold:
            # 是否加粗
            paragraph_run.bold = True
