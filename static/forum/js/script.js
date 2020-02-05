$(document).ready(function() {
	$('button.slideDown').click(function() {
		if ($(this).siblings('.slideDownHidden').is(':hidden')) {
			$(this).siblings('.slideDownHidden').slideDown('fast');
		} else {
			$(this).siblings('.slideDownHidden').slideUp('fast');
		}
	});
	$('button.CslideDown').click(function() {
		if ($(this).siblings('.CommentsSlideDownHidden').is(':hidden')) {
			$(this).siblings('.CommentsSlideDownHidden').slideDown('fast');
		} else {
			$(this).siblings('.CommentsSlideDownHidden').slideUp('fast');
		}
	});
	$('.HomePostBodyButton').click(function() {
		if ($(this).siblings('.HomePostBodyText').is(':hidden')) {
			$(this).siblings('.HomePostBodyText').slideDown('fast');
		} else {
			$(this).siblings('.HomePostBodyText').slideUp('fast');
		}
	});
	$('.reqs-button').click(function() {
		if ($('.panel').is(':hidden')) {
			$('.panel').slideDown('fast');
		} else {
			$('.panel').slideUp('fast');
		}
	});
	$('.reqs-button2').click(function() {
		if ($('.panel2').is(':hidden')) {
			$('.panel2').slideDown('fast');
		} else {
			$('.panel2').slideUp('fast');
		}
	});
	$('.reqs-button3').click(function() {
		if ($('.panel3').is(':hidden')) {
			$('.panel3').slideDown('fast');
		} else {
			$('.panel3').slideUp('fast');
		}
	});
	$('.menu, #menu-wrapper').click(function() {
		$('.box, #menu-text').animate({
			width: 'toggle'
		});
	});
	$('.menu, #menu-wrapper, #menu-text').click(function() {
		$('#menu-wrapper').fadeToggle('slow');
	});
});
function textAreaAdjust(o) {
	o.style.height = '1px';
	o.style.height = 25 + o.scrollHeight + 'px';
}

function onReady(callback) {
	var intervalID = window.setInterval(checkReady, 1000);

	function checkReady() {
		if (document.getElementsByTagName('body')[0] !== undefined) {
			window.clearInterval(intervalID);
			callback.call(this);
		}
	}
}

function show(id, value) {
	document.getElementById(id).style.display = value ? 'block' : 'none';
}

onReady(function() {
	$('#user-menu').fadeIn(1000);
	$('#wrapper').fadeIn(200).addClass('flex');
	$('#loading').fadeOut(200);
});
var jmediaquery = window.matchMedia('(min-width: 999px)');
if (jmediaquery.matches) {
	$(function() {
		//Keep track of last scroll
		var lastScroll = 0;
		$(window).scroll(function(event) {
			//Sets the current scroll position
			var st = $(this).scrollTop();
			//Determines up-or-down scrolling
			if (st > lastScroll) {
				$('.structural').animate({ top: '20px' }, { queue: false, duration: 500 });
			} else {
				$('.structural').animate({ top: '193px' }, { queue: false, duration: 500 });
			}
			//Updates scroll position
			lastScroll = st;
		});
	});
}
// var acc = document.getElementsByClassName('accordion');
// var i;

// for (i = 0; i < acc.length; i++) {
// 	acc[i].onclick = function() {
// 		this.classList.toggle('active');
// 		var panel = this.nextElementSibling;
// 		if (panel.style.maxHeight) {
// 			panel.style.maxHeight = null;
// 		} else {
// 			panel.style.maxHeight = panel.scrollHeight + 'px';
// 		}
// 	};
// }

$('a[href*="#"]')
	// Remove links that don't actually link to anything
	.not('[href="#"]')
	.not('[href="#0"]')
	.click(function(event) {
		// On-page links
		if (
			location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
			location.hostname == this.hostname
		) {
			// Figure out element to scroll to
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			// Does a scroll target exist?
			if (target.length) {
				// Only prevent default if animation is actually gonna happen
				event.preventDefault();
				$('html, body').animate(
					{
						scrollTop: target.offset().top
					},
					200,
					function() {
						// Callback after animation
						// Must change focus!
						var $target = $(target);
						$target.focus();
						if ($target.is(':focus')) {
							// Checking if the target was focused
							return false;
						} else {
							$target.attr('tabindex', '-1'); // Adding tabindex for elements not focusable
							$target.focus(); // Set focus again
						}
					}
				);
			}
		}
	});
tinymce.init({
	selector: 'textarea',
	resize: 'both',
	menubar: 'none',
	statusbar: true,
	plugins: [
		'advlist autolink lists link image charmap print preview anchor',
		'searchreplace visualblocks code fullscreen',
		'insertdatetime media table paste',
		'emoticons',
		'autoresize',
		'autolink',
		'autosave',
		'media'
	],
	default_link_target: '_blank',
	autosave_ask_before_unload: false,
	mobile: {
		theme: 'silver'
	},
	toolbar: 'restoredraft | bold italic | link image | media | emoticons'
	// toolbar: "restoredraft | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | media | emoticons"
});
