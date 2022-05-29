# vvit

# Веб-приложение с нейросетью для детектирования СИЗ на фоторграфиях

# Установка и запуск
## Запуск Docker - контейнера с проектом:
```bash
$ git clone https://github.com/DarinaStepanova/vvit.git
$ cd vvit
$ docker build . -t docker_vvit
$ docker run -p 0.0.0.0:8080:8080 -p 0.0.0.0:8081:8081 docker_vvit
```
## Остановить контейнер можно командой.
```bash
$ docker ps 
$ docker stop имя_контейнера
```
# Использование:
## Перейдите по ссылке http://127.0.0.1:8080/ .
<img src="https://github.com/DarinaStepanova/vvit/blob/d29ece114487f9e443743d85136b79235977a61c/src/1.jpg"/>

