#!/bin/bash
# Script para visualizar a estrutura de branches do repositório

echo "=== Estrutura de Branches ==="
echo ""
git branch -a
echo ""
echo "=== Histórico de Commits (últimos 10) ==="
echo ""
git log --oneline --graph --all --decorate -10
echo ""
echo "=== Status Atual ==="
echo ""
git status

