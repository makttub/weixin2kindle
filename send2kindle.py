from calibre.web.feeds.recipes import BasicNewsRecipe
 
class Git_Pocket_Guide(BasicNewsRecipe):
 
    title = 'Git Pocket Guide'
    description = ''
    cover_url = 'http://akamaicovers.oreilly.com/images/0636920024972/lrg.jpg'
 
    url_prefix = 'http://chimera.labs.oreilly.com/books/1230000000561/'
    no_stylesheets = True
    keep_only_tags = [{ 'class': 'chapter' }]
 
    def get_title(self, link):
        return link.contents[0].strip()
    
    @staticmethod
    def parse_index(self):
        soup = self.index_to_soup(self.url_prefix + 'index.html')
 
        div = soup.find('div', { 'class': 'toc' })
 
        articles = []
        for link in div.findAll('a'):
            if '#' in link['href']:
                continue
 
            if not 'ch' in link['href']:
                continue
 
            til = self.get_title(link)
            url = self.url_prefix + link['href']
            a = { 'title': til, 'url': url }
 
            articles.append(a)
 
        ans = [('Git_Pocket_Guide', articles)]
        
        return ans