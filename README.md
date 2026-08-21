# PiSolid: aumenta la seguridad en internet

![Licencia](https://img.shields.io/badge/Licencia-GPLv3-orange.svg)
![Último commit](https://img.shields.io/github/last-commit/kveld9/PiSolid/main)

<img src="images/banner.png" alt="Banner de PiSolid" style="max-width: 100%; height: auto;">

## ¿En qué consiste?

PiSolid utiliza la herramienta de compilación de listas del equipo de AdGuard para combinar y procesar distintas fuentes con objetivos específicos. Las listas se actualizan automáticamente cada 12 horas y reúnen fuentes seleccionadas para mejorar la seguridad, la privacidad y la experiencia general de navegación en la red.

## Listas disponibles

| Lista                  |                                                                                 Dominios actuales | Frecuencia de actualización |
| ---------------------- | ------------------------------------------------------------------------------------------------: | --------------------------- |
| **PiSolid Ultra**      |          <!-- AUTO_COUNT_ULTRA --> ![ULTRA](https://img.shields.io/badge/dominios-2481142-blue) | Cada 12 horas               |
| **PiSolid Ultra Lite** | <!-- AUTO_COUNT_ULTRA_LITE --> ![ULTRA\_LITE](https://img.shields.io/badge/dominios-405658-blue) | Cada 12 horas               |
| **PiSolid NSFW**       |              <!-- AUTO_COUNT_NSFW --> ![NSFW](https://img.shields.io/badge/dominios-570265-blue) | Cada 12 horas               |

> **Nota:** PiSolid NSFW puede combinarse con PiSolid Ultra o PiSolid Ultra Lite si también deseas bloquear contenido para adultos.

## Contenido bloqueado por cada lista

### PiSolid Ultra

* Estafas
* Malware
* Phishing
* Anuncios y publicidad
* Rastreadores y telemetría

### PiSolid Ultra Lite

* Anuncios y publicidad
* Rastreadores y telemetría
* Malware y phishing con cobertura reducida

### PiSolid NSFW

* Contenido para adultos (NSFW)

## ¿Cómo se utiliza?

PiSolid utiliza el formato de reglas **AdBlock**, que permite bloquear dominios específicos y sus subdominios asociados. Es compatible con una amplia variedad de programas y herramientas, entre ellos:

* Pi-hole
* AdGuard
* AdGuard Home
* Technitium DNS Server
* uBlock Origin
* AdBlock

Para que estas herramientas puedan aplicar correctamente las reglas, debes añadir la URL RAW correspondiente a la lista que deseas utilizar.

## Enlaces para utilizar

### PiSolid Ultra

* [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/main/pisolid-ultra.txt)
* [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-ultra.txt)

### PiSolid Ultra Lite

* [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/main/pisolid-ultra-lite.txt)
* [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-ultra-lite.txt)

### PiSolid NSFW

* [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/main/pisolid-nsfw.txt)
* [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-nsfw.txt)

## Fuentes

### PiSolid Ultra

* [HaGeZi's Threat Intelligence Feeds DNS Blocklist — versión completa](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt)
* [HaGeZi Ultimate](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt)
* [OISD Big](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/big/domains.adblock)
* [Destroylist: Phishing & Scam Domain Blacklist](https://cdn.jsdelivr.net/gh/phishdestroy/destroylist@main/rootlist/formats/primary/adblock.txt)
* [AWAvenue Ads Rule](https://script.cx.ms/awavenue/AWAvenue-Ads-Rule-Adguard.txt)

### PiSolid Ultra Lite

* [HaGeZi's Threat Intelligence Feeds DNS Blocklist — versión mini](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.mini.txt)
* [HaGeZi Ultimate](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt)
* [AWAvenue Ads Rule](https://script.cx.ms/awavenue/AWAvenue-Ads-Rule-Adguard.txt)

### PiSolid NSFW

* [OISD NSFW](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/nsfw/domains.adblock)
* [StevenBlack NSFW](https://raw.githubusercontent.com/cbuijs/stevenblack/refs/heads/main/adblock/porn.txt)
* [HaGeZi's NSFW Blocklist](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/nsfw.txt)

## Agradecimientos

* Gracias a [xdL](https://t.me/xdlane) por la colaboración en el diseño gráfico.
* Gracias a [HostlistCompiler](https://github.com/AdguardTeam/HostlistCompiler) por proporcionar la herramienta utilizada para compilar y generar las listas finales de PiSolid.

---

## Licencia

Este proyecto se distribuye bajo la licencia **GNU General Public License v3.0**. Consulta el archivo [LICENSE](LICENSE) para obtener más información.
