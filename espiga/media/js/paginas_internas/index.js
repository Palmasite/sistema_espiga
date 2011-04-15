/**
 * @author palmasite
 */


/*carregar pagina*/
	jQuery(function($){
		$( "button, input:submit", "" ).button();
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

function full_banner_fade(){
	
}



