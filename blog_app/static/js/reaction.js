async function setReaction(){
    const el = event.target;
    const id = el.attributes["data-id"].value;
    const entity = el.attributes["data-entity"].value;
    const operation = el.attributes["data-operation"].value;
    const token = document.querySelector(
        'input[name="csrfmiddlewaretoken"]'
    ).value;
    console.log(token);
    
    const response = await fetch (
        "http://127.0.0.1:8000/reaction/change",
        {
            method:'POST',
            headers: {
                'X-CSRFToken': token
            },
            body:JSON.stringify({
                id,
                entity,
                operation
            })
        }
    ).then(async (response) => {
        console.log(response.ok);
        console.log(
            await response.json().then(
                (res) => {
                    setCount(res, "like", el);
                    setCount(res, "dislike", el);
                    


                }
            )
        );
    });
}

function setCount(res, operation, el){
    const elParent = el.parentNode.parentNode;
    const selector =`span[data-type="${operation}"]`;
    const count = res[operation + "s"];
    const elCounter = elParent.querySelector(
        selector
    )
    elCounter.innerText = count;

    const activeBtn = "reaction-set";
    const btnSelector = `i[data-operation="${operation}"]`;
    const elBtn = elParent.querySelector(btnSelector);
    
    if (res["is_my_"+operation]){
        elBtn.classList.add(activeBtn); 
    } else {
        elBtn.classList.remove(activeBtn);
    }
                    
}