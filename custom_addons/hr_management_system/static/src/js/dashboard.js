// ============================================================
//  Dashboard — UI interactions (vanilla JS)
// ============================================================

(function () {
    var KEY = "hrms_sidebar_collapsed";

    var MOBILE = 768;   // <= iss width pe sidebar off-canvas drawer banta hai

    // Page load pe pichli collapsed state wapas lagao (sirf desktop pe)
    function applySaved() {
        var app = document.querySelector(".app");
        if (app && localStorage.getItem(KEY) === "1" && window.innerWidth > MOBILE) {
            app.classList.add("is-collapsed");
        }
    }
    applySaved();
    document.addEventListener("DOMContentLoaded", applySaved);

    // Viewport resize pe conflicting state hatao (mobile <-> desktop)
    window.addEventListener("resize", function () {
        var app = document.querySelector(".app");
        if (!app) return;
        if (window.innerWidth <= MOBILE) {
            app.classList.remove("is-collapsed");   // mobile pe collapse nahi, drawer hota hai
        } else {
            app.classList.remove("nav-open");        // desktop pe drawer band
        }
    });

    // ---- Multi-step wizard (Create from Template modal) ----
    // Panels [data-step-panel], footers [data-foot-panel], stepper [data-ind]/[data-line]
    function rtplSetStep(modal, step) {
        if (!modal) return;
        var panels = modal.querySelectorAll("[data-step-panel]");
        var max = panels.length || 1;
        if (step < 1) step = 1;
        if (step > max) step = max;
        panels.forEach(function (p) {
            p.style.display = (parseInt(p.getAttribute("data-step-panel"), 10) === step) ? "" : "none";
        });
        modal.querySelectorAll("[data-foot-panel]").forEach(function (f) {
            f.style.display = (parseInt(f.getAttribute("data-foot-panel"), 10) === step) ? "" : "none";
        });
        modal.querySelectorAll("[data-ind]").forEach(function (s) {
            var ind = parseInt(s.getAttribute("data-ind"), 10);
            s.classList.toggle("is-done", ind < step);
            s.classList.toggle("is-active", ind === step);
        });
        modal.querySelectorAll("[data-line]").forEach(function (l) {
            l.classList.toggle("is-done", parseInt(l.getAttribute("data-line"), 10) < step);
        });
        var lbl = modal.querySelector("[data-step-label]");
        if (lbl) { lbl.textContent = "Step " + step + " of 4"; }
        modal.setAttribute("data-current-step", String(step));
    }

    // Per-template pre-fill data — har template alag content dikhata hai
    var TPL_DATA = {
        "HR Template":        { role: "HR Manager",         dept: "Human Resources", reports: "CEO",     scope: "Team Members",    total: "25 Permissions", summary: [["Employees", "8 Permissions"], ["Attendance", "5 Permissions"], ["Leave", "4 Permissions"], ["Payroll", "2 Permissions"], ["Performance", "3 Permissions"], ["Reports", "2 Permissions"], ["Settings", "1 Permissions"]] },
        "Team Lead Template": { role: "Team Lead",           dept: "Engineering",     reports: "Manager", scope: "Team Members",    total: "12 Permissions", summary: [["Employees", "3 Permissions"], ["Attendance", "3 Permissions"], ["Leave", "2 Permissions"], ["Payroll", "0 Permissions"], ["Performance", "2 Permissions"], ["Reports", "1 Permissions"], ["Settings", "1 Permissions"]] },
        "Manager Template":   { role: "Operations Manager",  dept: "Operations",      reports: "CEO",     scope: "Department Only", total: "18 Permissions", summary: [["Employees", "5 Permissions"], ["Attendance", "4 Permissions"], ["Leave", "3 Permissions"], ["Payroll", "2 Permissions"], ["Performance", "2 Permissions"], ["Reports", "1 Permissions"], ["Settings", "1 Permissions"]] },
        "Finance Template":   { role: "Finance Lead",        dept: "Finance",         reports: "CEO",     scope: "Department Only", total: "22 Permissions", summary: [["Employees", "4 Permissions"], ["Attendance", "2 Permissions"], ["Leave", "2 Permissions"], ["Payroll", "8 Permissions"], ["Performance", "2 Permissions"], ["Reports", "3 Permissions"], ["Settings", "1 Permissions"]] },
        "Custom Role":        { role: "Custom Role",         dept: "—",               reports: "—",       scope: "Own Data Only",   total: "0 Permissions",  summary: [["Employees", "0 Permissions"], ["Attendance", "0 Permissions"], ["Leave", "0 Permissions"], ["Payroll", "0 Permissions"], ["Performance", "0 Permissions"], ["Reports", "0 Permissions"], ["Settings", "0 Permissions"]] }
    };

    function rtplFillTemplate(modal, name) {
        var titleEl = modal.querySelector("[data-tpl-title]");
        if (titleEl) { titleEl.textContent = "Create from " + name; }
        modal.querySelectorAll("[data-tpl-desc]").forEach(function (el) {
            var txt = "Pre-filled from " + name;
            if (el.tagName === "TEXTAREA") { el.value = txt; } else { el.textContent = txt; }
        });
        var data = TPL_DATA[name];
        if (!data) { return; }
        // Step 3 — access scope radio
        modal.querySelectorAll("[data-scope]").forEach(function (radio) {
            radio.checked = (radio.getAttribute("data-scope") === data.scope);
        });
        // Step 4 — review fields
        function setFill(key, val) { var el = modal.querySelector('[data-fill="' + key + '"]'); if (el) { el.textContent = val; } }
        setFill("role", data.role);
        setFill("dept", data.dept);
        setFill("reports", data.reports);
        setFill("scope", data.scope);
        setFill("total", data.total);
        // Step 4 — permissions summary rows
        data.summary.forEach(function (pair) {
            var el = modal.querySelector('[data-sum="' + pair[0] + '"]');
            if (el) { el.textContent = pair[1]; }
        });
    }

    // ---- Collapse toggle (EVENT DELEGATION) ----
    // document pe ek hi listener — chahe button kab bhi render ho,
    // ya SVG/path pe click ho, closest() se pakad leta hai. Cache-safe.
    document.addEventListener("click", function (e) {
        var target = e.target.closest && e.target.closest(".topbar__collapse");
        if (target) {
            var app = document.querySelector(".app");
            if (app) {
                if (window.innerWidth <= MOBILE) {
                    // Mobile: sidebar ko drawer ki tarah khol/band karo
                    app.classList.toggle("nav-open");
                } else {
                    // Desktop: icon-only collapse (state yaad rakho)
                    var collapsed = app.classList.toggle("is-collapsed");
                    try { localStorage.setItem(KEY, collapsed ? "1" : "0"); } catch (ex) {}
                }
            }
            return;
        }

        // Mobile drawer band karo (backdrop click)
        var navClose = e.target.closest && e.target.closest("[data-nav-close]");
        if (navClose) {
            var appNc = document.querySelector(".app");
            if (appNc) { appNc.classList.remove("nav-open"); }
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

        // Role Template wizard modal — open ("Use Template") / close (overlay, ×, Cancel)
        var tplOpen = e.target.closest && e.target.closest("[data-tpl-open]");
        if (tplOpen) {
            var tplMo = document.querySelector("[data-tpl-modal]");
            if (tplMo) {
                rtplFillTemplate(tplMo, tplOpen.getAttribute("data-tpl-name") || "HR Template");
                tplMo.classList.add("is-open");
                rtplSetStep(tplMo, 1);
            }
            return;
        }
        var tplClose = e.target.closest && e.target.closest("[data-tpl-close]");
        if (tplClose) {
            var tplMc = document.querySelector("[data-tpl-modal]");
            if (tplMc) { tplMc.classList.remove("is-open"); }
            return;
        }
        // wizard step navigation (Continue / Back)
        var stepNext = e.target.closest && e.target.closest("[data-step-next]");
        if (stepNext) {
            var snM = stepNext.closest("[data-tpl-modal]");
            if (snM) { rtplSetStep(snM, (parseInt(snM.getAttribute("data-current-step"), 10) || 1) + 1); }
            return;
        }
        var stepPrev = e.target.closest && e.target.closest("[data-step-prev]");
        if (stepPrev) {
            var spM = stepPrev.closest("[data-tpl-modal]");
            if (spM) { rtplSetStep(spM, (parseInt(spM.getAttribute("data-current-step"), 10) || 1) - 1); }
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
