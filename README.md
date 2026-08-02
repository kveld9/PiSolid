# PiSolid: aumenta la seguridad en internet

![License](https://img.shields.io/badge/License-GPLv3-orange.svg)
![Last commit](https://img.shields.io/github/last-commit/kveld9/PiSolid/main)

<img src="images/banner.png" alt="banner" style="max-width: 100%; height: auto;">

## ¿En qué consiste?

Mediante la herramienta de compilación de listas del equipo de AdGuard, cada 12 horas se compilan distintas listas con objetivos específicos, recolectando las mejores fuentes para mejorar la seguridad general de la red.

## Listas disponibles

| Lista               | Dominios actuales | Última actualización |
|---------------------|-------------------|----------------------|
| **PiSolid Ultra**       | <!-- AUTO_COUNT_ULTRA --> ![Ultra](https://img.shields.io/badge/dominios-2.511.074-blue) | ![Ultra updated](https://img.shields.io/github/last-commit/kveld9/PiSolid/main/pisolid-ultra.txt?label=actualizado) |
| **PiSolid Ultra Lite**  | <!-- AUTO_COUNT_ULTRA_LITE --> ![Ultra Lite](https://img.shields.io/badge/dominios-393.083-blue) | ![Lite updated](https://img.shields.io/github/last-commit/kveld9/PiSolid/main/pisolid-ultra-lite.txt?label=actualizado) |
| **PiSolid NSFW**        | <!-- AUTO_COUNT_NSFW --> ![NSFW](https://img.shields.io/badge/dominios-583.177-blue) | ![NSFW updated](https://img.shields.io/github/last-commit/kveld9/PiSolid/main/pisolid-nsfw.txt?label=actualizado) |

> **Nota:** La lista NSFW puede combinarse con Ultra o Ultra Lite si deseas bloquear también contenido adulto.

## Contenido bloqueado por cada lista

### PiSolid Ultra
- Estafas
- Malware
- Phishing
- Anuncios / publicidad
- Rastreadores / telemetría

### PiSolid Ultra Lite
- Anuncios / publicidad
- Rastreadores / telemetría
- Malware y phishing (cobertura reducida)

### PiSolid NSFW
- Contenido para adultos (NSFW)

## ¿Cómo se utiliza?

El formato de bloqueo de dominios en AdBlock permite filtrar contenido al bloquear dominios específicos y, por tanto, sus subdominios asociados. Es compatible con una amplia gama de software y herramientas: Pi-hole, AdGuard, AdGuard Home, Technitium, y extensiones de navegador como uBlock Origin o AdBlock.

Para que estos programas apliquen correctamente las reglas, debes proporcionar la URL del archivo en formato RAW.

## Enlaces para utilizar

### PiSolid Ultra
- [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/main/pisolid-ultra.txt)
- [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-ultra.txt)

### PiSolid Ultra Lite
- [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/main/pisolid-ultra-lite.txt)
- [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-ultra-lite.txt)

### PiSolid NSFW
- [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/main/pisolid-nsfw.txt)
- [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-nsfw.txt)

## Fuentes

### PiSolid Ultra
- [HaGeZi's Threat Intelligence Feeds DNS Blocklist - full version](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.txt)
- [HaGeZi-Ultimate](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt)
- [OISD-Big-cbuijs](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/big/domains.adblock)
- [Destroylist: Phishing & Scam Domain Blacklist](https://cdn.jsdelivr.net/gh/phishdestroy/destroylist@main/rootlist/formats/primary/adblock.txt)
- [AWAvenue Ads Rule](https://script.cx.ms/awavenue/AWAvenue-Ads-Rule-Adguard.txt)

### PiSolid Ultra Lite
- [HaGeZi's Threat Intelligence Feeds DNS Blocklist - mini version](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.mini.txt)
- [HaGeZi-Ultimate](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/ultimate.txt)
- [AWAvenue Ads Rule](https://script.cx.ms/awavenue/AWAvenue-Ads-Rule-Adguard.txt)

### PiSolid NSFW
- [OISD-NSFW-cbuijs](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/nsfw/domains.adblock)
- [StevenBlack-NSFW-cbuijs](https://raw.githubusercontent.com/cbuijs/stevenblack/refs/heads/main/adblock/porn.txt)
- [HaGeZi's NSFW Blocklist](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/nsfw.txt)

## Agradecimientos
- Gracias a [xdL](https://t.me/xdlane) por la colaboración en el diseño gráfico.
- Gracias a [HostlistCompiler](https://github.com/AdguardTeam/HostlistCompiler) por la herramienta utilizada en cada una de las presentaciones finales de PiSolid.

---

## Licencia

Este proyecto está bajo la licencia GNU General Public License v3.0. [Leer más](LICENSE).
