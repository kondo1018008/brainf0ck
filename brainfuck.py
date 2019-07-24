# -*- coding: utf-8 -*-
import sys

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
                count = 1
                while count != 0:
                    i += 1
                    if i == len(bf_code):
                        print("構文エラー")
                        sys.exit(1)
                    if bf_code[i] == '[':
                        count += 1
                    elif bf_code[i] == ']':
                        count -= 1
        elif bf_code[i] == ']':
            if bf_out[ptr] != 0:
                count = 1
                while count != 0:
                    i -= 1
                    if i < 0:
                        print("構文エラー")
                    if bf_code[i] == ']':
                        count += 1
                    elif bf_code[i] == '[':
                        count -= 1
        else:
            pass
        i += 1