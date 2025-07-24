# Tipos Python ↔ JavaScript

Uma tabela comparando os tipos de dados mais comuns entre Python e JavaScript.

| Python         | JavaScript               | Descrição                                                                 |
|----------------|--------------------------|---------------------------------------------------------------------------|
| `int`          | `number`                 | Números inteiros (`1`, `-5`, etc.)                                       |
| `float`        | `number`                 | Números de ponto flutuante (`3.14`, `-0.5`)                              |
| `bool`         | `boolean`                | Valores booleanos (`True`, `False`) ↔ (`true`, `false`)                  |
| `str`          | `string`                 | Texto (`"hello"`)                                                        |
| `list`         | `Array`                  | Lista ordenada de elementos (`[1, 2, 3]`) ↔ (`[1, 2, 3]`)                |
| `tuple`        | `Array` (imutável: não tem) | Tupla imutável (`(1, 2, 3)`), mas JS não tem equivalente nativo imutável |
| `dict`         | `Object`                 | Dicionário (`{"a": 1, "b": 2}`) ↔ (`{ a: 1, b: 2 }`)                      |
| `set`          | `Set`                    | Conjunto de elementos únicos                                             |
| `None`         | `null` / `undefined`     | Ausência de valor                                                        |
| `bytes`        | `Uint8Array` / `Buffer`  | Sequência de bytes                                                       |
| `complex`      | —                        | Números complexos não têm tipo nativo em JS                              |
| `range`        | `Array.from({length: N})`| Intervalo iterável (`range(5)` ↔ `[0,1,2,3,4]`)                          |
| `function`     | `function`               | Funções são objetos de primeira classe em ambas                          |
| `class`        | `class`                  | Definição de tipos personalizados                                        |
| `object`       | `Object`                 | Qualquer valor customizado / instância                                   |
| `type()`       | `typeof` ou `instanceof` | Usado para verificar tipos                                               |
| `any` (tipagem) | `any` (TypeScript)       | Representa qualquer tipo                                                 |

---

## Obs

- `tuple` não tem um equivalente exato em JS, mas você pode usar `Object.freeze([1, 2, 3])` para simular uma tupla imutável.
- `dict` em Python aceita qualquer tipo como chave. Em JS, apenas strings e symbols são válidas como chaves de objetos — para chaves mais complexas, use `Map`.
- `set` é mais comum em Python. Em JS, o `Set` é mais recente e menos comum em código legado.
- `None` do Python é similar a `null` do JS. `undefined` é um valor "ausente" específico do JavaScript.
- Python não tem `undefined`; JavaScript não tem `None`.

---

Se quiser, posso gerar um guia de **exemplos lado a lado** mostrando como converter valores ou estruturas de uma linguagem para outra.


# 🐍 Tipos de Dados em Python — Tabela com Detalhes

| Tipo Python   | Exemplo            | Descrição                                                                 | Comparação com JS                      |
|---------------|--------------------|---------------------------------------------------------------------------|----------------------------------------|
| `int`         | `5`, `-10`, `0`    | Número inteiro de precisão ilimitada                                      | `number` em JS                         |
| `float`       | `3.14`, `-0.5`     | Número de ponto flutuante com precisão limitada (IEEE 754)                | `number` em JS                         |
| `bool`        | `True`, `False`    | Subclasse de `int`; `True == 1`, `False == 0`                             | `boolean` em JS                        |
| `str`         | `"hello"`          | Texto imutável com suporte a f-strings e slicing                          | `string` em JS                         |
| `list`        | `[1, 2, 3]`         | Lista ordenada e mutável, aceita tipos mistos                             | `Array` em JS                          |
| `tuple`       | `(1, 2, 3)`        | Lista imutável, útil para retornos múltiplos                              | Não possui equivalente direto          |
| `dict`        | `{"a": 1}`         | Mapeamento chave-valor; chaves imutáveis                                  | `Object` ou `Map` em JS                |
| `set`         | `{1, 2, 3}`        | Conjunto de elementos únicos e não ordenados                              | `Set` em JS                            |
| `None`        | `None`             | Representa ausência de valor                                              | `null` ou `undefined` em JS            |
| `bytes`       | `b"hello"`         | Sequência imutável de bytes                                               | `Uint8Array`, `Buffer` em Node.js      |
| `complex`     | `2 + 3j`           | Número com parte real e imaginária                                        | Não possui equivalente nativo          |
| `range`       | `range(5)`         | Intervalo preguiçoso, ideal para laços                                    | `Array.from({length: N}, (_, i) => i)` |
| `object`      | —                  | Base de todos os tipos Python                                             | `Object` em JS                         |
| `class`       | `class MinhaClasse`| Definição de tipos personalizados, suporta OOP                            | `class` em JS                          |
| `type()`      | `type(x)`          | Retorna o tipo do valor                                                   | `typeof`, `instanceof` em JS           |
| `function`    | `def x():`         | Funções são objetos de primeira classe                                    | `function` em JS                       |

---

## 📝 Notas:
- **Tuples** podem ser simuladas em JS com `Object.freeze([1, 2, 3])` para imutabilidade.
- **Dict** permite chaves de qualquer tipo imutável; em JS, apenas `string` e `symbol` são válidas como chaves de `Object`.
- **None** em Python é próximo de `null` em JS, mas Python **não tem** `undefined`.
- Para verificação de tipos em Python, prefira `isinstance(x, tipo)` ao invés de `type(x) == tipo`.

IEEE 754 (Institute of Electrical and Electronics Engineers Standard 754) é um padrão que define como representar números de ponto flutuante binários (como 3.14, -0.5, 1e10) na memória do computador, garantindo portabilidade, precisão e previsibilidade entre diferentes sistemas e linguagens.

## Sobre tuplas
Funções Python podem retornar múltiplos valores com facilidade usando tuplas.
Se preciso agrupar valores que não deveriam mudar, a tupla deixa isso claro no próprio código.
Pode ser usado como chave de dict ou em set

### Segurança
Garante que os dados não serão modificados acidentalmente
Permite o uso como chaves em dicionários (dict)
Ajuda a escrever funções mais previsíveis e confiáveis

### Performance
Tuplas são mais rápidas e mais leves que listas, pois:
Usam menos memória
São otimizadas internamente pelo interpretador
Podem ser usadas como constantes

```python 

(x, y) → ponto no plano
(nome, idade) → registro simples
(soma, media) → múltiplos retornos de função
```


