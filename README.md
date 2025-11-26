# Repositório de Teste - Estratégia de Branching Git

Este é um repositório de teste criado para demonstração de estratégias de branching do Git.

## Como usar

Sinta-se à vontade para:
- Criar branches
- Fazer merges
- Testar diferentes estratégias
- Experimentar comandos Git
- Fazer rebase
- Resolver conflitos

## Estrutura inicial

O repositório já vem com alguns branches e commits de exemplo:

- **main**: Branch principal (produção)
- **develop**: Branch de desenvolvimento
- **feature/nova-funcionalidade**: Branch de feature em desenvolvimento
- **hotfix/correcao-urgente**: Branch de hotfix

## Comandos úteis

### Ver estrutura de branches
```bash
./show-branches.sh
```

### Ver histórico visual
```bash
git log --oneline --graph --all --decorate
```

### Criar um novo branch de feature
```bash
git checkout -b feature/nome-da-feature
```

### Criar um novo branch de hotfix
```bash
git checkout -b hotfix/nome-do-hotfix
```

### Fazer merge de uma feature
```bash
git checkout develop
git merge feature/nova-funcionalidade
```

## Estratégias de Branching

Este repositório demonstra o modelo **Git Flow**:
- `main`: código em produção
- `develop`: branch de desenvolvimento
- `feature/*`: novas funcionalidades
- `hotfix/*`: correções urgentes
- `release/*`: preparação para release (pode ser criado conforme necessário)

