# vvit

# Веб-приложение с нейросетью для детектирования СИЗ на фоторграфиях

# Установка приложения
## Запуск контейнера с проектом:
```bash
$ git clone https://github.com/DarinaStepanova/vvit.git
$ cd vvit
$ docker build . -t docker_siz
$ docker run -p 0.0.0.0:8080:8080 -p 0.0.0.0:8081:8081 docker_siz
```

# Использование веб-приложения
## Перейдите по ссылке http://127.0.0.1:8080/ .
<img src="https://github.com/DarinaStepanova/vvit/blob/f408552d33103b5693be68a69c17d05eacc9cf79/src/img.png"/>

## Выберите фото и загрузите на сайт.

## Нажмите кнопку "Начать", чтобы загрузить и продетектировать выбранный файл.
<img src="https://github.com/DarinaStepanova/vvit/blob/f408552d33103b5693be68a69c17d05eacc9cf79/src/img_1.png"/>

## Дождитесь окончания процесса (должна появиться галочка на фото) и нажмите на кнопку "Перейти к результату".
<img src="https://github.com/DarinaStepanova/vvit/blob/f408552d33103b5693be68a69c17d05eacc9cf79/src/3.jpg"/>

## Результат:
<img src="https://github.com/DarinaStepanova/vvit/blob/f408552d33103b5693be68a69c17d05eacc9cf79/src/4.jpg"/>
