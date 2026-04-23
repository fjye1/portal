// Function to load a file into a container
function loadHTML(containerId, url, callback) {
  fetch(url)
    .then((res) => res.text())
    .then((html) => {
      document.getElementById(containerId).innerHTML = html;
      if (callback) callback();
    })
    .catch((err) => console.error(`Failed to load ${url}:`, err));
}

const FILMS = [
  {
    title: "Film",
    type: "film",
    image: "https://picsum.photos/400/210",
    favicon: "assets/images/film-solid-full.svg",
    links: [
      {
        text: "View",
        url: "https://www.example.com",
      },
    ],
  },

  {
    title: "Film",
    type: "film",
    image: "https://picsum.photos/400/210",
    favicon: "assets/images/film-solid-full.svg",
    links: [
      {
        text: "View",
        url: "https://www.example.com",
      },
    ],
  },

  {
    title: "Film",
    type: "film",
    image: "https://picsum.photos/400/210",
    favicon: "assets/images/film-solid-full.svg",
    links: [
      {
        text: "View",
        url: "https://www.example.com",
      },
    ],
  },

  {
    title: "Film",
    type: "film",
    image: "https://picsum.photos/400/210",
    favicon: "assets/images/film-solid-full.svg",
    links: [
      {
        text: "View",
        url: "https://www.example.com",
      },
    ],
  },

  // Add more filmcards here...
];

const cardColors = ["#85B5FF", "#B62F3A", "#162924", "#9DC8B1", "#FADB56"];

function createFilmCard(film, color) {
  const linksHTML = film.links
    .map((link) => `<a href="${link.url}" class="film-link">${link.text}</a>`)
    .join("\n                ");

  return `
    <div class="film-card" style="background: ${color};">
      <a href="${film.links[0].url}" target="_blank" rel="noopener">
        <img
          src="${film.image}"
          alt="${film.title}"
          class="film-img"
        />
      </a>
    
      <div class="film-body">
        <h3 class="film-title">
          <img
            src="${film.favicon}"
            alt="${film.title} favicon"
            class="film-icon"
          />
          ${film.title}
        </h3>

        <p class="film-type">${film.type}</p>

        <div class="film-links-container">
          ${linksHTML}
        </div>
      </div>
    </div>
  `;
}

const filmContainer = document.querySelector(".film-container");

FILMS.forEach((film, index) => {
  const color = cardColors[index % cardColors.length]; // cycles through colors
  filmContainer.innerHTML += createFilmCard(film, color);
});
