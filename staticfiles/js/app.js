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

for (t in tags.childNodes) {
    if (tags.childNodes[t].localName === "li") {
        let li = tags.childNodes[t]
        let color = Math.round(Math.random() * colorClasses.length)

        li.classList.add(`${colorClasses[color]}`)


    }

}

function AddLike(postId) {

    let d = {
        post_id: postId,
    }
    let data = JSON.stringify(d)
    if (window.XMLHttpRequest) {
        var xhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        var xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            if (data["status" === 404]) {
                let up = document.getElementById("up")
                up.setAttribute("disabled")
            }
        } else {

        }
    }
    var url = "/like/"
    xhttp.open("GET", url + `?data=${data}`, true);
    xhttp.send();
}

// search

// SEARCH
// let form = document.getElementById("searchForm")
// console.dir(form[0].value)

function InlineSearch(query) {
    console.log(query)
    let data = JSON.stringify(query)
    if (window.XMLHttpRequest) {
        var xhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        var xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            console.log(data)
            let list = document.getElementById("result_list")
            let elem = `<span>`
            for (let i = 0; i < data.object_list.length; i++) {

                obj = data.object_list[i]
                let panel = `<a class="panel-block" href="/post/${obj.id}">
                <span class="panel-icon">
                    <i class="fas fa-tags" aria-hidden="true"></i>
                  </span> ${obj.title}</a>
                `
                elem += panel
            }
            elem += `</span>`
            console.log(elem)
            list.innerHTML = elem



        } else {

        }
    }
    var url = "/search/"
    xhttp.open("GET", url + `?data=${data}`, true);
    xhttp.send();
}


function PostUpDownQuery(post_id, statement) {
    console.log(post_id)
    let data = JSON.stringify({ post_id: post_id, statement: statement })
        // console
    if (window.XMLHttpRequest) {
        var xhttp = new XMLHttpRequest();
    } else { // code for IE6, IE5
        var xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            let up = document.getElementById("ups");
            let down = document.getElementById("downs");
            up.innerHTML = data["post_up"]
            down.innerHTML = data["post_down"]

        } else {

        }
    }
    var url = "/up/"
    xhttp.open("GET", url + `?data=${data}`, true);
    xhttp.send();
}
