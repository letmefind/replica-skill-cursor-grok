<div align="center">

[English](../../README.md) · [简体中文](README_zh.md) · [繁體中文](README_zh-TW.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Türkçe](README_tr.md) · [Русский](README_ru.md) · [Tiếng Việt](README_vi.md) · [ไทย](README_th.md) · [Deutsch](README_de.md) · **Español** · [Français](README_fr.md) · [Українська](README_uk.md) · [Polski](README_pl.md) · [Português (Brasil)](README_pt-BR.md) · [العربية](README_ar.md) · [فارسی](README_fa.md) · [Bahasa Indonesia](README_id.md) · [Italiano](README_it.md)
· [Ελληνικά](README_el.md) · [മലയാളം](README_ml.md) · [Roman Urdu](README_ur-Latn.md) · [Română](README_ro.md)

# Skills Replica para Cursor y Grok Bot

</div>

Once skills que reconstruyen lo que hace una aplicación, más un skill, `replica`, que guarda el orden. Gratis, MIT, y no hay que instalar nada aparte de Python 3.8 y la biblioteca estándar.

El trabajo es de sala limpia. Los skills estudian las funciones y el camino de una persona a través de ellas, y luego lo escriben todo de nuevo. No se quedan con el código, el logo, el texto ni el contenido del objetivo. La letra pequeña está al final, y los skills la repiten.

## Crédito

El método, las plantillas y las seis herramientas de Python son de Jake Schincariol:

- https://github.com/Jakeschincariol/replica-skill
- https://opusjake.ai

Este repositorio es el port de letmefind para Cursor y para Grok Bot. El texto de los skills se tomó de https://github.com/letmefind/replica-skill, un fork del repositorio de arriba.

Otros paquetes del mismo autor: [Arena](https://github.com/Jakeschincariol/arena-skill),
[X](https://github.com/Jakeschincariol/x-agent-skill),
[LinkedIn](https://github.com/Jakeschincariol/linkedin-agent-skill),
[Instagram](https://github.com/Jakeschincariol/instagram-agent-skill).

## Los doce

| skill | qué hace |
| --- | --- |
| `replica` | El orden, los archivos que lee y escribe cada paso, y qué paso toca. |
| `replica-recon` | Pantallas, flujos, componentes, modelo de datos, matriz de funciones. Páginas públicas, capturas, fichas de tienda y tu propia cuenta. |
| `replica-architect` | Stack, esquema de base de datos y API. |
| `replica-design` | Roles de color, tipo, espaciado, componentes, como tokens, con tus propios assets. |
| `replica-build` | La aplicación, pantalla por pantalla, a partir del mapa de recon. |
| `replica-backend` | Acceso, base de datos, pagos e integraciones. |
| `replica-test` | Cada flujo, recorrido a clics y probado. |
| `replica-diff` | Una puntuación de paridad, y lo que todavía falta. |
| `replica-entrepreneur` | Lo que odian los usuarios reales, convertido en correcciones y un ángulo de posicionamiento. |
| `replica-brand` | Un nombre y una marca propios, y después un barrido de lo que quede. |
| `replica-launch` | Página de aterrizaje, precios y la ficha de la tienda. |
| `replica-deploy` | En vivo, en tu propio dominio, cuando pasa la revisión previa. |

En este orden:

```
recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy
```

Una aplicación de citas, de esas en las que compartes un enlace y alguien reserva una hora, va así.

1. **replica-recon** lee el centro de ayuda, la página de precios, la ficha de la tienda y los recorridos públicos. Tú recorres tu propia cuenta. Salen `replica/recon.md` y `replica/features.csv`. Un mercado de socios queda fuera: es su red, no una función.
2. **replica-architect** elige un stack aburrido y gestionado, escribe el esquema (incluida una restricción para que dos invitados no reserven el mismo hueco) y ordena la construcción alrededor del flujo de reserva.
3. **replica-design** mide las capturas en tokens: roles de color, tipo, espaciado, el selector de fecha, el botón del hueco. Iconos abiertos, una fuente abierta, tus propias palabras.
4. **replica-build** construye el armazón, luego el flujo de reserva, luego cada pantalla con sus estados, y va marcando `features.csv`.
5. **replica-backend** añade el registro, el calendario por la API propia del proveedor con tus claves, pagos en modo de prueba y el correo de recordatorio.
6. **replica-test** escribe un plan a partir de los flujos, pruebas de extremo a extremo para el camino feliz y los bordes, y fallos por gravedad hasta que no quede ningún S1 ni S2 abierto.
7. **replica-diff** lo puntúa. Si falta un must-have, no se puede publicar.
8. **replica-entrepreneur** lee reseñas reales y solo reseñas reales. Cada cita está copiada de una fila que tú aportaste, con la URL de esa fila.
9. **replica-brand** le pone nombre, después de ejecutar de verdad las comprobaciones de marca y de dominio, y barre el árbol hasta que no quede nada del original.
10. **replica-launch** escribe la página de aterrizaje alrededor del ángulo, pone precios frente a la página pública de precios (con la fecha en que se leyó) y revisa la ficha de la tienda.
11. **replica-deploy** ejecuta la revisión previa y, cuando tú dices que adelante, lo publica.

Cualquier skill se puede ejecutar solo. replica-entrepreneur, sobre una aplicación que aún no has empezado, es una forma razonable de decidir si conviene construirla.

## Instalar en Cursor

Cursor carga los skills de un proyecto desde `.cursor/skills/<name>/SKILL.md` y `.agents/skills/<name>/SKILL.md`, y para tu usuario desde `~/.cursor/skills/` y `~/.agents/skills/`. El nombre de la carpeta es el nombre del skill. `name` y `description` en el frontmatter son obligatorios, y `name` tiene que coincidir con la carpeta.

Este instalador usa `.cursor/skills` (proyecto) y `~/.cursor/skills` (`--global`). Los skills del proyecto viajan con el repositorio. Los de `~/.cursor/skills/` se quedan en esa máquina hasta que actives la sincronización para Cloud Agents en Settings, Agents. Un skill que quieras en cada ejecución de Cloud Agent sobre un repositorio va en `.cursor/skills/` de ese repositorio.

```bash
git clone https://github.com/letmefind/replica-skill-cursor-grok.git
cd replica-skill-cursor-grok
./cursor/install.sh                  # ./.cursor/skills
./cursor/install.sh --project /path/to/app
./cursor/install.sh --global         # ~/.cursor/skills
```

Volver a ejecutarlo sustituye las carpetas de Replica y `replica-tools/`, y deja en paz cualquier otro skill que haya ahí.

En el chat, escribe `/` y elige `replica` o `replica-recon`. Eso une el skill a un mensaje. Para mantenerlo toda la sesión, ábrelo como Custom Mode: Option+Enter en macOS, Alt+Enter en Windows.

Las plantillas se quedan en la carpeta del skill. Las herramientas de Python son una sola copia. Después de instalar están en `replica-tools/` junto a las carpetas de los skills. Desde un checkout de este repositorio, pon `REPLICA_HOME` en ese checkout y los skills usan `tools/` ahí. Python 3.8 o más nuevo. Nada que instalar con pip.

## Instalar en Grok Bot

Envía esto, como mensaje completo:

```
Install the Replica skills from https://github.com/letmefind/replica-skill-cursor-grok
```

Los pasos siguientes están en [grok-bot/INSTALL.md](../../grok-bot/INSTALL.md). En corto: clona este repositorio en `/home/box/replica-skill` (`REPLICA_HOME` cambia la ruta), ejecuta `grok-bot/install.sh` y guarda cada archivo de `grok-bot/skills/*/SKILL.md` como skill. El nombre, la descripción y el cuerpo se copian tal cual. Un skill de Grok Bot es ese único archivo. Las herramientas y las plantillas se quedan en disco y los skills las llaman por ruta absoluta, por ejemplo `python3 "${REPLICA_HOME:-/home/box/replica-skill}/tools/parity.py"`.

Las notas de investigación de un proyecto viven en `/workspace/<project-slug>/replica/`. Cuando un paso escribe la aplicación, `replica/` vive en tu repositorio de código. Los cambios de código se entregan a un Cursor cloud coding agent en ese repositorio de GitHub, como una tarea que incluye los archivos `replica/` que hagan falta. Tú inicias sesión, pagas, compras el dominio y escribes las claves en vivo.

## Herramientas

```bash
python3 tools/imgdiff.py original.png clone.png --out diff.png
python3 tools/parity.py replica/features.csv
python3 tools/reviews.py replica/reviews.csv
python3 tools/contrast.py replica/design/tokens.json
python3 tools/sweep.py . --avoid "Original App"
python3 tools/listing.py replica/launch/listing.json
```

Ninguna usa la red. `imgdiff.py` compara la disposición, no el color, para que un cambio de marca no cuente en tu contra. `parity.py` pondera must, should y could, cuenta partial como la mitad y no puntúa una fila que dejaste fuera a propósito. `reviews.py` descarta cualquier fila sin enlace. `sweep.py` bloquea un lanzamiento mientras el nombre, el dominio o los colores del original sigan en el árbol. `listing.py` comprueba los límites de la tienda y rechaza el nombre del original en tu ficha.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

## Disposición

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

Los archivos de tu proyecto van en `replica/`, no en este repositorio.

## Letra pequeña

**Reconstruye funciones y patrones de uso, en sala limpia.** Estudia lo que hace la aplicación y cómo se mueve la gente por ella, y luego lo escribe todo de nuevo. No copia el código fuente, los assets propietarios, los logos, las marcas, el texto ni las API privadas del objetivo.

**Solo lee lo que tienes permiso de leer.** Páginas públicas y tu propia cuenta. No raspa detrás de un inicio de sesión ni contra las condiciones de un sitio, no entra en la cuenta de otra persona y no pasa una barrera de pago. Si las condiciones de tu cuenta prohíben usarla para construir un competidor, el skill lo dice y se queda en fuentes públicas.

**Cambia la marca antes de publicar.** Nombre nuevo, paleta nueva, logo nuevo, palabras nuevas. replica-deploy no publica hasta que el barrido está limpio.

**«Clonar cualquier aplicación» significa las funciones y el flujo.** No el contenido, la red ni las licencias que posee una aplicación. Se puede reconstruir el reproductor, las listas y el uso compartido de una aplicación de música. No su catálogo.

**No hay promesa de un clon perfecto.** Una herramienta de reservas son semanas. Un motor de hojas de cálculo no. replica-recon da el tamaño antes de empezar, y replica-diff te da un número.

**El skill entrepreneur no inventa.** Ni reseñas, ni citas, ni cifras inventadas. Cada afirmación tiene un enlace, y se indica el tamaño de la muestra.

**Comprueba antes de vender.** Ejecuta las búsquedas de marca que lista replica-brand, lee las condiciones de todo lo que hayas usado y habla con un abogado antes de publicar si hay dinero de por medio. Esto no es asesoramiento jurídico.

## Licencia

MIT. El copyright original es de Jake Schincariol. El port añade una línea para letmefind. Véase [LICENSE](../../LICENSE).
