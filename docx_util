def set_table_name(document, text, bold=False, style=None, size=12):
    """ 为表或者图设定名
    
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
