function perfil() {
    window.location.href = "../perfil"
}

let lastScrollTop = 0;
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    let scrollTop = window.scrollY || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
        // Rolando para baixo - esconde o navbar
        navbar.classList.add('hide');
    } else {
        // Rolando para cima - mostra o navbar
        navbar.classList.remove('hide');
    }

    lastScrollTop = scrollTop;
});

const modal = document.querySelector('.modal-container')

function openModal() {
    modal.classList.add('active')
}

function closeModal() {
    modal.classList.remove('active')
}

// Dados dos cards (imagem, nome e profissão)
const cardData = [
    {
        imagem: "images/istockphoto-954305374-612x612.jpg",
        nome: "A",
        descricao: "A",
    },
    {
        imagem: "images/istockphoto-954305374-612x612.jpg",
        nome: "B",
        descricao: "B",
    },
    {
        imagem: "images/istockphoto-954305374-612x612.jpg",
        nome: "C",
        descricao: "C",
    },
    {
        imagem: "images/istockphoto-954305374-612x612.jpg",
        nome: "D",
        descricao: "D",
    },
];

function createCard(data) {
    const card = document.createElement("a");
    card.className = "swiper-slide card";
    card.innerHTML = `
      <div class="card-content">
        <div class="imagem">
          <img src="${data.imagem}" alt="Imagem" />
        </div>
        <div class="dados">
          <span class="nome">${data.nome}</span>
          <span class="descricao">${data.descricao}</span>
        </div>
      </div>
    `;
    return card;
}


const cardContainer = document.getElementById("card-container");
cardData.forEach((data) => {
    const card = createCard(data);
    cardContainer.appendChild(card);
});

var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30, // Espaço entre os slides
    grabCursor: true, // Mostra um cursor de "mão" ao passar o mouse
    loop: true, // Ativa o looping infinito dos slides

    pagination: {
        el: ".swiper-pagination", // Seletor do elemento de paginação
        clickable: true, // Permite clicar nos indicadores de paginação
    },

    // Configura os botões próximo e anterior
    navigation: {
        nextEl: ".swiper-button-next", // Botão de próximo
        prevEl: ".swiper-button-prev", // Botão de anterior
    },

    // Configurações de responsividade
    breakpoints: {
        0: {
            slidesPerView: 1, // Mostra 1 slide em telas pequenas
        },
        768: {
            slidesPerView: 2, // Mostra 2 slides em telas médias
        },
        1024: {
            slidesPerView: 3, // Mostra 3 slides em telas grandes
        },
    },
});