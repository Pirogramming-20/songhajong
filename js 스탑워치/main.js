// date니 뭐니 너무 보기 어려운 것 같아서 그냥 쉽게 만들고, 쉽게 볼 수 있도록 노력했습니다:)
const display = document.querySelector('#watch')
const start_btn = document.querySelector('#start')
const stop_btn = document.querySelector('#stop')
const reset_btn = document.querySelector('#reset')
const record_body = document.querySelector('#record_body')
const all_btn = document.querySelector('#all_btn')
const trash = document.querySelector('#trash')

// 각 기능별 버튼

let watch
let timer = 0
let state = 0

// watch는 setinterval, clearinterval 함수를 사용하기 위한 변수로 사용
// timer는 말 그대로 보여지는 시간
// state는 시작버튼 클릭 후, 연속해서 클릭하면 중첩되어 시간이 가속되는 현상을 막기 위해 넣은 변수(0,1로 바꿔가며 토글 함. 사실상 toggle버튼)

start_btn.addEventListener('click', () => {
    if (state === 0){
        state = 1
        watch = setInterval(() => {
            timer += 0.01
            display.innerHTML = timer.toFixed(2)
        }, 10);
    }
})
// 0.01s 단위로 체크하며 timer변수를 새로 고쳐주기
// 버튼 클릭 시 state가 1로 변하고, 이 이후에는 눌러도 변화 x
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
// stop버튼을 누르면 state를 0으로 바꿔 start버튼이 활성화 되도록 만든 코드.
// 그 후, template를 이용해 간단하게 html동적 추가
reset_btn.addEventListener('click', () => {
    timer = 0
    display.innerHTML = timer.toFixed(2)
})
// 그냥 timer 초기화 시켜주기
let all_btn_state = false
// input박스가 check되지 않았으면 전체 체크, 아니라면 전체 해제를 만들어 주기 위해
// 마찬가지로 토글 버튼을 만들어줌
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
// 어려운것 없으니(?) 패스
trash.addEventListener('click', () => {
    const record_list = document.getElementsByName('record');

    const elements_to_remove = Array.from(record_list).filter(record => record.checked);

    elements_to_remove.forEach(element => {
        record_body.removeChild(element.parentElement);
    });
});

// 필터를 사용하여 체크된 인풋박스만 골라서 따로 배열로 만들어줌.
// 그런 후, 체크된 인풋박스 배열을 순회하며 삭제하면 끝:)