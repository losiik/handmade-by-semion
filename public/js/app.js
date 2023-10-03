document.addEventListener("DOMContentLoaded", () => {
    // let menuLinkSet = []
    // for (let i = 0; i<document.querySelectorAll('.b_menuLinks')[0].children.length; i++) {
    //     console.log(document.querySelectorAll('.b_menuLinks')[0].children[i].children[0].attributes.href.value)
    //     console.log(document.querySelectorAll('.b_menuLinks')[0].children[i].children)

    // }
    // if (menuLinkSet.find(location.pathname)) {
    //     document.querySelectorAll('.b_menuLinks')[0].children[i].children[0].attributes.href.value
    // }
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
    
});