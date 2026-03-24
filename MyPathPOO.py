import json
import os
from datetime import datetime, timedelta


class Estudo:
    def __init__(self, data: str, status: str, horas=0, justificativa=""):
        """
        => Inicializa um novo registro de estudo.
        """
        self.data = data
        self.status = status
        self.horas = horas
        self.justificativa = justificativa

    def to_dict(self):
        """ "
        => Converte o objeto Estudo em um dicionário para transformar em JSON.
        => Retorna um dicionário com os dados do estudo.
        """
        return {
            "data": self.data,
            "status": self.status,
            "horas": self.horas,
            "justificativa": self.justificativa,
        }


class GerenciadorEstudos:
    """
    => Classe que gerencia e conecta funções.
    """

    def __init__(self, arquivo="estudos.json"):
        """
        => Inicializa o gerenciador e carrega os dados.
        """
        self.arquivo = arquivo
        self.estudos = self.carregar_dados()

    def carregar_dados(self):
        """
        =>Lê o arquivo JSON e transforma os dados em umma lista de objetos Estudo.

        """
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                return [Estudo(**log) for log in dados["estudos"]]
        return []

    def salvar_dados(self):
        """
        => Serializa a lista de objeto e salva no arquivo JSON.
        """
        dados = {"estudos": [est.to_dict() for est in self.estudos]}
        with open(self.arquivo, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)

    def registrar_estudo(
        self, data: str, status: str, horas=0, justificativa=""
    ):
        """
        => Cria um novo registro de estudo e adiciona à lista.
        => Se já existir um registro para a mesma data, atualiza os dados.
        """

        existente = next(
            (est for est in self.estudos if est.data == data), None
        )

        if existente:
            existente.status = status
            existente.horas = horas
            existente.justificativa = justificativa
        else:
            novo = Estudo(data, status, horas, justificativa)
            self.estudos.append(novo)

        self.salvar_dados()

    def verificar_dias_faltantes(self):
        """
        => Verifica se existem dias entre o último registro e hoje que não foram registrados.
        => Retorna uma lista com as datas faltantes.
        """
        if not self.estudos:
            return []

        registros_ordenados = sorted(
            self.estudos,
            key=lambda est: datetime.strptime(est.data, "%d/%m/%Y"),
        )

        ultimo_registro = registros_ordenados[-1]
        data_ultimo = datetime.strptime(ultimo_registro.data, "%d/%m/%Y")
        hoje = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        dias_faltantes = []
        data_atual = data_ultimo + timedelta(days=1)

        while data_atual < hoje:
            data_str = data_atual.strftime("%d/%m/%Y")
            if not any(est.data == data_str for est in self.estudos):
                dias_faltantes.append(data_str)
            data_atual += timedelta(days=1)

        return dias_faltantes

    def calcular_total_horas(self):
        """
        => Soma as horas de todos os registros de estudo armazenados.
        """
        return sum(est.horas for est in self.estudos)

    def gerar_relatorio(self):
        """
        => Processa os dados para gerar estatísticas sobre o desempenho dos estudos.
        => Retorna um dicionário contendo os dados.
        """
        if not self.estudos:
            return {
                "total_horas": 0,
                "total_dias": 0,
                "media_diaria": 0,
                "recorde": (None, 0),
                "status": "Sem dados",
            }

        total_horas = self.calcular_total_horas()
        total_dias = len(self.estudos)
        media_diaria = total_horas / total_dias

        maior_dia = max(self.estudos, key=lambda est: est.horas)
        recorde = (maior_dia.data, maior_dia.horas)

        return {
            "total_horas": total_horas,
            "total_dias": total_dias,
            "media_diaria": media_diaria,
            "recorde": recorde,
        }


class Menu:
    def __init__(self, gerenciador: GerenciadorEstudos):
        self.gerenciador = gerenciador

    def exibir(self):
        while True:
            print("\n" + "=" * 40)
            print(" 🔥 MyPath - LOG DE ESTUDOS")
            print(
                f" TOTAL ACUMULADO: {self.gerenciador.calcular_total_horas()} HORAS"
            )

            faltantes = self.gerenciador.verificar_dias_faltantes()
            if faltantes:
                print(f" ⚠️  {len(faltantes)} dia(s) não registrado(s)!")

            print("=" * 40)
            print("1. Registrar/Atualizar Estudo de Hoje")
            print("2. Registrar Dia Passado")
            print("3. Ver Histórico/Relatório")
            print("4. Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                data_hoje = datetime.now().strftime("%d/%m/%Y")
                horas = float(input("Quantas horas de estudo hoje? "))
                self.gerenciador.registrar_estudo(data_hoje, "Estudado", horas)

            elif opcao == "2":
                faltantes = self.gerenciador.verificar_dias_faltantes()
                if faltantes:
                    print("\n📋 Dias não registrados:")
                    for i, dia in enumerate(faltantes, 1):
                        print(f"   {i}. {dia}")
                    escolha = input("\nEscolha o número do dia: ")
                    try:
                        idx = int(escolha) - 1
                        if 0 <= idx < len(faltantes):
                            data_registrar = faltantes[idx]
                            horas = float(
                                input(f"Quantas horas em {data_registrar}? ")
                            )
                            self.gerenciador.registrar_estudo(
                                data_registrar, "Estudado", horas
                            )
                    except ValueError:
                        print("❌ Opção inválida!")

            elif opcao == "3":
                relatorio = self.gerenciador.gerar_relatorio()
                print("-" * 40)
                print(
                    f"📊 RESUMO: {relatorio['total_horas']}h em {relatorio['total_dias']} dias."
                )
                print(f"📈 Média diária: {relatorio['media_diaria']:.2f}h")
                print(
                    f"🏆 Recorde: {relatorio['recorde'][1]}h no dia {relatorio['recorde'][0]}"
                )

            elif opcao == "4":
                print("\n👋 Até logo! Continue firme nos estudos!")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    g = GerenciadorEstudos()
    menu = Menu(g)
    menu.exibir()
