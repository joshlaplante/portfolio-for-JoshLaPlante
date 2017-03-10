/* make sure nav is hidden for mobile (flickers when wrapped in document.ready)*/
$('#fixed-nav').hide();

/* slide nav up/down on scroll thru header */
$(document).scroll(function() {
  var y = $(this).scrollTop();
  if (y > 450) {
    $('#fixed-nav').slideDown(800);
  } else {
    $('#fixed-nav').slideUp(800);
  }
});

/* slide first project columns in after delay (so icon popIn animations finish) */
$(document).ready(function() {
    $('#audio-visualizer-project').delay(1500).queue(function(next) {
  		$(this).children().addClass("slide-right");
  		next();
  	});
});

/* slide all other project columns in on scroll down page */
$(document).scroll(function() {
  var y = $(this).scrollTop();
  if (y > 700) {
    $('#ssb64-12cb-app-project').children().addClass('slide-left');
  }
});

$(document).scroll(function() {
  var y = $(this).scrollTop();
  if (y > 1200) {
    $('#image-resize-gui-project').children().addClass('slide-right');
  }
});

$(document).scroll(function() {
  var y = $(this).scrollTop();
  if (y > 1700) {
    $('#project-euler-project').children().addClass('slide-left');
  }
});

