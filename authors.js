// JavaScript source code
function createNode(element) {
    return document.createElement(element);
}

function append(parent, el) {
    return parent.appendChild(el);
}

const ul = document.getElementById('authors');
const url = 'https://randomuser.me/api/?results=10';

const fetchUsers = async () => {
    const response = await fetch(url);
    const json = await response.json();
    console.log(json);
    let authors = await json.results;
    return authors.map(function (author) {
        let li = createNode('li'),
            img = createNode('img'),
            span = createNode('span');
        button = createNode('button');
        img.src = author.picture.medium;
        span.innerHTML = `${author.name.first} ${author.name.last}`;
        append(li, img);
        append(li, span);
        append(li, button);
        append(ul, li);
    })
}
fetchUsers();