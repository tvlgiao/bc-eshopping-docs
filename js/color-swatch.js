/* Prepend a live color chip before any inline <code> that holds a hex color.
   Hooks Material's document$ observable so it also runs after instant nav. */
(function () {
  var HEX = /^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/;

  function decorate() {
    document.querySelectorAll(".md-typeset code").forEach(function (el) {
      if (el.dataset.swatch) return;
      var hex = el.textContent.trim();
      if (!HEX.test(hex)) return;
      el.dataset.swatch = "1";
      var chip = document.createElement("span");
      chip.className = "color-swatch";
      chip.style.setProperty("--swatch", hex);
      chip.setAttribute("title", hex);
      el.parentNode.insertBefore(chip, el);
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(decorate);
  } else {
    document.addEventListener("DOMContentLoaded", decorate);
  }
})();
