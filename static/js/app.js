(function($){
    'use strict';

    var $filters = $('.filter[data-filter]'),
        $pun = $('.pun[data-category]');
    
    $filters.on('click', function(e){
        e.preventDefault();
        var $this = $(this);

        $filters.removeClass('active');
        $this.addClass('active');

        var $filterCategory = $this.attr('data-filter');

        if ($filterCategory='all'){
            $pun.removeClass('is-animated')
            .fadeOut().promise().done(function(){
                $pun.addClass('is-animated').fadeIn();
            });
        } else{
            $pun.removeClass('is-animated')
            .fadeOut().promise().done(function(){
                $pun.filter('[data-category = "' + $filterCategory + '"]')
                .addClass('is-animated').fadeIn(); 
            });
        }
    });
    console.log("its working")
});