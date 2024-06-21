function nav_main(hrf) {


 document.write('<a href="/" class="header-logo">');
 document.write('<img class="header-logo-image" src="/static/images/logo.png" alt="СтройКонтроль" loading="lazy"/></a>');

 document.write('<div class="nav-scroller">');
 document.write('<nav class="nav-scroller__items dragscroll">');

 if(hrf=="main") {
   document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Главная</a>');
 }
 else {
  document.write('<a href="/" class="nav-scroller__item">Главная</a>');
 }
  if(hrf=="about") {
   document.write('<a href="#" class="nav-scroller__item  nav-scroller__item_active">О компании</a>');
  }
  else {
   document.write('<a href="/about" class="nav-scroller__item">О компании</a>');
 }
  if(hrf=="SK") {
    document.write(' <a href="#" class="nav-scroller__item   nav-scroller__item_active">СК</a>');
   }
  else {
   document.write(' <a href="/SK" class="nav-scroller__item">СК</a>');
  }
  if(hrf=="TKzaII") {
     document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">ТК за ИИ</a>');
   }
   else {
   document.write('<a href="/TKzaII" class="nav-scroller__item">ТК за ИИ</a>');
  }
  if(hrf=="DK") {
     document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">ДК</a>');
  }
  else {
   document.write('<a href="/DK" class="nav-scroller__item">ДК</a>');
  }
    if(hrf=="techzakaz") {
      document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Техзаказчик</a>');
     }
    else {
    document.write('<a href="/techzakaz" class="nav-scroller__item">Техзаказчик</a>');
    }
      if(hrf=="TA") {
       document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Техаудит</a>');
      }
      else {
       document.write('<a href="/TA" class="nav-scroller__item">Техаудит</a>');
     }
      if(hrf=="contacts") {
          document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Контакты</a>');
       }
       else {
       document.write('<a href="/contacts" class="nav-scroller__item">Контакты</a>');
       }
 document.write('</nav>');
 document.write('</div>');
}
