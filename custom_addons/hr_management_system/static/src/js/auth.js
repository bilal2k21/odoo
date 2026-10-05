// ============================================================
//  AUTH pages — small interactions (vanilla JS)
//  Signup + Login dono ke liye. OWL sirf tab jab page truly
//  complex interactive ho.
// ============================================================

document.addEventListener("DOMContentLoaded", function () {

    // 1) Password show / hide (har eye button apne input ko toggle karta hai)
    document.querySelectorAll("[data-toggle-pwd]").forEach(function (btn) {
        btn.addEventListener("click", function () {
            var wrap = btn.closest(".input-icon");
            var input = wrap ? wrap.querySelector("input") : null;
            if (!input) return;
            var show = input.type === "password";
            input.type = show ? "text" : "password";
            btn.classList.toggle("is-on", show);
        });
    });

    // 2) Password strength bar (sirf signup page par hota hai)
    var pwd = document.getElementById("hrms-password");
    var bar = document.querySelector(".pwd-strength > span");
    if (pwd && bar) {
        pwd.addEventListener("input", function () {
            var v = pwd.value, score = 0;
            if (v.length >= 6) score++;
            if (/[A-Z]/.test(v)) score++;
            if (/[0-9]/.test(v)) score++;
            if (/[^A-Za-z0-9]/.test(v)) score++;

            var pct = [0, 30, 55, 80, 100][score];
            var color = score < 2 ? "#e5564b" : (score < 3 ? "#f29a2e" : "#2fa36b");
            bar.style.width = pct + "%";
            bar.style.background = color;
        });
    }

    // 3) Submit UX — form natively /dummy-login pe POST karta hai,
    //    server khud /dashboard pe redirect karta hai (no preventDefault).
    document.querySelectorAll("form.form").forEach(function (form) {
        form.addEventListener("submit", function () {
            var btn = form.querySelector(".btn-primary");
            if (btn) { btn.innerHTML = "Please wait…"; btn.style.opacity = "0.85"; }
        });
    });
});
