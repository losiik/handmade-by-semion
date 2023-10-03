document.addEventListener("DOMContentLoaded", () => {
    document.body.addEventListener("click", function(e) {
        if(e.target && e.target.classList.value.includes('i-modal') && e.target.hasAttribute('href')) {
            var targetModal = document.querySelector(e.target.attributes.href.value)
            targetModal.classList.add('d-block')
            document.body.classList.add('block')
        }
    });
    document.querySelector('.b_modal_closeX')?.addEventListener('click', (e) => {
      e.target.closest('.modal').classList.remove('d-block')
      document.body.classList.contains('block') ? document.body.classList.remove('block') : null;
    })
    document.querySelector('#form_contact_us')?.addEventListener('submit', () => {
        var userName = $("#user_name").val();
        var userPhone = $("#user_contact").val();
        var userMessage = $("#user_message").val();
        $.ajax({
            method: 'POST',
            url: location.protocol + '//' + location.host + '/api/send_email/',
            data: {'message': `user left data: \nName: ${userName} \nContact: ${userPhone}\nMessage: ${userMessage}`},
            success: function(data) {
                console.log(data)
                alert("Your message was successfully delivered, we\'ll contact you asap")
            },
            error: function(error) {
                console.log(error)
            }
        })
    })
});