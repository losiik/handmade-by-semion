function getURLParamValue(param) {
    var urlString = new URL(location.href);
    var c = urlString.searchParams.get(param);
    return c;
}

function storePosition(){
    const currentYPosiiton = window.scrollY + 200;
    localStorage.setItem('Ypos', currentYPosiiton);
}

function scrollToSPosiiton() {
    if(localStorage.getItem('Ypos') !== undefined){
        window.scrollTo(0, parseInt(localStorage.getItem('Ypos')))
        localStorage.removeItem('Ypos');
    }
    return false;
}
document.addEventListener("DOMContentLoaded", () => {
    scrollToSPosiiton();
    document.body.addEventListener("click", function(e) {
        console.log(e.target)
        if(e.target && e.target.classList.value.includes('i-modal') && e.target.hasAttribute('href')) {
            var targetModal = document.querySelector(e.target.attributes.href.value)
            targetModal.classList.add('d-block')
            document.body.classList.add('block')
        }
    });
    document.querySelector('.b_modal_closeX').addEventListener('click', (e) => {
        e.target.closest('.modal').classList.remove('d-block')
        document.body.classList.contains('block') ? document.body.classList.remove('block') : null;
        
      })
    if(location.pathname == '/projects/') {
        document.querySelector('.show_more').addEventListener('click', (e) => {
            e.preventDefault()
            const currentPage = Number.isNaN(parseInt(getURLParamValue('show_more'))) ? 1 : parseInt(getURLParamValue('show_more')) + 1;
            storePosition();
            if (getURLParamValue('tag') !== undefined && getURLParamValue('tag') !== null && getURLParamValue('tag') !== '') {
                let tag = getURLParamValue('tag')
                location.replace(`/projects/?show_more=${currentPage}&tag=${tag}`);
            } else {
                 location.replace(`/projects/?show_more=${currentPage}`);
            }
           
        })
    }
    document.querySelector('#form_contact_us')?.addEventListener('submit', (e) => {
        e.preventDefault();
        var userName = $("#user_name").val();
        var userPhone = $("#user_contact").val();
        var userMessage = $("#user_message").val();
        var userSelectedSkill = $("#skill_selection").find(":selected").text();
        const currentPage = location.pathname;
        $.ajax({
            method: 'POST',
            url: location.protocol + '//' + location.host + '/api/send_email/',
            data: {'message': `user left data: \nName: ${userName} \nContact: ${userPhone}\nMessage: ${userMessage}\nSelected service: ${userSelectedSkill}\nPage from which the request came (Referer): ${currentPage}`},
            success: function(data) {
                console.log(data)
                alert("Your message was successfully delivered, we\'ll contact you asap")
            },
            error: function(error) {
                console.log(error)
            }
        })
    })
    $('.b_about__certificatesGrid').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 3000,
        prevArrow: '',
        nextArrow: '',
        variableWidth: true,
        responsive: [
            {
              breakpoint: 993,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                infinite: true,
              }
            },
            {
              breakpoint: 450,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                autoplaySpeed: 5000
              }
            }
        ]
      });

});
