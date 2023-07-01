<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
   ufd>
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../static/css/style.css">
  <title>Расчет энергоэффективности умного дома</title>
</head>
<body>
  <header class="header">
    <div class="header__text">
      <h1>Расчитай энергоэффективность своего дома!</h1>
      <p>Реши проблему излишнего электропотребления самостоятельно!</p>
    </div>
  </header>
  <main>
    {% block content %}
    <h2 class="main__title">Выбери количество электрических приборов:</h2>
    <ul class="list" id="list">
      <!-- Задание №3 -->
      <li class="list__item">
        <a href="{{lights + "/4"}}">
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>3-5 прибора</span></a>
      </li>
      <li class="list__item">
        <a href="{{lights + "/7"}}">
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>6-8 приборов</span></a>
      </li>
      <li class="list__item">
        <a href="{{lights + "/10"}}">
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>10 и более</span></a>
      </li>
      <li class="list__item">
        <a href={{size + "/3" }}>
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>2-4 лампочки</span></a>
      </li>
      <!--  -->
    </ul>
    {% endblock %}
  </main>
  <footer>

  </footer>
</body>
</html>
