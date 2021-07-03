jQuery(document).ready(function($) {


  var slideCount = $('#slider ul li').length;
  var slideWidth = $('#slider ul li').width();
  var slideHeight = $('#slider ul li').height();
  var sliderUlWidth = slideCount * slideWidth;



  $('#slider ul li:last-child').prependTo('#slider ul');

  function moveLeft() {
    $('#slider ul').animate({
      left: +slideWidth
    }, 200, function() {
      $('#slider ul li:last-child').prependTo('#slider ul');
      $('#slider ul').css('left', '');
    });
  };

  function moveRight() {
    $('#slider ul').animate({
      left: -slideWidth
    }, 200, function() {
      $('#slider ul li:first-child').appendTo('#slider ul');
      $('#slider ul').css('left', '');
    });
  };

  $('button.control_prev').click(function() {
    moveLeft();
  });

  $('button.control_next').click(function() {
    moveRight();
  });

});

jQuery(document).ready(function($) {


  var slideCount = $('#slider1 ul li').length;
  var slideWidth = $('#slider1 ul li').width();
  var slideHeight = $('#slider1 ul li').height();
  var sliderUlWidth = slideCount * slideWidth;


  $('#slider1 ul li:last-child').prependTo('#slider1 ul');

  function moveLeft() {
    $('#slider1 ul').animate({
      left: +slideWidth
    }, 200, function() {
      $('#slider1 ul li:last-child').prependTo('#slider1 ul');
      $('#slider1 ul').css('left', '');
    });
  };

  function moveRight() {
    $('#slider1 ul').animate({
      left: -slideWidth
    }, 200, function() {
      $('#slider1 ul li:first-child').appendTo('#slider1 ul');
      $('#slider1 ul').css('left', '');
    });
  };

  $('button.control_prev1').click(function() {
    moveLeft();
  });

  $('button.control_next1').click(function() {
    moveRight();
  });

});

jQuery(document).ready(function($) {


  var slideCount = $('#slider2 ul li').length;
  var slideWidth = $('#slider2 ul li').width();
  var slideHeight = $('#slider2 ul li').height();
  var sliderUlWidth = slideCount * slideWidth;


  $('#slider2 ul li:last-child').prependTo('#slider2 ul');

  function moveLeft() {
    $('#slider2 ul').animate({
      left: +slideWidth
    }, 200, function() {
      $('#slider2 ul li:last-child').prependTo('#slider2 ul');
      $('#slider2 ul').css('left', '');
    });
  };

  function moveRight() {
    $('#slider2 ul').animate({
      left: -slideWidth
    }, 200, function() {
      $('#slider2 ul li:first-child').appendTo('#slider2 ul');
      $('#slider2 ul').css('left', '');
    });
  };

  $('button.control_prev2').click(function() {
    moveLeft();
  });

  $('button.control_next2').click(function() {
    moveRight();
  });

});




