
let state = 0

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
    console.log(state)
}

const likeHandleResponse = (id) => {
    const element = document.querySelector(`.btn-${id}`)
    const num = document.querySelector(`.btn-${id} span`)
    let count = Number(num.innerHTML)

    if(state === 0){
        count += 1
        state = 1
    }
    else{
        count -= 1
        state = 0
    }

    element.innerHTML = `좋아요 <span>${count}</span>`
    
}