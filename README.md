MyPath - Log de Estudos
Sistema em Python para registrar e acompanhar horas de estudo diárias.

Sobre:
Projeto criado como parte do meu aprendizado em programação. Permite registrar estudos, acompanhar estatísticas e identificar dias não registrados.

Funcionalidades
-> Registrar estudo do dia atual
-> Registrar dias passados
-> Ver relatório com estatísticas

Como usar:
- > Clone o repositório: git clone https://github.com/louishb7/log-de-estudos.git
cd log-de-estudos

Execute o programa:
-> python estudos_v2_com_dias_passados.py

Estrutura de dados
-> Os registros são salvos em estudos.json no formato:

json
{
  "estudos": [
    {
      "data": "05/02/2026",
      "status": "Estudado",
      "horas": 3.5,
      "meta_amanha": "4 horas de Python"
    }
  ]
}