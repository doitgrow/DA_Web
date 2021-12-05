// console.log(document.getElementsByClassName('keyword-query-set').length);

// function addQueryBox() {
//     const pTag = document.createAttributeElement("p")
// }   

// 키워드 입력을 통해 쿼리를 자동 생성하는 영역 추가 버튼
function addQueryBox() {
    let newDiv = document.createElement('div');
    newDiv.setAttribute('class', 'title-button-group');
    
    let newP = document.createElement('p');
    let newText = document.createTextNode("키워드");
    newP.appendChild(newText);

    let newInputTyping = document.createElement('input');
    newInputTyping.setAttribute('type', 'text');
    newInputTyping.setAttribute('class', 'typing-box');
    newInputTyping.setAttribute('placeholder', '키워드1; 키워드2; 키워드3');

    let newInputConfirm = document.createElement('input');
    newInputConfirm.setAttribute('type', 'text');
    newInputConfirm.setAttribute('class', 'confirm-box');
    newInputConfirm.setAttribute('placeholder', '쿼리 생성 결과');

    newP.appendChild(newText);
    newDiv.appendChild(newP);
    newDiv.appendChild(newInputTyping);
    newDiv.appendChild(newInputConfirm);

    let targetTag = document.querySelector('.keyword-query-set');
    targetTag.appendChild(newDiv);
}

// 키워드-쿼리 처리 영역 삭제
function delQueryBox() {
    let titleButtonGroupCount = document.getElementsByClassName('title-button-group').length;
    if (titleButtonGroupCount == 1) {
        alert("입력창 개수가 1개 이하는 삭제가 불가합니다.")    
    } else {
        
    }
}