## TurtleBot 3: Configurando o Ambiente

Já tendo o ambiente do ROS configurado, basta acessar o repositório do **TurtleBot 3** no Git (https://github.com/ROBOTIS-GIT/turtlebot3/tree/master) e clonar o repositório dentro da pasta *source* do *catkin workspace*.

> `$ cd catkin_ws/src`
>
> `$ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git`

Não se esqueça de selecionar o branch compatível com a distribuição do ROS instalada. Neste caso:

> `$ cd turtlebot3`
>
> `$ git checkout noetic-devel`

Além disso, é preciso instalar o pacote de mensagens (https://github.com/ROBOTIS-GIT/turtlebot3_msgs) e simulações (https://github.com/ROBOTIS-GIT/turtlebot3_simulations). Repita os passos acima, sempre instalando em `catkin_ws/src/`, e com a distro do ROS correta.

Agora, retorne ao *workspace*, execute o comando *make* para gerar as dependências necessárias do projeto, o *script* de configuração e selecione o modelo de simulação desejado.

> `$ cd ~user/catkin_ws`
>
> `$ catkin_make`
> 
> `$ source devel/setup.bash`
> 
> `$ export TURTLEBOT3_MODEL=burger`

Um passo opcional é configurar o *bash* para configurar o ambiente ambiente automaticamente sempre que uma nova instância do terminal for aberta. Abra o arquivo

> `$ vim .bashrc`

e acrescente, ao fim, as linhas

> `cd catkin_ws`
>
> `source devel/setup.bash`
>
> `export TURTLEBOT3_MODEL=burger`

Lembrando que o vim tem alguns comandos diferentes:

- **i** insere texto antes do cursor;
- **a** adiciona texto após o cursor;
- **esc** retorna ao modo de comandos;
- **:wq** salva e sai.

<hr>

## O Burger em Mundo Aberto

Tendo o ambiente configurado, agora basta lançar a aplicação do **turtlebot3_gazebo** com o ambiente de simulação desejado. Neste exemplo, será utilizado o mundo aberto.

> `$ roslaunch turtlebot3_gazebo turtlebot3_emty_world.launch`

Para efeitos de curiosidade, dê uma olhada nos tópicos ativos em um novo terminal, lançados pela simulação.

> `$ rostopic list`

Para controlar o robô, antes de mais nada, vá no gazebo e insira qualquer objeto no mapa (será mais fácil de ver o deslocamento tendo um referencial).

Feito isso, publique uma mensagem no tópico `cmd_vel`, que comanda a velocidade do robô. Ao começar a digitar o comando e dar duplo *tab*, o auto-completar do terminal já informa o formato da mensagem.

> `$ rostopic pub cmd_vel geometry_msgs/Twist "
linear: 
   x: 0.2 
   y: 0.0
   z: 0.0
angular:
   x: 0.0
   y: 0.0
   z: 0.5
"`

Uma outra forma (bem melhor) de controlar o **Burger** é chamando a aplicação de **Teleop**, que captura as teclas (W/A/S/D/X) e publica o comando no tópico `cmd_vel`. Para executar essa aplicação, digite

> `$ roslaunch turtlebot3_teleop turtlebot3_tele_key.launch`

<hr>

## O Waffle Escaneando a Casa

Agora, vamos testar o modelo **Waffle** em um mapa elaborado, experimentar a câmera do robô em ação.

> `$ export TURTLEBOT3_MODEL=waffle`
>
> `$ roslaunch turtlebot3_gazebo turtlebot3_house.launch`

Em um novo terminal, abra o programa e visualização gráfica dos tópicos.

> `$ rosrun rviz rviz`

Então clique em `Add`, filtre por tópicos e selecione

> `/camera/depth/image_raw/Image`

Após uns instantes de inicialização, irá aparecer a imagem capturada pela câmera do *waffle*. Experimente executar o *teleop* para mover o robô e explorar a casa.

<hr>