jQuery(document).ready(function(){

    $(window).scroll(function(){
        var top = $(window).scrollTop();
        if(top >= 60){
            $("nav").addClass('secondary');
        }

        else
            if($("nav").hasClass('secondary')){
                $("nav").removeClass('secondary');
            }
    });

    $('.work').magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true,
        }
    });

    
        $('.owl-carousel').owlCarousel();

});

var typed = new Typed('.text', {
    // Waits 1000ms after typing "First"
    strings: ["^1500I am ^1000 <span class='primary'>Talent Planet</span>^1500"],
    typeSpeed: 40,
    loop: true
  });

  
// $('owl-carousel').owlCarousel({
//     loop: true,
//     margin: 10,
//     nav: true,
//     responsive:{
//         0:{
//             items:1
//         },
//         600:{
//             items:3
//         },
//         1000:{
//             items:5
//         }
//     }
// })

