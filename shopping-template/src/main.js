const loadItems = () => {
    return fetch('data/data.json')
    .then((res) => {return res.json()})
    .then((json) => {return json.items})
}

const displayItems = (items) => {
    const container = document.querySelector(".items");
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

const createHTMLString = (item) => {
    return (
    `
        <li class="item">
            <img src="${item.image}" alt="" class="item__thumbnail">
            <span class="item__description">${item.gender}, ${item.size}</span>
        </li>
    `
    )
}

loadItems()
    .then((items) => {
        console.log(items)
        displayItems(items)
    })
    .catch(err => console.log(err))