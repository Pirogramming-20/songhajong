const add_task_btn = document.getElementById('addTaskBtn')
const list_container = document.querySelector('#list_container')

show_data()

add_task_btn.addEventListener('click', () => {
    // const template = `
    // <li>
    //     <input id="task_input" type="text" placeholder="할일 입력 ㄱㄱ">
    //     <div id="addTaskBtn" class="add_task_btn"><i class="ri-add-line"></i></div>
    // </li>
    // `
    const li = document.createElement("li");

    const input = document.createElement("input");
    input.setAttribute("type", "text");
    input.setAttribute("placeholder", "할일 입력 ㄱㄱ");
    input.setAttribute("id", "task_input");

    const btn = document.createElement("div");
    btn.setAttribute("id", "addListBtn")
    btn.className = "add_task_btn"
    btn.addEventListener('click', () => {
        const task_input = document.querySelector('#task_input')
        const task = task_input.value

        if(task === ""){
            alert('칸입력 하셈')
        }
        else{
            const li = document.createElement("li")
            li.innerText = task

            list_container.appendChild(li)

            list_container.removeChild(task_input.parentElement)
            save_data()
        }
    })

    const icon = document.createElement('i')
    icon.classList.add("ri-add-line")

    btn.appendChild(icon);
    li.appendChild(input);
    li.appendChild(btn);

    list_container.appendChild(li)
})

function save_data(){
    localStorage.setItem("data", list_container.innerHTML)
}

function show_data(){
    list_container.innerHTML = localStorage.getItem("data");
}

list_container.addEventListener('click', (e) => {
    e.target.classList.toggle("checked")

    let checked_todos = document.querySelector('#today').innerText
    
    if(e.target.tagName === "LI" ){
        if(e.target.classList.contains('checked')){
            checked_todos = parseInt(checked_todos) + 1
        }
        else if(checked_todos != 0){
            checked_todos = parseInt(checked_todos) - 1
        }
    }
    document.querySelector('#today').innerText = checked_todos
})

const TODO_LIST_DATA = [
    {
      category: "동아리",
      todolist: [
        "후회없는 여름방학 보내기",
        "좋은 인연 많이 만들기",
        "헤맨만큼 내 땅이다! 마음껏 헤매기",
        "자식같은 프로젝트 해보기",
      ],
    },
    {
      category: "학교",
      todolist: ["등교하기", "하교하기"],
    },
];

const main = document.querySelector('#to_do')

TODO_LIST_DATA.forEach((block) => {
    
    const category = document.createElement("div");
  category.classList.add("category");

  const categoryName = document.createElement("p");
  categoryName.innerText = block.category;

  const addTaskBtn = document.createElement("div");
  addTaskBtn.classList.add("add_task_btn");
  addTaskBtn.setAttribute("id", "addTaskBtn");

  const icon = document.createElement("i");
  icon.classList.add("ri-add-line");

  addTaskBtn.appendChild(icon);
  category.appendChild(categoryName);
  category.appendChild(addTaskBtn);
  main.appendChild(category);

  const ul = document.createElement("ul");
  ul.setAttribute("id", "list_container");

  block.todolist.forEach((item) => {
    const li = document.createElement("li");
    li.innerText = item;
    ul.appendChild(li);
  })
  main.appendChild(ul);
})
