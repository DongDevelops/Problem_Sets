document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');

    // Send Mail
    const recipients = document.querySelector('#compose-recipients');
    const subject = document.querySelector('#compose-subject');
    const body = document.querySelector('#compose-body');
    const submit = document.querySelector('#submit');

    submit.disabled = true;

    recipients.onkeyup = () => {
      if (recipients.value.length > 0) {
        submit.disabled = false;
      }
      else {
        submit.disabled = true;
      }
    }

    document.querySelector('#compose-form').onsubmit = () => {

      const new_recipients = recipients.value;
      const new_subject = subject.value;
      const new_body = body.value;

      fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
          recipients: new_recipients,
          subject: new_subject,
          body: new_body
        })
      })
      .then(response => response.json())
      .then(result => {
        console.log(result);
        load_mailbox('sent');
      });
      return false;
    }
  });




  // Mailbox
  function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#email-view').style.display = 'none';


    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }

  function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
    const table = document.createElement('table');
    table.className = "table";
    document.querySelector('#emails-view').append(table);

    fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      emails.forEach(email => {
        const tr = document.createElement('tr');
        const td1 = document.createElement('td');
        const td2 = document.createElement('td');
        const td3 = document.createElement('td');
        td1.innerHTML = email.sender;
        td2.innerHTML = email.id;
        td3.innerHTML = email.archived;
        tr.onclick = function() {
          seeMail(email.id);
        }
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);

        table.appendChild(tr);
        if (email.read === true) {
          tr.style.backgroundColor = "gray";
        } else {
          tr.style.backgroundColor = "white";
        }
      });
    })


    function archiveMail(x) {
      fetch(`/emails/${x}`, {
        method: 'PUT',
        body: JSON.stringify({
          archived: true
        })
      })
    }


    function unarchiveMail(x) {
      fetch(`/emails/${x}`, {
        method: 'PUT',
        body: JSON.stringify({
          archived: false
        })
      })
      load_mailbox('inbox');
    }

    function reply(x) {

    }



    // Show a mail

    function seeMail(x) {
      fetch(`/emails/${x}`, {
        method: 'PUT',
        body: JSON.stringify({
          read: true
        })
      })
      fetch(`/emails/${x}`)
      .then(response => response.json())
      .then(email => {
          console.log(email);
          document.querySelector('#emails-view').style.display = 'none';
          document.querySelector('#compose-view').style.display = 'none';
          document.querySelector('#email-view').style.display = 'block';
          if (email.archived === true) {
            document.querySelector('#email-view').innerHTML = `
            <ul>
            <li>Sender: ${email.sender}</li>
            <li>Recipients: ${email.recipients}</li>
            <li>Subject: ${email.subject}</li>
            <li>Timestamp: ${email.timestamp}</li>
            <li>Body: ${email.body}</li>
            <button id="btn">Unarchive</button>
            <button id="reply">Reply</button>
            </ul>
            `
          } else if (email.recipients == document.querySelector('#user').value) {
            document.querySelector('#email-view').innerHTML = `
            <ul>
            <li>Sender: ${email.sender}</li>
            <li>Recipients: ${email.recipients}</li>
            <li>Subject: ${email.subject}</li>
            <li>Timestamp: ${email.timestamp}</li>
            <li>Body: ${email.body}</li>
            <button id="archiveMail">
            <button id="reply">Reply</button>
            </ul>
            `
          } else {
            document.querySelector('#email-view').innerHTML = `
            <ul>
            <li>Sender: ${email.sender}</li>
            <li>Recipients: ${email.recipients}</li>
            <li>Subject: ${email.subject}</li>
            <li>Timestamp: ${email.timestamp}</li>
            <li>Body: ${email.body}</li>
            </ul>
            `
          }
          const button = document.getElementById('btn');
          button.onclick = function() {
            unarchiveMail(email.id);
          }
          const reply = document.getElementById('reply');
          reply.onclick = function() {
            fetch(`/emails/${email.id}`)
            .then(response => response.json())
            .then(result => {
              console.log(result);
              document.querySelector('#emails-view').style.display = 'none';
              document.querySelector('#compose-view').style.display = 'block';
              document.querySelector('#email-view').style.display = 'none';

              document.querySelector('#compose-recipients').value = `${result.sender}`;
              document.querySelector('#compose-subject').value = `Re: ${result.subject}`;
              document.querySelector('#compose-body').value = `On ${result.timestamp} ${result.sender} wrote: ${result.body}`;
            });
          }
      });
    }
  }



