import pywikibot
from pywikibot import pagegenerators
siteC = pywikibot.Site(u'commons', u'commons')
siteC.login()

category = pywikibot.Category(siteC, u'Images from Wiki Loves Africa 2021')
gen = pagegenerators.CategorizedPageGenerator(category)
cmp_sound = 0
cmp_video = 0

for file in gen:

    title = file.title()
    text = file.text
    print('Analyze: ' + file.title())

    if title[-4:] == '.webm' or title[-4:] == '.ogv':
        if '[[Category:Videos from Wiki Loves Africa 2021]]' not in text:
            newtext = text + '\r\n' + '[[Category:Videos from Wiki Loves Africa 2021]]'
            file.text = newtext
            file.save(u"Add category video WLA")
            print(file.title() + ' - WLA ***************************')
            cmp_sound = cmp_sound + 1
    elif title[-4:] == '.ogg' or title[-4:] == '.wav':
        if '[[Category:Audio from Wiki Loves Africa 2021]]' not in text:
            newtext = text + '\r\n' + '[[Category:Audio from Wiki Loves Africa 2021]]'
            file.text = newtext
            file.save(u"Add category sound WLA")
            print(file.title() + ' - WLA ***************************')
            cmp_video = cmp_video + 1

print(str(cmp_sound) + ' sounds')
print(str(cmp_video) + ' videos')

