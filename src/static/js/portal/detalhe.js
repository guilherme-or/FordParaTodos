// $('#preco_carro').mask('000.000.000.000.000,0', { reverse: true });

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

function handleShoppingCart(personalizacao) {
  function createShoppingCartItem(personalizacao) {
    const cartItem = document.createElement('div');
    cartItem.classList.add('d-flex', 'justify-content-between', 'align-items-center', 'mt-3', 'p-2', 'rounded');
    cartItem.setAttribute('data-nome', personalizacao.id);

    cartItem.innerHTML = `
        <div class="d-flex flex-row">
            <img src="/static/img/customizacoes/${personalizacao.id}.png"
                class="rounded mx-2 my-2" alt="Imagem de ${personalizacao.id}" style="height: 50px; width: auto;">
            <span class="fw-bold d-block mx-3">${personalizacao.id}</span>
        </div>
        <div class="d-flex flex-row align-items-center">
            <span class="d-block ml-3 fw-bold">R$ ${personalizacao.dataset.preco}</span>
        </div>
    `;

    return cartItem;
  }

  const listElement = document.getElementById('shopping-cart-items');
  const existingCartItem = listElement.querySelector(`[data-nome="${personalizacao.id}"]`);
  const subtotal = document.getElementById('subtotal');

  if (existingCartItem) {
    existingCartItem.remove();
    subtotal.innerHTML = parseInt(subtotal.innerHTML) - parseInt(personalizacao.dataset.preco) + ",0";
  } else {
    listElement.append(createShoppingCartItem(personalizacao));
    subtotal.innerHTML = parseInt(subtotal.innerHTML) + parseInt(personalizacao.dataset.preco) + ",0";
  }

  let itemsCount = listElement.childElementCount;
  document.getElementById('shopping-cart-item-count-text').innerHTML =
    itemsCount === 0 ?
      'Você ainda não selecionou nenhum item' :
      itemsCount === 1 ? 'Você tem 1 item selecionado' : `Você tem ${itemsCount} itens selecionados`;
  document.getElementById('shopping-cart-item-count').innerHTML = itemsCount;
  document.getElementById('total').innerHTML = parseInt(document.getElementById('preco_carro').innerHTML) + parseInt(subtotal.innerHTML) + ",0";

  // $('#subtotal').mask('000.000.000.000.000,0', { reverse: true });
  // $('#total').mask('000.000.000.000.000,0', { reverse: true });
}

document.querySelectorAll('.personalizacoes')
  .forEach(personalizacao => {
    personalizacao.addEventListener('change', e => {
      const elemento = e.target;

      document.getElementById(`checked-${elemento.id}`).classList.toggle('d-none', !elemento.checked);
      document.getElementById(`unchecked-${elemento.id}`).classList.toggle('d-none', elemento.checked);

      handleShoppingCart(elemento);
    });
  });
