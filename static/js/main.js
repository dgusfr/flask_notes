function changeContent() {
  document.getElementById("content").innerHTML = "Conteúdo alterado!";
}

function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Nome deve ser preenchido");
    return false;
  }
  return true; // Permite o envio do formulário se a validação for bem-sucedida
}
