#!/usr/bin/env python

import sys
from Bio import SeqIO

fasta_in = sys.argv[1] #fastaファイルを読みこみ
search = sys.argv[2]  #抽出したい文字列(一つだけしか指定できない)
l = 0

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

    if search in desc_part:
        print('id:', id_part)
        print('desc:', desc_part)
        print('seq:', seq)
    
#結果をファイルに保存したい場合はリダイレクトを使う

#コマンドプロンプトでの例
#python fasta_extraction.py fasta_extraction arsa_result.fasta palmata > res.fasta



