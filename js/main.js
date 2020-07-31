jQuery(document).ready({
    $(window).scroll(function () {
        
        var top = $(window).scrollTop();
        if(top >= 60){
            $("nav").addClass('secondary');
        }

        else
            if($("nav").hasClass('secondary')){
                $("nav").removeClass('secondary');
            }

    });

});

var typed = new Typed('.text', {
    // Waits 1000ms after typing "First"
    strings: ["^1500I am ^1000 <span class='primary'>Talent Planet</span>^1500"],
    typeSpeed: 40,
    loop: true
  });

