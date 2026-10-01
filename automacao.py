import csv
import datetime
import os
import platform
import shutil


def criar_pastas():
	"""Garante que as pastas de log e backup existem."""
	os.makedirs("logs", exist_ok=True)
	os.makedirs("backups", exist_ok=True)


def gerar_relatorio():
	print("\n--- [AUDITORIA] Coletando informações da máquina ---")

	sistema = platform.system()
	versao = platform.release()
	nome_rede = platform.node()

	disco = shutil.disk_usage(os.path.abspath(os.sep))
	total_gb = disco.total // (2**30)
	livre_gb = disco.free // (2**30)
	porcentagem_livre = (disco.free / disco.total) * 100

	print(f"Nome do Computador: {nome_rede}")
	print(f"Sistema Operacional: {sistema} {versao}")
	print(
		f"Espaço em Disco: {livre_gb} GB livres de {total_gb} GB"
		f" ({porcentagem_livre:.2f}% livre)"
	)

	with open("logs/relatorio_maquina.txt", "w", encoding="utf-8") as arquivo:
		arquivo.write("=== RELATÓRIO DE AUDITORIA DE SUPORTE ===\n")
		arquivo.write(f"Computador: {nome_rede}\n")
		arquivo.write(f"SO: {sistema} {versao}\n")
		arquivo.write(f"Espaço Total: {total_gb} GB\n")
		arquivo.write(
			f"Espaço Disponível: {livre_gb} GB ({porcentagem_livre:.2f}%)\n"
		)

	print("[Sucesso] Relatório salvo na pasta 'logs/relatorio_maquina.txt'!")


def executar_backup():
	print("\n--- [BACKUP] Iniciando rotina de compactação ---")
	pasta_origem = input(
		"Digite o caminho da pasta que deseja fazer backup: "
	).strip()

	if not os.path.isdir(pasta_origem):
		print("[Erro] A pasta de origem informada não existe.")
		return

	data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	nome_arquivo = f"backup_{data_atual}"
	caminho_destino = os.path.join("backups", nome_arquivo)

	try:
		shutil.make_archive(caminho_destino, "zip", pasta_origem)
		print(f"[Sucesso] Backup criado em: {caminho_destino}.zip")

		with open("logs/backup_log.txt", "a", encoding="utf-8") as log:
			log.write(
				f"[{datetime.datetime.now()}] SUCESSO: Backup da pasta"
				f" '{pasta_origem}' gerado como '{nome_arquivo}.zip'\n"
			)
	except Exception as erro:
		print(f"[Erro] Falha ao realizar o backup: {erro}")


def cadastrar_usuarios():
	print("\n--- [USUÁRIOS] Cadastro em Lote via CSV ---")
	arquivo_csv = "novos_usuarios.csv"

	if not os.path.exists(arquivo_csv):
		with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
			writer = csv.writer(arquivo)
			writer.writerow(["nome", "email", "departamento"])
			writer.writerow(["João Silva", "joao.silva@empresa.com", "Suporte"])
			writer.writerow(["Maria Souza", "maria.souza@empresa.com", "Financeiro"])
		print(
			"[Info] Um arquivo 'novos_usuarios.csv' de exemplo foi gerado na raiz"
			" do projeto."
		)

	try:
		with open(arquivo_csv, "r", encoding="utf-8", newline="") as arquivo:
			leitor = csv.DictReader(arquivo)
			campos = {"nome", "email", "departamento"}
			if not campos.issubset(leitor.fieldnames or []):
				raise ValueError("O CSV deve conter nome, email e departamento.")

			print("\nProcessando cadastros...")
			for linha in leitor:
				print(
					f"-> Usuário cadastrado: {linha['nome']} ({linha['email']}) -"
					f" Depto: {linha['departamento']}"
				)
		print("[Sucesso] Todos os usuários do CSV foram processados com êxito!")
	except (OSError, csv.Error, ValueError, KeyError) as erro:
		print(f"[Erro ao processar o CSV]: {erro}")


def main():
	criar_pastas()
	while True:
		print("\n========================================")
		print("   AUTOMATOR DE SUPORTE TÉCNICO - v1.0  ")
		print("========================================")
		print("1. Gerar Relatório de Auditoria da Máquina")
		print("2. Executar Backup Compactado com Log")
		print("3. Cadastrar Usuários em Lote (CSV)")
		print("0. Sair")

		opcao = input("\nEscolha uma opção: ").strip()

		if opcao == "1":
			gerar_relatorio()
		elif opcao == "2":
			executar_backup()
		elif opcao == "3":
			cadastrar_usuarios()
		elif opcao == "0":
			print("\nSaindo do sistema. Até logo!")
			break
		else:
			print("\n[Opção Inválida] Escolha uma opção entre 0 e 3.")


if __name__ == "__main__":
	main()
0