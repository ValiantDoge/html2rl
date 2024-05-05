from bs4 import BeautifulSoup
from reportlab.platypus import Paragraph

def cleanHTML(rich_text, font_name):
    soup = BeautifulSoup(rich_text, 'html.parser')

    for pTag in soup.find_all('p'):
        if pTag.parent.name == 'li':
            pTag.unwrap()

    for spanTag in soup.find_all('span'):
        spanTag.name = 'font'
        style_value = spanTag['style']
        if style_value:
            color = style_value.split('color:')[-1].strip()
            spanTag['color'] = color
            del spanTag['style']

    for ul_ol in soup.find_all(['ul', 'ol']):
        ul_ol.wrap(soup.new_tag("p"))
        
    for p_el in soup.find_all('p'):
        p_el.name = 'para'

        for strong_tags in p_el.find_all('strong'):
            strong_tags.name = 'b'
        for em_tags in p_el.find_all('em'):
            em_tags.name = 'i'

        bold_italic_tags = soup.find_all('b')
        if bold_italic_tags:
            for tag in bold_italic_tags:
                italic_tags_inside_bold = tag.find_all('i')
                for italic_tag in italic_tags_inside_bold:
                    # Replace <b><i> tags with appropriate font tag
                    italic_tag.name = 'font'
                    italic_tag['name'] = font_name  # Specify the bold italic font

                    # Remove the <b> tag
                    tag.unwrap()
        
        
        p_el.insert_after(soup.new_tag("br"))
    
    return str(soup)

def toRParagraph(rich_text, styleList):
    para_list = rich_text.split('<br/>')
    list_of_para = []
    for para in para_list:
        paraSoupObj = BeautifulSoup(para, 'html.parser')
        liTags = paraSoupObj.find_all('li')
        if liTags:
            bullet_count = 1
            for li in liTags:
                if li.parent.name == 'ul':
                    para_obj = Paragraph(f"""{li}""", style=styleList["ContentCal"], bulletText='●')
                    list_of_para.append([para_obj])
                elif li.parent.name == 'ol':
                    para_obj = Paragraph(f"""{li}""", style=styleList["ContentCal"], bulletText=str(bullet_count))
                    list_of_para.append([para_obj])
                    bullet_count += 1
        else:
            para_obj = Paragraph(f"""{para}""", style=styleList["ContentCal"])
            list_of_para.append([para_obj])

    return list_of_para