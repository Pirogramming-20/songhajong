
const ajax_like = async(id) => {
    const res = await fetch('/like/', {
        method : 'POST',
        headers : {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body : JSON.stringify({id: id}),
    })
    const {id : post_id} = await res.json()
    likeHandleResponse(post_id)
}

const likeHandleResponse = (id) => {
    const element = document.querySelector(`.btn-${id}`)
    const num = document.querySelector(`.btn-${id} span`)
    let number = Number(num.innerHTML) + 1

    element.innerHTML = `좋아요 <span>${number}</span>`
    
}