$(document).ready(function() {
  $('#send-button').click(function() {
    let message = $('#message-input').val();
    if (message.trim() !== '') {
      $('.messages').append(`<div class="message user-message">${message}</div>`);
      $('#message-input').val('');
      // Send message to backend
      $.post('/chat', {message: message}, function(data) {
        $('.messages').append(`<div class="message bot-message">${data.response}</div>`);
      });
    }
  });
});
