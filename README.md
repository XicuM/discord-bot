# discord-bot

**discord-bot** es un bot de discord simple para gamificar el servidor de *La Caverna Ecléctica*. El bot responde a diferentes comandos y actúa en función del canal en el que se encuentre el usuario.

*La Caverna Ecléctica* es un servidor que se creó en 2021 para fomentar las ideas y creatividad entre los miembros de su comunidad. Para ello, cuenta con diferentes actividades, entre las que se encuentran:

- El **programa semanal** (:warning: INTERRUMPIDO): Un programa semanal de hasta 4 participantes en el que se hablan de diferentes temas. Los miembros pueden apuntarse a la lista de participantes con un comando del bot.

- La **sala de trabajo**: Un espacio virtual en el que los miembros se conectan para hacerse compañía mientras trabajan en sus proyectos personales. Se inspira en la sala de trabajo creada por Jaime Altozano en su servidor de Discord. A medida que van pasando horas en la sala, el bot va sumando puntos a los miembros y les asigna roles en función de su actividad:
  - **nini**: menos de 1 hora.
  - **novato**: entre 1 y 2 horas.
  - **iniciado**: entre 2 y 6 horas.
  - **padawan**: entre 6 y 24 horas.
  - **emprendedor**: entre 24 y 120 horas.
  - **empresario**: entre 120 y 720 horas.
  - **magnate**: entre 720 y 5040 horas.
  - **maestro vital**: más de 5040 horas.

A parte de asistir a los miembros en el programa semanal y la sala de trabajo, el bot también envía un mensaje de bienvenida a los nuevos miembros.


# Estructura del servidor

La estructura de canales del servidor es la siguiente:

## ℹ INFORMACIÓN

### #general
Aquí se comparte información general y anuncios sobre el servidor. Únicamente los administradores y el bot pueden escribir en este canal.
**Comandos disponibles**:
- `!act`: Actualiza la descripción general del servidor.

## 🗨 PROGRAMA SEMANAL

### #participar
En este canal los miembros pueden gestionar su participación en el programa semanal.
**Comandos disponibles**:
- `!help`: Muestra la lista de comandos disponibles.
- `!unirme`: Añade al usuario a la lista de participantes del programa semanal.
- `!cancel`: Elimina al usuario de la lista de participantes.
- `!fecha`: Cambia la fecha del programa semanal.
- `!clear`: Borra la lista de participantes.

### #chat
Es el canal de texto que se usa durante el programa semanal.
**Comandos disponibles**:
- `!help`: Muestra la lista de comandos disponibles.
- `!preg -add <topic> <preg>`: Añade una pregunta a la lista de preguntas de un tema.
- `!preg <topic>`: Muestra una pregunta aleatoria de un tema de la lista. Con el tema `random` se muestra una pregunta aleatoria de cualquier tema.
- `!enc -add <topic> <enc>`: Añade una encuesta a la lista de encuestas de un tema.
- `!enc <topic>`: Muestra una encuesta aleatoria de la lista. Con el tema `random` se muestra una encuesta aleatoria de cualquier tema.

### 🔈en transmisión
Es el canal de voz que se usa durante el programa semanal.

## 🖊 SALA DE TRABAJO

### #anotaciones
Es el canal de texto en el que se los usuarios pueden dejar anotaciones para recordar cosas importantes. Los usuarios también pueden pedir el número de horas que llevan en la sala de trabajo.
**Comandos disponibles**:
- `!help`: Muestra la lista de comandos disponibles.
- `!horas`: Muestra las horas totales que lleva el usuario en la sala de trabajo, así como el rango que tiene asignado.

### 🔈reunión
Es el canal de voz que se usa durante la sala de trabajo.

## ⚙ ADMIN

### #ideas
En este canal los administradores pueden compartir ideas y sugerencias para mejorar el servidor.

### #direct
En este canal los administradores pueden enviar mensajes directos a los miembros del servidor como si fueran enviados por el bot.
**Comandos disponibles**:
- `!dm <user> <message>`: Envía un mensaje directo a un usuario.

### #testbench
Este canal es específico para pruebas del bot.
**Comandos disponibles**:
- `!clear`: Borra los mensajes del canal.


# Notas del desarrollador

## 📝 Tareas pendientes
- [ ] Valorar usar bases de datos para almacenar información de los usuarios.
- [ ] Solucionar problemas con las tildes en los mensajes guardados.
- [ ] Mejorar la gestión de errores en los comandos.