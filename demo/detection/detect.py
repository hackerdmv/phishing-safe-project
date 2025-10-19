#!/usr/bin/env python3
"""
detect.py — heurística simples para pontuar URLs suspeitas.

Uso:
  python3 detect.py "http://exemplo.com/login" "https://192.168.0.1/mal" ...
"""
import sys
import re
from urllib.parse import urlparse

def score_url(url):
    score = 0
    u = urlparse(url)
    host = u.hostname or ""
    path = u.path or ""
    # heurística 1: host é um IP (sinal de alerta)
    if re.match(r'^\d+\.\d+\.\d+\.\d+$', host):
        score += 30
    # heurística 2: domínio muito longo ou com hífens excessivos
    if host.count('-') >= 2:
        score += 15
    # heurística 3: muitos subdomínios (ex: a.b.c.d.e)
    if host.count('.') >= 3:
        score += 10
    # heurística 4: path com parâmetros longos
    if len(u.query) > 40:
        score += 10
    # heurística 5: domínio usa punycode (xn--) — possível homograph
    if host.startswith('xn--') or 'xn--' in host:
        score += 25
    # heurística 6: domínio contém palavras como "login", "account" combinadas com outros sinais
    if re.search(r'login|signin|account|secure', host+path, re.I):
        score += 8
    # heurística 7: TLDs pouco comuns (exemplo simplificado)
    if host.endswith('.tk') or host.endswith('.pw'):
        score += 15
    return score

def label(score):
    if score >= 50:
        return 'ALTO (provável phishing)'
    if score >= 25:
        return 'MÉDIO (suspeito)'
    if score >= 10:
        return 'BAIXO (possível)'
    return 'BAIXÍSSIMA (pouco suspeito)'

def main(urls):
    for url in urls:
        s = score_url(url)
        print(f'{url} -> Score: {s} -> {label(s)}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 detect.py <url1> <url2> ...")
    else:
        main(sys.argv[1:])
