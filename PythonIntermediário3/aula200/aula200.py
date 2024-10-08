# type: ignore
# PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# Raiz da pasta
PASTA_RAIZ = Path(__file__).parent

# Pasta aonde esta os documentos
ORIGINAIS = PASTA_RAIZ / 'pdfsaula200'

# Cria uma pasta nova
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

# Caminho do arquivo
RELATORIO_BACEN = ORIGINAIS / 'R20240322.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print()

page0= reader.pages[0]
image0 = page0.images[0]
# print(page0.extract_text())
# with open(PASTA_NOVA / page0.images[0].name, 'wb') as fp:
#     fp.write(image0.data)

# writer = PdfWriter()

# with open(PASTA_NOVA / 'NOVO_PDF.pdf','wb') as fp:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(fp)
        
# with open(PASTA_NOVA / 'NOVO_PDF.pdf','wb') as fp:
# writer.write(fp)

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(PASTA_NOVA / f'page{i}.pdf','wb') as fp:
#         writer.add_page(page0)
#         writer.write(fp)

merger = PdfMerger()

files = [
    PASTA_NOVA / 'page0.pdf'
    PASTA_NOVA / 'page1.pdf'
]

for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()