# Proposta para isolar o token dos outros programas
# É necessário rodar apenas uma vez, ou quando não tiver conexão com a IBM
from qiskit import IBMQ

apitoken = 'TOKEN'

if __name__ == "__main__":
    IBMQ.save_account(apitoken)
