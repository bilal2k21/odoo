// ============================================================
//  Dashboard — UI interactions (vanilla JS)
// ============================================================

(function () {
    var KEY = "hrms_sidebar_collapsed";

    // Page load pe pichli collapsed state wapas lagao
    function applySaved() {
        var app = document.querySelector(".app");
        if (app && localStorage.getItem(KEY) === "1") {
            app.classList.add("is-collapsed");
        }
    }
    applySaved();
    document.addEventListener("DOMContentLoaded", applySaved);

    // ---- Collapse toggle (EVENT DELEGATION) ----
    // document pe ek hi listener — chahe button kab bhi render ho,
    // ya SVG/path pe click ho, closest() se pakad leta hai. Cache-safe.
    document.addEventListener("click", function (e) {
        var target = e.target.closest && e.target.closest(".topbar__collapse");
        if (target) {
            var app = document.querySelector(".app");
            if (app) {
                var collapsed = app.classList.toggle("is-collapsed");
                try { localStorage.setItem(KEY, collapsed ? "1" : "0"); } catch (ex) {}
            }
            return;
        }

        // Attendance — calendar popup toggle
        var calBtn = e.target.closest && e.target.closest("[data-att-cal-btn]");
        if (calBtn) {
            var pop = document.querySelector("[data-att-cal]");
            if (pop) { pop.classList.toggle("is-open"); }
            return;
        }

        // New Request — field dropdowns (Employees / Type of Leave)
        var ddTrigger = e.target.closest && e.target.closest("[data-dropdown]");
        if (ddTrigger) {
            var ddWrap = ddTrigger.parentElement;
            var ddMenu = ddWrap ? ddWrap.querySelector("[data-dropdown-menu]") : null;
            document.querySelectorAll("[data-dropdown-menu].is-open").forEach(function (m) { if (m !== ddMenu) m.classList.remove("is-open"); });
            if (ddMenu) { ddMenu.classList.toggle("is-open"); }
            return;
        }

        // New Request modal — open ("New request" button) / close (overlay, ×, Cancel)
        var nrOpen = e.target.closest && e.target.closest("[data-nr-open]");
        if (nrOpen) {
            var moOpen = document.querySelector("[data-nr-modal]");
            if (moOpen) { moOpen.classList.add("is-open"); }
            return;
        }
        var nrClose = e.target.closest && e.target.closest("[data-nr-close]");
        if (nrClose) {
            var moClose = document.querySelector("[data-nr-modal]");
            if (moClose) { moClose.classList.remove("is-open"); }
            return;
        }

        // Notifications drawer — open (bell) / close (overlay, ×)
        var ntOpen = e.target.closest && e.target.closest("[data-notif-open]");
        if (ntOpen) {
            var ntO = document.querySelector("[data-notif]");
            if (ntO) { ntO.classList.add("is-open"); }
            return;
        }
        var ntClose = e.target.closest && e.target.closest("[data-notif-close]");
        if (ntClose) {
            var ntC = document.querySelector("[data-notif]");
            if (ntC) { ntC.classList.remove("is-open"); }
            return;
        }

        // Add Document modal — open ("Upload document") / close (overlay, ×, Save draft)
        var dcOpen = e.target.closest && e.target.closest("[data-doc-open]");
        if (dcOpen) {
            var dcMo = document.querySelector("[data-doc-modal]");
            if (dcMo) { dcMo.classList.add("is-open"); }
            return;
        }
        var dcClose = e.target.closest && e.target.closest("[data-doc-close]");
        if (dcClose) {
            var dcMc = document.querySelector("[data-doc-modal]");
            if (dcMc) { dcMc.classList.remove("is-open"); }
            return;
        }

        // Add Work Location modal — open ("Work Locations" card) / close (overlay, chevron, Cancel)
        var wlOpen = e.target.closest && e.target.closest("[data-wl-open]");
        if (wlOpen) {
            var wlMo = document.querySelector("[data-wl-modal]");
            if (wlMo) { wlMo.classList.add("is-open"); }
            return;
        }
        var wlClose = e.target.closest && e.target.closest("[data-wl-close]");
        if (wlClose) {
            var wlMc = document.querySelector("[data-wl-modal]");
            if (wlMc) { wlMc.classList.remove("is-open"); }
            return;
        }

        // Add Asset modal — open ("Assets" card) / close (overlay, ×, Cancel)
        var asOpen = e.target.closest && e.target.closest("[data-asset-open]");
        if (asOpen) {
            var asMo = document.querySelector("[data-asset-modal]");
            if (asMo) { asMo.classList.add("is-open"); }
            return;
        }
        var asClose = e.target.closest && e.target.closest("[data-asset-close]");
        if (asClose) {
            var asMc = document.querySelector("[data-asset-modal]");
            if (asMc) { asMc.classList.remove("is-open"); }
            return;
        }

        // Add Asset — category cards (single select)
        var cat = e.target.closest && e.target.closest(".asset-cat");
        if (cat) {
            document.querySelectorAll(".asset-cat").forEach(function (c) { c.classList.remove("is-active"); });
            cat.classList.add("is-active");
            return;
        }

        // Department filter tabs — active toggle
        var tab = e.target.closest && e.target.closest(".deptabs .deptab");
        if (tab) {
            document.querySelectorAll(".deptabs .deptab").forEach(function (t) { t.classList.remove("is-active"); });
            tab.classList.add("is-active");
            return;
        }

        // Day / Week / Month toggle
        var seg = e.target.closest && e.target.closest(".seg .seg__btn");
        if (seg) {
            document.querySelectorAll(".seg .seg__btn").forEach(function (b) { b.classList.remove("is-active"); });
            seg.classList.add("is-active");
            return;
        }

        // Employee Action — action type cards (single select + fields adjust)
        var type = e.target.closest && e.target.closest(".ea-type");
        if (type) {
            document.querySelectorAll(".ea-type").forEach(function (t) { t.classList.remove("is-active"); });
            type.classList.add("is-active");

            var key = type.getAttribute("data-type") || "promotion";
            var nameEl = type.querySelector(".ea-type__name");
            var label = nameEl ? nameEl.textContent.trim() : "Promotion";

            var step3 = document.querySelector("[data-step-details]");
            if (key === "none") {
                // koi action details form nahi (jaise Demotion) -> pura Step 3 chhupao
                if (step3) step3.style.display = "none";
            } else {
                if (step3) step3.style.display = "";
                // Field groups toggle (jis type ka group ho wahi dikhao; warna promotion)
                var groups = document.querySelectorAll(".ea-grid[data-fields]");
                if (groups.length) {
                    var hasMatch = false;
                    groups.forEach(function (g) { if (g.getAttribute("data-fields") === key) hasMatch = true; });
                    var target = hasMatch ? key : "promotion";
                    groups.forEach(function (g) { g.style.display = (g.getAttribute("data-fields") === target) ? "" : "none"; });
                }
                var sub = document.querySelector("[data-ea-subtitle]");
                if (sub) { sub.textContent = label + " details — fill the fields below; the summary on the right updates live."; }
            }

            // pick value + summary badge hamesha update
            var pick = document.querySelector("[data-ea-pick]");
            if (pick) { pick.value = label; }
            var badge = document.querySelector("[data-ea-badge]");
            if (badge) { badge.textContent = label.toUpperCase(); }
            return;
        }
    });
})();
