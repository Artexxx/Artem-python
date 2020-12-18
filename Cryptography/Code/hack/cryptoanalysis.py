"""
Частотный криптоанализ помогает дешифровать сообщения, которые были зашифрованы при помощи простого шифра замены
"""

print('''
\t\t A = 8.17% \t N = 6.75% 
\t\t B = 1.49% \t O = 7.51%  
\t\t C = 2.78% \t P = 1.93%
\t\t D = 4.25% \t Q = 0.10%
\t\t E = 12.7% \t R = 5.99%
\t\t F = 2.23% \t S = 6.33%
\t\t G = 2.02% \t T = 9.06% 
\t\t H = 6.09% \t U = 2.76%
\t\t I = 6.97% \t V = 0.98%
\t\t J = 0.15% \t W = 2.36% 
\t\t K = 0.77% \t X = 0.15%
\t\t L = 4.03% \t Y = 1.97%
\t\t M = 2.41% \t Z = 0.05%
''')

text = input("Text: ")
dict = [i for i in set(text) if i not in " \n"]

print("[*] Result: ")
for index, symbol in enumerate(dict):
    stat = 100 * text.count(symbol) / len(text)
    if index % 2 == 0:
        print("\t{} - {:.3}%".format(symbol, stat), end="\t\t")
    else:
        print("{} - {:.3}%".format(symbol, stat))
