const month = new Date().toDateString().split(' ')[1]; // BOOKMARKLET
const year = new Date().toDateString().split(' ')[3];
if (location.href.indexOf(`github.com/maciejjankowski/${year}/wiki`) > -1) {
  const searchToken = '# Worth checking:\n';
  const textarea = document.querySelector('#gollum-editor-body');
  const textIndex = textarea.value.indexOf(searchToken);
  const textLength = searchToken.length;
  textarea.value =
    textarea.value.slice(0, textIndex + textLength) +
    prompt() +
    textarea.value.slice(textIndex + textLength);
  document.querySelector('#gollum-editor-submit').click();
} else {
  prompt(
    '',
    (function() {
      let header = (
        document.querySelector('h1') ||
        document.querySelector('h2') || { innerText: document.title }
      ).innerText;
      let address = window.location.href;
      return `* [${header}](${address})`;
    })()
  );
  window.location.href = `https://github.com/maciejjankowski/${year}/wiki/${month}/_edit`;
}


const month = new Date().toDateString().split(' ')[1]; const year = new Date().toDateString().split(' ')[3];  if (location.href.indexOf(`github.com/maciejjankowski/${year}/wiki`) > -1) {   const searchToken = '#%20Worth%20checking:\n';%20%20%20const%20textarea%20=%20document.querySelector('#gollum-editor-body');%20%20%20const%20textIndex%20=%20textarea.value.indexOf(searchToken);%20%20%20const%20textLength%20=%20searchToken.length;%20%20%20textarea.value%20=%20%20%20%20%20textarea.value.slice(0,%20textIndex%20+%20textLength)%20+%20%20%20%20%20prompt()%20+"\n"%20+%20%20%20%20%20%20textarea.value.slice(textIndex%20+%20textLength);%20%20%20document.querySelector('#gollum-editor-submit').click();%20}%20else%20{%20%20%20prompt(%20%20%20%20%20'',%20%20%20%20%20(function()%20{%20%20%20%20%20%20%20let%20header%20=%20(%20%20%20%20%20%20%20%20%20document.querySelector('h1')%20||%20%20%20%20%20%20%20%20%20document.querySelector('h2')%20||%20{%20innerText:%20document.title%20}%20%20%20%20%20%20%20).innerText;%20%20%20%20%20%20%20let%20address%20=%20window.location.href;%20%20%20%20%20%20%20return%20`\n\n*%20[${header}](${address})\n`;%20%20%20%20%20})()%20%20%20);%20%20%20window.location.href%20=%20`https://github.com/maciejjankowski/${year}/wiki/${month}/_edit`;%20%20%20void%200;%20}
