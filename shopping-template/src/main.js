const loadItems = () => {
    return fetch('data/data.json')
    .then((res) => {return res.json()})
    .then((json) => {return json.items})
}

loadItems()
    .then((items) => {
        console.log(items)
    })
    .catch(err => console.log(err))