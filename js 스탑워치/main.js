
const display = document.querySelector('#watch')
const start_btn = document.querySelector('#start')
const stop_btn = document.querySelector('#stop')
const reset_btn = document.querySelector('#reset')
const record_body = document.querySelector('#record_body')
const all_btn = document.querySelector('#all_btn')
const trash = document.querySelector('#trash')

let watch
let timer = 0
let state = 0

start_btn.addEventListener('click', () => {
    if (state === 0){
        state = 1
        watch = setInterval(() => {
            timer += 0.01
            display.innerHTML = timer.toFixed(2)
        }, 10);
    }
})

stop_btn.addEventListener('click', () => {

    state = 0
    clearInterval(watch)

    const template = `
        <div class="record_item">
            <input type="checkbox" name="record">
            <p>${timer.toFixed(2)}</p>
            <div></div>
        </div>
    `
    record_body.innerHTML += template
})

reset_btn.addEventListener('click', () => {
    timer = 0
    display.innerHTML = timer.toFixed(2)
})

let all_btn_state = false

all_btn.addEventListener('click', () => {
    const record_list = document.getElementsByName('record');

    if(all_btn_state === false){
        record_list.forEach(element => {
            element.checked = "checked"
        })
        all_btn_state = true
    }
    else{
        record_list.forEach(element => {
            element.checked = false
        })
        all_btn_state = false
    }
})

trash.addEventListener('click', () => {
    const record_list = document.getElementsByName('record');

    const elements_to_remove = Array.from(record_list).filter(record => record.checked);

    elements_to_remove.forEach(element => {
        record_body.removeChild(element.parentElement);
    });
});
