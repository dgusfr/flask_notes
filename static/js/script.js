var count = 0;

function changeContent() {
  count++;
  document.getElementById("content").innerHTML =
    "Conteúdo alterado " + (count > 1 ? count : "") + " vezes!";
}

function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Nome deve ser preenchido");
    return false;
  }
  return true; // Permite o envio do formulário se a validação for bem-sucedida
}
