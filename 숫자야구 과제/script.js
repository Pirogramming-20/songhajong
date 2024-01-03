// 숫자 3개 랜덤 생성하기 =========================================
const make_answer = (number) => {
    let random_number = Math.floor(Math.random() * (number.length))
    const answer = number[random_number]
    number.splice(random_number, 1)
    return answer
}
/* 위 코드는 0~9까지의 수 중에서 중복없이 숫자를 뽑는 코드로, 배열(number)에 0~9까지의 숫자를 넣고 난수(random_number)가 뽑히면
그 인덱스의 숫자(number[random_number])를 해당 배열에서 삭제(number.splice(random_number, 1))하고 
뽑힌 인덱스의 숫자(number[random_number])를 리턴하는 함수이다. 

+ 갈수록 배열의 길이가 줄기 때문에 10이 아닌 number.length로 동적으로 맞춰준다.*/
const number = [0,1,2,3,4,5,6,7,8,9]

// const answer1 = make_answer(number)
// const answer2 = make_answer(number)
// const answer3 = make_answer(number)
const answer = [make_answer(number), make_answer(number), make_answer(number)]

console.log(answer)
// 숫자 3개 랜덤 생성하기 =========================================
// 사용자가 입력한 값 가져오기 ====================================
let count = 9
let strike = 0
let ball = 0

const input_answer1 = document.querySelector("#number1");
const input_answer2 = document.querySelector("#number2");
const input_answer3 = document.querySelector("#number3");
const check = document.querySelector(".submit-button");
const count_tag = document.querySelector("#count");

function check_numbers(){
        const input_answer = [input_answer1.value, input_answer2.value, input_answer3.value]
        let s = 0
        let b = 0
        console.log(input_answer)
    
        if(input_answer1.value && input_answer2.value && input_answer3.value ){
            count--
            count_tag.innerHTML = count;
            for(let i = 0; i < 3; i++){
                if(input_answer[i] == answer[i]){
                    s++
                }
                else if(answer.includes(Number(input_answer[i]))){
                    b++
                }
            }
    
            const template = `
                <div class="check-result">
                    <div class="left">${input_answer[0]} ${input_answer[1]} ${input_answer[2]}</div>
                    :
                    <div class="right">
                        ${(s == 0 && b == 0) ? `<div class="strike num-result">O</div>`: `${s} <div class="strike num-result">S</div> ${b} <div class="ball num-result">B</div>`}
                    </div>
            </div>
            `
            const result_display = document.querySelector('.result-display')
            result_display.innerHTML += template
    
            if(s == 3){
                const img = document.querySelector('#game-result-img')
                check.style.display = "none"
                img.src = "./success.png"
            }
            else if(count <= 0){
                const img = document.querySelector('#game-result-img')
                check.style.display = "none"
                img.src = "./fail.png"
            }

            input_answer1.value = ''
            input_answer2.value = ''
            input_answer3.value = ''
        }
        else{
            alert('칸이 비었습니다.')
            input_answer1.value = ''
            input_answer2.value = ''
            input_answer3.value = ''
        }
}
// 사용자가 입력한 값 가져오기, 로직 ====================================