document.querySelectorAll('.cor__input_radio').forEach(input => {
  input.addEventListener('change', () => {
    const labels = document.querySelectorAll('.cor__input_radio__label')
    labels.forEach(label => label.classList.remove('bordered'));
    if (!input.checked) { return; }

    labels.forEach(label => {
      if (label.getAttribute("for") != input.getAttribute("id")) {
        return;
      }
      label.classList.add("bordered");
    });
  });
});

const firstInput = document.querySelector('.cor__input_radio');
firstInput.checked = true;
firstInput.dispatchEvent(new Event('change'));

function manageShoppingCart(personalizacao) {

}

document.querySelectorAll('.personalizacoes')
  .forEach(personalizacao => personalizacao.addEventListener('change', e => {
    const element = e.target;

    if (e.target.checked) {
      document.getElementById(`checked-${element.id}`).classList.remove('d-none');
      document.getElementById(`unchecked-${element.id}`).classList.add('d-none');
    } else {
      document.getElementById(`unchecked-${element.id}`).classList.remove('d-none');
      document.getElementById(`checked-${element.id}`).classList.add('d-none');
    }
  }));