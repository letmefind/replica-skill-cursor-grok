<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · **Português (Brasil)** · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Skills Replica para Cursor e Grok Bot

</div>

Onze skills que reconstroem o que um aplicativo faz, mais uma skill, `replica`, que mantém a ordem. Grátis, MIT. Fora o Python 3.8 e a biblioteca padrão, não há o que instalar.

O trabalho é de sala limpa. As skills estudam as funções e o caminho de uma pessoa por elas, e depois escrevem tudo de novo. Não ficam com o código, o logotipo, o texto nem o conteúdo do alvo. A letra miúda está no fim, e as skills a repetem.

## Crédito

O método, os modelos e as seis ferramentas em Python são de Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Este repositório é o port da letmefind desse pacote, para o Cursor e para o Grok Bot. O texto das skills veio de https://github.com/letmefind/replica-skill, um fork do repositório acima.

Outros pacotes do mesmo autor: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## As doze

| skill | o que faz |
| --- | --- |
| `replica` | A ordem, os arquivos que cada passo lê e grava, e qual passo rodar. |
| `replica-recon` | Telas, fluxos, peças, modelo de dados, matriz de funções. Páginas públicas, capturas, fichas da loja e a sua conta. |
| `replica-architect` | Pilha, esquema do banco e API. |
| `replica-design` | Papéis de cor, tipo, espaçamento, peças, como tokens, com os seus materiais. |
| `replica-build` | O aplicativo, tela por tela, a partir do mapa de reconhecimento. |
| `replica-backend` | Acesso, banco, pagamentos e integrações. |
| `replica-test` | Cada fluxo, percorrido no clique e testado. |
| `replica-diff` | Uma nota de paridade, e o que ainda falta. |
| `replica-entrepreneur` | O que usuários reais detestam, virado em correções e um ângulo de posição. |
| `replica-brand` | Um nome e uma marca seus, depois uma varredura do que sobrou. |
| `replica-launch` | Página de chegada, preço e a ficha da loja. |
| `replica-deploy` | No ar, no seu domínio, depois que a checagem prévia passa. |

Rode nesta ordem:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Um aplicativo de agendamento, do tipo em que você manda um link e alguém marca um horário, segue assim.

1. **replica-recon** lê a central de ajuda, a página de preços, a ficha da loja e os percursos públicos. Você clica na sua própria conta. Saem `replica/recon.md` e `replica/features.csv`. Um mercado de parceiros fica de fora: é a rede deles, não uma função.
2. **replica-architect** escolhe uma pilha sem graça e gerenciada, escreve o esquema (incluindo uma restrição para dois convidados não marcarem o mesmo horário) e ordena a construção em volta do fluxo de reserva.
3. **replica-design** mede as capturas em tokens: papéis de cor, tipo, espaçamento, o seletor de data, o botão do horário. Ícones abertos, uma fonte aberta, as suas palavras.
4. **replica-build** constrói a casca, depois o fluxo de reserva, depois cada tela com os seus estados, e vai marcando `features.csv`.
5. **replica-backend** acrescenta o cadastro, o calendário pela API do próprio provedor com as suas chaves, pagamentos em modo de teste e o e-mail de lembrete.
6. **replica-test** escreve um plano a partir dos fluxos, testes de ponta a ponta para o caminho feliz e as bordas, e defeitos por gravidade até não restar S1 nem S2 aberto.
7. **replica-diff** dá a nota. Faltar um item obrigatório quer dizer: não dá para publicar.
8. **replica-entrepreneur** lê avaliações reais e só avaliações reais. Cada citação é copiada de uma linha que você forneceu, com a URL dessa linha.
9. **replica-brand** dá o nome depois que as checagens de marca e de domínio rodaram de verdade, e varre a árvore até não sobrar nada do original.
10. **replica-launch** escreve a página de chegada em volta do ângulo, põe preços diante da página pública de preços (com a data em que foi lida) e confere a ficha da loja.
11. **replica-deploy** roda a checagem prévia e, quando você diz para ir, publica.

Qualquer skill pode rodar sozinha. replica-entrepreneur, num aplicativo que você ainda não começou, é um jeito sensato de decidir se vale construir.

## Instalar no Cursor

O Cursor carrega skills de um projeto em `.cursor/skills/<name>/SKILL.md` e `.agents/skills/<name>/SKILL.md`, e para o seu usuário em `~/.cursor/skills/` e `~/.agents/skills/`. O nome da pasta é o nome da skill. `name` e `description` no preâmbulo são obrigatórios, e `name` tem de bater com a pasta.

Este instalador usa `.cursor/skills` (projeto) e `~/.cursor/skills` (`--global`). Skills de projeto viajam com o repositório. Skills de usuário em `~/.cursor/skills/` ficam naquela máquina até você ligar a sincronização para Cloud Agents em Settings, Agents. Uma skill que você quer em toda execução de Cloud Agent de um repositório fica em `.cursor/skills/` desse repositório.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Rodar de novo substitui as pastas Replica e `replica-tools/`, e deixa as outras skills no lugar.

No chat, digite `/` e escolha `replica` ou `replica-recon`. Isso prende a skill a uma mensagem. Para mantê-la a sessão inteira, comece como Custom Mode: Option+Enter no macOS, ou Alt+Enter no Windows.

Os modelos ficam na pasta da skill. As ferramentas em Python são uma cópia compartilhada. Depois da instalação elas estão em `replica-tools/`, ao lado das pastas das skills. A partir de uma cópia deste repositório, defina `REPLICA_HOME` para essa cópia e as skills usam `tools/` ali. Python 3.8 ou mais novo. Nada para instalar com pip.

## Instalar no Grok Bot

Envie isto, como a mensagem inteira:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Os passos seguintes estão em [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). Versão curta: clone este repositório para `/home/box/replica-skill` (mude com `REPLICA_HOME`), rode `grok-bot/install.sh` e salve cada arquivo em `grok-bot/skills/*/SKILL.md` como uma skill. O nome, a descrição e o corpo são copiados ao pé da letra. Uma skill do Grok Bot é esse único arquivo. As ferramentas e os modelos ficam no disco, e as skills os chamam por caminho absoluto, por exemplo `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

As notas de pesquisa de um projeto ficam em `/workspace/<project-slug>/replica/`. Quando um passo passa a escrever o aplicativo, `replica/` fica no seu repositório de código. Mudanças de código vão para um Cursor cloud coding agent nesse repositório do GitHub, como uma tarefa que inclui os arquivos `replica/` de que ele precisa. Você entra, paga, compra o domínio e digita as chaves reais.

## Ferramentas

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Nenhuma usa a rede. `imgdiff.py` compara o layout, não a cor, então uma troca de marca não conta contra você. `parity.py` pesa must, should e could, conta partial como metade e não pontua uma linha que você pulou de propósito. `reviews.py` descarta qualquer linha sem link. `sweep.py` segura a publicação enquanto o nome, o domínio ou as cores do original ainda estão na árvore. `listing.py` confere os limites da loja e rejeita o nome do original na sua ficha.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Disposição

```
tools/                 contrast.py, parity.py, imgdiff.py, reviews.py, sweep.py, listing.py, themes.json
cursor/skills/         twelve SKILL.md folders, templates beside the skills that use them
cursor/install.sh
grok-bot/skills/       the same twelve skills, one SKILL.md each
grok-bot/install.sh
grok-bot/INSTALL.md
tests/
scripts/validate.py
```

Os arquivos do seu projeto vão em `replica/`, não neste repositório.

## Letra miúda

**Reconstrói funcionalidade e padrões de uso, em sala limpa.** Estuda o que o aplicativo faz e como as pessoas passam por ele, e depois escreve tudo de novo. Não copia o código-fonte do alvo, os materiais fechados, logotipos, marcas, texto nem APIs privadas.

**Só lê o que você pode ler.** Páginas públicas e a sua conta. Não raspa atrás de um login nem contra os termos de um site, não entra na conta de outra pessoa e não passa de um paywall. Se os termos da sua conta proíbem usá-la para montar um concorrente, a skill diz isso e fica nas fontes públicas.

**Troca a marca antes de publicar.** Nome novo, paleta nova, logotipo novo, palavras novas. replica-deploy não publica até a varredura estar limpa.

**«Clonar qualquer aplicativo» quer dizer as funções e o fluxo.** Não o conteúdo, a rede, nem as licenças que um aplicativo possui. Dá para reconstruir o player, as playlists e o compartilhamento de um aplicativo de música. Não dá para clonar o catálogo.

**Não há promessa de um clone perfeito.** Uma ferramenta de reserva são semanas. Um motor de planilha não é. replica-recon mede o tamanho antes de você começar, e replica-diff entrega um número.

**A skill de negócio não inventa.** Sem avaliações, citações ou números inventados. Cada afirmação tem um link, e o tamanho da amostra está escrito.

**Confira antes de vender.** Rode as checagens de marca que replica-brand lista, leia os termos de tudo o que você usou e fale com um advogado antes de publicar se houver dinheiro em jogo. Isto não é aconselhamento jurídico.

## Licença

MIT. O direito autoral original é de Jake Schincariol. O port acrescenta uma linha de direito autoral para a letmefind. Veja [LICENSE](../../LICENSE).
