const ajax_like = (id) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/like/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const { id: post_id, post_like_count } = JSON.parse(xhr.responseText);
            likeHandleResponse(post_id, post_like_count);
        }
    };

    const requestBody = JSON.stringify({ id: id });
    xhr.send(requestBody);
};

const likeHandleResponse = (id, post_like_count) => {
    const element = document.querySelector(`.btn-${id}`);
    const num = document.querySelector(`.btn-${id} span`);
    let count = post_like_count;

    element.innerHTML = `좋아요 <span>${count}</span>`;
};