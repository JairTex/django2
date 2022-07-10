from django.db import models
from  stdimage.models import StdImageField

#Signals
from django.db.models import signals
#Serve para definir o que vai acontecer antes ou depois de receber um dado
from django.template.defaultfilters import slugify
#slug = produto-nome-exemplo

#Classe Abstrada (Ñ será criada no banco mas extendida pelas outras classes)
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now_add=True)
    ativo =  models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb' : (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

#classe signal
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)
