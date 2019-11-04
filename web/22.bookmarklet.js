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
