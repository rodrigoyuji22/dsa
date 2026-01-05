class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        _map = {}
        output = []
        for i in range(len(nums)):
            if nums[i] not in _map:
                _map[nums[i]] = 1
            _map[nums[i]] += 1
        
        for i in range(k):
            number = max(_map, key=_map.get)  # pyright: ignore[reportCallIssue, reportArgumentType]
            output.append(number)
            del _map[number]
        return output
    '''
    Abordagem:
        Criar um hashmap para anotar as frequencias dos numeros e retornar os k que mais aparecem
    
    Observações:
        - Na função max() passo o _map como iterável para procurar o maior e uso o método key para
    definir qual é o critério, que no caso é o value da chave, pois _map.get vai retornar o value
    da chave.
        - Após encontrar a key com maior value e appendar no output, removo do hashmap para evitar que
    a próxima a ser appendada em output seja a segunda maior frequencia.
    '''