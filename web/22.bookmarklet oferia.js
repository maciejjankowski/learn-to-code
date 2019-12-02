var month = new Date().toDateString().split(' ')[1]; // BOOKMARKLET
var year = new Date().toDateString().split(' ')[3];

var projectDescription = document.querySelector('#user_field').innerText;
var phoneNumber, clientName;
var projectTitle = document.querySelector('.cardOrderName').innerText;
var projectLink = location.href;

pubsub.subscribe('cardactions:contentloaded', function() {
  let contactDetails = (Array.from(
    document.querySelectorAll('.cardActionsContactMethod td')
  )
    .map(e => e.innerText.trim())
    .filter(e => e)
    .filter(e => e !== 'Telefon:')[(clientName, phoneNumber)] = contactDetails);
  prompt(
    '',
    JSON.stringify({
      clientName,
      phoneNumber,
      projectLink,
      projectTitle,
      projectDescription
    })
  );
});

document.querySelector('[class="showHiddenValues"]').click();
