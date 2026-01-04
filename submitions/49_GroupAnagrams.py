from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        _map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            _map[str(count)].append(word)
        return list(_map.values())
        
        '''
        Abordagem:
            Criar um contador de frequencia por meio do alfabeto e do ASCI, que será a key
        do dict e o value será um array contendo as strings que tiverem a mesma frequencia das letras.
        Por fim retornar as values que serão as listas das strings que possuem tal frequência.
        
        Observações: 
            - Uso do defaultdict para que os valores das chaves seja por padrão uma lista vazia, assim posso appendar
        na lista as strings no momento em que instancio uma key, caso contrário seria necessário criar a key caso ela não exista
        e iniciar uma lista vazia como value
            - Uma array não pode ser a key de um dicionário pois é mutável, então transformo essa array em uma
        string ou poderia transformar em uma tupla que é uma estrutura imutável também.
            - Complexidade temporal de O(m * n) sendo m = qtd de palavras e n = maior qtd de letras de uma string
        '''
        
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        _map = defaultdict(list)
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            _map[key].append(strs[i])
        return list(_map.values())
        '''
        Abordagem: 
            Criar um hashmap que vai armazenar como key a string de forma ordenada, assim todos os anagramas
        vão resultar na mesma string se ordenada, por exemplo ['eat', 'ate'] ambos se ordenados são 'aet' então
        é um anagrama. Vou armazenar as strings que formam essa string ordenada em uma lista assim como a abordagem anterior
        
        Observações:
            - Essa implementação resultada em uma complexidade temporal de O(m * nlogn)
            
        '''