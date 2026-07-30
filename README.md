# EduKids Adventure 🐾

**Aprender nunca fue tan divertido**

Plataforma educativa interactiva para el aprendizaje de lenguas afrodescendientes e indígenas de Nicaragua, dirigida a niños y niñas de Educación Inicial y Primaria (Preescolar I, II, III y 1° a 6° grado).

Proyecto desarrollado por el equipo **Alphanica** para Hackathon Nicaragua 2026 (HN26).

---

## 📖 Descripción

EduKids Adventure es una aplicación educativa disponible en **Web**, **APK (Android)** y **EXE (Escritorio)**, diseñada para niños y niñas de Educación Inicial y Primaria. A través de juegos interactivos, actividades dinámicas y la compañía de la mascota virtual **Mushu**, la aplicación promueve el aprendizaje de las lenguas afrodescendientes e indígenas de Nicaragua, fortaleciendo la identidad cultural y preservando el patrimonio lingüístico del país.

El sistema incorpora contenido multimedia, recompensas y seguimiento del progreso para ofrecer una experiencia de aprendizaje divertida, accesible y motivadora.

## ❗ Problemática

En Nicaragua, muchas lenguas afrodescendientes e indígenas enfrentan el riesgo de perderse debido al escaso acceso a recursos educativos digitales que promuevan su aprendizaje. La falta de herramientas interactivas dirigidas a niños limita el conocimiento y la preservación de este importante patrimonio cultural.

## 💡 Solución

EduKids Adventure ofrece una plataforma educativa que combina tecnología, gamificación y contenido multimedia para enseñar estas lenguas de manera entretenida. Mediante juegos, pronunciaciones, imágenes, recompensas y la interacción con Mushu, los estudiantes desarrollan habilidades lingüísticas mientras fortalecen el respeto por la diversidad cultural.

## 🎯 Objetivo General

Desarrollar una aplicación educativa interactiva que promueva el aprendizaje y la preservación de las lenguas afrodescendientes e indígenas de Nicaragua mediante actividades lúdicas, juegos educativos y un sistema de recompensas que incentive el aprendizaje continuo.

### Objetivos Específicos

- Enseñar vocabulario, frases y expresiones básicas en diferentes lenguas afrodescendientes e indígenas de Nicaragua.
- Promover el conocimiento y la valoración de la diversidad lingüística y cultural del país.
- Motivar el aprendizaje mediante juegos interactivos, retos y actividades dinámicas.
- Implementar un sistema de recompensas y progreso que incentive la participación de los estudiantes.
- Integrar a Mushu, la mascota virtual, como guía y acompañante del proceso de aprendizaje.
- Facilitar el acceso al contenido educativo desde dispositivos Android (APK), Web y computadoras (EXE).

## 🌍 Visión

Ser la plataforma educativa digital líder en Nicaragua y la región, reconocida por transformar la forma en que los niños aprenden, a través de experiencias interactivas, inclusivas y multilingües.

## 🚀 Misión

Brindar a niños y niñas de Educación Inicial y Primaria una herramienta educativa digital divertida, accesible y de calidad, que fortalezca sus conocimientos y habilidades a través de juegos, actividades y contenido interactivo en múltiples idiomas.

## 👥 Público objetivo

- Niños de Educación Inicial (Preescolar I, II y III)
- Estudiantes de Primaria (1° a 6° grado)
- Docentes y tutores
- Padres de familia

## 🗣️ Idiomas disponibles

- Español
- Inglés
- Miskitu
- Garífuna
- Mayangna
- Creole

## 🛠️ Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Backend | Python, Django |
| API | Django REST Framework |
| Base de datos | SQLite (desarrollo, escalable a futuro) |
| Frontend / APK | Java (Android Studio) |
| Escritorio (EXE) | Java Swing (NetBeans) |

## 🏗️ Arquitectura del backend (apps de Django)

- **usuarios** — gestión de usuarios y perfiles
- **idiomas** — idiomas disponibles en la aplicación
- **categorías** — categorías de aprendizaje (Saludos, Familia, Colores, Animales, Números, Frutas, Escuela, Partes del cuerpo, Naturaleza, Profesiones, Objetos, Expresiones)
- **lecciones** — lecciones dentro de cada categoría
- **contenido** — palabras, frases, traducciones y datos educativos
- **multimedia** — imágenes, audios, videos y recursos
- **juegos** — información de juegos, tipos y configuraciones
- **recompensas** — estrellas, monedas, medallas y accesorios
- **mushu** — datos, estados y evolución de la mascota
- **progreso** — avances, logros, experiencia y niveles
- **api** — APIs REST para comunicar el frontend (Java) con el backend (Django)

El backend administra el contenido educativo y lo envía al APK y al EXE mediante peticiones API REST.

## 👨‍💻 Equipo — Alphanica

| Integrante | Rol | Responsabilidades |
|---|---|---|
| Lenna | Diseño e Interfaz (Java) | Pantallas y navegación, diseño visual y animaciones, experiencia de usuario, integración de Mushu |
| Luis | Juegos y Lógica (Java) | Desarrollo de juegos educativos, lógica y validaciones, puntajes, audio y pronunciación |
| Margareth | Backend (Python - Django) | Base de datos y modelos, API REST, usuarios, contenido y multimedia, recompensas, progreso y Mushu, administración del sistema |
| Equipo de Marketing | Publicidad y Branding | Identidad visual, redes sociales, materiales publicitarios, modelo de negocio |
| Administrador de Organización | Coordinación | Tiempos y entregas, documentación, explicación técnica y modelo de negocio, coordinación de la presentación final |

## 📂 Estructura del proyecto

```
edukids-adventure/
├── edukids/
├── materias/
├── recompensas/
├── usuarios/
├── manage.py
├── requirements.txt
└── .gitignore
```

## 🏆 Impacto esperado

- Contribuir a la preservación de las lenguas afrodescendientes e indígenas de Nicaragua.
- Fomentar el interés de niños y niñas por aprender nuevos idiomas desde edades tempranas.
- Promover el respeto por la diversidad cultural y lingüística.
- Facilitar el aprendizaje mediante una experiencia educativa innovadora, accesible y divertida.
- Motivar a los estudiantes a continuar aprendiendo gracias al sistema de recompensas y a la interacción con Mushu.

---

> *"Nuestro compromiso es crear una experiencia educativa que inspire, motive y transforme el aprendizaje."*

**Hackathon Nicaragua 2026 — hN10 · ¡Siempre más allá!**
