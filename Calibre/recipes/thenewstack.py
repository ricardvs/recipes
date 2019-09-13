from bs4 import BeautifulSoup, Tag

with open('to_process/newstack.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    to_delete = ['noscript', 'head', 'header', 'nav', 'aside', 'footer']
    to_delete_multiple = [{'tag': 'script', 'attrs': None},
                          {'tag': 'style', 'attrs': None},
                          {'tag': 'div', 'attrs': {'class': 'postshare'}},
                          {'tag': 'div', 'attrs': {'id': 'post-tags'}},
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

    article = soup.find('article')
    old_h1 = article.find('div', {'id': 'post-title'})  # type: Tag
    h1 = soup.new_tag('h1')
    h1.append(old_h1.text.strip())

    old_h1.replace_with(h1)

    body = soup.find('body') # type: Tag
    body.clear()

    body.append(article)

    print soup.prettify()
