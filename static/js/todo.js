
const body = document.body;
const toggleBtn = document.getElementById("themeToggle");

if (localStorage.getItem("theme")) {
  body.className = localStorage.getItem("theme");
  toggleBtn.textContent = body.classList.contains("dark") ? "🌙" : "☀";
}

toggleBtn.addEventListener("click", () => {
  body.classList.toggle("dark");
  body.classList.toggle("light");

  toggleBtn.textContent = body.classList.contains("dark") ? "🌙" : "☀";

  localStorage.setItem("theme", body.className);
});