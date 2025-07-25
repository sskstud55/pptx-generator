document.addEventListener('DOMContentLoaded', function() {
  const sendButton = document.getElementById('send-button');
  const messageInput = document.getElementById('message-input');
  const messagesContainer = document.querySelector('.messages');

  sendButton.addEventListener('click', function() {
    const message = messageInput.value;
    if (message.trim() !== '') {
      messagesContainer.innerHTML += `<div class="message user-message">${message}</div>`;
      messageInput.value = '';

      fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(message)}`
      })
      .then(response => response.json())
      .then(.data => {
        messagesContainer.innerHTML += `<div class="message bot-message">${data.response}</div>`;
      });
    }
  });
});
