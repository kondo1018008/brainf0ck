# -*- coding: utf-8 -*-


"""
BrainF0ck 仕様
1,配列は0～29999の範囲の30000バイト配列
2,配列の要素値は0で初期化されている
3,ポインタ位置は最初、配列の先頭にある

参考: http://hakugetu.so.land.to/program/brainfuck/1-1.php
"""

import sys #この行を消すとなぜか動かなくなる()

# メイン関数
if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    with open(path) as f:
        bf = f.read()
    bf_code = list(bf)#bfのコードを1文字ずつリストにしたもの
    ptr = 0 #ポインタ
    bf_out = [0 for i in range(3000)]#bf出力用リスト
    i = 0 #bf_codeのインデックス用

    while i < len(bf_code):
        if bf_code[i] == '>':
            ptr+=1
        elif bf_code[i] == '<':
            ptr-=1
        elif bf_code[i] == '+':
            bf_out[ptr] += 1
        elif bf_code[i] == '-':
            bf_out[ptr] -= 1
        elif bf_code[i] == '.':
            print(chr(bf_out[ptr]), end="")
        elif bf_code[i] == ',':
            bf_out[ptr] = ord(sys.stdin.buffer.read(1))
        elif bf_code[i] == '[':
            if bf_out[ptr] == 0:
                d = 1
                while d != 0:
                    i += 1
                    if i == len(bf_code):
                        print("構文エラー")
                        sys.exit(1)
                    if bf_code[i] == '[':
                        d += 1
                    elif bf_code[i] == ']':
                        d -= 1
        elif bf_code[i] == ']':
            if bf_out[ptr] != 0:
                d = 1
                while d != 0:
                    i -= 1
                    if i < 0:
                        print("構文エラー")
                    if bf_code[i] == ']':
                        d += 1
                    elif bf_code[i] == '[':
                        d -= 1
        else:
            pass #><[],.+-以外は全てコメントアウトになる
        i += 1
