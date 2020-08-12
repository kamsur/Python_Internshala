class book:
    def __init__(self,t=None,a=None,pub=None,p=0):
        self.title=t
        self.author=a
        self.publisher=pub
        self.price=p
        self.royalty=0
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_publisher(self):
        return self._publisher
    def get_price(self):
        return self._price
    def get_royalty(self):
        return self._royalty
    def set_title(self,t):
        if t is None:
            print('No title entered')
        else:
            self._title=t
    def set_author(self,a):
        if a is None:
            print('No author entered')
        else:
            self._author=a
    def set_publisher(self,pub):
        if pub is None:
            print('No publisher entered')
        else:
            self._publisher=pub
    def set_price(self,p):
        if type(p)!=int or p<0:
            print('Price should be a no greater than zero')
        else:
            self._price=p
    def set_royalty(self,r):
        if type(r)!=int or r<0:
            print('Royalty should be a no greater than zero')
        else:
            self._royalty=r
    title=property(get_title,set_title)
    author=property(get_author,set_author)
    publisher=property(get_publisher,set_publisher)
    price=property(get_price,set_price)
    royalty=property(get_royalty,set_royalty)
    def royalty(n):
        if type(n)!=int or n<0:
            print('Number of copies should be a no greater than zero')
        elif n<=500:
            self.royalty=0.1*p*n
        elif n>500 and n<=1000:
            self.royalty=0.1*p*500+0.125*p*(n-500)
        else:
            self.royalty=0.1*p*500+0.125*p*1000+0.15*p*(n-1500)
        print('Royalty is {}'.format(self.royalty))
class ebook(book):
    def __init__(self,t,a,pub,p,f=''):
        super().__init__(t,a,pub,p)
        self.format=f
    def get_format(self):
        return self._format
    def set_format(self,f):
        if f is None:
            print('No format entered')
        else:
            self._format=f
    format=property(get_format,set_format)
    def royalty(n):
        if type(n)!=int or n<0:
            print('Number of copies should be a no greater than zero')
        elif n<=500:
            self.royalty=0.1*p*n
        elif n>500 and n<=1000:
            self.royalty=0.1*p*500+0.125*p*(n-500)
        else:
            self.royalty=0.1*p*500+0.125*p*1000+0.15*p*(n-1500)
        self.royalty=(1-0.12)*self.royalty
        print('Royalty is {}'.format(self.royalty))
