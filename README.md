# Repositório de Teste - Estratégia de Branching Git

Este é um repositório de teste criado para demonstração da estratégia de branching do Git da bazar

## Estratégia de Branching

### Fluxo de trabalho para features

1. **Criar feature branch a partir de main:**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature
   ```

2. **Desenvolver e fazer commits:**
   ```bash
   git commit -m "feat: descrição da mudança"
   ```

3. **Fazer push da feature:**
   ```bash
   git push origin feature
   ```

4. **Merge em develop (deploy automático):**
   ```bash
   git checkout develop
   git pull origin develop
   git merge feature
   git push origin develop  # -> deploy automático
   ```

5. **Pull Request para main (code review):**
   - Criar PR: `feature` → `main`
   - Code review
   - Após aprovação, merge em `main` → deploy automático

### Resumo do fluxo

```
main (produção)
  ↓
feature (desenvolvimento)
  ↓
develop (deploy automático) + PR → main (code review → deploy)
```

## Estrutura de branches

- **main**: Branch principal (produção) - deploy automático após merge
- **develop**: Branch de desenvolvimento - deploy automático após push
- **feature/***: Branches de features individuais

## Comandos úteis

### Ver estrutura de branches
```bash
./show-branches.sh
```

### Ver histórico visual
```bash
git log --oneline --graph --all --decorate
```

## CI/CD

O workflow do GitHub Actions está configurado para:
- Disparar em push para `develop` → deploy automático
- Disparar quando uma release é criada

Veja `.github/workflows/ci.yml` para mais detalhes.

