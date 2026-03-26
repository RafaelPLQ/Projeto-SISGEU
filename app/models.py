from django.db import models
import uuid


class Usuario(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    curso = models.CharField(max_length=150, blank=True, null=True)
    instituicao = models.CharField(max_length=200, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    TIPO_CHOICES = [
        ('despesa', 'Despesa'),
        ('receita', 'Receita'),
        ('ambos', 'Ambos'),
    ]

    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, db_column='idusuario')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cor = models.CharField(max_length=7, default='#6366F1')
    icone = models.CharField(max_length=50, null=True, blank=True)
    padrao = models.BooleanField(default=False)

    class Meta:
        db_table = 'categorias'
        indexes = [
            models.Index(fields=['usuario']),
        ]

    def __str__(self):
        return self.nome


class Orcamento(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idusuario')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='idcategoria')
    mes = models.IntegerField()
    ano = models.IntegerField()
    limite = models.DecimalField(max_digits=12, decimal_places=2)
    gasto_atual = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = 'orcamentos'
        unique_together = ('usuario', 'categoria', 'mes', 'ano')
        indexes = [
            models.Index(fields=['mes', 'ano']),
            models.Index(fields=['categoria']),
        ]

    def __str__(self):
        return f"Orçamento {self.categoria} - {self.mes}/{self.ano}"


class Despesa(models.Model):
    STATUS_CHOICES = [
        ('confirmado', 'Confirmado'),
        ('pendente', 'Pendente'),
        ('cancelado', 'Cancelado'),
    ]
    
    PERIODICIDADE_CHOICES = [
        ('diario', 'Diário'),
        ('semanal', 'Semanal'),
        ('mensal', 'Mensal'),
        ('anual', 'Anual'),
    ]

    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idusuario')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, db_column='idcategoria')
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    descricao = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='confirmado')
    recorrente = models.BooleanField(default=False)
    periodicidade = models.CharField(max_length=10, choices=PERIODICIDADE_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'despesas'
        indexes = [
            models.Index(fields=['usuario']),
            models.Index(fields=['categoria']),
            models.Index(fields=['data']),
        ]

    def __str__(self):
        return f"Despesa de {self.valor} - {self.data}"


class Receita(models.Model):
    PERIODICIDADE_CHOICES = [
        ('unica', 'Única'),
        ('diario', 'Diário'),
        ('semanal', 'Semanal'),
        ('mensal', 'Mensal'),
        ('anual', 'Anual'),
    ]

    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idusuario')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, db_column='idcategoria')
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    fonte = models.CharField(max_length=100)
    periodicidade = models.CharField(max_length=10, choices=PERIODICIDADE_CHOICES, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'receitas'
        indexes = [
            models.Index(fields=['usuario']),
            models.Index(fields=['categoria']),
            models.Index(fields=['data']),
        ]

    def __str__(self):
        return f"Receita de {self.valor} - {self.data}"


class Meta(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idusuario')
    nome = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    valor_alvo = models.DecimalField(max_digits=12, decimal_places=2)
    valor_atual = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    prazo = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'metas'
        indexes = [
            models.Index(fields=['usuario']),
        ]
        verbose_name_plural = 'Metas'

    def __str__(self):
        return self.nome


class Alerta(models.Model):
    TIPO_CHOICES = [
        ('orcamento_80', 'Orçamento 80%'),
        ('orcamento_100', 'Orçamento 100%'),
        ('meta_prazo', 'Meta com Prazo'),
        ('saldo_negativo', 'Saldo Negativo'),
    ]

    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idusuario')
    orcamento = models.ForeignKey(Orcamento, on_delete=models.SET_NULL, null=True, blank=True, db_column='idorcamento')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensagem = models.TextField()
    lido = models.BooleanField(default=False)

    class Meta:
        db_table = 'alertas'
        indexes = [
            models.Index(fields=['usuario', 'lido']),
            models.Index(fields=['orcamento']),
        ]

    def __str__(self):
        return f"Alerta: {self.tipo} - {self.usuario}"

        