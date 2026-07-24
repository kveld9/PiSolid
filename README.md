# PiSolid: aumenta la seguridad en internet.

![License](https://img.shields.io/badge/License-GPLv3-orange.svg)

<img src="images/banner.png" alt="banner" style="max-width: 100%; height: auto;">

## ¿En qué consiste?

Mediante la herramienta de compilación de listas del equipo de AdGuard, cada 12 horas se compilarán distintas listas con distintos objetivos cada una, donde se recolectan las mejores fuentes de la actualidad para mejorar la seguridad general de la red.

## Contenido bloqueado
- Estafas.
- Malware.
- Phishing.
- NSFW (solo la lista que lo indica).

## ¿Cómo se utiliza?

El formato de bloqueo de dominios en AdBlock permite filtrar contenido al bloquear dominios específicos y, por ende, sus subdominios asociados de manera efectiva. Esta técnica es compatible con una amplia gama de softwares y herramientas de filtrado de anuncios, incluyendo Pi-Hole, AdGuard, AdGuard Home, y Technitium, entre otros. Además, este formato se puede utilizar en navegadores que admiten listas de bloqueo basadas en el formato AdBlock, como en las extensiones AdBlock o uBlock Origin.

Para que estos softwares o extensiones puedan aplicar correctamente las reglas de bloqueo, es crucial proporcionar la URL del archivo en formato RAW.

## Enlaces para utilizar
### **PiSolid-Ultra**
- [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/refs/heads/main/pisolid-ultra.txt)
- [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-ultra.txt)
- [Mirror](https://brevent.sytes.net/dns/pisolid-ultra.txt)

### **PiSolid-Ultra-Lite**
- [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/refs/heads/main/pisolid-ultra-lite.txt)
- [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-ultra-lite.txt)
- [Mirror](https://brevent.sytes.net/dns/pisolid-ultra-lite.txt)

### **PiSolid-NSFW**
- [GitHub](https://raw.githubusercontent.com/kveld9/PiSolid/refs/heads/main/pisolid-nsfw.txt)
- [Codeberg](https://codeberg.org/kveld9/PiSolid/raw/branch/main/pisolid-nsfw.txt)
- [Mirror](https://brevent.sytes.net/dns/pisolid-nsfw.txt)

## Fuentes
### **PiSolid-Ultra**
- [HaGeZi's Threat Intelligence Feeds DNS Blocklist - full version](https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/tif.txt)  
- [HaGeZi-Ultimate](https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/ultimate.txt)  
- [OISD-Big-cbuijs](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/big/domains.adblock)  
- [Malicious URL Blocklist (URLHaus)](https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt)
- [uBlock filters – Badware risks](https://adguardteam.github.io/HostlistsRegistry/assets/filter_50.txt)
- [Peter Lowe - hosts](https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts)

### **PiSolid-Ultra-Lite**
- [HaGeZi's Threat Intelligence Feeds DNS Blocklist - mini version](https://codeberg.org/hagezi/mirror2/raw/branch/main/dns-blocklists/adblock/tif.mini.txt)
- [HaGeZi-Ultimate](https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/ultimate.txt)
- [OISD-Big-cbuijs](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/big/domains.top-n.adblock)

### **PiSolid-NSFW**
- [OISD-NSFW-cbuijs](https://raw.githubusercontent.com/cbuijs/oisd/refs/heads/master/nsfw/domains.top-n.adblock)  
- [StevenBlack-NSFW](https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn-only/hosts)  
- [HaGeZi's NSFW DNS Blocklist](https://codeberg.org/hagezi/mirror2/raw/branch/main/dns-blocklists/adblock/nsfw.txt)

## Agradecimientos
- Gracias a [xdL](https://t.me/xdlane) por la colaboración en el diseño gráfico.
- Gracias a [hostslistcompiler](https://github.com/AdguardTeam/HostlistCompiler) por la herramienta utilizada en cada una de las presentaciones finales de PiSolid.

## Contribuciones

Si deseas contribuir al proyecto o sugerir mejoras, por favor, contacta a través del siguiente correo. Se agradece cualquier colaboración para hacer de este proyecto una herramienta más efectiva para todos.

• kveld9@disroot.org

---

## Licencia

Este proyecto está bajo la licencia GNU General Public License v3.0. [Leer más](LICENSE).
