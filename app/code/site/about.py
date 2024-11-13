# mrthompson.wft/code/site/about.py

import fasthtml.common as fhtml

from code.components.footer import Footer
from code.components.header import Navbar

def about():
    page = (
        fhtml.Title("mrthompson's personal read-along blog: About Mister Thompson"),
        fhtml.Main(
            # first component is navbar
            Navbar(),
            # second component is small intro
            fhtml.Main(
                fhtml.Article(
                    fhtml.H1("😁"),
                    fhtml.NotStr("<p>Ya va, les cuento un poco de mí. Porque <i>me cuesta mucho ser autoreferente</i> 🙄"),
                    fhtml.P("🪡 Soy un tecnologista, político, poeta y músico, con opinión de todo y muchas ganas de espetarla al mundo."),
                    fhtml.NotStr("<p>🪡 Creo en las <em>opiniones fuertes debilmente sostenidas</em>. Debatamos de todo, y cambiemos constantemente de opinion. Es una excelente forma de obtener certezas - y buenas anecdotas.</p>"),
                    fhtml.P("🪡 Pertenezco a un movimiento político bien novedoso e interesante, denominado Partido Pirata, que propugna varios principios interesantes, que les invito a revisar."),
                    fhtml.P("🪡 Pertenezco a un país convulso, conservador, con nula conciencia de clase. Donde los trabajadores luchamos por sobrevivir usando tarjetas de crédito, mientras que el 1% más rico concentra casi el 50% de la riqueza nacional. No me creen? Revisen el Reporte de Inequidad Global de 2022, y hablemos con números en la mano de lo que ocurre en esta tierra."),
                    fhtml.P("🪡 Pertenezco a una casta de personas que fueron educadas en la meritocracia, creyendo en las bondades del libremercado, y sufrimos hoy las consecuencias de la deshumanización: salud mental como una utopía inalcanzable, salud financiera como una ilusión desamparada, salud física como un privilegio de pocos, salud emocional como una frase estúpida que reverbera en salones vacíos. Nos amparamos en que no sabíamos, no podíamos, éramos jóvenes y alocados; sabemos que el espíritu edípico no nos salva, como Kundera escribió alguna vez."),
                    fhtml.P("🪡 Pertenezco a los escapados de un culto religioso pedófilo y abusivo, como lo son los jesuitas. Un poco de ciencia me llevó al agnosticismo, un cientificismo profundo, a la estupidez. Dejé al barbón de lado, eso sí, y lo reemplacé por la Gran Albóndiga Voladora, con el Señor de la Silla y Loki. Porque todo panteón que se precie debiera tener a Loki."),
                    fhtml.P("🪡 Creo en la nada todopoderosa, creadora del hedonismo y de otros proselitismos, y creo en su hijo, el nihilismo, señor de nadie. No creo mucho en el hombre, mas sí en algunas personas; no creo mucho en la sociedad, mas sí en las utopías."),
                    fhtml.P("🪡 Sé un poco de mucho y mucho de muy poco. La tecnología ha sido mi pan y mi circo durante años (y no creo que cambie en el corto plazo). Juegos, sí, pero más lo nerd-cool: programar, diseñar sistemas, resolver problemas tontos - y otro no tanto - con tecnología."),
                    fhtml.P("No me malentiendan: tecnología no es sólo computadoras y teléfonos inteligentes. Es mucho más (y tanto menos) que eso. Tecnología es una pieza de papel y un lápiz; es un palo cortado en un lugar específico; es una nueva forma de hacer las cosas. Tecnología, de los vocablos griegos τέχνη (téchnē), \"arte\", y λόγος (lógos) ,\"tratado\", es una manera de crear técnica de forma artística. Es una forma de sistematizar el arte con técnicas. Es un lenguaje propio. Y es ese lenguaje el que me he dedicado a estudiar."),
                    fhtml.NotStr("<p>Hablando del lenguaje de la tecnología, un poco de mi <i>resume</i>:</p>"),
                    fhtml.Div("⚙️ Programo en Python hace más años de los que quiero contar."),
                    fhtml.Div("⚙️ Extraigo y exploto datos con SQL. Un piu con bases NoSQL."),
                    fhtml.Div("⚙️ Creo aplicaciones web, locales, y otras locuras de esa índole."),
                    fhtml.Div("⚙️ Y como no todo es computadores en la vida, también escribo poesía."),
                    fhtml.Div("⚙️ Y toco un par de instrumentos."),
                    fhtml.Div("⚙️ En algún momento de la vida, decidí que era buena idea levantar la voz por la gente."),
                    fhtml.Div("⚙️ Y, en otro momento posterior, Mikhail Bakunin y Rosa de Luxemburgo iluminaron mi camino."),
                    fhtml.P(),
                    fhtml.P("Y, entre otras cosas, me dedico a:"),
                    fhtml.Div("⚙️ La ingeniería de datos,"),
                    fhtml.Div("⚙️ El desarrollo web,"),
                    fhtml.Div("⚙️ El desarrollo de backends,"),
                    fhtml.Div("⚙️ La poesía escrita y slam,"),
                    fhtml.Div("⚙️ La música, como bajista y DJ,"),
                    fhtml.Div("⚙️ La política, como un cyberactivista de cartón y caviar"),
                    fhtml.Div("⚙️ Entre algunas cosas más."),
                    fhtml.P(),
                    fhtml.NotStr("<p>Ahora, si tengo que responder a la pregunta <i>\"¿quién soy?\"</i>, creo que mi respuesta sería que <b>soy</b>.</p>"),
                    fhtml.B(fhtml.Em("Yo soy.")),
                )
            ),
            Footer(),
            cls="container",
        ),
    )
    return page
