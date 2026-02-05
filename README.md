# 🔥 The Grind - Log de Estudos

Sistema para registrar e acompanhar minhas horas de estudo diárias desenvolvido durante minha jornada de aprendizado em Python.

## 📌 Sobre o Projeto

Este é um projeto de aprendizado prático! Estou construindo este sistema enquanto aprendo programação, e ele me ajuda a:
- 📝 Registrar minhas horas de estudo diárias
- 📊 Acompanhar minha evolução e estatísticas
- 🎯 Definir e acompanhar metas diárias
- ⚠️ Identificar dias que esqueci de registrar

## 🚀 Funcionalidades

- ✅ Registrar estudo do dia atual
- ✅ Registrar dias passados que ficaram faltando
- ✅ Ver relatório completo com estatísticas
- ✅ Definir metas para o próximo dia
- ✅ Detectar automaticamente dias não registrados
- ✅ Três tipos de status: Estudado, Não Estudado, Justificado

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **JSON** - Armazenamento de dados
- **datetime** - Manipulação de datas e horários
- **Git/GitHub** - Controle de versão

## 📊 O Que Aprendi Construindo Este Projeto

- Manipulação de arquivos JSON (leitura e escrita)
- Trabalho com datas em Python (`datetime`, `strftime`, `strptime`, `timedelta`)
- Estruturas de dados (dicionários e listas)
- Funções e modularização de código
- Loops (`for` e `while`)
- Condicionais (`if`, `elif`, `else`)
- Tratamento de dados do usuário (`input`, validações)
- Persistência de dados em arquivos
- Controle de versão com Git

## 💻 Como Usar

### Pré-requisitos
- Python 3.x instalado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/log-de-estudos.git
cd log-de-estudos
```

2. Execute o programa:
```bash
python estudos_v2_com_dias_passados.py
```

### Uso

O programa apresenta um menu interativo com as seguintes opções:

1. **Registrar/Atualizar Estudo de Hoje** - Registra suas horas do dia atual
2. **Registrar Dia Passado** - Permite registrar dias que você esqueceu
3. **Ver Histórico/Relatório** - Mostra estatísticas completas
4. **Planejar Meta para Amanhã** - Define sua meta para o próximo dia
5. **Sair** - Fecha o programa

## 📂 Estrutura de Dados

O programa salva os dados em formato JSON (`estudos.json`):

```json
{
    "estudos": [
        {
            "data": "05/02/2026",
            "status": "Estudado",
            "horas": 3.5,
            "meta_amanha": "4 horas de Python e algoritmos"
        }
    ]
}
```

## 📈 Estatísticas Disponíveis

- **Total de horas estudadas**
- **Número de dias registrados**
- **Média diária de horas**
- **Dia com recorde de horas**
- **Contagem por status** (Estudado, Não Estudado, Justificado)
- **Detecção de dias faltantes**

## 🎯 Próximos Passos / Melhorias Planejadas

- [ ] Adicionar gráficos de progresso semanal/mensal
- [ ] Exportar relatórios em PDF
- [ ] Interface gráfica (GUI) com Tkinter
- [ ] Categorias de estudo (Python, Git, Algoritmos, etc.)
- [ ] Backup automático na nuvem
- [ ] Notificações de lembrete
- [ ] Análise de produtividade (melhores dias/horários)

## 🤝 Contribuições

Este é um projeto de aprendizado pessoal, mas sugestões e feedback são sempre bem-vindos! 

Se você também está aprendendo Python, sinta-se livre para:
- Fazer fork do projeto
- Propor melhorias
- Reportar bugs
- Compartilhar ideias

## 📝 Licença

Este projeto está sob a licença MIT - sinta-se livre para usar e modificar.

## 👨‍💻 Autor

**[Luis Henrique]** - Estudante de Programação

- GitHub: [@louishb7](https://github.com/louishb7)

---

⭐ Se este projeto te ajudou de alguma forma, considere dar uma estrela!

**Feito com 💪 e muito ☕ durante minha jornada de aprendizado**
