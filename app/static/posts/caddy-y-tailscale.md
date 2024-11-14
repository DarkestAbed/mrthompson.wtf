---
title: Tailscale, Caddy, Cloudflare, y una historia de mixturas
description: "Un viaje que pareciera nunca acabar"
date: '2024-11-13'
categories:
  - computer-science
  - networking
  - redes
  - caddy
  - tailscale
published: false
---
Hace unos dias descubri un servicio en linea tremendamente interesante, que puede aliviar una montonera de problemas para compartir cosas: [Tailscale](https://tailscale.com). No me acuerdo, realmente, que estaba buscando, en que agujero de conejo de internet estaba, pero sali - lo que yo considero - victorioso de alli.
Tailscale es un servicio de DNS privado (o algo asi, mis conocimientos de redes me fallan gravemente), que permite generar una PAN (_Private Area Network_, concepto bien olvidado a traves de los anos) y poder conectarse a multiples dispositivos de manera privada. Asi, con Tailscale, puedes conectar tu celular, tus tablets, tus laptops y tus computadores, sin problemas y sin grandes sobresaltos.
Quienes leen que no son techies, se preguntaran y con justa razon: _**para que chucha**_ quiero conectar dispositivos en una red privada? Y la respuesta es multiple:

- Con muchos dispositivos distintos conectados, puedo acceder a servicios privados de manera publica. Por ejemplo, puedo montar mi propia nube privada en [Nextcloud](https://nextcloud.com), tener una instancia de [Immich](https://immich.app) adicional y poder servir mi propia biblioteca de libros en EPUB desde [BookStairs](https://github.com/bookstairs/bookstairs).
- Con muchos dispositivos conectados, puedo desarrollar una app web en mi laptop, servirla desde mi compu y mirarla desde mis cel y tablet.
- Puedo compartir archivos usando el protocolo WebDAV, que es multiplataforma e interoperable, y asi tener una biblioteca de documentos, todos en linea, y todos actualizados instantaneamente
- Puedo incluso hacer cosas tan locas como [tener flujos de trabajo ordenados]() para todo lo que necesites. Porque si lo necesitas, probablemente hay una aplicacion para ello.

Como este servidor es un alto nono, le he dedicado esta ultima semana una buena cantidad de tiempo a explocar Tailscale, tanto como 
