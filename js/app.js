document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});

// TAGS STYLE 
let tags = document.querySelector("#banner_tags")
let colorClasses = ["is-black", "is-dark", "is-primary", "is-link", "is-info", "is-success", "is-warning", "is-danger"]
console.log(tags.childNodes)
for (t in tags.childNodes) {
    if (tags.childNodes[t].localName === "li") {
        let li = tags.childNodes[t]
        let color = Math.round(Math.random() * colorClasses.length)
        console.log(color)
        li.classList.add(`${colorClasses[color]}`)


    }

}