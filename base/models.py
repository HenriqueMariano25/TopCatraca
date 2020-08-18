# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arquivos(models.Model):
    cod_arquivo = models.AutoField(db_column='COD_ARQUIVO', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.
    caminho = models.CharField(db_column='Caminho', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=250, blank=True, null=True)  # Field name made lowercase.
    marcacoes = models.SmallIntegerField(db_column='Marcacoes')  # Field name made lowercase.
    pessoasexportar = models.SmallIntegerField(db_column='PessoasExportar')  # Field name made lowercase.
    tipoexportacao = models.SmallIntegerField(db_column='TipoExportacao')  # Field name made lowercase.
    tipobilhetes = models.IntegerField(db_column='TipoBilhetes')  # Field name made lowercase.
    textoentrada = models.CharField(db_column='TextoEntrada', max_length=20)  # Field name made lowercase.
    textosaida = models.CharField(db_column='TextoSaida', max_length=20)  # Field name made lowercase.
    textofuncao0 = models.CharField(db_column='TextoFuncao0', max_length=20)  # Field name made lowercase.
    textofuncao1 = models.CharField(db_column='TextoFuncao1', max_length=20)  # Field name made lowercase.
    textofuncao2 = models.CharField(db_column='TextoFuncao2', max_length=20)  # Field name made lowercase.
    textofuncao3 = models.CharField(db_column='TextoFuncao3', max_length=20)  # Field name made lowercase.
    textofuncao4 = models.CharField(db_column='TextoFuncao4', max_length=20)  # Field name made lowercase.
    textofuncao5 = models.CharField(db_column='TextoFuncao5', max_length=20)  # Field name made lowercase.
    textofuncao6 = models.CharField(db_column='TextoFuncao6', max_length=20)  # Field name made lowercase.
    textofuncao7 = models.CharField(db_column='TextoFuncao7', max_length=20)  # Field name made lowercase.
    textofuncao8 = models.CharField(db_column='TextoFuncao8', max_length=20)  # Field name made lowercase.
    textofuncao9 = models.CharField(db_column='TextoFuncao9', max_length=20)  # Field name made lowercase.
    automatico = models.SmallIntegerField(db_column='Automatico', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Arquivos'


class Arquivosinners(models.Model):
    cod_arquivo = models.ForeignKey(Arquivos, models.DO_NOTHING, db_column='COD_ARQUIVO')  # Field name made lowercase.
    numinner = models.ForeignKey('Inners', models.DO_NOTHING, db_column='NumInner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivosInners'


class Auditoria(models.Model):
    login = models.BooleanField(db_column='Login', blank=True, null=True)  # Field name made lowercase.
    logoff = models.BooleanField(db_column='Logoff', blank=True, null=True)  # Field name made lowercase.
    altperfil = models.BooleanField(db_column='AltPerfil', blank=True, null=True)  # Field name made lowercase.
    altzonatempo = models.BooleanField(db_column='AltZonaTempo', blank=True, null=True)  # Field name made lowercase.
    altlocaisacesso = models.BooleanField(db_column='AltLocaisAcesso', blank=True, null=True)  # Field name made lowercase.
    altcadinners = models.BooleanField(db_column='AltCadInners', blank=True, null=True)  # Field name made lowercase.
    altcadfunc = models.BooleanField(db_column='AltCadFunc', blank=True, null=True)  # Field name made lowercase.
    altcadvisit = models.BooleanField(db_column='AltCadVisit', blank=True, null=True)  # Field name made lowercase.
    libacessomon = models.BooleanField(db_column='LibAcessoMon', blank=True, null=True)  # Field name made lowercase.
    bloqlogin = models.BooleanField(db_column='BloqLogin', blank=True, null=True)  # Field name made lowercase.
    marcacoes = models.BooleanField(db_column='Marcacoes', blank=True, null=True)  # Field name made lowercase.
    usuariobio = models.BooleanField(db_column='UsuarioBIO', blank=True, null=True)  # Field name made lowercase.
    altcartoes = models.BooleanField(db_column='AltCartoes', blank=True, null=True)  # Field name made lowercase.
    altferiados = models.BooleanField(db_column='AltFeriados', blank=True, null=True)  # Field name made lowercase.
    acessonegado = models.BooleanField(db_column='AcessoNegado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auditoria'


class Bilhetes(models.Model):
    cod_pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA')  # Field name made lowercase.
    cod_local = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='COD_LOCAL', blank=True, null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    numinner = models.ForeignKey('Inners', models.DO_NOTHING, db_column='NumInner', blank=True, null=True, related_name='numinner')  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora', primary_key=True)  # Field name made lowercase.
    ordem = models.IntegerField(db_column='Ordem', blank=True, null=True)  # Field name made lowercase.
    exportado = models.SmallIntegerField(db_column='Exportado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bilhetes'
        ordering = ['datahora']

    def str_data(self):
        return str(self.datahora)

class Bilhetesinvalidos(models.Model):
    id = models.AutoField(primary_key=True)
    numinner = models.SmallIntegerField(db_column='NumInner', blank=True, null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora', blank=True, null=True)  # Field name made lowercase.
    cod_barras = models.CharField(db_column='Cod_barras', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BilhetesInvalidos'


class Bilhetesoffline(models.Model):
    numerocartao = models.ForeignKey('Cartoes', models.DO_NOTHING, db_column='NumeroCartao')  # Field name made lowercase.
    cod_local = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='COD_LOCAL', blank=True, null=True)  # Field name made lowercase.
    numeroinner = models.ForeignKey('Inners', models.DO_NOTHING, db_column='NumeroInner')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora')  # Field name made lowercase.
    ordem = models.IntegerField(db_column='Ordem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BilhetesOffline'


class Bilhetestemp(models.Model):
    cod_pessoa = models.IntegerField(db_column='COD_PESSOA')  # Field name made lowercase.
    cod_local = models.IntegerField(db_column='COD_LOCAL', blank=True, null=True)  # Field name made lowercase.
    numinner = models.SmallIntegerField(db_column='NumInner', blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BilhetesTemp'


class Cartoes(models.Model):
    num_cartao = models.CharField(db_column='NUM_CARTAO', primary_key=True, max_length=16)  # Field name made lowercase.
    cod_pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA', blank=True, null=True)  # Field name made lowercase.
    codigodebarras = models.CharField(db_column='CodigoDeBarras', unique=True, max_length=20)  # Field name made lowercase.
    darbaixa = models.BooleanField(db_column='DarBaixa')  # Field name made lowercase.
    offline = models.BooleanField(db_column='Offline', blank=True, null=True)  # Field name made lowercase.
    semdigital = models.SmallIntegerField(db_column='SemDigital')  # Field name made lowercase.
    enviadolistasemdigital = models.SmallIntegerField(db_column='EnviadoListaSemDigital')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cartoes'


class Cartoesprovisorios(models.Model):
    cod_cartaoprovisorio = models.AutoField(db_column='COD_CARTAOPROVISORIO', primary_key=True)  # Field name made lowercase.
    numerocartao = models.CharField(db_column='NumeroCartao', max_length=16)  # Field name made lowercase.
    cod_pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA')  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio')  # Field name made lowercase.
    fim = models.DateTimeField(db_column='Fim')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CartoesProvisorios'


class Configuracoes(models.Model):
    comunicacao = models.SmallIntegerField(db_column='Comunicacao')  # Field name made lowercase.
    porta = models.SmallIntegerField(db_column='Porta', blank=True, null=True)  # Field name made lowercase.
    portatcp = models.BigIntegerField(db_column='PortaTCP', blank=True, null=True)  # Field name made lowercase.
    listaoffline = models.SmallIntegerField(db_column='ListaOffline')  # Field name made lowercase.
    etiqmargemsuperior = models.FloatField(db_column='EtiqMargemSuperior')  # Field name made lowercase.
    etiqmargemesquerda = models.FloatField(db_column='EtiqMargemEsquerda')  # Field name made lowercase.
    etiqlargura = models.FloatField(db_column='EtiqLargura')  # Field name made lowercase.
    etiqaltura = models.FloatField(db_column='EtiqAltura')  # Field name made lowercase.
    etiqlinhas = models.SmallIntegerField(db_column='EtiqLinhas')  # Field name made lowercase.
    etiqcolunas = models.SmallIntegerField(db_column='EtiqColunas')  # Field name made lowercase.
    etiqdistanciacolunas = models.FloatField(db_column='EtiqDistanciaColunas')  # Field name made lowercase.
    etiqdistancialinhas = models.FloatField(db_column='EtiqDistanciaLinhas')  # Field name made lowercase.
    etiqtamanhopapel = models.SmallIntegerField(db_column='EtiqTamanhoPapel')  # Field name made lowercase.
    etiqlargurafolha = models.FloatField(db_column='EtiqLarguraFolha', blank=True, null=True)  # Field name made lowercase.
    etiqalturafolha = models.FloatField(db_column='EtiqAlturaFolha', blank=True, null=True)  # Field name made lowercase.
    etiqfoto = models.BooleanField(db_column='EtiqFoto')  # Field name made lowercase.
    etiqcodbarras = models.BooleanField(db_column='EtiqCodBarras')  # Field name made lowercase.
    gravaeventos = models.BigIntegerField(db_column='GravaEventos')  # Field name made lowercase.
    ipservidorsmtp = models.CharField(db_column='IPServidorSMTP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    portaservidorsmtp = models.IntegerField(db_column='PortaServidorSMTP', blank=True, null=True)  # Field name made lowercase.
    usersmtp = models.CharField(db_column='UserSMTP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passsmtp = models.CharField(db_column='PassSMTP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    versao = models.CharField(db_column='Versao', max_length=10)  # Field name made lowercase.
    idexportacaovazio = models.BooleanField(db_column='IDExportacaoVazio')  # Field name made lowercase.
    exibereltrilhaauditoria = models.BooleanField(db_column='ExibeRelTrilhaAuditoria')  # Field name made lowercase.
    habilitarrelogiosegundos = models.BooleanField(db_column='HabilitarRelogioSegundos')  # Field name made lowercase.
    habilitarcadastrodigitaisbio = models.BooleanField(db_column='HabilitarCadastroDigitaisBio')  # Field name made lowercase.
    sobrescreverdigitaisbio = models.BooleanField(db_column='SobrescreverDigitaisBio')  # Field name made lowercase.
    intervalobuscatemplate = models.SmallIntegerField(db_column='IntervaloBuscaTemplate')  # Field name made lowercase.
    tempoesperaautorizacao = models.SmallIntegerField(db_column='TempoEsperaAutorizacao')  # Field name made lowercase.
    controlarmarcacaoporminuto = models.BooleanField(db_column='ControlarMarcacaoPorMinuto')  # Field name made lowercase.
    monitorargirocatraca = models.BooleanField(db_column='MonitorarGiroCatraca')  # Field name made lowercase.
    variacao11 = models.BooleanField(db_column='Variacao11')  # Field name made lowercase.
    liberasaidavisita = models.BooleanField(db_column='LiberaSaidaVisita')  # Field name made lowercase.
    qtdetemplatesbio = models.CharField(db_column='QtdeTemplatesBio', max_length=1)  # Field name made lowercase.
    numdigitos = models.IntegerField(db_column='NumDigitos', blank=True, null=True)  # Field name made lowercase.
    permissaoentrada = models.BooleanField(db_column='PermissaoEntrada')  # Field name made lowercase.
    desabilitawebserver = models.BooleanField(db_column='DesabilitaWebServer')  # Field name made lowercase.
    variacao12 = models.CharField(db_column='Variacao12', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Configuracoes'


class Configuracoesvisitantes(models.Model):
    configuravisitantes = models.BooleanField(db_column='ConfiguraVisitantes', blank=True, null=True)  # Field name made lowercase.
    cod_zt = models.IntegerField(db_column='COD_ZT', blank=True, null=True)  # Field name made lowercase.
    cod_perfil = models.IntegerField(db_column='COD_PERFIL', blank=True, null=True)  # Field name made lowercase.
    cod_visitado = models.IntegerField(db_column='COD_VISITADO', blank=True, null=True)  # Field name made lowercase.
    ignorarrota = models.BooleanField(db_column='IgnorarRota', blank=True, null=True)  # Field name made lowercase.
    ignorarantipassback = models.BooleanField(db_column='IgnorarAntiPassback', blank=True, null=True)  # Field name made lowercase.
    ignorarentradas = models.BooleanField(db_column='IgnorarEntradas', blank=True, null=True)  # Field name made lowercase.
    tempovisita = models.DateTimeField(db_column='TempoVisita', blank=True, null=True)  # Field name made lowercase.
    senhaacesso = models.CharField(db_column='SenhaAcesso', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfiguracoesVisitantes'


class Departamentos(models.Model):
    cod_departamento = models.AutoField(db_column='COD_DEPARTAMENTO', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.
    cod_empresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='COD_EMPRESA',related_name="COD_EMPRESA")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Empresas(models.Model):
    cod_empresa = models.AutoField(db_column='COD_EMPRESA', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=70, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=13, blank=True, null=True)  # Field name made lowercase.
    telefone2 = models.CharField(db_column='Telefone2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=13, blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='Contato', max_length=80, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=70, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresas'


class Eventos(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora')  # Field name made lowercase.
    cod_local = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='COD_LOCAL', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ninner = models.SmallIntegerField(db_column='nInner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eventos'


class Feriados(models.Model):
    cod_feriado = models.AutoField(db_column='COD_FERIADO', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data')  # Field name made lowercase.
    repete = models.BooleanField(db_column='Repete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feriados'


class Fotos(models.Model):
    cod_pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA')  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia')  # Field name made lowercase.
    foto = models.BinaryField(db_column='Foto')  # Field name made lowercase.
    padrao = models.BooleanField(db_column='Padrao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fotos'


class Funcionarios(models.Model):
    cod_pessoa = models.OneToOneField('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    cod_departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='COD_DEPARTAMENTO')  # Field name made lowercase.
    cod_zt = models.ForeignKey('Zonasdetempo', models.DO_NOTHING, db_column='COD_ZT')  # Field name made lowercase.
    cod_perfil = models.ForeignKey('Perfisdeacesso', models.DO_NOTHING, db_column='COD_PERFIL')  # Field name made lowercase.
    ignorarrota = models.BooleanField(db_column='IgnorarRota')  # Field name made lowercase.
    ignorarantipassback = models.BooleanField(db_column='IgnorarAntiPassback')  # Field name made lowercase.
    ignorarentradas = models.BooleanField(db_column='IgnorarEntradas')  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=60, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=60, blank=True, null=True)  # Field name made lowercase.
    niveldeacesso = models.IntegerField(db_column='NivelDeAcesso', blank=True, null=True)  # Field name made lowercase.
    bloqueado = models.BooleanField(db_column='Bloqueado')  # Field name made lowercase.
    iniciobloqueio = models.DateTimeField(db_column='InicioBloqueio', blank=True, null=True)  # Field name made lowercase.
    fimbloqueio = models.DateTimeField(db_column='FimBloqueio', blank=True, null=True)  # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=20, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idexportacao = models.CharField(db_column='IDExportacao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    senhaacesso = models.CharField(db_column='SenhaAcesso', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtultimaalteracaosenha = models.DateTimeField(db_column='DtUltimaAlteracaoSenha', blank=True, null=True)  # Field name made lowercase.
    cripteddata = models.BooleanField(db_column='CriptedData', blank=True, null=True)  # Field name made lowercase.
    precisaalterarsenha = models.BooleanField(db_column='PrecisaAlterarSenha', blank=True, null=True)  # Field name made lowercase.
    countsenhainvalida = models.IntegerField(db_column='CountSenhaInvalida', blank=True, null=True)  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funcionarios'


class Funcoes(models.Model):
    cod_funcao = models.SmallIntegerField(db_column='COD_FUNCAO', primary_key=True)  # Field name made lowercase.
    habilitada = models.BooleanField(db_column='Habilitada')  # Field name made lowercase.
    linha1 = models.CharField(db_column='Linha1', max_length=16)  # Field name made lowercase.
    linha2 = models.CharField(db_column='Linha2', max_length=16)  # Field name made lowercase.
    tempo = models.SmallIntegerField(db_column='Tempo')  # Field name made lowercase.
    permitirvisitantes = models.BooleanField(db_column='PermitirVisitantes')  # Field name made lowercase.
    acionaporta1 = models.BooleanField(db_column='AcionaPorta1')  # Field name made lowercase.
    acionaporta2 = models.BooleanField(db_column='AcionaPorta2')  # Field name made lowercase.
    consultazona = models.BooleanField(db_column='ConsultaZona')  # Field name made lowercase.
    consultaantipassback = models.BooleanField(db_column='ConsultaAntipassback')  # Field name made lowercase.
    consultarota = models.BooleanField(db_column='ConsultaRota')  # Field name made lowercase.
    consultanumeroentradas = models.BooleanField(db_column='ConsultaNumeroEntradas')  # Field name made lowercase.
    liberacatraca = models.SmallIntegerField(db_column='LiberaCatraca')  # Field name made lowercase.
    fazverificacaobiometrica = models.BooleanField(db_column='FazVerificacaoBiometrica')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funcoes'


class Historicosenhas(models.Model):
    id = models.AutoField(primary_key=True)
    cod_pessoa = models.IntegerField(db_column='COD_PESSOA', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cripted = models.BooleanField(db_column='Cripted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistoricoSenhas'


class Horariossirene(models.Model):
    numinner = models.ForeignKey('Inners', models.DO_NOTHING, db_column='NumInner')  # Field name made lowercase.
    horario = models.DateTimeField(db_column='Horario')  # Field name made lowercase.
    diashabilitados = models.SmallIntegerField(db_column='DiasHabilitados')  # Field name made lowercase.
    desativada = models.BooleanField(db_column='Desativada')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HorariosSirene'


class Inners(models.Model):
    numero = models.AutoField(db_column='Numero', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.
    leitor1habilitado = models.BooleanField(db_column='Leitor1Habilitado')  # Field name made lowercase.
    leitor1local = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='Leitor1Local', blank=True, null=True, related_name="leitor1local")  # Field name made lowercase.
    leitor1acessoa = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='Leitor1AcessoA', blank=True, null=True,related_name="leitor1acesso")  # Field name made lowercase.
    leitor1porta = models.SmallIntegerField(db_column='Leitor1Porta', blank=True, null=True)  # Field name made lowercase.
    leitor1negavisitante = models.BooleanField(db_column='Leitor1NegaVisitante', blank=True, null=True)  # Field name made lowercase.
    leitor2habilitado = models.BooleanField(db_column='Leitor2Habilitado')  # Field name made lowercase.
    leitor2local = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='Leitor2Local', blank=True, null=True,related_name="leitor2local")  # Field name made lowercase.
    leitor2acessoa = models.ForeignKey('Locaisdeacesso', models.DO_NOTHING, db_column='Leitor2AcessoA', blank=True, null=True,related_name="leitor2acessoa")  # Field name made lowercase.
    leitor2porta = models.SmallIntegerField(db_column='Leitor2Porta', blank=True, null=True)  # Field name made lowercase.
    leitor2negavisitante = models.BooleanField(db_column='Leitor2NegaVisitante', blank=True, null=True)  # Field name made lowercase.
    aceitateclado = models.BooleanField(db_column='AceitaTeclado')  # Field name made lowercase.
    sensor1 = models.SmallIntegerField(db_column='Sensor1', blank=True, null=True)  # Field name made lowercase.
    rele1 = models.SmallIntegerField(db_column='Rele1', blank=True, null=True)  # Field name made lowercase.
    tempoporta1aberta = models.SmallIntegerField(db_column='TempoPorta1Aberta', blank=True, null=True)  # Field name made lowercase.
    tempoporta1 = models.SmallIntegerField(db_column='TempoPorta1', blank=True, null=True)  # Field name made lowercase.
    acionabipporta1 = models.BooleanField(db_column='AcionaBipPorta1')  # Field name made lowercase.
    sensor2 = models.SmallIntegerField(db_column='Sensor2', blank=True, null=True)  # Field name made lowercase.
    rele2 = models.SmallIntegerField(db_column='Rele2', blank=True, null=True)  # Field name made lowercase.
    tempoporta2aberta = models.SmallIntegerField(db_column='TempoPorta2Aberta', blank=True, null=True)  # Field name made lowercase.
    tempoporta2 = models.SmallIntegerField(db_column='TempoPorta2', blank=True, null=True)  # Field name made lowercase.
    acionabipporta2 = models.BooleanField(db_column='AcionaBipPorta2')  # Field name made lowercase.
    veridenviatemplates = models.BooleanField(db_column='VeridEnviaTemplates')  # Field name made lowercase.
    veridrecebetemplates = models.BooleanField(db_column='VeridRecebeTemplates')  # Field name made lowercase.
    veridtransmissaodecadastros = models.BooleanField(db_column='VeridTransmissaoDeCadastros')  # Field name made lowercase.
    veridpermitecadastramento = models.BooleanField(db_column='VeridPermiteCadastramento')  # Field name made lowercase.
    usabiometria = models.BooleanField(db_column='UsaBiometria')  # Field name made lowercase.
    equipamentobiometria = models.SmallIntegerField(db_column='EquipamentoBiometria')  # Field name made lowercase.
    nivelsegbio = models.SmallIntegerField(db_column='NivelSegBio', blank=True, null=True)  # Field name made lowercase.
    catraca = models.BooleanField(db_column='Catraca')  # Field name made lowercase.
    tempoacionamentocatraca = models.SmallIntegerField(db_column='TempoAcionamentoCatraca', blank=True, null=True)  # Field name made lowercase.
    catracainvertida = models.BooleanField(db_column='CatracaInvertida')  # Field name made lowercase.
    catracasaidalib = models.BooleanField(db_column='CatracaSaidaLib')  # Field name made lowercase.
    urna = models.BooleanField(db_column='Urna')  # Field name made lowercase.
    catunidirecional = models.BooleanField(db_column='CatUnidirecional')  # Field name made lowercase.
    cartaomaster = models.FloatField(db_column='CartaoMaster', blank=True, null=True)  # Field name made lowercase.
    logicasensor = models.BooleanField(db_column='LogicaSensor', blank=True, null=True)  # Field name made lowercase.
    antipassback = models.BooleanField(db_column='AntiPassback', blank=True, null=True)  # Field name made lowercase.
    tempoavaliarantipassback = models.DateTimeField(db_column='TempoAvaliarAntiPassback', blank=True, null=True)  # Field name made lowercase.
    controlarentradas = models.BooleanField(db_column='ControlarEntradas')  # Field name made lowercase.
    senha = models.BooleanField(db_column='Senha')  # Field name made lowercase.
    controlesemsenha = models.SmallIntegerField(db_column='ControleSemSenha', blank=True, null=True)  # Field name made lowercase.
    msgpadraol1 = models.CharField(db_column='MsgPadraoL1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alpadraol1 = models.SmallIntegerField(db_column='AlPadraoL1', blank=True, null=True)  # Field name made lowercase.
    msgpadraol2 = models.CharField(db_column='MsgPadraoL2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alpadraol2 = models.SmallIntegerField(db_column='AlPadraoL2', blank=True, null=True)  # Field name made lowercase.
    msgliberadol1 = models.CharField(db_column='MsgLiberadoL1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alliberadol1 = models.SmallIntegerField(db_column='AlLiberadoL1', blank=True, null=True)  # Field name made lowercase.
    msgliberadol2 = models.CharField(db_column='MsgLiberadoL2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alliberadol2 = models.SmallIntegerField(db_column='AlLiberadoL2', blank=True, null=True)  # Field name made lowercase.
    msgnegadol1 = models.CharField(db_column='MsgNegadoL1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alnegadol1 = models.SmallIntegerField(db_column='AlNegadoL1', blank=True, null=True)  # Field name made lowercase.
    msgnegadol2 = models.CharField(db_column='MsgNegadoL2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alnegadol2 = models.SmallIntegerField(db_column='AlNegadoL2', blank=True, null=True)  # Field name made lowercase.
    funcoeshabilitadas = models.IntegerField(db_column='FuncoesHabilitadas')  # Field name made lowercase.
    exibirfoto = models.BooleanField(db_column='ExibirFoto')  # Field name made lowercase.
    relesirene = models.SmallIntegerField(db_column='ReleSirene')  # Field name made lowercase.
    duracaosirene = models.SmallIntegerField(db_column='DuracaoSirene')  # Field name made lowercase.
    leitor1baixaautomatica = models.BooleanField(db_column='Leitor1BaixaAutomatica')  # Field name made lowercase.
    leitor2baixaautomatica = models.BooleanField(db_column='Leitor2BaixaAutomatica')  # Field name made lowercase.
    balcaobidirecional = models.BooleanField(db_column='BalcaoBidirecional')  # Field name made lowercase.
    habmsgverleitor2 = models.BooleanField(db_column='HabMsgVerLeitor2')  # Field name made lowercase.
    ganhobio = models.SmallIntegerField(db_column='GanhoBio', blank=True, null=True)  # Field name made lowercase.
    brilhobio = models.SmallIntegerField(db_column='BrilhoBio', blank=True, null=True)  # Field name made lowercase.
    contrastebio = models.SmallIntegerField(db_column='ContrasteBio', blank=True, null=True)  # Field name made lowercase.
    segurancaidentbio = models.SmallIntegerField(db_column='SegurancaIdentBio', blank=True, null=True)  # Field name made lowercase.
    segurancaverifbio = models.SmallIntegerField(db_column='SegurancaVerifBio', blank=True, null=True)  # Field name made lowercase.
    qualidaderegistrobio = models.SmallIntegerField(db_column='QualidadeRegistroBio', blank=True, null=True)  # Field name made lowercase.
    qualidadeverifbio = models.SmallIntegerField(db_column='QualidadeVerifBio', blank=True, null=True)  # Field name made lowercase.
    filtrobio = models.SmallIntegerField(db_column='FiltroBio', blank=True, null=True)  # Field name made lowercase.
    capturabio = models.SmallIntegerField(db_column='CapturaBio', blank=True, null=True)  # Field name made lowercase.
    numcapturasbio = models.SmallIntegerField(db_column='NumCapturasBio', blank=True, null=True)  # Field name made lowercase.
    tempocaptura = models.SmallIntegerField(db_column='TempoCaptura', blank=True, null=True)  # Field name made lowercase.
    habilitaverificacao = models.BooleanField(db_column='HabilitaVerificacao', blank=True, null=True)  # Field name made lowercase.
    habilitaidentificacao = models.BooleanField(db_column='HabilitaIdentificacao', blank=True, null=True)  # Field name made lowercase.
    coletorurna = models.BooleanField(db_column='ColetorUrna', blank=True, null=True)  # Field name made lowercase.
    tempoacionamentocoletorurna = models.SmallIntegerField(db_column='TempoAcionamentoColetorUrna', blank=True, null=True)  # Field name made lowercase.
    inner2 = models.BooleanField(db_column='Inner2', blank=True, null=True)  # Field name made lowercase.
    innerinativo = models.BooleanField(db_column='InnerInativo', blank=True, null=True)  # Field name made lowercase.
    timeoutidentificacao = models.SmallIntegerField(db_column='TimeoutIdentificacao', blank=True, null=True)  # Field name made lowercase.
    nivellfd = models.SmallIntegerField(db_column='NivelLFD', blank=True, null=True)  # Field name made lowercase.
    numdigitos = models.IntegerField(db_column='NumDigitos')  # Field name made lowercase.
    tipoleitor = models.IntegerField(db_column='TipoLeitor')  # Field name made lowercase.
    digitosvariaveis = models.CharField(db_column='DigitosVariaveis', max_length=8)  # Field name made lowercase.
    tipocriptografia = models.IntegerField(db_column='TipoCriptografia', blank=True, null=True)  # Field name made lowercase.
    localarquivo = models.CharField(db_column='LocalArquivo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nomeempresa = models.CharField(db_column='NomeEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    naovalidasentidocartao = models.BooleanField(db_column='NaoValidaSentidoCartao')  # Field name made lowercase.
    segurancaidentbiolc = models.SmallIntegerField(db_column='SegurancaIdentBioLC', blank=True, null=True)  # Field name made lowercase.
    timeoutidentificacaolc = models.IntegerField(db_column='TimeoutIdentificacaoLC')  # Field name made lowercase.
    dedoduplicado = models.IntegerField(db_column='DedoDuplicado')  # Field name made lowercase.
    habsensorviolacao = models.BooleanField(db_column='HabSensorViolacao')  # Field name made lowercase.
    habsinalizacaosonora = models.BooleanField(db_column='HabSinalizacaoSonora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inners'
        ordering = ['numero']


class Intertravamentos(models.Model):
    cod_intertravamento = models.AutoField(db_column='COD_INTERTRAVAMENTO', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Intertravamentos'


class Intertravamentosdados(models.Model):
    cod_intertravamento = models.ForeignKey(Intertravamentos, models.DO_NOTHING, db_column='COD_INTERTRAVAMENTO')  # Field name made lowercase.
    numinner = models.ForeignKey(Inners, models.DO_NOTHING, db_column='NumInner')  # Field name made lowercase.
    porta = models.SmallIntegerField(db_column='Porta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntertravamentosDados'


class Locaisdeacesso(models.Model):
    cod_local = models.AutoField(db_column='COD_LOCAL', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.
    solicitarsenha = models.BooleanField(db_column='SolicitarSenha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocaisDeAcesso'


class Locaisdeacessoemails(models.Model):
    cod_email = models.AutoField(db_column='COD_EMAIL', primary_key=True)  # Field name made lowercase.
    cod_local = models.ForeignKey(Locaisdeacesso, models.DO_NOTHING, db_column='COD_LOCAL')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocaisDeAcessoEmails'


class Locaisdeacessopermissoes(models.Model):
    cod_local = models.ForeignKey(Locaisdeacesso, models.DO_NOTHING, db_column='COD_LOCAL')  # Field name made lowercase.
    cod_pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocaisDeAcessoPermissoes'


class Locaisrefeicao(models.Model):
    codlocal = models.OneToOneField(Locaisdeacesso, models.DO_NOTHING, db_column='CodLocal', primary_key=True)  # Field name made lowercase.
    codrefeicao = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='CodRefeicao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocaisRefeicao'
        unique_together = (('codlocal', 'codrefeicao'),)


class Maquinasconectadas(models.Model):
    maquina = models.CharField(db_column='Maquina', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ultimologin = models.DateTimeField(db_column='UltimoLogin', blank=True, null=True)  # Field name made lowercase.
    ipestacao = models.CharField(db_column='IPEstacao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaquinasConectadas'


class Mensagens(models.Model):
    cod_pessoa = models.ForeignKey('Pessoas', models.DO_NOTHING, db_column='COD_PESSOA')  # Field name made lowercase.
    datahora = models.BooleanField(db_column='DataHora')  # Field name made lowercase.
    linha1 = models.CharField(db_column='Linha1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alinhamentol1 = models.SmallIntegerField(db_column='AlinhamentoL1', blank=True, null=True)  # Field name made lowercase.
    linha2 = models.CharField(db_column='Linha2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alinhamentol2 = models.SmallIntegerField(db_column='AlinhamentoL2', blank=True, null=True)  # Field name made lowercase.
    tempo = models.SmallIntegerField(db_column='Tempo', blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio')  # Field name made lowercase.
    fim = models.DateTimeField(db_column='Fim')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mensagens'


class Parametros(models.Model):
    nome = models.CharField(db_column='Nome', primary_key=True, max_length=20)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parametros'


class Perfisdeacesso(models.Model):
    cod_perfil = models.AutoField(db_column='COD_PERFIL', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfisDeAcesso'


class Perfisdeacessodados(models.Model):
    cod_perfil = models.ForeignKey(Perfisdeacesso, models.DO_NOTHING, db_column='COD_PERFIL')  # Field name made lowercase.
    cod_local = models.ForeignKey(Locaisdeacesso, models.DO_NOTHING, db_column='COD_LOCAL')  # Field name made lowercase.
    cod_zt = models.ForeignKey('Zonasdetempo', models.DO_NOTHING, db_column='COD_ZT', blank=True, null=True)  # Field name made lowercase.
    numentradas = models.IntegerField(db_column='NumEntradas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfisDeAcessoDados'


class Perfisdeacessoexcecao(models.Model):
    cod_pessoa = models.ForeignKey(Funcionarios, models.DO_NOTHING, db_column='COD_PESSOA')  # Field name made lowercase.
    cod_local = models.ForeignKey(Locaisdeacesso, models.DO_NOTHING, db_column='COD_LOCAL')  # Field name made lowercase.
    cod_zt = models.ForeignKey('Zonasdetempo', models.DO_NOTHING, db_column='COD_ZT', blank=True, null=True)  # Field name made lowercase.
    numentradas = models.IntegerField(db_column='NumEntradas', blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio')  # Field name made lowercase.
    fim = models.DateTimeField(db_column='Fim')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfisDeAcessoExcecao'


class Pessoas(models.Model):
    cod_pessoa = models.AutoField(db_column='COD_PESSOA', primary_key=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pessoas'


class Politicaseguranca(models.Model):
    compmindigitsenha = models.IntegerField(db_column='CompMinDigitSenha', blank=True, null=True)  # Field name made lowercase.
    habcomplexidadesenha = models.BooleanField(db_column='HabComplexidadeSenha', blank=True, null=True)  # Field name made lowercase.
    periodotrocasenha = models.IntegerField(db_column='PeriodoTrocaSenha', blank=True, null=True)  # Field name made lowercase.
    naopermitirnsenhas = models.IntegerField(db_column='NaoPermitirNSenhas', blank=True, null=True)  # Field name made lowercase.
    bloqueioaposnmalsucedidas = models.IntegerField(db_column='BloqueioAposNMalSucedidas', blank=True, null=True)  # Field name made lowercase.
    habilitarcriptosenhalogin = models.BooleanField(db_column='HabilitarCriptoSenhaLogin', blank=True, null=True)  # Field name made lowercase.
    pedirsenhaloginmon = models.BooleanField(db_column='PedirSenhaLoginMon', blank=True, null=True)  # Field name made lowercase.
    operadorliberaporta = models.BooleanField(db_column='OperadorLiberaPorta', blank=True, null=True)  # Field name made lowercase.
    gerarmarcacao = models.BooleanField(db_column='GerarMarcacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PoliticaSeguranca'


class Presenca(models.Model):
    cod_pessoa = models.IntegerField(db_column='COD_PESSOA', blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presenca'


class Refeicoes(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.
    horainicio = models.CharField(db_column='HoraInicio', max_length=10)  # Field name made lowercase.
    horafim = models.CharField(db_column='HoraFim', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Refeicoes'


class Renomear(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    de = models.CharField(db_column='De', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='Para', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Renomear'


class Templateshamster(models.Model):
    cod_template = models.AutoField(db_column='COD_TEMPLATE', primary_key=True)  # Field name made lowercase.
    numinner = models.ForeignKey(Inners, models.DO_NOTHING, db_column='NumInner')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=16)  # Field name made lowercase.
    template = models.CharField(db_column='Template', max_length=844, blank=True, null=True)  # Field name made lowercase.
    template2 = models.CharField(db_column='Template2', max_length=844, blank=True, null=True)  # Field name made lowercase.
    acao = models.IntegerField(db_column='Acao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TemplatesHamster'


class Templateshamstercama(models.Model):
    cod_template = models.AutoField(db_column='COD_TEMPLATE', primary_key=True)  # Field name made lowercase.
    numinner = models.ForeignKey(Inners, models.DO_NOTHING, db_column='NumInner', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=16, blank=True, null=True)  # Field name made lowercase.
    template = models.CharField(db_column='Template', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    template2 = models.CharField(db_column='Template2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    acao = models.IntegerField(db_column='Acao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TemplatesHamsterCama'


class Trilhaauditoria(models.Model):
    id = models.AutoField(primary_key=True)
    tpevento = models.CharField(db_column='TPEVENTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cod_pessoa = models.CharField(db_column='COD_PESSOA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipestacao = models.CharField(db_column='IPESTACAO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descalt = models.CharField(db_column='DESCALT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DATAHORA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrilhaAuditoria'


class Trilhaauditoriaacessosnegados(models.Model):
    id = models.AutoField(primary_key=True)
    tpevento = models.CharField(db_column='TPEVENTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cod_pessoa = models.CharField(db_column='COD_PESSOA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipestacao = models.CharField(db_column='IPESTACAO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descalt = models.CharField(db_column='DESCALT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DATAHORA', blank=True, null=True)  # Field name made lowercase.
    numinner = models.IntegerField(db_column='NumInner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrilhaAuditoriaAcessosNegados'


class Usuariosbio(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    cartao = models.ForeignKey(Cartoes, models.DO_NOTHING, db_column='Cartao')  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=16, blank=True, null=True)  # Field name made lowercase.
    master = models.CharField(db_column='Master', max_length=1, blank=True, null=True)  # Field name made lowercase.
    template1 = models.CharField(db_column='Template1', max_length=404)  # Field name made lowercase.
    template2 = models.CharField(db_column='Template2', max_length=404, blank=True, null=True)  # Field name made lowercase.
    datahoracadastro = models.CharField(db_column='DataHoraCadastro', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosBio'


class Usuariosbiocama(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    cartao = models.ForeignKey(Cartoes, models.DO_NOTHING, db_column='Cartao', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=16, blank=True, null=True)  # Field name made lowercase.
    master = models.CharField(db_column='Master', max_length=1, blank=True, null=True)  # Field name made lowercase.
    template1 = models.CharField(db_column='Template1', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    template2 = models.CharField(db_column='Template2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    datahoracadastro = models.CharField(db_column='DataHoraCadastro', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosBioCama'


class Usuariosespecificosbio(models.Model):
    codigousuario = models.ForeignKey(Usuariosbio, models.DO_NOTHING, db_column='CodigoUsuario')  # Field name made lowercase.
    numeroinner = models.ForeignKey(Inners, models.DO_NOTHING, db_column='NumeroInner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosEspecificosBio'


class Usuariosespecificosbiocama(models.Model):
    codigousuario = models.IntegerField(db_column='CodigoUsuario')  # Field name made lowercase.
    numeroinner = models.SmallIntegerField(db_column='NumeroInner')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosEspecificosBioCama'


class Visitantes(models.Model):
    cod_pessoa = models.OneToOneField(Pessoas, models.DO_NOTHING, db_column='COD_PESSOA', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', max_length=25, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_zt = models.IntegerField(db_column='COD_ZT')  # Field name made lowercase.
    cod_perfil = models.IntegerField(db_column='COD_PERFIL')  # Field name made lowercase.
    bloqueado = models.BooleanField(db_column='Bloqueado')  # Field name made lowercase.
    ignorarrota = models.BooleanField(db_column='IgnorarRota')  # Field name made lowercase.
    ignorarantipassback = models.BooleanField(db_column='IgnorarAntiPassback')  # Field name made lowercase.
    ignorarentradas = models.BooleanField(db_column='IgnorarEntradas')  # Field name made lowercase.
    idexportacao = models.CharField(db_column='IDExportacao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    senhaacesso = models.CharField(db_column='SenhaAcesso', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Visitantes'


class Visitas(models.Model):
    cod_visita = models.AutoField(db_column='COD_VISITA', primary_key=True)  # Field name made lowercase.
    cod_visitante = models.ForeignKey(Visitantes, models.DO_NOTHING, db_column='COD_VISITANTE', blank=True, null=True)  # Field name made lowercase.
    validade_inicio = models.DateTimeField(db_column='VALIDADE_INICIO', blank=True, null=True)  # Field name made lowercase.
    validade_fim = models.DateTimeField(db_column='VALIDADE_FIM', blank=True, null=True)  # Field name made lowercase.
    cod_visitado = models.IntegerField(db_column='COD_VISITADO', blank=True, null=True)  # Field name made lowercase.
    passoucartao = models.SmallIntegerField(db_column='PassouCartao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Visitas'


class Zonasdetempo(models.Model):
    cod_zt = models.AutoField(db_column='COD_ZT', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZonasDeTempo'


class Zonasdetempodados(models.Model):
    cod_zt = models.ForeignKey(Zonasdetempo, models.DO_NOTHING, db_column='COD_ZT')  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio')  # Field name made lowercase.
    fim = models.DateTimeField(db_column='Fim')  # Field name made lowercase.
    seg = models.BooleanField(db_column='Seg')  # Field name made lowercase.
    ter = models.BooleanField(db_column='Ter')  # Field name made lowercase.
    qua = models.BooleanField(db_column='Qua')  # Field name made lowercase.
    qui = models.BooleanField(db_column='Qui')  # Field name made lowercase.
    sex = models.BooleanField(db_column='Sex')  # Field name made lowercase.
    sab = models.BooleanField(db_column='Sab')  # Field name made lowercase.
    dom = models.BooleanField(db_column='Dom')  # Field name made lowercase.
    fer = models.BooleanField(db_column='Fer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZonasDeTempoDados'


class Zonasdetempopermissoes(models.Model):
    cod_zt = models.ForeignKey(Zonasdetempo, models.DO_NOTHING, db_column='COD_ZT', blank=True, null=True)  # Field name made lowercase.
    cod_pessoa = models.ForeignKey(Pessoas, models.DO_NOTHING, db_column='COD_PESSOA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZonasDeTempoPermissoes'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
