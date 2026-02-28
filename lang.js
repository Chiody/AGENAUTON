/* Agenauton i18n — shared language module */
(function(){
var LANG_KEY='agenauton_lang';

function detect(){
  var saved=localStorage.getItem(LANG_KEY);
  if(saved)return saved;
  var nav=navigator.language||navigator.userLanguage||'zh';
  return nav.toLowerCase().startsWith('zh')?'zh':'en';
}

function apply(lang){
  document.documentElement.lang=lang==='zh'?'zh-CN':'en';
  var els=document.querySelectorAll('[data-zh][data-en]');
  for(var i=0;i<els.length;i++){
    var el=els[i];
    var text=el.getAttribute('data-'+lang);
    if(text!==null){
      if(el.tagName==='INPUT'||el.tagName==='TEXTAREA'){
        el.placeholder=text;
      }else{
        el.innerHTML=text;
      }
    }
  }
  var cnEls=document.querySelectorAll('.logo-cn');
  for(var j=0;j<cnEls.length;j++){
    cnEls[j].style.display=lang==='en'?'none':'';
  }
  var btn=document.getElementById('langToggle');
  if(btn)btn.textContent=lang==='zh'?'EN':'中文';
  localStorage.setItem(LANG_KEY,lang);
  window.__lang=lang;
}

function toggle(){
  var cur=window.__lang||detect();
  apply(cur==='zh'?'en':'zh');
}

window.agenautonLang={detect:detect,apply:apply,toggle:toggle};

document.addEventListener('DOMContentLoaded',function(){
  var lang=detect();
  apply(lang);
});
})();
