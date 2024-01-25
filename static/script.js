window.onload = function () {
  document.getElementById("artistForm").onsubmit = function (event) {
    event.preventDefault();
    var artistName = document.getElementById("artistName").value;
    window.location.href =
      "http://127.0.0.1:8000/movies/" + encodeURIComponent(artistName);
    var artistForm = document.getElementById("artistForm");
    var loader = document.createElement("div");
    loader.className = "loader";
    artistForm.appendChild(loader);
  };

  var films = [
    { name: "Avatar", year: 2009, image: "avatar.jpg" },
    { name: "Jurassic Park", year: 1993, image: "jurassicparc.jpg" },
    { name: "Your Name", year: 2016, image: "yourname.jpg" },
  ];
  var randomFilm = films[Math.floor(Math.random() * films.length)];
  document.getElementById(
    "example_name"
  ).innerText = `${randomFilm.name}, ${randomFilm.year}`;
  document.getElementById("example_image").src =
    "/static/asset/" + randomFilm.image;
};
