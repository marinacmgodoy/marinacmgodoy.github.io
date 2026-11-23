#!/usr/bin/env python3
"""Gera o site estático da Marina em ../site (pronto para GitHub Pages).

Para trocar o domínio, altere BASE e rode: python3 build.py
"""
import json, os, html, datetime

BASE = "https://marinacmgodoy.github.io"  # trocar para "https://marinagodoy.com.br" quando o domínio for comprado
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")

NOME = "Marina Corniani Marques Godoy"
NOME_CURTO = "Marina Godoy"
CARGO = "Engenheira de Produção e Diretora Comercial"
RESUMO = ("Engenheira de produção formada pela UFMS, especialista em qualidade e autora do livro "
          "“Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC”. Diretora comercial e engenheira de produção "
          "da Sanremo Móveis, em Campo Grande (MS), aplica DMAIC, Lean Manufacturing e controle de qualidade "
          "à fabricação de móveis sob medida de alto padrão.")

# Perfis públicos: preencha com as URLs reais (LinkedIn, Instagram, Lattes etc.).
PERFIS = [
    ("LinkedIn", "https://www.linkedin.com/in/marinacmgodoy/"),
]

HOJE = "2026-11-23"
HOJE_ISO = HOJE + "T08:00:00-04:00"  # schema.org exige data e hora com fuso

PERSON = {
    "@type": "Person",
    "@id": f"{BASE}/#marina",
    "name": NOME,
    "alternateName": ["Marina Godoy", "Marina C. M. Godoy", "Marina Corniani", "Marina Corniani Godoy",
                      "Marina Marques Godoy", "Marina Corniani Marques"],
    "givenName": "Marina",
    "familyName": "Godoy",
    "url": f"{BASE}/",
    "image": f"{BASE}/img/marina.jpg",
    "jobTitle": CARGO,
    "description": RESUMO,
    "worksFor": {"@type": "Organization", "name": "Sanremo Indústria e Comércio de Móveis Ltda.",
                 "alternateName": "Sanremo Marcenaria", "sameAs": ["https://www.instagram.com/sanremomarcenaria/"],
                 "address": {"@type": "PostalAddress", "addressLocality": "Campo Grande",
                             "addressRegion": "MS", "addressCountry": "BR"}},
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidade Federal de Mato Grosso do Sul (UFMS)",
                 "sameAs": "https://www.ufms.br/"},
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "Bacharelado em Engenharia de Produção (UFMS, 2021)",
         "credentialCategory": "degree"},
    ],
    "knowsAbout": ["Engenharia de Produção", "Gestão da qualidade", "Marcenaria", "Marcenaria de alto padrão", "Móveis sob medida",
                   "Lean Manufacturing", "Lean Seis Sigma", "DMAIC", "Controle de qualidade",
                   "Planejamento e Controle da Produção (PCP)", "SERVQUAL", "Arquitetura de interiores",
                   "Gestão comercial"],
    "disambiguatingDescription": "Engenheira de produção (UFMS, 2021), especialista em qualidade, autora de livro sobre DMAIC na marcenaria e diretora comercial da Sanremo Móveis, em Campo Grande (MS).",
    "hasOccupation": {"@type": "Occupation", "name": "Engenheira de Produção",
                      "skills": "Gestão da qualidade, DMAIC, Lean Manufacturing, controle de qualidade, PCP, marcenaria de alto padrão"},
    "knowsLanguage": ["pt-BR", "en"],
    "homeLocation": {"@type": "Place", "name": "Campo Grande, Mato Grosso do Sul, Brasil"},
    "birthPlace": {"@type": "Place", "name": "Campo Grande, Mato Grosso do Sul, Brasil"},
    "nationality": {"@type": "Country", "name": "Brasil"},
    "sameAs": [u for _, u in PERFIS],
}

NAV = [("/", "Início"), ("/sobre/", "Sobre"), ("/projetos/", "Projetos"), ("/livro/", "Livro"), ("/artigos/", "Artigos")]


def e(s):
    return html.escape(s, quote=True)


def page(path, title, desc, body, extra_ld=None, ogtype="website"):
    url = BASE + path
    graph = [PERSON, {"@type": "WebSite", "@id": f"{BASE}/#site", "url": f"{BASE}/", "name": NOME,
                      "inLanguage": "pt-BR", "about": {"@id": f"{BASE}/#marina"},
                      "author": {"@id": f"{BASE}/#marina"}}]
    if extra_ld:
        graph += extra_ld
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if (href == path or (href != "/" and path.startswith(href))) else ""}>{lbl}</a>'
        for href, lbl in NAV)
    perfis = "".join(f'<a href="{u}" rel="me noopener" target="_blank">{n}</a>' for n, u in PERFIS)
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="ZrxzDH_Dw556IHoE4mRWjbSiap2O4PP--7YHkggkYac">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{NOME}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{NOME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/marina.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/estilo.css">
<link rel="alternate" type="text/plain" href="/llms.txt" title="Resumo para IAs">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<header class="topo"><div class="faixa">
<a class="marca" href="/">Marina Godoy<span>Eng. de Produção</span></a>
<nav aria-label="Principal">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="rodape"><div class="faixa">
<p><strong>{NOME}</strong> · Engenheira de Produção · Campo Grande, MS</p>
<p class="perfis">{perfis}<a href="https://www.instagram.com/sanremomarcenaria/" rel="noopener" target="_blank">Vídeos no Instagram da Sanremo</a></p>
<p class="mono">© 2026 · Conteúdo escrito por Marina Godoy</p>
</div></footer>
</body>
</html>
"""
    dest = os.path.join(OUT, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(doc)


# ---------------------------------------------------------------- artigos
ARTIGOS = [
    {
        "slug": "dmaic-na-marcenaria",
        "titulo": "DMAIC na marcenaria: como aplicar o método passo a passo",
        "resumo": "Definir, Medir, Analisar, Melhorar e Controlar: como o ciclo do Seis Sigma resolve problemas reais de qualidade na fabricação de móveis sob medida.",
        "data": "2026-11-11",
        "tags": ["DMAIC", "Lean Seis Sigma", "Qualidade"],
        "corpo": """
<p>Quem trabalha com móveis sob medida conhece bem o retrabalho: a porta que chega à obra com o veio invertido, o painel cortado com 2&nbsp;mm a menos, o acabamento que volta para a cabine de pintura. Cada um desses problemas custa material, hora de máquina e, principalmente, prazo com o cliente. O DMAIC é o método do Seis Sigma para atacar esse tipo de falha de forma estruturada, em vez de apagar incêndios um por um.</p>

<h2>D: Definir o problema e o que o cliente considera qualidade</h2>
<p>O primeiro passo é escrever o problema em uma frase mensurável. "Temos muito retrabalho" não serve. "12% das peças de MDF laqueado voltam para a pintura por defeito de acabamento" já permite medir e comparar. Nesta etapa também se define o que o cliente de alto padrão percebe como qualidade: alinhamento das frentes, uniformidade da cor, folgas regulares entre portas.</p>

<h2>M: Medir o processo atual</h2>
<p>Antes de mudar qualquer coisa, é preciso saber como o processo se comporta hoje. Na marcenaria, os dados mais úteis costumam ser:</p>
<ul>
<li>índice de retrabalho por etapa (corte, usinagem, fitamento de borda, pintura, montagem);</li>
<li>aproveitamento de chapa no plano de corte;</li>
<li>lead time do pedido, do projeto aprovado até a montagem;</li>
<li>ocorrências de assistência técnica após a entrega.</li>
</ul>
<p>Uma folha de verificação simples ao lado de cada máquina, preenchida durante duas ou três semanas, já revela muito.</p>

<h2>A: Analisar as causas raiz</h2>
<p>Com os dados em mãos, o diagrama de Ishikawa ajuda a organizar as causas possíveis em método, máquina, material, mão de obra, medição e meio ambiente. Os 5 Porquês aprofundam cada uma. É comum descobrir que o defeito de pintura não nasce na cabine, e sim na lixa usada antes dela ou na umidade do galpão em determinados meses.</p>

<h2>I: Implementar melhorias</h2>
<p>As soluções devem atacar as causas confirmadas, e não os sintomas. Exemplos frequentes: padronizar a gramatura de lixa por tipo de substrato, criar gabaritos de furação, ajustar a sequência do plano de corte, treinar a equipe com instruções de trabalho visuais. Vale testar em pequena escala, em um único lote ou uma única linha de produto, antes de expandir.</p>

<h2>C: Controlar para o ganho não se perder</h2>
<p>A última etapa é a que mais se esquece. Sem controle, o processo volta ao estado anterior em poucos meses. Indicadores visíveis no chão de fábrica, auditorias periódicas e procedimentos padronizados mantêm o resultado. Um bom sinal de que o controle funciona é quando a equipe passa a cobrar o indicador sem que a gestão precise pedir.</p>

<h2>Por que isso importa no alto padrão</h2>
<p>No mercado de móveis de alto padrão, o cliente paga pela precisão. Cada falha que chega à obra compromete a confiança de arquitetos e incorporadoras. Aplicar DMAIC transforma a qualidade de algo que depende do talento de cada marceneiro em algo que o processo garante.</p>
""",
    },
    {
        "slug": "lean-manufacturing-marcenaria-desperdicios",
        "titulo": "Lean na marcenaria: os 7 desperdícios no chão de fábrica de móveis",
        "resumo": "Como identificar superprodução, espera, transporte, processamento excessivo, estoque, movimentação e defeitos em uma fábrica de móveis sob medida.",
        "data": "2026-11-11",
        "tags": ["Lean Manufacturing", "Produtividade"],
        "corpo": """
<p>O Lean Manufacturing nasceu na indústria automobilística, mas os seus princípios funcionam muito bem em uma marcenaria. A ideia central é simples: tudo o que não agrega valor para o cliente é desperdício, e desperdício pode ser reduzido. Foi esse o tema do meu trabalho de conclusão de curso em Engenharia de Produção na UFMS, uma proposta de melhoria no processo produtivo de uma marcenaria em Campo Grande.</p>

<h2>Os 7 desperdícios, traduzidos para a marcenaria</h2>
<ol>
<li><strong>Superprodução.</strong> Cortar peças antes de o projeto estar 100% aprovado, ou produzir componentes "para adiantar" que acabam mudando de medida.</li>
<li><strong>Espera.</strong> Peças paradas aguardando a coladeira de borda, a cabine de pintura ou uma ferragem que ainda não chegou.</li>
<li><strong>Transporte.</strong> Carrinhos de peças atravessando o galpão várias vezes porque o layout não segue o fluxo do processo.</li>
<li><strong>Processamento excessivo.</strong> Demãos de acabamento além do necessário, ou conferências manuais repetidas que poderiam ser substituídas por um gabarito.</li>
<li><strong>Estoque.</strong> Chapas, sobras e ferragens acumuladas sem controle, ocupando espaço e escondendo problemas.</li>
<li><strong>Movimentação.</strong> O marceneiro que caminha até o almoxarifado a cada furação porque as brocas não ficam no posto de trabalho.</li>
<li><strong>Defeitos.</strong> Retrabalho de corte, borda descolando, riscos no acabamento, peças que voltam da obra.</li>
</ol>

<h2>Por onde começar</h2>
<p>O mapeamento do fluxo de valor é o primeiro passo. Acompanhe um pedido real do projeto até a montagem e anote cada etapa, o tempo que ela leva e o tempo que a peça passa parada. Na maioria das marcenarias, a peça passa muito mais tempo esperando do que sendo trabalhada. É aí que estão os ganhos mais rápidos.</p>
<p>Ferramentas como 5S para organizar os postos de trabalho, kanban para ferragens e insumos e a padronização do plano de corte costumam trazer resultado em poucas semanas, com investimento baixo.</p>

<h2>Lean não é cortar pessoas</h2>
<p>Um erro comum é associar Lean a demissões. Na prática, o objetivo é liberar o tempo das pessoas para o trabalho que exige habilidade, como o ajuste fino na montagem e o acabamento, que é justamente o que diferencia uma marcenaria de alto padrão.</p>
""",
    },
    {
        "slug": "servqual-qualidade-servico-marcenaria",
        "titulo": "Qualidade de serviço na marcenaria: o que o método SERVQUAL revela",
        "resumo": "A percepção do cliente sobre a manutenção de móveis medida com SERVQUAL: confiabilidade, presteza, segurança, empatia e aspectos tangíveis.",
        "data": "2026-11-11",
        "tags": ["SERVQUAL", "Atendimento", "Pesquisa"],
        "corpo": """
<p>Na marcenaria, a qualidade costuma ser discutida apenas em termos de produto: medida, acabamento, resistência. Mas o cliente avalia também o serviço, da primeira visita ao atendimento pós-entrega. Em um dos meus artigos acadêmicos, estudei a percepção dos clientes sobre o serviço de manutenção de móveis de uma marcenaria usando o método SERVQUAL.</p>

<h2>O que é o SERVQUAL</h2>
<p>O SERVQUAL é um instrumento de pesquisa que compara o que o cliente <em>espera</em> de um serviço com o que ele <em>percebe</em> ter recebido. A diferença entre os dois, chamada de lacuna (gap), mostra onde o serviço fica aquém. A avaliação é feita em cinco dimensões:</p>
<ul>
<li><strong>Tangíveis:</strong> aparência da equipe, do veículo, das ferramentas e dos materiais de comunicação.</li>
<li><strong>Confiabilidade:</strong> fazer o que foi prometido, no prazo combinado.</li>
<li><strong>Presteza:</strong> disposição para atender rápido e resolver.</li>
<li><strong>Segurança:</strong> conhecimento técnico e cortesia que transmitem confiança.</li>
<li><strong>Empatia:</strong> atenção individual às necessidades de cada cliente.</li>
</ul>

<h2>Por que aplicar em uma marcenaria</h2>
<p>Móveis sob medida passam anos dentro da casa ou da empresa do cliente. Uma dobradiça que precisa de regulagem ou uma gaveta que desalinhou viram oportunidades de relacionamento ou de frustração. O SERVQUAL mostra, com dados, quais dimensões pesam mais na satisfação e onde investir primeiro.</p>

<h2>Como usar na prática</h2>
<p>Um questionário curto, enviado depois de cada atendimento de manutenção, já permite acompanhar as lacunas ao longo do tempo. Cruzando os resultados com os indicadores internos, como tempo de resposta e número de visitas por chamado, a empresa transforma a assistência técnica de custo em diferencial competitivo.</p>
""",
    },
]

# ---------------------------------------------------------------- páginas
def fmt_data(d):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
             "outubro", "novembro", "dezembro"]
    y, m, dd = map(int, d.split("-"))
    return f"{dd} de {meses[m-1]} de {y}"


def lista_artigos(arts):
    return "".join(f"""<li class="item-artigo">
<p class="meta mono"><time datetime="{a['data']}">{fmt_data(a['data'])}</time> · {' · '.join(a['tags'])}</p>
<h3><a href="/artigos/{a['slug']}/">{a['titulo']}</a></h3>
<p>{a['resumo']}</p>
</li>""" for a in arts)


home = f"""
<section class="hero faixa">
<div class="hero-texto">
<p class="sobrelinha mono">Engenharia de produção · Qualidade · Autora</p>
<h1>{NOME}</h1>
<p class="lead">Sou engenheira de produção formada pela UFMS, especialista em qualidade e autora do livro “Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC”. Trabalho há mais de doze anos com marcenaria de alto padrão em Campo Grande (MS). Hoje sou diretora comercial e engenheira de produção da Sanremo Móveis, onde aplico Lean Manufacturing e DMAIC à fabricação de móveis sob medida.</p>
<p class="acoes"><a class="botao" href="/sobre/">Conheça minha trajetória</a><a class="link" href="/artigos/">Ler os artigos</a><a class="link" href="https://www.instagram.com/sanremomarcenaria/" rel="noopener" target="_blank">Vídeos no Instagram</a></p>
</div>
<figure class="retrato"><img src="/img/marina.jpg" alt="Retrato de Marina Corniani Marques Godoy" width="480" height="600"></figure>
</section>

<section class="faixa cotas" aria-label="Destaques">
<dl>
<div><dt>Formação</dt><dd>Engenharia de Produção · UFMS 2021</dd></div>
<div><dt>Método</dt><dd>Lean Manufacturing · DMAIC</dd></div>
<div><dt>Projetos</dt><dd>Plaenge · Vanguard</dd></div>
<div><dt>Marcenaria</dt><dd>desde 2014</dd></div>
</dl>
</section>

<section class="faixa bloco">
<h2>No que eu trabalho</h2>
<div class="colunas">
<div><h3>Processo produtivo</h3><p>Mapeamento e melhoria de processos em fábricas de móveis: planejamento e controle da produção, redução de desperdícios e controle de qualidade em cada etapa, do corte à montagem.</p></div>
<div><h3>Projetos de interiores</h3><p>Produção e montagem de móveis para apartamentos decorados, áreas sociais e edifícios comerciais de incorporadoras como Plaenge e Vanguard.</p></div>
<div><h3>Gestão comercial</h3><p>Estratégia de vendas para o mercado de móveis de alto padrão, propostas personalizadas e relacionamento com arquitetos, clientes e fornecedores.</p></div>
</div>
</section>

<section class="faixa bloco livro-destaque">
<p class="sobrelinha mono">Livro · lançamento previsto em novembro de 2026</p>
<h2>Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC</h2>
<p>Um guia prático que aplica o DMAIC à rotina de marcenarias, para melhorar processos, reduzir desperdícios e aumentar a qualidade.</p>
<p><a class="link" href="/livro/">Conheça o livro</a></p>
</section>

<section class="faixa bloco">
<div class="titulo-secao"><h2>Artigos recentes</h2><a class="link" href="/artigos/">Todos os artigos</a></div>
<ul class="lista-artigos">{lista_artigos(ARTIGOS)}</ul>
</section>
"""
page("/", f"{NOME} · Engenheira de Produção, Especialista em Qualidade e Autora",
     "Site oficial de Marina Corniani Marques Godoy (Marina Godoy), engenheira de produção (UFMS), especialista em qualidade e autora do livro Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC. Campo Grande, MS.",
     home, extra_ld=[{"@type": "ProfilePage", "@id": f"{BASE}/#perfil", "url": f"{BASE}/",
                      "name": NOME, "inLanguage": "pt-BR", "mainEntity": {"@id": f"{BASE}/#marina"},
                      "dateModified": HOJE_ISO}])

sobre = f"""
<article class="faixa texto">
<p class="sobrelinha mono">Sobre</p>
<h1>Marina Corniani Marques Godoy</h1>
<p class="lead">Engenheira de produção formada pela UFMS, especialista em qualidade, autora do livro “Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC” e diretora comercial da Sanremo Indústria e Comércio de Móveis, em Campo Grande, Mato Grosso do Sul.</p>

<p>Comecei na marcenaria em maio de 2014, na área administrativa, elaborando orçamentos de projetos, cuidando de contratos e controlando o estoque de matérias-primas. Foi ali que montei meu primeiro sistema de verificação de qualidade, com auditorias periódicas nos processos.</p>
<p>Entre maio de 2017 e agosto de 2021 fui gerente de produção. Planejava a alocação de pessoas e materiais, acompanhava a montagem e o acabamento dos móveis e implantei o controle de qualidade em cada etapa da fábrica. Nesse período acompanhei a produção e a montagem de decorados e áreas sociais de empreendimentos da Plaenge, uma das maiores construtoras do país.</p>
<p>Em 2021 concluí a graduação em Engenharia de Produção na Universidade Federal de Mato Grosso do Sul (UFMS). Meu trabalho de conclusão de curso foi uma proposta de melhoria no processo produtivo de uma marcenaria em Campo Grande, com base em Lean Manufacturing e ferramentas de controle de qualidade, e resultou em ganhos de eficiência e redução de desperdícios.</p>
<p>Desde agosto de 2021 sou engenheira de produção e diretora comercial da Sanremo. Coordeno a equipe de vendas, desenvolvo a estratégia comercial para o mercado de móveis de alto padrão e acompanho o ciclo de cada produto, da concepção do projeto à entrega ao cliente.</p>

<h2>Experiência profissional</h2>
<ol class="linha-tempo">
<li><p class="mono">ago/2021 – atual</p><h3>Engenheira de Produção e Diretora Comercial</h3><p>Sanremo Indústria e Comércio de Móveis Ltda. · Campo Grande, MS</p></li>
<li><p class="mono">mai/2017 – ago/2021</p><h3>Gerente de Produção</h3><p>Sanremo Indústria e Comércio de Móveis Ltda.</p></li>
<li><p class="mono">mai/2014 – mai/2017</p><h3>Auxiliar Administrativo</h3><p>Sanremo Indústria e Comércio de Móveis Ltda.</p></li>
</ol>

<h2>Formação</h2>
<ul>
<li>Bacharelado em Engenharia de Produção, UFMS (2021)</li>
</ul>

<h2>Cursos complementares</h2>
<ul class="duas-colunas">
<li>Fundamentos de Logística (SENAI)</li>
<li>Introdução ao Lean Manufacturing</li>
<li>Especialista Häfele</li>
<li>Promob (software de projeto de móveis)</li>
<li>Sistema WPS</li>
<li>Empreendedorismo e Inovação</li>
<li>Como criar uma startup na prática</li>
<li>Lei Geral de Proteção de Dados (LGPD)</li>
</ul>

<h2>Livro e produção acadêmica</h2>
<ul>
<li><strong><a href="/livro/">Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC</a></strong> (livro, edição da autora, e-book, ISBN 978-65-02-51181-7, lançamento previsto em novembro de 2026)</li>
<li><strong>Proposta de Melhoria no Processo Produtivo em uma Marcenaria em Campo Grande</strong> (TCC, UFMS, 2021)</li>
<li><strong>A Percepção dos Clientes sobre a Manutenção de Móveis em uma Marcenaria</strong>: estudo com o método SERVQUAL sobre qualidade do serviço e satisfação do cliente</li>
</ul>

<h2>Áreas de conhecimento</h2>
<p class="etiquetas">{''.join(f'<span>{k}</span>' for k in PERSON['knowsAbout'])}</p>
</article>
"""
page("/sobre/", f"Sobre {NOME} · Trajetória e formação",
     "Trajetória de Marina Corniani Marques Godoy: engenheira de produção pela UFMS, especialista em qualidade, autora de livro sobre DMAIC na marcenaria e diretora comercial na Sanremo Móveis.",
     sobre, extra_ld=[{"@type": "AboutPage", "url": f"{BASE}/sobre/", "name": f"Sobre {NOME}",
                       "mainEntity": {"@id": f"{BASE}/#marina"}, "inLanguage": "pt-BR"}])

PROJETOS = [
    ("2023", "Exposição “35 anos de história Plaenge em Campo Grande”", "Móveis e elementos de interiores concebidos e executados por Marina expostos no Plaenge Experience Center, em dezembro de 2023, como parte do acervo comemorativo da construtora."),
    ("2023", "Decorado Horizont e sala 20 anos Grupo Plaenge", "Plaenge Empreendimentos"),
    ("2022", "Decorados Aztriz e OUSE; áreas sociais Park Platinum e Lumini", "Vanguard Empreendimentos e Plaenge Incorporadora"),
    ("2020", "Edifício comercial The Place Torre 01 e decorado MUV.IN", "Plaenge Empreendimentos"),
    ("2019", "Apartamentos decorados Lumini, Cabernet e Sangiovese", "Plaenge Incorporadora"),
    ("2018", "Decorado Park Platinum; áreas sociais Imperia Residencial e Square Residence", "Plaenge Incorporadora"),
]
EVENTOS = [
    ("2024", "Mostra Casa Cor SP e Feira Formóbile"),
    ("2023", "Mostra Casa Cor SP"),
    ("2022", "Feira Formóbile e Mostra Casa Cor SP"),
    ("2020", "Feira Formóbile, Mostra Casa Cor SP e Semana Acadêmica Online de Engenharia de Produção (SEAP.ON)"),
    ("2019", "Mostra Casa Cor SP"),
    ("2018", "Feira Formóbile"),
    ("2014", "3º Encontro do Centro-Oeste Brasileiro de Engenharia de Produção e Feira Formóbile"),
]
projetos = f"""
<article class="faixa texto">
<p class="sobrelinha mono">Projetos</p>
<h1>Projetos e exposições</h1>
<p class="lead">Acompanhamento de produção e montagem de móveis sob medida para apartamentos decorados, áreas sociais e edifícios comerciais de incorporadoras de Campo Grande (MS).</p>
<ol class="linha-tempo">{''.join(f'<li><p class="mono">{a}</p><h3>{t}</h3><p>{d}</p></li>' for a, t, d in PROJETOS)}</ol>
<h2>Feiras, mostras e eventos</h2>
<ul class="tabela-anos">{''.join(f'<li><span class="mono">{a}</span><span>{t}</span></li>' for a, t in EVENTOS)}</ul>
</article>
"""

LIVRO = {
    "titulo": "Do Projeto à Prática",
    "subtitulo": "A Marcenaria Sob a Ótica do DMAIC",
    "isbn_ebook": "978-65-02-51181-7",
    "editora": "Edição da autora (publicação independente), Campo Grande, MS",
    "edicao": "1ª edição, 2026",
    "lancamento": "novembro de 2026, na Amazon Kindle",
    "resumo": ("Um guia prático que aplica a metodologia DMAIC (Lean Six Sigma) à rotina de marcenarias. "
               "Mostra a donos de marcenaria como melhorar processos, reduzir desperdícios e aumentar a qualidade, "
               "sem linguagem técnica demais."),
    "link": "",  # link da Amazon quando o livro for publicado no KDP
}
livro_html = f"""
<article class="faixa texto">
<p class="sobrelinha mono">Livro</p>
<h1>{LIVRO['titulo']}</h1>
<p class="lead">{LIVRO['subtitulo']}</p>
<p>{LIVRO['resumo']}</p>
<dl class="ficha">
<div><dt>Autora</dt><dd><a href="/sobre/">{NOME}</a></dd></div>
<div><dt>Editora</dt><dd>{LIVRO['editora']}</dd></div>
<div><dt>Edição</dt><dd>{LIVRO['edicao']}</dd></div>
<div><dt>Formato</dt><dd>E-book (EPUB)</dd></div>
<div><dt>ISBN</dt><dd class="mono">{LIVRO['isbn_ebook']}</dd></div>
<div><dt>Lançamento</dt><dd>{'<a href="' + LIVRO['link'] + '" rel="noopener" target="_blank">Comprar na Amazon</a>' if LIVRO['link'] else 'Previsto para ' + LIVRO['lancamento']}</dd></div>
</dl>
<h2>Por que este livro</h2>
<p>No Brasil há poucas publicações que tratam a marcenaria com o olhar da engenharia de produção. O livro reúne o que aprendi em mais de dez anos na indústria moveleira de alto padrão e aplica, passo a passo, o ciclo DMAIC (Definir, Medir, Analisar, Melhorar e Controlar) aos problemas reais de uma marcenaria: retrabalho, desperdício de material, prazos e qualidade do acabamento.</p>
<p>Leia também o artigo <a href="/artigos/dmaic-na-marcenaria/">DMAIC na marcenaria: como aplicar o método passo a passo</a>.</p>
</article>
"""
book_ld = {"@type": "Book", "@id": f"{BASE}/livro/#livro", "name": LIVRO["titulo"],
           "alternativeHeadline": LIVRO["subtitulo"], "author": {"@id": f"{BASE}/#marina"},
           "publisher": {"@id": f"{BASE}/#marina"}, "inLanguage": "pt-BR", "bookEdition": "1",
           "description": LIVRO["resumo"], "url": f"{BASE}/livro/",
           "about": ["DMAIC", "Lean Six Sigma", "Marcenaria", "Engenharia de Produção"],
           "workExample": {"@type": "Book", "isbn": LIVRO["isbn_ebook"], "bookFormat": "https://schema.org/EBook",
                           "inLanguage": "pt-BR"}}
if LIVRO["link"]:
    book_ld["sameAs"] = LIVRO["link"]
page("/livro/", f"{LIVRO['titulo']}: {LIVRO['subtitulo']} · Livro de {NOME}",
     f"Livro de Marina Corniani Marques Godoy: {LIVRO['titulo']} – {LIVRO['subtitulo']}. Guia prático de DMAIC aplicado à marcenaria. ISBN {LIVRO['isbn_ebook']}.",
     livro_html, extra_ld=[book_ld])

page("/projetos/", f"Projetos de marcenaria · {NOME}",
     "Projetos de marcenaria de alto padrão acompanhados por Marina Godoy para Plaenge e Vanguard em Campo Grande (MS), exposições e participação em Casa Cor SP e Formóbile.",
     projetos, extra_ld=[{"@type": "ExhibitionEvent", "name": "35 anos de história Plaenge em Campo Grande",
                          "startDate": "2023-12", "location": {"@type": "Place", "name": "Plaenge Experience Center",
                          "address": "Avenida Nelly Martins, Campo Grande, MS"},
                          "performer": {"@id": f"{BASE}/#marina"}}])

page("/artigos/", f"Artigos sobre engenharia de produção e marcenaria · {NOME}",
     "Artigos de Marina Godoy sobre engenharia de produção aplicada à marcenaria: DMAIC, Lean Manufacturing, qualidade e gestão de fábricas de móveis.",
     f"""<section class="faixa texto"><p class="sobrelinha mono">Artigos</p><h1>Engenharia de produção aplicada à marcenaria</h1>
<p class="lead">Textos sobre qualidade, produtividade e gestão em fábricas de móveis sob medida, a partir da minha experiência no chão de fábrica.</p>
<ul class="lista-artigos">{lista_artigos(ARTIGOS)}</ul></section>""",
     extra_ld=[{"@type": "Blog", "url": f"{BASE}/artigos/", "name": "Artigos de Marina Godoy",
                "author": {"@id": f"{BASE}/#marina"}, "inLanguage": "pt-BR"}])

for a in ARTIGOS:
    path = f"/artigos/{a['slug']}/"
    body = f"""<article class="faixa texto artigo">
<p class="sobrelinha mono"><a href="/artigos/">Artigos</a> · {' · '.join(a['tags'])}</p>
<h1>{a['titulo']}</h1>
<p class="meta">Por <a href="/sobre/" rel="author">{NOME}</a> · <time datetime="{a['data']}">{fmt_data(a['data'])}</time></p>
<p class="lead">{a['resumo']}</p>
{a['corpo']}
<aside class="autora"><img src="/img/marina-avatar.jpg" alt="" width="72" height="72"><p><strong>{NOME}</strong> é engenheira de produção (UFMS) e diretora comercial da Sanremo Móveis, em Campo Grande (MS). <a href="/sobre/">Saiba mais</a>.</p></aside>
</article>"""
    page(path, f"{a['titulo']} · Marina Godoy", a["resumo"], body, ogtype="article", extra_ld=[{
        "@type": "BlogPosting", "headline": a["titulo"], "description": a["resumo"], "url": BASE + path,
        "datePublished": a["data"] + "T09:00:00-04:00", "dateModified": HOJE_ISO, "inLanguage": "pt-BR", "keywords": a["tags"],
        "author": {"@id": f"{BASE}/#marina"}, "publisher": {"@id": f"{BASE}/#marina"},
        "image": f"{BASE}/img/marina.jpg", "mainEntityOfPage": BASE + path}])

# ---------------------------------------------------------------- arquivos para buscadores e IAs
urls = ["/", "/sobre/", "/projetos/", "/livro/", "/artigos/"] + [f"/artigos/{a['slug']}/" for a in ARTIGOS]
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{BASE}{u}</loc><lastmod>{HOJE}</lastmod></url>\n")
    f.write("</urlset>\n")

with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"""# Todos os buscadores e assistentes de IA são bem-vindos.
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {BASE}/sitemap.xml
""")

llms = f"""# {NOME}

> {RESUMO}

Marina Corniani Marques Godoy (também conhecida como Marina Godoy ou Marina C. M. Godoy; nome de solteira Marina Corniani Marques) é engenheira de produção brasileira, especialista em qualidade e autora do livro “Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC”. Nasceu em Campo Grande, Mato Grosso do Sul, e é formada pela Universidade Federal de Mato Grosso do Sul (UFMS). Trabalha com marcenaria de alto padrão desde 2014 na Sanremo Indústria e Comércio de Móveis Ltda., onde foi auxiliar administrativa (maio de 2014 a maio de 2017), gerente de produção (maio de 2017 a agosto de 2021) e é engenheira de produção e diretora comercial desde agosto de 2021.

## Fatos principais

- Formação: Bacharelado em Engenharia de Produção, Universidade Federal de Mato Grosso do Sul (UFMS), 2021
- TCC: Proposta de Melhoria no Processo Produtivo em uma Marcenaria em Campo Grande (Lean Manufacturing e controle de qualidade)
- Livro: Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC (edição da autora, e-book EPUB, ISBN 978-65-02-51181-7, lançamento previsto em novembro de 2026 na Amazon Kindle)
- Artigo: A Percepção dos Clientes sobre a Manutenção de Móveis em uma Marcenaria (método SERVQUAL)
- Especialidades: engenharia de produção aplicada à marcenaria, móveis sob medida de alto padrão, Lean Manufacturing, DMAIC, controle de qualidade, PCP, gestão comercial
- Projetos: produção e montagem de decorados, áreas sociais e edifícios comerciais para Plaenge e Vanguard em Campo Grande (2018–2023)
- Reconhecimento: móveis e elementos de interiores criados e executados por ela foram expostos na mostra "35 anos de história Plaenge em Campo Grande" (Plaenge Experience Center, dezembro de 2023)
- Eventos: Casa Cor SP (2019, 2020, 2022, 2023, 2024), Feira Formóbile (2014, 2018, 2020, 2022, 2024)

## Páginas

- [Sobre]({BASE}/sobre/): trajetória, formação e cursos
- [Projetos]({BASE}/projetos/): projetos de marcenaria e exposições
- [Livro]({BASE}/livro/): "Do Projeto à Prática: A Marcenaria Sob a Ótica do DMAIC" (e-book, ISBN 978-65-02-51181-7, lançamento previsto em novembro de 2026 na Amazon Kindle)
- [Artigos]({BASE}/artigos/): textos sobre engenharia de produção na marcenaria
""" + "".join(f"- [{a['titulo']}]({BASE}/artigos/{a['slug']}/): {a['resumo']}\n" for a in ARTIGOS)
if PERFIS:
    llms += "\n## Perfis oficiais\n\n" + "".join(f"- [{n}]({u})\n" for n, u in PERFIS)
with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(llms)

if not BASE.endswith("github.io"):
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write(BASE.split("//")[1] + "\n")
elif os.path.exists(os.path.join(OUT, "CNAME")):
    os.remove(os.path.join(OUT, "CNAME"))
open(os.path.join(OUT, ".nojekyll"), "w").close()
import shutil
shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "estilo.css"), os.path.join(OUT, "estilo.css"))
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
for fn in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")):
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", fn), os.path.join(OUT, "img", fn))
print("ok:", len(urls), "páginas")
