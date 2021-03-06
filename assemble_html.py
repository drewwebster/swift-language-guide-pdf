from bs4 import BeautifulSoup

directory = '2018-06-04/source/docs.swift.org/swift-book/LanguageGuide/'
directoryWrite = '2018-06-04/final/docs.swift.org/swift-book/LanguageGuide/'

with open(directory + '/TheBasics.html') as fp:
    sp = BeautifulSoup(fp, 'html.parser')

# Grab the filenames that have the sections we will slam into full book

filenames = []
for tag in sp.find_all("li", class_="toctree-l2"):
    # print(tag.find('a')['href'].strip('#'))
    filenames.append(tag.find('a')['href'].strip('#'))

# print(filenames)

# Open each filename, get the content section

sections = []
for filename in filenames:
    file = open(directory + filename)
    section = BeautifulSoup(file, 'html.parser')
    section = section.find('main').find('article').find(
        'div', class_='section', recursive=False)
    print(section['id'])
    sections.append(section)

# Put the sections together in the html document
# We use already parsed "TheBasics.html" to start since we already have it handy
article = sp.find('main').find('article').find(
    'div', class_='section', recursive=False)

print('removing', article['id'])

# removes existing "the basics section"
article.extract()

# add all the sections

page = sp.find("article", class_='page')
for section in sections:
    print("appending ", section['id'])
    page.append(section)

# write out the assembled html
out = open(directoryWrite + "WholeBook.html", "w")
out.write(str(sp))
