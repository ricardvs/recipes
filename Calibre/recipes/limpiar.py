from bs4 import BeautifulSoup, Tag

with open('to_process/androidQ.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    to_delete = ['noscript', 'head', 'header', 'nav', 'aside', 'footer']
    to_delete_multiple = [{'tag': 'script', 'attrs': None},
                          {'tag': 'style', 'attrs': None},
                          {'tag': 'div', 'attrs': {'id': 'sidebarLastestPosts'}},
                          {'tag': 'div', 'attrs': {'id': 'slidersFooter'}},
                          {'tag': 'div', 'attrs': {'id': 'singlePopularPosts'}},
                          {'tag': 'div', 'attrs': {'id': 'singleNavDesktopPrev'}},
                          {'tag': 'div', 'attrs': {'id': 'singlePostComments'}},
                          {'tag': 'div', 'attrs': {'class': 'singlePostShare'}},
                          {'tag': 'div', 'attrs': {'class': 'sliderFooterRRSS'}},
                          ]

    for elem in to_delete:
        tag = soup.find(elem)  # type: Tag

        if tag is not None:
            tag.decompose()

    for elem in to_delete_multiple:
        for script in soup.findAll(elem['tag'], elem['attrs']):  # type: Tag
            script.decompose()

    for tag in soup.findAll('div', {'id': 'menu'}):  # type: Tag
        tag.decompose()

    for tag in soup.findAll('div', {'id': 'singlePostTags'}):  # type: Tag
        tag.decompose()

    # print soup.prettify()

    print soup.find('h1').prettify()
    print soup.find('section', {'id': 'article'}).prettify()
