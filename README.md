1. Simular cadastro e Login com Hash + Salt (senha.py)
passos: 
   Criar uma hash(dicionario em python) para armazenar usuarios e seus hashes

   Usar hashlib para gerar o hash da senha concatenada com o salt

   No login, verificar se o hash gerado bate com o armazenado


No meu código, a Hash Table está representada pelo dicionário self.usuarios. Cada e-mail funciona como chave única, permitindo que o sistema acesse rapidamente os dados do usuário sem precisar percorrer toda a lista. Isso demonstra como a Hash Table é aplicada na prática para garantir eficiência e segurança no gerenciamento de logins.

2. Git simplificado
Objetivo: simular versionamento de arquivos.

Passos:

    Criar função que recebe o conteúdo de um arquivo e gera um hash.

    Usar a Hash Table para armazenar versões com seus respectivos hashes


Aqui a Hash Table aparece no dicionário self.commits. Cada commit é indexado pelo seu hash, funcionando como chave única. Isso permite que o sistema acesse rapidamente qualquer commit sem precisar percorrer todos os registros, simulando como o Git real organiza versões de arquivos. O uso da Hash Table garante eficiência e integridade, já que cada hash identifica de forma única o estado do repositório.



3. Blockchain simplificada
Objetivo: criar blocos encadeados com hash anterior.

Passos:

     Cada bloco guarda dados, hash atual e hash do bloco anterior.

     Alterar um bloco inicial quebra a cadeia.


Neste código, a Hash Table aparece de forma conceitual: cada bloco é identificado por um hash único, que funciona como chave de integridade. O encadeamento de hash_atual e hash_anterior garante que qualquer alteração em um bloco invalide toda a cadeia. Assim, o blockchain simula uma Hash Table distribuída, onde os hashes são usados para indexar e validar os dados.



-- A ideia central da atividade foi mostrar que a Hash Table não serve apenas para armazenar pares chave-valor, mas também pode ser aplicada em cenários de segurança e controle de integridade. Na parte das senhas, ela garante que cada usuário tenha seu hash único com salt, dificultando ataques. No Git simplificado, a tabela organiza versões de arquivos e seus hashes, permitindo identificar alterações. Já no blockchain, mesmo sem usar uma tabela explícita, o conceito de encadeamento de hashes funciona como uma estrutura que assegura consistência dos dados. Assim, a Hash Table aparece como um recurso versátil, que conecta criptografia, versionamento e integridade de blocos. --
