document.getElementById("fileInput").addEventListener("change", function () {
  const file = this.files[0];
  const reader = new FileReader();

  reader.onload = e => buildSlides(e.target.result);
  reader.readAsText(file);
});

function buildSlides(html) {
  document.getElementById("loader").style.display = "none";

  // Parse full HTML document
  const parser = new DOMParser();
  const fullDoc = parser.parseFromString(html, "text/html");

  // Import <head> content (CSS + JS)
  document.head.innerHTML += fullDoc.head.innerHTML;

  // Clone the entire body
  const bodyClone = fullDoc.body.cloneNode(true);

  // Find the HackMD content root
  const root = bodyClone.querySelector("#doc") || bodyClone;

  const elements = Array.from(root.children);

  const slides = [];
  let current = [];

  function isSeparator(el) {
  if (el.tagName === "HR") return true;
  const t = el.textContent.trim();
  return t === "---" || t === "----";
    }

  elements.forEach(el => {
    if (isSeparator(el)) {
      if (current.length > 0) slides.push(current);
      current = [el];
    } else {
      current.push(el);
    }
  });

  if (current.length > 0) slides.push(current);

  const container = document.getElementById("slides");

  slides.forEach((group, i) => {
    const div = document.createElement("div");
    div.className = "slide" + (i === 0 ? " active" : "");

    // Append full HackMD wrapper structure
    const wrapper = bodyClone.cloneNode(false);
    const inner = root.cloneNode(false);

    group.forEach(el => inner.appendChild(el.cloneNode(true)));

    wrapper.appendChild(inner);
    div.appendChild(wrapper);

    container.appendChild(div);
  });

  initNavigation(slides.length);
}

function initNavigation(total) {
  let index = 0;

  function show(i) {
    const all = document.querySelectorAll(".slide");
    all.forEach(s => s.classList.remove("active"));
    all[i].classList.add("active");
  }

  function next() {
    index = Math.min(index + 1, total - 1);
    show(index);
  }

  function prev() {
    index = Math.max(index - 1, 0);
    show(index);
  }

  document.addEventListener("keydown", e => {
    if (e.key === "ArrowRight" || e.key === " ") next();
    if (e.key === "ArrowLeft") prev();
  });
}

