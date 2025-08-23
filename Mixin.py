class Livro(object):

    def __init__(self, nome, counteudo):
        self.nome = nome
        self.countedo = counteudo

class Jornal(object):

    def __init__(self, nome, counteudo):
        self.nome = nome
        self.countedo = counteudo

class LivroHTMLMixin(object):

    def renderizar(self):
        return f'<html><title>{self.nome}</title><body>{self.countedo}</body></html>'

class LivroHTML(Livro, LivroHTMLMixin):
    pass

class JornalHTML(Jornal, LivroHTMLMixin):
    pass

livro_html = LivroHTML('Psicologia do Sucesso', 'Mindset de Cresccimento')
jornal_html = JornalHTML('Noticiário', 'Acidente Grave')
print(livro_html.renderizar())
print(jornal_html.renderizar())