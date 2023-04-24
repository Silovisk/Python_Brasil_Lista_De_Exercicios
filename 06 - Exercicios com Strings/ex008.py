import re
import unidecode

palavras = [    
    "A base do teto desaba.",
    "A cara rajada da jararaca.",
    "Acuda cadela da Leda caduca.",
    "A dama admirou o rim da amada.",
    "A Daniela ama a lei? Nada!",
    "Adias a data da saída.",
    "A diva em Argel alegra-me a vida.",
    "A droga do dote é todo da gorda.",
    "A gorda ama a droga.",
    "A grama é amarga.",
    ]

for p in palavras:
    p = unidecode.unidecode(p)  # Saneamento nos acentos remove acentos das letras
    p = re.sub(r"[^a-zA-Z0-9]", "", p).upper().strip()  # a-zA-Z0-9 representa que a string só pode ter letras
    # pequenas, maiúsculas e dígitos numéricos

    if p == p[::-1]:
        print(f"{p} E um Palindrodmo")
    else:
        print(f"{p} Nao e um Palindrodmo")

