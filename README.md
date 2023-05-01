# pfsw-multicalendar
> Projeto demo de aplicação de multi calendário. 
>
> Este projeto é referente ao back-end, realizado com Python + FastAPI.
>
> Ref a conexão e base de dados, foram feitas usando SQLAlchemy e MySQL.
>
> Posteriomente será realizado um projeto front-end utilizando vueJs + Vite.


---

## Utilização:
Nos arquivos clonados contém os arquivos dockerfile e docker-compose.yaml, então como pré-requisito é necessário que tenha a instalação do docker.
> Caso não tenha o docker instalado, pode ser realizado seguindo a seguinte documentação: [Windows](https://docs.docker.com/desktop/install/windows-install/) e [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Para execução dos containers referentes à aplicação, guie-se pelos seguintes passos:
1. Abra o shell do seu sistema operacional
2. Faça o comando ```cd {local_do_clone}```.
3. Execute: ```docker-compose up```

Será executado uma stack container na seguinte estrutura:
- pfsw-multicalendar
    - webservice-1
    - database-1

Ao executar o comando ```docker ps```, encontrará os seguintes containers:
- pfsw-multicalendar-webservice-1
- pfsw-multicalendar-database-1

--- 
## Inicializando o banco de dados:
Aguarde o comando ```docker-compose up``` finalizar o processo.
Seu console ficará bloqueado exibindo o log de todos os containers da stack.

Abra outro console, execute o seguinte comando:
```sh
docker exec -it pfsw-multicalendar-database-1 mysql -u application -p
```
Insirá a senha contida no arquivo docker-compose.yaml

Neste ponto, estara logado na base de dados.

Execute o comando ```use multicalendar;``` e posteriormente copie e cole o arquivo contido em ***src/database/ddl/pfsw-multicalendar.sql*** no console mysql.

Após isso, digite ***exit*** no terminal.

---

## Agora é só brincar!

Para acessar a documentação, basta acessar o navegador no endereço ```http://localhost:8080/documentation```

Ajude-me a criar uma aplicação API para a comunidade, principalmente para os iniciantes terem um caso de uso concreto em um exemplo complexo.