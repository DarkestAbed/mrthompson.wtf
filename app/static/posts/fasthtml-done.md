---
title: "Una experiencia con FastHTML: la historia de una ida y una vuelta"
description: Repensando el desarrollo fullstack usando solo Python, pt 2.
date: '2024-11-02'
categories:
  - python
  - fasthtml
  - frontend
  - webdev
published: true
---

Hace una o dos semanas, me embarque en el noble proyecto de redisenar, _from the ground up_, mi sitio web. Este sitio web. Porque tengo otro sitio, que es mas profesional, y no les voy a contar donde esta. Pero si les puedo contar que en ambos empece a trabajar en SvelteKit, y ahora los estoy moviendo a FastHTML.

> FastHTML? Que clase de droga alucinogena estas tomando? Porque, si algo de Fast* he escuchado, es FastAPI.

Enhorabuena, lector! Ahora existe un **FastHTML**, un framework de diseno y desarrollo web front-end, basado en Python y que comparte mucha de la filosofia de diseno con FastAPI.

De su sitio web:
> "With FastHTML you create good-looking modern web applications in pure Python and deploy them in minutes."\n
> (En espanol: 'Con FastHTML puedes crear aplicaciones web modernas y visualmente bellas en Python puro, y desplegarlas en minutos'.)

Y, la verdad, no es tanto _minutos_, en mi experiencia; me costo enganchar con algunas tecnicas, y encontrar algunas soluciones. Por ejemplo: al ser esto un blog, necesito rutear sitios a archivos estaticos con nombres dinamicos. Eso lo soluciona SvelteKit (y, entiendo, cualquier framework de front en Javascript moderno) con lo que llaman _slugs_, piezas de URI que dirigen de forma dinamica a un sitio en particular. En FastHTML tuve que construir una solucion de _slugging_ a mi medida, en base a mi particular necesidad. Lo que no esta malo, es solo algo mas tedioso.

FastHTML es una solucion bastante solida. La he podido probar con exito en mi red local, en conjunto con **[Tailscale](https://tailscale.com/)**, lo que me permite probar sin proxies y con desarrollo remoto. Que oferton!

![Puta, que oferton](https://cdn.eldeforma.com/wp-content/uploads/2020/11/Oferton.jpg)

Me gusta la idea de poder construir productos completos, fullstack, en un solo idioma. Y como mi conocimiento en Javascript es, actualmente, no tan bueno, hacerlo en Python con algunos tintes de HTML y de CSS es fantastico.

Algo muy interesante de FastHTML son los _tags **FT**_, que funcionan como wrappers de etiquetas HTML en Python:

<div>
<pre><code>
import fasthtml.common as ft

def fasthtml_function() -> Any:
    paragraph: str = ft.P("Esto es un parrafo")
    multiparagraph: str = ft.P(
        ft.B("Esto es un texto en negrita"),
        ft.I("Y esto un texto en italicas"),
    )
    return ft.Div(
        ft.P("Aca va un texto"),
    )
</code></pre>
</div>

Y si bien, no he logrado aun hacer que el codigo se vea bonito como _a mi me gusta que se vea bonito_, da una idea de lo idiomaticamente agradable que es usar el tipo de tags FT.

Ademas, FastHTML trabaja sobre HTMX, lo que genera una capa de interactividad super interesante. En un proximo proyecto mas o menos importante que tengo, la voy a probar y les cuento.

Lo mas desafiante de todo este trabajo fue el reescribir el sitio web desde HTML/CSS/JS hacia Python. Porque [la documentacion de FastHTML](https://docs.fastht.ml) no es la mejor del mundo, la verdad. Pero se puede. Con algo de conocimiento de todas las tecnologias, se puede bien.

En conclusion:
* FastHTML es un framework muy interesante y muy potente para hacer cosas en web.
* Construir HTML con _"funciones"_ de Python tiene mucho sentido idiomatico.
* La documentacion podria ser mejor.
  * Dicho esto, hay un buen punto de partida en ella.
* Si sabes Python y quieres hacer front sin aprender Javascript, es una muy, MUY buena herramienta.

<p><i>#eso</i></p>
Peace out.
