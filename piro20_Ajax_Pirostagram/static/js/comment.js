
const ajax_comment = async(id) => {
    const detail_comment = document.querySelector('.comment_input')
    const res = await fetch('/comment/', {
        method : 'POST',
        headers : {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body : JSON.stringify({id: id, comment: detail_comment.value}),
    })
    const {id: com_id, user: com_user, content: com_content} = await res.json()
    create_comment(com_id, com_user, com_content)

    detail_comment.value = null
}

const create_comment = (id, user, content) => {
    const comment_ul = document.querySelector('.detail_comment_modal ul')
    let template = `
        <span class="com_nick comment_nick-${id}">${user}</span>
        <li class='comment_li-${id}'>
            <span class="com_content comment_content-${id}">${content}</span>
            <i class="fa-solid fa-trash" onclick="ajax_delete(${id})"></i>
        </li>
    `
    comment_ul.innerHTML += template
}



const ajax_delete = async(comment_id) => {
    const res = await fetch('/comment_delete/', {
        method : 'POST',
        headers : {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body : JSON.stringify({comment_id: comment_id}),
    })
    const {id: com_id} = await res.json()
    delete_comment(com_id)
}

const delete_comment = (id) => {
    const delete_comment_span = document.querySelector(`.detail_comment_modal ul .comment_nick-${id}`)
    const delete_comment_li = document.querySelector(`.detail_comment_modal ul .comment_li-${id}`)

    delete_comment_span.remove()
    delete_comment_li.remove()
}