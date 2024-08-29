#!/usr/bin/env python3
import os
from datetime import datetime
import tldextract
import argparse
import requests
import re

# Definir rutas de archivo como variables
download_url = "https://raw.githubusercontent.com/kveld9/latam-hosts/main/adblock"
output_file = "adblock"   # Nombre por defecto del archivo de salida
link_comment = "https://github.com/kveld9/latam-hosts"

def get_base_domain(domain):
    extracted = tldextract.extract(domain)
    if not extracted.domain or not extracted.suffix:
        return None
    return f"{extracted.domain}.{extracted.suffix}"

def is_valid_domain(domain):
    # Verificar que el dominio tiene un formato correcto
    if re.match(r"^(?!\-)([A-Za-z0-9\-]{1,63}(?<!\-)\.)+[A-Za-z]{2,6}$", domain):
        return True
    return False

def has_minimum_length(domain, min_length=3):
    """ Verifica si el dominio tiene al menos 'min_length' caracteres antes del TLD """
    extracted = tldextract.extract(domain)
    if not extracted.domain:
        return False
    return len(extracted.domain) >= min_length

def download_and_process(domains, output_path, link_comment, download_url):
    # Descargar el archivo original
    if os.path.exists(output_path):
        os.remove(output_path)

    try:
        response = requests.get(download_url)
        response.raise_for_status()
        original_content = response.text
        print(f"\033[32m--> Archivo descargado correctamente desde '{download_url}'.\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"\033[31m--> Error al descargar el archivo: {e}\033[0m")
        return

    domain_groups = {}
    for line in original_content.splitlines():
        if line.startswith('||'):
            base_domain = get_base_domain(line[2:].strip('^'))
            if base_domain and is_valid_domain(base_domain):
                domain_groups[line.strip()] = base_domain

    # Contar dominios únicos del archivo original
    initial_domain_count = len(domain_groups)

    invalid_domains = []
    duplicate_domains = []
    false_positives = []

    # Agregar dominios proporcionados por el usuario
    for domain in domains:
        base_domain = get_base_domain(domain)
        if base_domain:
            if is_valid_domain(base_domain):
                entry = f"||{base_domain}^"
                if entry in domain_groups:
                    duplicate_domains.append(domain)
                else:
                    domain_groups[entry] = base_domain
            else:
                false_positives.append(domain)
        else:
            invalid_domains.append(domain)

    # Filtrar dominios que tengan menos de 3 letras o números antes del TLD
    domain_groups = {entry: domain for entry, domain in domain_groups.items() if has_minimum_length(domain)}

    # Ordenar dominios alfabéticamente
    grouped_domains = sorted(domain_groups.keys())

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(output_path, 'w') as f:
        f.write(f"# total dominios bloqueados: {len(grouped_domains)}\n")
        f.write(f"# {link_comment}\n")
        f.write("# proyecto creado con la finalidad de aumentar la seguridad en la navegación en latinoamérica.\n")
        f.write("# este archivo bloquea dominios phishing, fake news, apuestas, pornografía.\n")
        f.write(f"# elaboración: {current_datetime}\n")
        f.write("###################\n")
        for domain in grouped_domains:
            f.write(f"{domain}\n")

    # Mostrar estadísticas en la terminal
    print(f"\033[32m--> Proceso completado. El archivo adblock se ha guardado en '{output_path}'.\033[0m")
    print(f"\033[34m   Total de dominios ingresados: {len(domains)}\033[0m")
    print(f"\033[34m   Total de dominios únicos agrupados: {len(grouped_domains)}\033[0m")
    print(f"\033[34m   Reducción de entradas: {len(duplicate_domains) + len(invalid_domains) + len(false_positives)}\033[0m")

    # Mostrar dominios inválidos, duplicados y falsos positivos
    if invalid_domains:
        print(f"\033[31m   Dominios inválidos eliminados ({len(invalid_domains)}):\033[0m")
        for domain in invalid_domains:
            print(f"      - {domain}")

    if duplicate_domains:
        print(f"\033[33m   Dominios duplicados eliminados ({len(duplicate_domains)}):\033[0m")
        for domain in duplicate_domains:
            print(f"      - {domain}")

    if false_positives:
        print(f"\033[35m   Posibles falsos positivos eliminados ({len(false_positives)}):\033[0m")
        for domain in false_positives:
            print(f"      - {domain}")

def main():
    parser = argparse.ArgumentParser(description='Script para generar listas de Adblock a partir de dominios proporcionados.')
    parser.add_argument('output_file', nargs='?', default="adblock", help='Archivo de salida (por defecto: adblock)')
    args = parser.parse_args()

    output_path = os.path.abspath(args.output_file)

    print("Introduce los dominios que deseas procesar (uno por línea). Escribe 'done' para terminar:")
    domains = []
    while True:
        try:
            domain = input().strip()
            if domain.lower() == 'done':
                break
            domains.append(domain)
        except EOFError:
            break

    download_and_process(domains, output_path, link_comment, download_url)

if __name__ == "__main__":
    main()
