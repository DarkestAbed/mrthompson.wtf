---
title: Cómo nace este espacio feat. SvelteKit
description: Una breve historia de cómo se gestó este espacio.
date: '2024-05-14'
categories:
  - sveltekit
  - hola
published: true
---

Hace algunos años atrás, trabajando con [Rodrigo Abt👨🏽‍💻](https://www.linkedin.com/in/rodabt/) en un proyecto de consultoría, me mostró un framework de Javascript llamado [Svelte](https://www.svelte.dev): una forma liviana y bastante amigable de desarrollar sitios web modernos, sin los 250mil megabytes y las 535mill de líneas de código _boilerplate_ que tomaban React y Angular (los actores dominantes de esa época en el espacio del desarrollo front). En un par de días, levantamos con relativamente poco esfuerzo, una POC (prueba de concepto, o _proof of concept_) de lo que queríamos entregar y productivizar. Como mi expertise en JS era bien baja en esa época, me quedé con la experiencia y las palabras dándome vueltas en la cabeza.

Aceleramos el tiempo hasta el 2023: en un impulso, compré un par de dominios, incluyendo éste ([mrthompson.xyz](/)). Pensando que podría ser un buen espacio para hablar de cosas que me gustan, que no, de lo que pasa a mi alrededor y _rantear_ ([_to rant_](https://www.urbandictionary.com/define.php?term=Rant): expresar opiniones de manera desorganizada y agraviada, según [The Urban Dictionary](https://www.urbandictionary.com)), hablé conmigo mismo y le dije:
> Mismo, esta es una buena oportunidad para que hablemos de las cosas que nos gustan, las que no, lo que pasa a nuestro alrededor y _rantear_.

Y me encontré con una barrera: no soy experto en desarrollo web moderno. Algo de HTML5 y CSS manejaba, pero crear un sitio hermoso como éste, nihablar.

Un poco más de tiempo: **abril de 2024**. Me encontré con más tiempo en mis manos (porque mi empleador, de una forma muy clínica y con no mucha gracia, [me devolvió al mercado laboral](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2x1YXZmZXVsNm53aHN6a2ljNW8wODB2a2Uwd2I5Ynl5d2R3eTJ6aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orieLabblWfHRFDkA/giphy.gif)), y me reencontré con este hermoso proyecto. Así que, volví a mirarme al espejo, y le dije a mí mismo:
> Mismo, qué tal si estudiamos un poco y creamos un blog bonito, responsivo, moderno, usando alguna tecnología buena onda que nos permita tener un producto rápido e iterativo?

Y Mí Mismo me respondió:
> 🤡, debieras haberlo hecho hace años. Papafrita.

_Mi Mismo no es particularmente amable. Le apodé "Lotso" hace algún tiempo, porque es rosadito y felpudo y un culiado, como el personaje de Toy Story:_

<iframe title="lotso-gif" src="https://giphy.com/embed/wBDmRXskq8H3W" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><a href="https://giphy.com/gifs/disney-pixar-disney-toy-story-3-wBDmRXskq8H3W">via GIPHY</a>

Entonces, me puse a buscar tutoriales de cómo crear blogs usando Javascript y desarrollo moderno. Deseché las ideas de React y Vue y Next.js, porque son MUCHÍSIMO código y mucho tiempo de configuración inicial. O lo que, en ese momento, sentí que era una cantidad ridícula de tiempo para iniciar y configurar, versus algo en HTML plano.

Pensé en [HTMX](https://htmx.org/), un framework bastante nuevo de desarrollo, que mejora las capacidades de SSR y SSE (_server side rendering_ y _server side events_, respectivamente). Y me confundí un chingo al empezar a desarrollar.

Finalmente, apareció un enviado del cielo: [Joy of Code](https://joyofcode.xyz/) en [YouTube](https://youtu.be/RhScu3uqGd0), mostrando cómo hacer un blog en SvelteKit usando Markdown.

Y, naturalmente, me pregunté: _qué chúcha es **SvelteKit**?_

Así que seguí el tutorial, le puse un poco de mi cosecha, y **PAF nació Chocapic**. Gracias a Dior, [SvelteKit](https://kit.svelte.dev/) es un framework de desarrollo **FACILÍSSIMO** de usar: toda la infra de este blog me tomó dos horas en configurar, probar y desplegar. Y se ve bacano. Y también te dice que _**el modo oscuro es el modo correcto de ver las cosas**_. Un poco de sabiduría allí 😌

Honest? Ahora quiero hacer todo el front en Svelte + SvelteKit. Recomiendo ENORMEMENTE aprenderlo, usarlo, divertirse con él, y dejar de lado Tailwind, React, NextJS, y toda esa majamama de weás difíciles y sobrecomplicadas, porque **no existe la bala plateada en tecnología**. Cada herramienta tiene su lugar y su caso de uso, y es fundamental que tengamos eso siempre como perspectiva.

<div>
<pre><code>
function developWithSvelte(name: string) {
    console.log(`Hey ${name}! 👋 Go learn Svelte! 🙌🏽`)
}
</code></pre>
</div>

Esa es mi historia con SvelteKit, en un nutshell. La próxima historia será para la próxima. Besitos!
