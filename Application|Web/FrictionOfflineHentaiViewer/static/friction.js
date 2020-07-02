var settingsToggle = document.getElementById('settings-toggle');
var filterElement = document.getElementById('filter');
var galleryElement = document.getElementById('pswp');
var idElement = document.getElementById('id');
var rtl = document.getElementById('rtl').checked;
var submitElement = document.getElementById('submit');
var messengerElement = document.getElementById('messenger');
var gallery;
var index;

function handleItems() {
  messengerElement.innerHTML = ''; // Убирается `loading...`

  if (this.status >= 500) {
    document.title = '500 code';
    messengerElement.innerHTML = "Извините, что-то плохое произошло <br/> <br/> у вас может быть плохой архив в библиотеке <br/> <br/> сервер, вероятно, распечатал или зарегистрировал дополнительную информацию <br/> <br/>";
  }

  var resp = JSON.parse(this.responseText);

  if (this.status != 200) {
    messengerElement.innerHTML = resp.message;
    document.title = 'sorry :<';
    showSettings();
    return;
  }

  if (!idElement.value) {
    window.history.replaceState({}, resp.title, window.location.pathname + '?id=' + resp.id + '&' + window.location.search.replace(/^\?/, ''));
  }

  if (index === undefined) {
    if (rtl) {
      resp.photoswipe.reverse();
      index = resp.photoswipe.length - 1;
    } else {
      index = 0;
    }
  }

  document.title = resp.title;
  gallery = new PhotoSwipe(
      galleryElement,
      PhotoSwipeUI_Default,
      resp.photoswipe,
      {
        spacing: 0,
        history: false,
        escKey: true,
        barsSize: {top: 0, bottom: 0},
        index: index
      }
  );

  function updateIndex() {
    index = gallery.getCurrentIndex();
  }

  gallery.listen('beforeChange', updateIndex);
  gallery.listen('destroy', function() {submitForm();});
  window.addEventListener('keypress', function(e) {
    if (e.keyCode == 13) submitForm();
  });
  gallery.init();
}

// *some* browsers won't let us submit the form unless we change something, so,,
function changeForm() {
  filterElement.value += ' ';
}

function submitForm() {
  changeForm();
  submitElement.click();
}

function getItems() {
  var url;

  if (idElement.value) url = '/items?id=' + encodeURIComponent(idElement.value);
  else url = '/items?f=' + encodeURIComponent(filterElement.value);

  var itemsRequest = new XMLHttpRequest();
  document.title = 'loading';
  itemsRequest.addEventListener('load', handleItems);
  itemsRequest.open('GET', url);
  itemsRequest.send();
}

function toggleSettings() {
  document.body.classList.toggle('settings-shown');
}

function showSettings() {
  if (!document.body.classList.contains('settings-shown')) toggleSettings();
  filterElement.focus();
}

window.addEventListener('keyup', function(e) {
  if (e.keyCode == 79) showSettings();
});

window.addEventListener('pageshow', function() {
  if ((gallery !== undefined) && !(galleryElement.classList.contains('pwsp--open'))) {
    getItems();
  }
});

settingsToggle.addEventListener('click', function(e) {
  toggleSettings();
  e.preventDefault();
});

setTimeout(function() {
  settingsToggle.classList.remove('just-loaded');
}, 1000);

getItems();