#!/usr/bin/env python3
"""
Aplicação de exemplo para demonstração de Git branching
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo app")
    parser.add_argument("--name", help="Nome a ser saudado", default="Usuário")
    args = parser.parse_args()
    print(f"Olá, {args.name}! Bem-vindo ao repositório de teste de Git!")
    print("Mudança de versão para teste de Git Flow")
    print("Versão: 1.1.0")

if __name__ == "__main__":
    main()

