/**
 * @author palmasite
 */


/*carregar pagina*/
	jQuery(function($){
		$( "button, input:submit", "" ).button();
		$( "#enquete").buttonset();
	});



/**
 * @post login
 */
function logar(){
	var	user = $('#login_user').val();
	var pass = $('#login_pass').val();
	$.post('/logar', {username:user,password:pass} ,function(data){
  		if (data.status == 'no'){
  			$("#messages_login").html(data.message);
  		}else{
  			$("#messages_login").html(data.message);
  			$("#login_form").hide();
  		}
	},'json');
}

/**
 * @post enquete
 */
var opsao;
var enquete = $("#id_enquete").val();
function escolher(x){opsao = x ;enquete = $("#id_enquete").val();}
function votar(){
	$.post('/enquete/votar', {enquete:enquete,opsao:opsao} ,function(data) {
  		$('#enquete').html(data);
	});
}
function relatorio(){
	$.get('/enquete/votar', {enquete:enquete} ,function(data) {
  		$('#enquete').html(data);
	});
}
/**
 * @full banner
 */
var full_banner_image = $("#full_banner .banner_image").size();
var full_bammer_id = 1;
$('#fullbanner-'+full_bammer_id).fadeIn();
var interval = setInterval("full_banner_fade()",10000);

function full_banner_fade(){
	$('#fullbanner-'+full_bammer_id).fadeOut();
	
	if (full_bammer_id >= full_banner_image){
		full_bammer_id = 1;
	}else{
		full_bammer_id = full_bammer_id+1;
	}
	$('#fullbanner-'+full_bammer_id).fadeIn();

}

/**
 * @ Noticia Destaque
 **/
 
var noticia_destaque = $(".noticia_destaque").size();
var noticia_destaque_id = 1;
$('#noticia_destaque_'+noticia_destaque_id).fadeIn();
var interval_noticia = setInterval("noticia_destaque_fade()",10000);

function noticia_destaque_fade(){
	$('#noticia_destaque_'+noticia_destaque_id).fadeOut();
	
	if (noticia_destaque_id >= noticia_destaque){
		noticia_destaque_id = 1;
	}else{
		noticia_destaque_id = noticia_destaque_id+1;
	}
	$('#noticia_destaque_'+noticia_destaque_id).fadeIn();

}




