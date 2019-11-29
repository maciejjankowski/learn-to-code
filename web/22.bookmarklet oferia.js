var month = new Date().toDateString().split(' ')[1]; // BOOKMARKLET
var year = new Date().toDateString().split(' ')[3];

var projectDescription = document.querySelector('#user_field').innerText;
var phoneNumber, clientName;

pubsub.subscribe('cardactions:contentloaded', function() {
  let contactDetails = Array.from(
    document.querySelectorAll('.cardActionsContactMethod td')
  )
    .map(e => e.innerText)
    .filter(e => e)
    .filter(e => e !== 'Telefon:');
  [clientName, phoneNumber] = contactDetails;
  prompt(
    '',
    JSON.stringify({
      clientName,
      phoneNumber,
      projectDescription
    })
  );
});

document.querySelector('[class="showHiddenValues"]').click();
