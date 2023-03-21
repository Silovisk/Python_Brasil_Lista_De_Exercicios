<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<meta name="robots" content="index,nofollow">

<title>EstruturaSequencial - PythonBrasil</title>
<script type="text/javascript" src="/static/common/js/common.js"></script>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-136790801-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-136790801-2');
</script>
    

<link rel="stylesheet" type="text/css" charset="utf-8" media="all" href="/static/pybr/css/common.css">
<link rel="stylesheet" type="text/css" charset="utf-8" media="screen" href="/static/pybr/css/screen.css">
<link rel="stylesheet" type="text/css" charset="utf-8" media="print" href="/static/pybr/css/print.css">
<link rel="stylesheet" type="text/css" charset="utf-8" media="projection" href="/static/pybr/css/projection.css">

<!-- css only for MS IE6/IE7 browsers -->
<!--[if lt IE 8]>
   <link rel="stylesheet" type="text/css" charset="utf-8" media="all" href="/static/pybr/css/msie.css">
<![endif]-->


<link rel="alternate" title="PythonBrasil: EstruturaSequencial" href="/EstruturaSequencial?diffs=1&amp;show_att=1&amp;action=rss_rc&amp;unique=0&amp;page=EstruturaSequencial&amp;ddiffs=1" type="application/rss+xml">


<link rel="Start" href="/PythonBrasil">
<link rel="Alternate" title="Marca��o da Wiki" href="/EstruturaSequencial?action=raw">
<link rel="Alternate" media="print" title="Visualizar Impress�o" href="/EstruturaSequencial?action=print">
<link rel="Search" href="/FindPage">
<link rel="Index" href="/%C3%8DndiceDeT%C3%ADtulos">
<link rel="Glossary" href="/WordIndex">
<link rel="Help" href="/HelpOnFormatting">
</head>

<body  lang="pt-br" dir="ltr">

<div id="head_bar">
  <span class="partners">
    <a href="http://associacao.python.org.br" title="Associa&ccedil;&atilde;o Python Brasil">associa&ccedil;&atilde;o</a>
    <a href="http://2015.pythonbrasil.org.br" title="Confer&ecirc;ncia PythonBrasil[11]">pythonbrasil[11]</a>
    <a href="http://www.djangobrasil.org" title="Django Brasil">django</a>
    <a href="http://www.plone.org.br" title="Plone Brasil">zope/plone</a>
    <a href="/planet/" title="Planet PythonBrasil">planet</a>
  </span>
<span class="login">    <a href="/" title="Volta para a p�gina inicial">       <img src="/static/pybr/img/home.png" alt="In�cio" />    </a> Logado como (<a class="user_preference" href="/EstruturaSequencial?action=login">Entrar</a>)</span>
</div>
<div id="core">

<form id="searchform" method="get" action="/EstruturaSequencial">
<div>
<input type="hidden" name="action" value="fullsearch">
<input type="hidden" name="context" value="180">
<label for="searchinput">Procurar:</label>
<input id="searchinput" type="text" name="value" value="" size="20"
    onfocus="searchFocus(this)" onblur="searchBlur(this)"
    onkeyup="searchChange(this)" onchange="searchChange(this)" alt="Search">
<input id="titlesearch" name="titlesearch" type="submit"
    value="T�tulos" alt="Search Titles">
<input id="fullsearch" name="fullsearch" type="submit"
    value="Texto" alt="Search Full Text">
</div>
</form>
<script type="text/javascript">
<!--// Initialize search form
var f = document.getElementById('searchform');
f.getElementsByTagName('label')[0].style.display = 'none';
var e = document.getElementById('searchinput');
searchChange(e);
searchBlur(e);
//-->
</script>

    <div id="logo" style="display:inline;">
      <a href="/PythonBrasil"><img src="/pybr/img/pythonbrasil_logo.png" title="PythonBrasil" alt="PythonBrasil" /></a>
    </div>


  <div id="sidebar">
      <p><a href="?action=edit" title="Editar esta p�gina">
          <img src="/static/pybr/img/edit.png" alt="Editar esta p�gina" />
      </a></p>
      <h1>Veja tamb�m:</h1>

<ul>
<li><a href="/PythonBrasil">PythonBrasil</a></li><li><a href="/Mudan%C3%A7asRecentes">Mudan�asRecentes</a></li><li><a href="/%C3%8DndiceDeT%C3%ADtulos">�ndiceDeT�tulos</a></li><li><a href="/DocumentacaoPython">DocumentacaoPython</a></li><li><a href="/CookBook">CookBook</a></li><li><a href="/OutrasSecoes">OutrasSecoes</a></li><li><a href="/EstruturaSequencial">Estrutura Sequencial</a></li>
</ul>

      <p><a href="/planet/" title="Planet PythonBrasil">Planet PythonBrasil</a></p>
      <p><a href="/Mais">Mais...</a></p>
      <p class="ad"></p>
  </div>
  <div id="page">

<h1 id="pagelocation"><span><a class="backlink" href="/EstruturaSequencial?action=fullsearch&amp;context=180&amp;value=linkto%3A%22EstruturaSequencial%22" rel="nofollow" title="Clique para fazer uma busca completa por este t�tulo">EstruturaSequencial</a></span></h1>
<!-- INICIO --><div dir="ltr" id="content" lang="pt-br"><span class="anchor" id="top"></span>
<span class="anchor" id="line-1"></span><p class="line862">Voltar para a <a href="/ListaDeExercicios">ListaDeExercicios</a> <span class="anchor" id="line-2"></span><hr /><p class="line874"> <span class="anchor" id="line-3"></span><span class="anchor" id="line-4"></span><ol type="1"><li>Fa�a um Programa que mostre a mensagem "Alo mundo" na tela.  <span class="anchor" id="line-5"></span><span class="anchor" id="line-6"></span></li><li class="gap"><p class="line862">Fa�a um Programa que pe�a um n�mero e ent�o mostre a mensagem <em>O n�mero informado foi [n�mero]</em>.  <span class="anchor" id="line-7"></span><span class="anchor" id="line-8"></span></li><li class="gap">Fa�a um Programa que pe�a dois n�meros e imprima a soma.  <span class="anchor" id="line-9"></span><span class="anchor" id="line-10"></span></li><li class="gap">Fa�a um Programa que pe�a as 4 notas bimestrais e mostre a m�dia.  <span class="anchor" id="line-11"></span><span class="anchor" id="line-12"></span></li><li class="gap">Fa�a um Programa que converta metros para cent�metros.  <span class="anchor" id="line-13"></span><span class="anchor" id="line-14"></span></li><li class="gap">Fa�a um Programa que pe�a o raio de um c�rculo, calcule e mostre sua �rea.  <span class="anchor" id="line-15"></span><span class="anchor" id="line-16"></span></li><li class="gap">Fa�a um Programa que calcule a �rea de um quadrado, em seguida mostre o dobro desta �rea para o usu�rio.  <span class="anchor" id="line-17"></span><span class="anchor" id="line-18"></span></li><li class="gap">Fa�a um Programa que pergunte quanto voc� ganha por hora e o n�mero de horas trabalhadas no m�s. Calcule e mostre o total do seu sal�rio no referido m�s.  <span class="anchor" id="line-19"></span><span class="anchor" id="line-20"></span></li><li class="gap">Fa�a um Programa que pe�a a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.  <span class="anchor" id="line-21"></span><ul><li style="list-style-type:none">C = 5 * ((F-32) / 9). <span class="anchor" id="line-22"></span><span class="anchor" id="line-23"></span></li></ul></li><li class="gap">Fa�a um Programa que pe�a a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.  <span class="anchor" id="line-24"></span><span class="anchor" id="line-25"></span></li><li class="gap">Fa�a um Programa que pe�a 2 n�meros inteiros e um n�mero real. Calcule e mostre: <span class="anchor" id="line-26"></span><ol type="a"><li>o produto do dobro do primeiro com metade do segundo . <span class="anchor" id="line-27"></span></li><li>a soma do triplo do primeiro com o terceiro. <span class="anchor" id="line-28"></span></li><li>o terceiro elevado ao cubo. <span class="anchor" id="line-29"></span><span class="anchor" id="line-30"></span></li></ol></li><li class="gap">Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte f�rmula: (72.7*altura) - 58 <span class="anchor" id="line-31"></span><span class="anchor" id="line-32"></span></li><li class="gap">Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes f�rmulas: <span class="anchor" id="line-33"></span><ol type="a"><li>Para homens: (72.7*h) - 58 <span class="anchor" id="line-34"></span></li><li>Para mulheres: (62.1*h) - 44.7 <span class="anchor" id="line-35"></span><span class="anchor" id="line-36"></span><span class="anchor" id="line-37"></span></li></ol></li><li class="gap"><p class="line862">Jo�o Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento di�rio de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de S�o Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. Jo�o precisa que voc� fa�a um programa que leia a vari�vel <em>peso</em> (peso de peixes) e calcule o excesso. Gravar na vari�vel <em>excesso</em> a quantidade de quilos al�m do limite e na vari�vel <em>multa</em> o valor da multa que Jo�o dever� pagar. Imprima os dados do programa com as mensagens adequadas. <span class="anchor" id="line-38"></span><span class="anchor" id="line-39"></span></li><li class="gap">Fa�a um Programa que pergunte quanto voc� ganha por hora e o n�mero de horas trabalhadas no m�s. Calcule e mostre o total do seu sal�rio no referido m�s, sabendo-se que s�o descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, fa�a um programa que nos d�: <span class="anchor" id="line-40"></span><ol type="a"><li>sal�rio bruto. <span class="anchor" id="line-41"></span></li><li>quanto pagou ao INSS. <span class="anchor" id="line-42"></span></li><li>quanto pagou ao sindicato. <span class="anchor" id="line-43"></span></li><li>o sal�rio l�quido. <span class="anchor" id="line-44"></span></li><li>calcule os descontos e o sal�rio l�quido, conforme a tabela abaixo: <span class="anchor" id="line-45"></span><span class="anchor" id="line-46"></span><span class="anchor" id="line-47"></span><span class="anchor" id="line-48"></span><span class="anchor" id="line-49"></span><span class="anchor" id="line-50"></span><span class="anchor" id="line-51"></span><pre><span class="anchor" id="line-1"></span>+ Sal�rio Bruto : R$
<span class="anchor" id="line-2"></span>- IR (11%) : R$
<span class="anchor" id="line-3"></span>- INSS (8%) : R$
<span class="anchor" id="line-4"></span>- Sindicato ( 5%) : R$
<span class="anchor" id="line-5"></span>= Sal�rio Liquido : R$</pre><span class="anchor" id="line-52"></span>Obs.: Sal�rio Bruto - Descontos = Sal�rio L�quido. <span class="anchor" id="line-53"></span><span class="anchor" id="line-54"></span></li></ol></li><li class="gap">Fa�a um programa para uma loja de tintas. O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada. Considere que a cobertura da tinta � de 1 litro para cada 3 metros quadrados e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usu�rio a quantidades de latas de tinta a serem compradas e o pre�o total. <span class="anchor" id="line-55"></span><span class="anchor" id="line-56"></span></li><li class="gap">Fa�a um Programa para uma loja de tintas. O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada. Considere que a cobertura da tinta � de 1 litro para cada 6 metros quadrados e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00 ou em gal�es de 3,6 litros, que custam R$ 25,00. <span class="anchor" id="line-57"></span><ul><li style="list-style-type:none">Informe ao usu�rio as quantidades de tinta a serem compradas e os respectivos pre�os em 3 situa��es: <span class="anchor" id="line-58"></span></li><li>comprar apenas latas de 18 litros; <span class="anchor" id="line-59"></span></li><li>comprar apenas gal�es de 3,6 litros; <span class="anchor" id="line-60"></span></li><li>misturar latas e gal�es, de forma que o desperd�cio de tinta seja menor. <span class="anchor" id="line-61"></span><span class="anchor" id="line-62"></span>Acrescente 10% de folga e sempre arredonde os valores para cima, isto �, considere latas cheias. <span class="anchor" id="line-63"></span><span class="anchor" id="line-64"></span></li></ul></li><li class="gap">Fa�a um programa que pe�a o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). <span class="anchor" id="line-65"></span><span class="anchor" id="line-66"></span></li></ol><p class="line867"><hr /><p class="line874"> <span class="anchor" id="line-67"></span>Voltar para a <a href="/ListaDeExercicios">ListaDeExercicios</a> <span class="anchor" id="line-68"></span><span class="anchor" id="bottom"></span></div><!-- FIM -->
  </div> <!-- page -->
</div> <!-- core -->
<div id="footer">
    <div class="partners"><p>
      <a href="http://moinmo.in/"><img src="/pybr/img/logo_moin.png" alt="Powered by MoinMoin" /></a>
      <a rel="license" href="https://creativecommons.org/licenses/by/2.5/br/"><img alt="Creative Commons License" style="border-width:0" src="https://creativecommons.org/images/public/somerights20.png" /></a>
    </p></div>
<div class="information">
    <p><span style="font-weight: bold;">Sobre esta p�gina</span></p>
<p id="pageinfo" class="info" lang="pt-br" dir="ltr">EstruturaSequencial  (editada pela �ltima vez em 2022-04-02 02:17:55 por <span title="ogordo @ 191-6-134-138.rev.netcom.tv.br[191.6.134.138]"><a class="nonexistent" href="/ogordo" title="ogordo @ 191-6-134-138.rev.netcom.tv.br[191.6.134.138]">ogordo</a></span>)</p>

<p><a href="?action=raw">Visualizar Texto</a> | <a href="?action=print">Visualizar Impress�o</a> | <a href="?action=info">Information</a> | <a href="?action=SubscribeUser">Fazer Usu�rio Acompanhar</a> | <a href="?action=AttachFile">Anexos</a></p>
<p>&nbsp;</p>
<p>"Python" e os logos de Python s&atilde;o marcas registradas da
        <a href="http://www.python.org/psf">Python Software Foundation</a>, usadas aqui mediante permiss&atilde;o da mesma. O conte&uacute;do deste site est&aacute; dispon&iacute;vel sob os termos da <a href="http://creativecommons.org/licenses/by/2.5/br/">Creative Commons Attribution 2.5</a> exceto quando explicitamente especificado outra licen&ccedil;a.</p>
</div> <!-- information -->
</div> <!-- footer -->
</body>
</html>

