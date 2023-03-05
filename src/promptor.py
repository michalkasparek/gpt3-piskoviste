import openai as ai
import pandas as pd

def ucet(znaku):
    cena = 0.02
    kurz = 22.17
    tokenu = znaku / 1.89494163
    ucet = tokenu / 1000 * cena * kurz
    ucet = round(ucet, 2)
    return ucet

def promptor(instrukce1, zanr, uryvek, instrukce2, stop, temperature, frequency_penalty, presence_penalty, max_tokens, engine, print=False):
    
    prompt = instrukce1 + "\n\n" + zanr + "=\"\"\"" + uryvek + "\"\"\"" + "\n\n" + instrukce2
    
    completions = ai.Completion.create(
        engine=engine,
        temperature=temperature,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=stop,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    completion = completions.choices[0].text

    if print:
        print(completion)

    return [uryvek, instrukce1, instrukce2, completion, stop, engine, temperature, frequency_penalty, presence_penalty, max_tokens, zanr, pd.to_datetime("today").strftime("%Y-%m-%d")]

def frejm(seznam):
    return pd.DataFrame([seznam], columns=["uryvek","instrukce1","instrukce2","completion","stop","engine","temperature","frequency_penalty","presence_penalty","max_tokens", "zanr", "datum"])
